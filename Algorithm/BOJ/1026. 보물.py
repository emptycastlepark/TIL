import heapq

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B = [-b for b in B]
heapq.heapify(A); heapq.heapify(B)
S = 0
for _ in range(N):
    a, b = heapq.heappop(A), -heapq.heappop(B)
    S += a * b
print(S)