from collections import Counter

symbols = ['A', 'A', 'B', 'C', 'A', 'A', 'B'] # Freq: A=4, B=2, C=1
freq = Counter(symbols)
print(freq)  # Output: Counter({'A': 4, 'B': 2, 'C': 1})   