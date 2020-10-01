
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

a.sort()
print(a[0]*a[1])


