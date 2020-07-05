import sys
import threading
def compute_height(n, parents):
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height
def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
