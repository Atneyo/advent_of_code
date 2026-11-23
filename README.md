# Advent of Code

This repository contains my solutions to [Advent of Code](https://adventofcode.com/) puzzles, along with the input files used to solve them.

The solutions are organized by year and day. Each day contains my personal input, the sample input, and a file solution with two functions: one for Part 1 and one for Part 2.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Project structure](#project-structure)
- [Run a solution](#run-a-solution)
- [Run a day directly](#run-a-day-directly)
- [Benchmarks](#benchmarks)

## Requirements

- Python **3.10.11**
- `pip`

Python 3.10.11 is recommended to match the environment used to develop the solutions and benchmarks.

## Installation

From the repository root, create a virtual environment and install the dependencies:

```powershell
py -3.10 -m venv env
.\env\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell execution policies prevent activation, activate the environment temporarily with:

```powershell
.\env\Scripts\activate
```

The repository currently uses:

- `numpy`
- `tabulate`

## Project structure

```text
advent_of_code/
├── 2025/
│   └── day1/
│       ├── input.txt
│       ├── sample.txt
│       └── solution.py
├── benchmarks/
│   ├── bench_2025.txt
│   └── create_benchmark.py
├── templates/
│   └── solution.py
├── main.py
├── requirements.txt
└── README.md
```

- `YYYY/` contains the solutions for a year.
- `YYYY/dayN/` contains the files for one day.
- `input.txt` contains the personal puzzle input.
- `sample.txt` contains the example provided in the puzzle statement.
- `solution.py` contains the two solution functions.
- `benchmarks/` contains the benchmark script and reports.
- `templates/solution.py` is used as a template for creating a new solution.

## Run a solution

The main launcher requires two positional arguments:

```text
year  Year, for example 2025
day   Day, for example 1
```

Display the launcher help:

```powershell
python .\main.py -h
```

Run Day 8 of 2025:

```powershell
python .\main.py 2025 8
```

This command automatically searches for:

```text
2025/day8/solution.py
```

It then executes the file with the active Python interpreter. If the solution or directory does not exist, the launcher prints a message indicating that the solution was not found.

## Run a day directly

A solution can also be run from the repository root:

```powershell
python .\2025\day8\solution.py
```

Each `solution.py` file should follow this interface:

```python
def part1(input_path: str) -> int:
    ...


def part2(input_path: str) -> int:
    ...
```

Both functions receive the path to an input file and usually return the answer for their corresponding part.

## Benchmarks

The benchmark script measures the average execution time of `part1` and `part2`. Each function is executed 20 times using `timeit`.

Create a benchmark report for a year from the repository root:

```powershell
python .\benchmarks\create_benchmark.py 2026
```

Without a year, the script defaults to 2025:

```powershell
python .\benchmarks\create_benchmark.py
```

The report is saved to:

```text
benchmarks/bench_2026.txt
```

For each implemented day containing a valid input, the script generates two measurements:

| Column | Description |
| --- | --- |
| `Day` | Day number |
| `Part 1` | Average time for Part 1 |
| `Part 2` | Average time for Part 2 |

Days without `solution.py`, `input.txt`, or an implemented function are ignored. Units are automatically displayed in microseconds (`µs`), milliseconds (`ms`), or seconds (`s`).

A report is already available for 2025:

- [benchmarks/bench_2025.txt](benchmarks/bench_2025.txt)
