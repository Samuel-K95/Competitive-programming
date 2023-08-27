import math
r, c = map(int, input().split())
total = math.pi * pow(r, 2)
cheese = math.pi * pow(r-c, 2)

print ("{:.10f}".format((cheese / total) * 100))