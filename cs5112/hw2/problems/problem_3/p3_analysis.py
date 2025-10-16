import random
import time
import statistics
import matplotlib.pyplot as plt
from p3_a import LinkedList
from p3_b import SkipList

def bench_insert(ds_factory, keys):
    ds = ds_factory()
    t0 = time.perf_counter()
    for k in keys:
        ds.insert(k)
    t1 = time.perf_counter()
    return t1 - t0

def bench_search(ds_factory, keys, queries):
    ds = ds_factory()
    for k in keys:
        ds.insert(k)
    t0 = time.perf_counter()
    hits = 0
    for q in queries:
        if ds.search(q) is not None:
            hits += 1
    t1 = time.perf_counter()
    return t1 - t0, hits

def bench_delete(ds_factory, keys):
    ds = ds_factory()
    for k in keys:
        ds.insert(k)
    t0 = time.perf_counter()
    for k in keys:
        ds.delete(k)
    t1 = time.perf_counter()
    return t1 - t0

def ll_factory():
    return LinkedList()

def sl_factory():
    return SkipList(max_level=16, p=0.5)

def run():
    random.seed(42)
    sizes = [200, 400, 800, 1600, 3200]
    trials = 5

    results = {
        "insert": {"LinkedList": [], "SkipList": []},
        "search": {"LinkedList": [], "SkipList": []},
        "delete": {"LinkedList": [], "SkipList": []},
    }

    for n in sizes:
        base_keys = random.sample(range(10_000_000), n)
        present_q = random.sample(base_keys, min(n, max(1000, n // 2)))
        absent_pool = set(range(10_000_000)) - set(base_keys)
        absent_q = random.sample(list(absent_pool), len(present_q))
        queries = []
        for i in range(len(present_q)):
            if i % 2 == 0:
                queries.append(present_q[i])
            else:
                queries.append(absent_q[i])

        for name, factory in [("LinkedList", ll_factory), ("SkipList", sl_factory)]:
            ins_times = []
            sea_times = []
            del_times = []
            for _ in range(trials):
                keys = list(base_keys)
                random.shuffle(keys)
                ins_times.append(bench_insert(factory, keys))
                t_search, _hits = bench_search(factory, keys, queries)
                sea_times.append(t_search)
                del_times.append(bench_delete(factory, keys))
            results["insert"][name].append((n, statistics.mean(ins_times), statistics.pstdev(ins_times)))
            results["search"][name].append((n, statistics.mean(sea_times), statistics.pstdev(sea_times)))
            results["delete"][name].append((n, statistics.mean(del_times), statistics.pstdev(del_times)))

    for op in ["insert", "search", "delete"]:
        plt.figure(figsize=(7, 4.5))
        for name in ["LinkedList", "SkipList"]:
            xs = [n for n, _, _ in results[op][name]]
            ys = [avg for _, avg, _ in results[op][name]]
            plt.plot(xs, ys, marker="o", label=name)
        plt.xlabel("n")
        plt.ylabel("time (s)")
        plt.title(f"{op.capitalize()} performance vs n")
        plt.grid(True, linestyle=":")
        plt.legend()
        plt.tight_layout()
        plt.show()

    print("Average times (seconds):")
    for op in ["insert", "search", "delete"]:
        print(op.upper())
        header = "n".rjust(8) + " | " + " | ".join(f"{name:^12}" for name in ["LinkedList", "SkipList"])
        print(header)
        print("-" * len(header))
        for i, n in enumerate(sizes):
            row = f"{n:8d}"
            for name in ["LinkedList", "SkipList"]:
                _, avg, sd = results[op][name][i]
                row += f" | {avg:10.6f}±{sd:>10.6f}"
            print(row)
        print()

if __name__ == "__main__":
    run()
