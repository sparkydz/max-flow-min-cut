# Max Flow/Min Cut Using CPLEX in Python

This program uses the Python `cplex` library to solve a max flow/min cut problem.  More information 
on max flow/min cut is available in the [Wikipedia article](https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem).  
The basic idea is to assign flow to each edge such that no edge's flow exceeds that edge's capacity.

Be aware that a linear program may not always be the most efficient technique for solving max flow/min cut.  This gist
is intended more as a demonstration of how to use CPLEX in Python.

The graph I used is:

        /---> a -2->e-
       /      ^       \
      1       5        3
     /        |         \
    s --9---> b --4----> t
     \        ^        /
     9.5      2       /
       \----> c -3.5-

Main items to take note of include:
* Edges: These are float variables constrained between 0 and that edge's capacity inclusive.
* Constraints: Conservation of flow into/out of each vertex.
* Objective: Maximize flow out of `s` or into `t`.  This example uses the former.

**Note**: Tested with Python 3.6.5 & `cplex` version 12.8.0.0
