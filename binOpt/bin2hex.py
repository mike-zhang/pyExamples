#! /usr/bin/env python3
#--*-- coding:utf-8 --*--

# 将二进制文件的内容转换为十六进制字符串，并写入文本文件中。
import os,sys

def bin2hex(srcFile,dstFile):
    with open(srcFile,"rb") as fin,open(dstFile,"w") as fout:
        fout.write(fin.read().hex())
    print("%s => %s" % (srcFile,dstFile))    
    
def bin2hex(srcFile, dstFile):
    """
    将二进制文件 srcFile 转换为大写十六进制字符串，
    并写入文本文件 dstFile，每行最多 80 个字符。
    采用分批读取，避免大文件一次性载入内存。
    """
    # 每次读取的字节数（64KB），避免一次性读入整个大文件
    CHUNK_SIZE = 64 * 1024
    # 每行最多 80 个十六进制字符
    LINE_CHARS = 80
    # 每个字节转为 2 个十六进制字符，因此每行对应 40 字节
    LINE_BYTES = LINE_CHARS // 2

    # 以二进制只读方式打开源文件，以文本写入方式打开目标文件
    with open(srcFile, "rb") as fin, open(dstFile, "w") as fout:
        # remainder 保存上次未凑满一行的剩余字节，保证跨块换行正确
        remainder = b""
        while True:
            # 分批读取
            chunk = fin.read(CHUNK_SIZE)
            if not chunk:
                break
            # 与上次剩余数据拼接，避免行被 chunk 边界截断
            data = remainder + chunk
            # 计算能凑成完整行的字节数
            full_len = len(data) // LINE_BYTES * LINE_BYTES
            full, remainder = data[:full_len], data[full_len:]

            if full:
                # 转为十六进制后统一转大写
                hex_str = full.hex().upper()
                # 按每行 80 个字符切分并写入，每行末尾换行
                for i in range(0, len(hex_str), LINE_CHARS):
                    fout.write(hex_str[i:i + LINE_CHARS] + "\n")

        # 处理文件末尾不足一行的剩余数据
        if remainder:
            fout.write(remainder.hex().upper() + "\n")

    # 打印转换结果，显示源文件和目标文件路径
    print("%s => %s" % (srcFile, dstFile))
    
        
if __name__ == '__main__':
    #print(sys.argv)
    argc = len(sys.argv)
    if argc < 3:
        print("usage : %s srcFileName dstFileName" % sys.argv[0])
        sys.exit(0)
    srcFile,dstFile = sys.argv[1],sys.argv[2]
    bin2hex(srcFile,dstFile)
    