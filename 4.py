from functools import reduce

sym = (reduce(lambda x, y: x + y, range(101)))**2
sym_kb = reduce(lambda x, y: x + y**2, range(101))
razn = sym - sym_kb