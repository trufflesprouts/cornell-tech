import time, random, gc, tracemalloc, statistics, io, builtins
from unittest.mock import patch
import matplotlib.pyplot as plt
from p1_b import stable_matching_1b
from p1_c import stable_matching_1c

RNG_SEED = 2
N_VALUES = [20, 50, 100, 200, 300, 500, 800]
REPS = 5
VIRTUAL_PATH = "VIRTUAL_INPUT"

def gen_random_preferences(n, rng):
    students = [rng.sample(range(n), n) for _ in range(n)]
    hospitals = [rng.sample(range(n), n) for _ in range(n)]
    return students, hospitals

def to_text(n, students, hospitals):
    lines = [str(n)] + [" ".join(map(str, row)) for row in students] + [" ".join(map(str, row)) for row in hospitals]
    return "\n".join(lines) + "\n"

def measure_once(func, text):
    real_open = builtins.open
    def fake_open(path, *args, **kwargs):
        if path == VIRTUAL_PATH:
            return io.StringIO(text)
        return real_open(path, *args, **kwargs)
    gc.collect()
    t0 = time.perf_counter()
    with patch("builtins.open", fake_open):
        r = func(VIRTUAL_PATH)
    t1 = time.perf_counter()
    return (t1 - t0), r

def benchmark(n_values, reps, seed):
    rng = random.Random(seed)
    results = {}
    for n in n_values:
        times = {"b": [], "c": []}
        for _ in range(reps):
            students, hospitals = gen_random_preferences(n, rng)
            txt = to_text(n, students, hospitals)
            tb, rb = measure_once(stable_matching_1b, txt)
            times["b"].append(tb)
            tc, rc = measure_once(stable_matching_1c, txt)
            times["c"].append(tc)
        for algo in ("b","c"):
            results.setdefault(algo, {})[n] = statistics.median(times[algo])
    return results

def plot_all_algorithms(results, ylabel, title):
    plt.figure()
    for algo, marker, style in [("b","o","-"),("c","s","--")]:
        ns = sorted(results[algo].keys())
        ys = [results[algo][n] for n in ns]
        plt.plot(ns, ys, marker=marker, linestyle=style, label=algo)
    plt.xlabel("n")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True, linestyle=":", linewidth=1, alpha=0.6)
    plt.tight_layout()
    plt.show()

results = benchmark(N_VALUES, REPS, RNG_SEED)
plot_all_algorithms(results,"Median runtime (s)","Runtime vs n")
