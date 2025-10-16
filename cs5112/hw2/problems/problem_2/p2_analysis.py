import random
import math
import time
import statistics
import matplotlib.pyplot as plt
from p2_a import closest_pair as cp_a
from p2_b import closest_pair as cp_b
from p2_c import closest_pair as cp_c

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def brute_force(points):
    best = (points[0], points[1])
    best_d = dist(points[0], points[1])
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(points[i], points[j])
            if d < best_d:
                best_d = d
                best = (points[i], points[j])
    return best

def pair_distance(pair):
    return dist(pair[0], pair[1])

def gen_points(n, rng):
    return [(rng.uniform(0.0, 1000.0), rng.uniform(0.0, 1000.0)) for _ in range(n)]

def time_once(fn, pts):
    data = list(pts)
    t0 = time.perf_counter()
    fn(data)
    t1 = time.perf_counter()
    return t1 - t0

def main():
    random.seed(42)
    sizes = [200, 400, 1000, 2000, 4000]
    trials = 5
    algos = {
        "Brute Force": cp_a,
        "Divide and Conquer": cp_b,
        "Randomized": cp_c,
    }

    tol = 1e-9
    for n in [20, 40, 80]:
        rng = random.Random(1000 + n)
        pts = gen_points(n, rng)
        bf = brute_force(pts)
        bf_d = pair_distance(bf)
        for name, fn in algos.items():
            got = fn(list(pts))
            if abs(pair_distance(got) - bf_d) > tol:
                raise RuntimeError(f"mismatch for {name} at n={n}")

    results = {name: [] for name in algos}
    for n in sizes:
        rng = random.Random(2000 + n)
        base = gen_points(n, rng)
        for name, fn in algos.items():
            ts = []
            for _ in range(trials):
                pts = list(base)
                rng.shuffle(pts)
                ts.append(time_once(fn, pts))
            results[name].append((n, statistics.mean(ts), statistics.pstdev(ts) if len(ts) > 1 else 0.0))

    plt.figure(figsize=(8, 5))
    for name, series in results.items():
        xs = [n for n, _, _ in series]
        ys = [avg for _, avg, _ in series]
        plt.plot(xs, ys, marker="o", label=name)
    plt.xlabel("Number of points (n)")
    plt.ylabel("Average runtime (seconds)")
    plt.title("Closest Pair of Points: Empirical Runtime")
    plt.grid(True, linestyle=":")
    plt.legend()
    plt.tight_layout()
    plt.show()

    header = "n".rjust(8) + " | " + " | ".join(f"{name:^26}" for name in algos)
    print(header)
    print("-" * len(header))
    for i, n in enumerate(sizes):
        row = f"{n:8d}"
        for name in algos:
            _, avg, sd = results[name][i]
            row += f" | {avg:10.6f} ± {sd:<10.6f}"
        print(row)

if __name__ == "__main__":
    main()
