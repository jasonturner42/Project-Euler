total_sum = 0

for x in range(1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        print x
        total_sum += x

print total_sum