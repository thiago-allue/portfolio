# Profiling

Profiling in Python.

Identify bottlenecks and measure execution times.

## Measure time taken

The most common approach is to measure the time before and after an activity.

```python
import time
t0 = time.perf_counter()
activity_or_process()
time_taken = time.perf_counter() - t0
print(f'Total time taken was {time_taken}')
```

## Using timeit

`python -m timeit '"-".join(map(str, range(100)))'`

or through code:

```python
import timeit
timeit.timeit('import time; time.sleep(2)', number=10000)
```

- https://docs.python.org/3.6/library/timeit.html

### Jupyter Notebooks

In a Jupyter Notebook, you can use the following to time the execution of a cell:

```python
import numpy as np

%%timeit
np.random.randn(100000).cumsum()
```

## Using profile / cProfile

1. `python -m cProfile -o module.prof module.py`
2. `python -m pstats module.prof`

```
strip
sort cumtime
stats 10

sort tottime
stats 10

stats timer
```

- https://docs.python.org/3.6/library/profile.html

### Example 1

`$ python -m cProfile -s cumtime profile_me.py`

### Example 2

1. `$ python -m cProfile -o output.pstats profile_me.py`
2. `$ python -m gprof2dot -f pstats output.pstats >> stats.dot`
3. `$ dot -Tpng -o output.png stats.dot` - implies graphviz binaries are in the current directory or PATH.

## Dependencies

- gprof2dot: `pip install gprof2dot`
- graphviz

## Other modules for Profiling

- line_profiler: `pip install line-profiler`
- pyprof2calltree
- pyinstrument
- snakeviz
- vprof

## Installing dependencies

As usual, `pip install <package>`.

Graphviz requires the graphviz binaries, usually in the PATH or available from the current working directory (http://www.graphviz.org/).

## Using QCacheGrind

If you want to use QCacheGrindWin:

1) Download it - https://sourceforge.net/projects/qcachegrindwin/
2) Generate cProfile output.
3) Use `pyprof2calltree` to convert the cProfile output to QCacheGrindWin file format.

### Install The Convertor

`$ sudo pip install pyprof2calltree` - produces a file to be used with QCacheGrindWin and related applications.

### Profile The Python Code

1. `$ python -m cProfile -o <output_filename> filename_to_profile.py`
2. `$ pyprof2calltree -i output.pstats -o import.callgrind`

And open the `import.callgrind` with the QCacheGrindWin application.

## Using SnakeViz

1. `$ python -m cProfile -o program.prof my_program.py`
2. `$ snakeviz program.prof` - it will open a web application to view and analyze.

## Tools

- https://github.com/nvdv/vprof
- https://github.com/rkern/line_profiler

## Bibliography and Resources

- http://jiffyclub.github.io/snakeviz/
- https://github.com/jrfonseca/gprof2dot
- http://www.graphviz.org/doc/info/command.html
- https://julien.danjou.info/blog/2015/guide-to-python-profiling-cprofile-concrete-case-carbonara
- https://realpython.com/python-timer/

### Graphviz Binaries

- https://www2.graphviz.org/Packages/stable/windows/10/msbuild/Release/Win32/
