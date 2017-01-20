# Solving _Rectangle-Fit_ problem

This repository focuses on solving the well-known problem of [Rectangle-Fit](https://en.wikipedia.org/wiki/Packing_problems#Different_rectangles_in_a_rectangle). Problem is known to be NP-hard, so a meta-heuristic approach called [Nelder-Mead method](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method) is used to find a near-optimal solution.

## Problem instance

Since packing problems like this problem can have many formulations & variants, I provide an exact problem description:

> Given `n` rectangles of width `w` and height `h` (`w`. `h` are real numbers), we want to find a _packing_ of those rectangles into a bigger _bounding_ rectangle which minimizes _bounding rectangle_ area. Rectangles can't overlap & they need to be within the _bounding rectangle_ area.
> We're interested in a minimal area that can be achieved for a given set of rectangles. Alternatively, `W`, `H` can be supplied - which are dimensions of _bounding rectangle_.

## Idea of solution

Minimalisation problem stated that way cannot be solved using typical linear programming techniques - at least without adding additional constraints. But there are effective (`O(n)` or `O(n * log(n))` algorithms finding an approximate result for _ribbon-fit_ problem. A _ribbon_ is a sub-surface of width `W` where we try to fit rectangles (similar constraints as in _Rectangle-Fit_ problem), minimizing the `y` position (effective _height_) of the top-most corner of rectangle placed in that way.

That may find a good approximate for _bounding rectangle_ area I'm looking for. But we don't know what `W` to choose to find an optimal _bounding rectangle_. Here, meta-heuristics come into play. _Nelder-Mead method_ is used to traverse solution space, finding optimal `W` (using meta-heuristics) and `H` (using heuristic algorithm from _bounding-ribbon_ problem).

## Installation

To use this code, you need to have Python (2.x) & [SciPy](https://docs.scipy.org/doc/scipy-0.14.0/reference/index.html) installed. The easiest way to have an environment for so-called _scientific Python_ is to use one of ready-made solutions like [Anaconda Python](https://www.continuum.io/downloads). You can also install scipy on your local Python - see [here](https://www.scipy.org/install.html) for details.

Then just clone the repo:

```
git clone https://github.com/Killavus/fitting-rectangles.git
cd fitting-rectangles
```

## Usage

There are two ways to use the code. Heuristics available are `naive`, `nfdh`, `ffdh`, `rf`:

* _test mode_, where you can run one of _bounding-ribbon_ heuristics with a given, set `W`:

```
python main.py -t 20.0 nfdh
```

Program then waits for your input, which are pairs of width & height for rectangles. You end entering input by emitting `EOF` (`ctrl + d` in majority of shells). So for example:

```
2.0 1.0
3.0 1.5
2.34 2.33
<EOF>
```

is a valid input. You can use `<` to easily feed file contents to this script:

```
python main.py -t 5.0 nfdh < test/simple1.in
```

* normal mode, where Nelder-Mead is used to find the solution:

```
python main.py nfdh < test/simple1.in
```

## Heuristics overview:

* `naive` - the simplest one. Go one-by-one through rectangles, trying to fit them right after the previously placed one. If it's not possible, place the new rectangle at the top of the previous 'level'. For data `(w, h): (3.0, 1.0), (2.0, 1.0), (1.0, 1.0), W: 4`, the result will be `(x, y): (0.0, 0.0), (0.0, 1.0), (1.0, 1.0)`. (no approximation error upper bound)
* `nfdh` - _next-fit decreasing height_ - very similar to naive, but we sort rectangles by decreasing height first. (at most 3 times worse than an optimal solution)
* `ffdh` - _first-fit decreasing height_` - idea is like in `nfdh`, but with every rectangle we try to fit it to every level "opened" before. So if there's W: 4 and (3.0, 3.0) rectangle on (0, 0) position, (1.0, 1.0) will be added to (3.0, 0.0) position, 'filling' the hole. (at most 2,7-times worse than an optimal solution)
* `rf` - _reverse-fit_. This one gives the best solution, but it's the most complex one. It is [described in this paper](https://www.researchgate.net/publication/220770161_Reverse-Fit_A_2-Optimal_Algorithm_for_Packing_Rectangles). (at most 2 times worse than an optimal solution).
