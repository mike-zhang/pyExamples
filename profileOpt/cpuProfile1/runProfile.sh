#! /bin/sh

python -m cProfile -o test1.out profileTest1.py
python -c "import pstats; p=pstats.Stats('test1.out'); p.sort_stats('time').print_stats()"

