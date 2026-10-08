import importlib.util
from pathlib import Path
import timeit
import argparse
from tabulate import tabulate

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BENCHS_DIR = Path(__file__).resolve().parent


def load_day_module(year: int, day: int):
    """Load solution.py module and input.txt file if existing."""
    day_dir = PROJECT_ROOT / str(year) / f"day{day}"
    solution_path = day_dir / "solution.py"
    input_path = day_dir / "input.txt"

    if not solution_path.exists() or not input_path.exists():
        return None, None

    spec = importlib.util.spec_from_file_location(
        f"aoc_{year}_{day}", solution_path
    )
    if spec is None or spec.loader is None:
        return None, None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, str(input_path)


def bench_function(func, input_path: str, number: int = 20) -> str:
    """Measure average function execution time and format it cleanly"""
    try:
        # Run function 'number' times and keep the average
        timer = timeit.Timer(lambda: func(input_path))
        total_time = timer.timeit(number=number)
        mean_time_sec = total_time / number

        # Format based on execution speed
        if mean_time_sec < 1e-3:
            return f"{mean_time_sec * 1e6:.2f} µs"
        elif mean_time_sec < 1:
            return f"{mean_time_sec * 1e3:.2f} ms"
        else:
            return f"{mean_time_sec:.2f} s"
    except Exception as e:
        return f"Error ({e.__class__.__name__})"


def generate_year_benchmark_report(year: int) -> Path:
    """Generate bench_{year}.txt file with benchmark for all days of the selected year."""
    table_data = []

    print(f"Generating benchmark report for year {year}...")

    # Go through the 25 days of AOC
    for day in range(1, 26):
        module, input_path = load_day_module(year, day)

        if module is None:
            continue  # Day not implemented

        p1_time = "N/A"
        p2_time = "N/A"

        if hasattr(module, "part1"):
            p1_time = bench_function(module.part1, input_path)

        if hasattr(module, "part2"):
            p2_time = bench_function(module.part2, input_path)

        table_data.append([f"Day {day:02d}", p1_time, p2_time])

    # Generating formatted table
    headers = ["Day", "Part 1", "Part 2"]
    report_table = tabulate(table_data, headers=headers, tablefmt="github")

    # Write table in bench file
    output_file = BENCHS_DIR / f"bench_{year}.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"=== AoC {year} - Performance Report ===\n\n")
        f.write(report_table)
        f.write("\n")

    print(f"Report saved to: {output_file}")
    return output_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate AoC benchmark report for a specific year."
    )
    parser.add_argument(
        "year",
        type=int,
        nargs="?",
        default=2025,
        help="The year to benchmark (default: 2025)",
    )

    args = parser.parse_args()
    generate_year_benchmark_report(args.year)