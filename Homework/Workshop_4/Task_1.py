"""
Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""

import math

pi = 1
n = 5
for _ in range(n):
    pi = math.sqrt(2 + pi)
pi = 3 * (2 ** n) * math.sqrt(2 - pi)
print(float('%.3f' % pi))
