Welcome to my repository of solutions to the annual Christmas challenge, [Advent of Code](https://adventofcode.com). 

The table you can see below is my estimation of "difficulty level" of each individual puzzle:
- Point 1 means that the puzzle does not require any knowledge relating to computer science or maths. These problems are fairly straightforward, simple logical reasoning translated to code would do the trick.
- Problems scoring 2 points, where it is useful to be familiar with programming and related concepts like:
  - data structures (trees, linked lists, maps, graphs, ...)
  - algorithms (breadth- and depth-first-search, Dijkstra, convolution, ...)
  - maths (congruences and fundamental number theory, ...)
- With 3 points, I find those problems not solvable with brute force. Many of them include either working with enormous input sizes or looping million (if not billion) times. A clever workaround and efficiency is key here, I sometimes spent days cracking and trying out solutions on problems like these.

|     |   2015  |   2016  |   2017  |   2018  |   2019  | 2020 |   2021  |   2022  |
|-----|:-------:|:-------:|:-------:|:-------:|:-------:|:----:|:-------:|:-------:|
|  1  |         |         |         |         |         |    1 |         |         |
|  2  |         |         |         |         |         |    1 |         |         |
|  3  |         |         |         |         |         |    1 |         |         |
|  4  |         |         |         |         |         |    1 |         |         |
|  5  |         |         |         |         |         |    1 |         |         |
|  6  |         |         |         |         |         |    1 |         |         |
|  7  |         |         |         |         |         |    2 |         |         |
|  8  |         |         |         |         |         |    1 |         |         |
|  9  |         |         |         |         |         |    1 |         |         |
|  10 |         |         |         |         |         |    3 |         |         |
|  11 |         |         |         |         |         |    2 |         |         |
|  12 |         |         |         |         |         |    1 |         |         |
|  13 |         |         |         |         |         |    2 |         |         |
|  14 |         |         |         |         |         |    2 |         |         |
|  15 |         |         |         |         |         |    2 |         |         |
|  16 |         |         |         |         |         |    2 |         |         |
|  17 |         |         |         |         |         |    2 |         |         |
|  18 |         |         |         |         |         |    1 |         |         |
|  19 |         |         |         |         |         |    3 |         |         |
|  20 |         |         |         |         |         |    2 |         |         |
|  21 |         |         |         |         |         |    1 |         |         |
|  22 |         |         |         |         |         |    3 |         |         |
|  23 |         |         |         |         |         |    2 |         |         |
|  24 |         |         |         |         |         |    2 |         |         |
|  25 |         |         |         |         |         |    2 |         |         |
| AVG | #DIV/0! | #DIV/0! | #DIV/0! | #DIV/0! | #DIV/0! | 1.68 | #DIV/0! | #DIV/0! |

# 2020
This was the first year, when I first heard about the competition. During that time, I was doing master's studies and was really excited to jump into this.
- 7 was the first problem where I had to implement a tree structure and the corresponding upwards-downwards traversal algorithm. It was fun!
- 10 it was needed to inspect & sort the input and then make the correct deduction that only the 1 differences matter between the adapters. Hence, we can extract the only sections in the adapter-array, which contribute to overall number of combinations. A year later, when I typed this into OEIS, I saw the pattern of the Tribonacci-numbers.
- 11 is not complicated. It is a reoccuring theme in AoC, but there are many variables that we need to keep track of
- 13 if you know about the Chinese Remainder Theorem, then it's surprisingly easy; at first, I solved this using pencil & paper
- 14 calculating floating bits with DFS
- 15 with proper structure and logic, it is easy
- 16 easy, but need a good amount of coding
- 17 your yearly dose on convolution
- 18 no fucking around formal grammar
- 22 daily dose of recursion, it gets messy
- 23 cannot be solved brute force
- 24 had to google up hexagonal coordinates, but otherwise ok
- 25 just  bit hard to digest / interpret
