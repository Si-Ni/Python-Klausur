import measure_mem

g = (n for n in range(10000))
g = (n for n in range(100000))
g = (n for n in range(1000000))

measure_mem.show_memory()

g = list(range(10000))
g = list(range(100000))
g = list(range(1000000))

measure_mem.show_memory()