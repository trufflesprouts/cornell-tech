import random
import time
import math
import cmath
from math import pi
import matplotlib.pyplot as plt
from statistics import median

# ============================================================
# Implementations — inputs/outputs are MSB-first bit lists
# ============================================================

def _bits_to_int_msb(bits):
    v = 0
    for b in bits:
        v = (v << 1) | (1 if b else 0)
    return v

def _int_to_bits_msb(n):
    if n == 0:
        return [0]
    out = []
    while n:
        out.append(n & 1)
        n >>= 1
    return list(reversed(out))

def reference_multiply(x, y):
    xi = _bits_to_int_msb(x)
    yi = _bits_to_int_msb(y)
    return _int_to_bits_msb(xi * yi)

# ---- Karatsuba ----

def _karatsuba_int(a, b):
    if a == 0 or b == 0:
        return 0
    # Use schoolbook when small to reduce overhead
    if a.bit_length() <= 32 or b.bit_length() <= 32:
        return a * b
    n = max(a.bit_length(), b.bit_length())
    m = n // 2
    a0 = a & ((1 << m) - 1)
    a1 = a >> m
    b0 = b & ((1 << m) - 1)
    b1 = b >> m
    z0 = _karatsuba_int(a0, b0)
    z2 = _karatsuba_int(a1, b1)
    z1 = _karatsuba_int(a0 + a1, b0 + b1) - z0 - z2
    return (z2 << (2 * m)) + (z1 << m) + z0

def karatsuba(x, y):
    xi = _bits_to_int_msb(x)
    yi = _bits_to_int_msb(y)
    return _int_to_bits_msb(_karatsuba_int(xi, yi))

# ---- FFT-based ----

