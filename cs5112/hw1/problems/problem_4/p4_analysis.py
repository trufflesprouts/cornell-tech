import sys, time, random, gc, tracemalloc, statistics
import matplotlib.pyplot as plt

sys.path.append("..")

from problem_4.p4_b import most_frequent_difference_b
from problem_4.p4_c import most_frequent_difference_c

RNG_SEED = 42
D_MODE = 1
N_VALUES = [200, 500, 1000, 2000, 3000]
REPS = 3

def measure_once(func, arr, d_mode):
    data = list(arr)
    gc.collect()
    tracemalloc.start()
    t0 = time.perf_counter()
    result = func(data, d_mode)
    t1 = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return (t1 - t0), (peak / 1024.0), result

def benchmark(n_values, d_mode, reps, seed):
    rng = random.Random(seed)
    results = {}
    for n in n_values:
        base = [rng.randint(-1_000_000, 1_000_000) for _ in range(n)]

        times = {"b": [], "c": []}
        mems  = {"b": [], "c": []}
        answers = []

        for _ in range(reps):
            t, m, rb = measure_once(most_frequent_difference_b, base, d_mode)
            times["b"].append(t); mems["b"].append(m)
            t, m, rc = measure_once(most_frequent_difference_c, base, d_mode)
            times["c"].append(t); mems["c"].append(m)
            answers.append((rb, rc))

        for algo in ("b","c"):
            results.setdefault(algo, {})[n] = {
                "time_med": statistics.median(times[algo]),
                "mem_med":  statistics.median(mems[algo]),
            }
    return results

results = benchmark(N_VALUES, D_MODE, REPS, RNG_SEED)


def plot_all_algorithms(results, metric_key, ylabel, title):
    plt.figure()

    series_order = ["b", "c"]
    marker_for_algo    = {"b": "o", "c": "s"}   # circle, square
    linestyle_for_algo = {"b": "-",  "c": "--"}

    for algo in series_order:
        pts = results[algo]
        ns = sorted(pts.keys())
        ys = [pts[n][metric_key] for n in ns]
        plt.plot(
            ns, ys,
            marker=marker_for_algo[algo],
            linestyle=linestyle_for_algo[algo],
            label=f"({algo})",
        )

    plt.xlabel("n (list length)")
    plt.ylabel(ylabel)
    plt.title(title + "  —  d_mode=1")
    # plt.yscale("log")
    plt.legend()
    plt.grid(True, linestyle=":", linewidth=1, alpha=0.6)
    plt.tight_layout()
    plt.show()


plot_all_algorithms(
    results,
    metric_key="time_med",
    ylabel="Median runtime (s)",
    title="Runtime vs n (algorithms b, c)",
)
plot_all_algorithms(
    results,
    metric_key="mem_med",
    ylabel="Median peak memory (KB)",
    title="Peak memory vs n (algorithms b, c)",
)