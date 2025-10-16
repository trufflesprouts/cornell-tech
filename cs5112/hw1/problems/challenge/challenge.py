import cmath
from math import pi

def _bits_to_int(bits):
    result = 0
    for bit in bits:
        result = (result << 1) | bool(bit)
    return result

def _int_to_bits(n):
    if n == 0:
        return [0]
    
    bits = []
    while n:
        bits.append(n & 1)
        n >>= 1
    return bits[::-1]

def reference_multiply(x, y):
    xi = _bits_to_int(x)
    yi = _bits_to_int(y)
    prod = xi * yi
    return _int_to_bits(prod)


def _karatsuba_int(a, b):
    if a == 0 or b == 0:
        return 0
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
    xi = _bits_to_int(x)
    yi = _bits_to_int(y)
    prod = _karatsuba_int(xi, yi)
    return _int_to_bits(prod)   

def _fft(a, invert):
    n = len(a)
    if n == 1:
        return a
    a_even = _fft(a[0::2], invert)
    a_odd = _fft(a[1::2], invert)
    ang = 2 * pi / n * (-1 if invert else 1)
    w = 1+0j
    wn = cmath.exp(1j * ang)
    out = [0j] * n
    for k in range(n // 2):
        u = a_even[k]
        v = w * a_odd[k]
        out[k] = u + v
        out[k + n // 2] = u - v
        w *= wn
    if invert:
        return [z / 2 for z in out]
    else:
        return out

def _convolve_ints(a_digits, b_digits):
    n = 1
    need = len(a_digits) + len(b_digits) - 1
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
    a = list(reversed([1 if b else 0 for b in x]))
    b = list(reversed([1 if b else 0 for b in y]))
    if not a or not b:
        return [0]
    conv = _convolve_ints(a, b)
    carry = 0
    for i in range(len(conv)):
        total = conv[i] + carry
        conv[i] = total & 1
        carry = total >> 1
    while carry:
        conv.append(carry & 1)
        carry >>= 1
    res = list(reversed(conv))
    idx = 0
    while idx < len(res) - 1 and res[idx] == 0:
        idx += 1
    return res[idx:]