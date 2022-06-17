"""
pip install gprof2dot
graphviz should be available in the PATH (dot executable).

gprof2dot -f pstats profile_for_func1_001 | dot -Tpng -o profile.png
"""
import sys
import time
import cProfile
import subprocess

import os
import pathlib
os.chdir(pathlib.Path(__file__).parent)


def profileit(name):
    def inner(func):
        def wrapper(*args, **kwargs):
            prof = cProfile.Profile()
            ret_val = prof.runcall(func, *args, **kwargs)
            prof.dump_stats(name + '.prof')
            try:
                dot = subprocess.check_output(f"gprof2dot -f pstats {name}.prof", shell=True)
                with open(f"{name}.dot", "w", encoding="utf-8") as f:
                    f.write(dot.decode(encoding="utf-8"))
                subprocess.call(f"dot {name}.dot -Tpng -o {name}.png", shell=True, stdout=sys.stdout)
            except Exception as e:
                print('Could not automatically generate dot graph.', e)
            return ret_val
        return wrapper
    return inner


def f2():
    time.sleep(1)
    s = "This is a list"
    for c in s:
        print(ord(c))


@profileit("profile_for_func1_001")
def func1():
    time.sleep(5)
    lst = [i for i in range(100000)]
    ret = 0
    for i in lst:
        ret += i
    print(lst)
    print(ret)
    print(sum(lst))
    f2()


if __name__ == '__main__':
    func1()
