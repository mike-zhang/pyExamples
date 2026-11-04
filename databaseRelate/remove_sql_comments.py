#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
remove_sql_comments.py —— 移除 SQL 文件中的注释

支持:
  -- 单行注释（可用 --strict-dash 要求 "--" 后必须跟空白）
  #  单行注释（需加 --hash-comments，MySQL 风格）
  /* ... */ 多行注释（可跨行）

会保留 /*! ... */ 和 /*+ ... */（MySQL 版本注释 / 优化器 hint）
字符串 '...'、"..." 以及反引号标识符 `...` 中的内容不会被误删。

用法:
  python remove_sql_comments.py input.sql                 # 输出到标准输出
  python remove_sql_comments.py input.sql -o output.sql   # 输出到文件
  python remove_sql_comments.py input.sql -i              # 原地修改
"""

import argparse
import sys


def strip_sql_comments(sql: str,
                       strict_dash: bool = False,
                       hash_comments: bool = False) -> str:
    """逐字符扫描，移除 SQL 注释，跳过字符串/标识符内部。"""
    out = []
    i, n = 0, len(sql)

    while i < n:
        ch = sql[i]
        nxt = sql[i + 1] if i + 1 < n else ''

        # ---------- 单行注释 -- ----------
        if ch == '-' and nxt == '-':
            ok = True
            if strict_dash:
                # 要求 "--" 后面是空白或行尾
                ok = (i + 2 >= n) or sql[i + 2] in ' \t\r\n'
            if ok:
                while i < n and sql[i] not in '\r\n':
                    i += 1
                continue

        # ---------- 单行注释 # ----------
        if hash_comments and ch == '#':
            while i < n and sql[i] not in '\r\n':
                i += 1
            continue

        # ---------- 多行注释 /* ... */ ----------
        if ch == '/' and nxt == '*':
            # 保留 /*! ... */ 与 /*+ ... */
            if i + 2 < n and sql[i + 2] in '!+':
                out.append('/*')
                i += 2
                while i < n:
                    if sql[i] == '*' and i + 1 < n and sql[i + 1] == '/':
                        out.append('*/')
                        i += 2
                        break
                    out.append(sql[i])
                    i += 1
                continue

            i += 2
            while i < n:
                if sql[i] == '*' and i + 1 < n and sql[i + 1] == '/':
                    i += 2
                    break
                # 保留换行，便于最后清理时保持行结构
                if sql[i] in '\r\n':
                    out.append(sql[i])
                i += 1
            continue

        # ---------- 字符串 / 标识符 ----------
        if ch in ("'", '"', '`'):
            quote = ch
            out.append(ch)
            i += 1
            while i < n:
                c = sql[i]
                # 反斜杠转义（反引号内不支持）
                if c == '\\' and quote != '`' and i + 1 < n:
                    out.append(c)
                    out.append(sql[i + 1])
                    i += 2
                    continue
                if c == quote:
                    # '' 或 "" 形式的转义
                    if i + 1 < n and sql[i + 1] == quote:
                        out.append(c)
                        out.append(sql[i + 1])
                        i += 2
                        continue
                    out.append(c)
                    i += 1
                    break
                out.append(c)
                i += 1
            continue

        out.append(ch)
        i += 1

    return ''.join(out)


def cleanup_lines(text: str, newline: str, keep_empty_lines: bool = False,
                  strip_trailing: bool = True) -> str:
    """去掉因注释产生的多余空行 / 行尾空白。"""
    lines = []
    for line in text.splitlines():
        if strip_trailing:
            line = line.rstrip()
        if not line and not keep_empty_lines:
            continue
        lines.append(line)
    result = newline.join(lines)
    return result


def main():
    parser = argparse.ArgumentParser(description='移除 SQL 文件中的注释')
    parser.add_argument('input', help='输入 SQL 文件')
    parser.add_argument('-o', '--output', help='输出文件（默认输出到标准输出）')
    parser.add_argument('-i', '--in-place', action='store_true', help='原地修改输入文件')
    parser.add_argument('--hash-comments', action='store_true',
                        help="同时移除 # 单行注释（MySQL）")
    parser.add_argument('--strict-dash', action='store_true',
                        help="仅当 '--' 后跟空白/行尾时才视为注释")
    parser.add_argument('--keep-empty-lines', action='store_true',
                        help='保留移除注释后产生的空行')
    parser.add_argument('--no-strip-trailing', action='store_true',
                        help='不去掉行尾空白')
    parser.add_argument('--encoding', default='utf-8', help='文件编码，默认 utf-8')
    args = parser.parse_args()

    with open(args.input, 'r', encoding=args.encoding, newline='') as f:
        sql = f.read()

    newline = '\r\n' if '\r\n' in sql else '\n'

    result = strip_sql_comments(sql,
                                strict_dash=args.strict_dash,
                                hash_comments=args.hash_comments)

    result = cleanup_lines(
        result,
        newline,
        keep_empty_lines=args.keep_empty_lines,
        strip_trailing=not args.no_strip_trailing,
    )

    if sql.endswith(('\n', '\r')) and result and not result.endswith(newline):
        result += newline

    if args.in_place:
        with open(args.input, 'w', encoding=args.encoding, newline='') as f:
            f.write(result)
    elif args.output:
        with open(args.output, 'w', encoding=args.encoding, newline='') as f:
            f.write(result)
    else:
        sys.stdout.write(result)


if __name__ == '__main__':
    main()