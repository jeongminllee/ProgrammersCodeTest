solution = lambda a, n:sorted(a, key=lambda x:(abs(x-n), x))[0]