def _fft(a, invert):
    n = len(a)
    if n == 1:
        return a
    ae = _fft(a[0::2], invert)
    ao = _fft(a[1::2], invert)
    ang = 2 * pi / n * (-1 if invert else 1)
    w = 1+0j
    wn = cmath.exp(1j * ang)
    out = [0j] * n
    for k in range(n // 2):
        u = ae[k]
        v = w * ao[k]
        out[k] = u + v
        out[k + n // 2] = u - v
        w *= wn
    if invert:
        return [z / 2 for z in out]
    else:
        return out

def _convolve_ints(a_digits, b_digits):
    # a_digits, b_digits are LSB-first digits (base 2)
    need = len(a_digits) + len(b_digits) - 1
    n = 1
    while n < need:
        n <<= 1
    fa = list(map(complex, a_digits)) + [0j] * (n - len(a_digits))
    fb = list(map(complex, b_digits)) + [0j] * (n - len(b_digits))
    fa = _fft(fa, invert=False)
    fb = _fft(fb, invert=False)
    fc = [fa[i] * fb[i] for i in range(n)]
    fc = _fft(fc, invert=True)
    return [int(round(fc[i].real)) for i in range(need)]

def fft(x, y):
    # Convert to LSB-first
    a = list(reversed([1 if b else 0 for b in x]))
    b = list(reversed([1 if b else 0 for b in y]))
    if not a or not b:
        return [0]
    conv = _convolve_ints(a, b)
    # Carry in base 2
    carry = 0
    for i in range(len(conv)):
        total = conv[i] + carry
        conv[i] = total & 1
        carry = total >> 1
    while carry:
        conv.append(carry & 1)
        carry >>= 1
    res = list(reversed(conv))
    i = 0
    while i < len(res) - 1 and res[i] == 0:
        i += 1
    return res[i:]

# ============================================================
# Benchmarking utilities — self-contained, no file I/O
# ============================================================

def gen_bits(n):
    """Generate an MSB-first bit list of length n with MSB=1 (no leading zeros)."""
    if n <= 0:
        return [0]
    arr = [random.getrandbits(1) for _ in range(n)]
    arr[0] = 1
    return arr

def bits_to_int_msb(bits):
    v = 0
    for b in bits:
        v = (v << 1) | (1 if b else 0)
    return v

def time_once(fn, x, y):
    t0 = time.perf_counter()
    out = fn(x, y)
    t1 = time.perf_counter()
    return (t1 - t0), out

def trials_for_size(n):
    """Enough trials for stability; taper as n grows to keep total runtime reasonable."""
    if n <= 128: return 12
    if n <= 512: return 10
    if n <= 2048: return 8
    if n <= 8192: return 6
    return 4

def choose_sizes(n_min=16, n_max=16384, steps=9):
    """
    Powers-of-two sweep that samples *enough* points to clearly differentiate curves.
    Defaults: 16 .. 16384 (9 points). Adjust 'steps' if needed.
    """
    sizes = []
    n = n_min
    while n <= n_max and len(sizes) < steps:
        sizes.append(n)
        n *= 2
    return sizes

def benchmark():
    random.seed(2025)
    sizes = choose_sizes()  # 16,32,...,16384
    results = []  # list of dicts with medians
    # Warmup
    xw, yw = gen_bits(64), gen_bits(64)
    for fn in (reference_multiply, karatsuba, fft):
        fn(xw, yw)

    print("n_bits |   reference (ms) |    karatsuba (ms) |          fft (ms)")
    print("-"*65)

    for n in sizes:
        T = trials_for_size(n)
        # Fix the random pairs for fairness across algorithms
        pairs = [(gen_bits(n), gen_bits(n)) for _ in range(T)]

        ref_times, kar_times, fft_times = [], [], []

        for (x, y) in pairs:
            tref, rref = time_once(reference_multiply, x, y)
            tkar, rkar = time_once(karatsuba, x, y)
            tfft, rfft = time_once(fft, x, y)

            # Correctness check via integer values
            ref_i = bits_to_int_msb(rref)
            if ref_i != bits_to_int_msb(rkar) or ref_i != bits_to_int_msb(rfft):
                raise AssertionError(f"Mismatch detected at n={n}")

            ref_times.append(tref)
            kar_times.append(tkar)
            fft_times.append(tfft)

        row = {
            "n": n,
            "ref_med": median(ref_times),
            "kar_med": median(kar_times),
            "fft_med": median(fft_times),
        }
        results.append(row)
        print(f"{n:6d} | {row['ref_med']*1e3:15.3f} | {row['kar_med']*1e3:15.3f} | {row['fft_med']*1e3:15.3f}")

    return results

# ============================================================
# Run & Plot (no disk writes)
# ============================================================

def plot_results(results):
    xs     = [r["n"] for r in results]
    ref_y  = [r["ref_med"] for r in results]
    kar_y  = [r["kar_med"] for r in results]
    fft_y  = [r["fft_med"] for r in results]

    # Linear scale
    plt.figure()
    plt.plot(xs, ref_y, marker="o", label="reference")
    plt.plot(xs, kar_y, marker="o", label="karatsuba")
    plt.plot(xs, fft_y, marker="o", label="fft")
    plt.xlabel("Input size (bits per operand)")
    plt.ylabel("Median time (s)")
    plt.title("Binary multiplication runtime (linear scale)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()

    # Log–log scale
    plt.figure()
    plt.plot(xs, ref_y, marker="o", label="reference")
    plt.plot(xs, kar_y, marker="o", label="karatsuba")
    plt.plot(xs, fft_y, marker="o", label="fft")
    plt.xscale("log", base=2)
    plt.yscale("log")
    plt.xlabel("Input size (bits per operand, log2)")
    plt.ylabel("Median time (s, log)")
    plt.title("Binary multiplication runtime (log–log)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    results = benchmark()
    # Optional quick textual takeaway:
    # print("\nObservation: curves are clearly separated at larger n; "
    #       "Karatsuba outpaces the reference in asymptotics, while the pure-Python FFT "
    #       "has higher constants and shines mainly for very large n.")
    plot_results(results)
