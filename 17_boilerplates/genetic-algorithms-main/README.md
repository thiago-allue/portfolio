# Genetic Algorithms

Repo for storing simple examples, snippets and pieces of reusable code using genetic algorithms and related algorithmic approaches.

# Outline of the Basic Genetic Algorithm

As described in [https://www.obitko.com/tutorials/genetic-algorithms/ga-basic-description.php](https://www.obitko.com/tutorials/genetic-algorithms/ga-basic-description.php)

1. [Start] Generate random population of n chromosomes (suitable solutions for the problem)
2. [Fitness] Evaluate the fitness f(x) of each chromosome x in the population
3. [New population] Create a new population by repeating following steps until the new population is complete
    1. [Selection] Select two parent chromosomes from a population according to their fitness (the better fitness, the bigger chance to be selected)
    2. [Crossover] With a crossover probability cross over the parents to form a new offspring (children). If no crossover was performed, offspring is an exact copy of parents.
    3. [Mutation] With a mutation probability mutate new offspring at each locus (position in chromosome).
    4. [Accepting] Place new offspring in a new population
4. [Replace] Use new generated population for a further run of algorithm
5. [Test] If the end condition is satisfied, stop, and return the best solution in current population
6. [Loop] Go to step 2
