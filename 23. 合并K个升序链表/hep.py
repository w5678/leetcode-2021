import heapq as hq

data=[12,3,42,5,12,23,123,2312,13]


heap=[]
for k in data:
    hq.heappush(heap,k)
print(heap)

print(hq.heappop(heap))
print(hq.heappop(heap))
print(hq.heappop(heap))
print(hq.heappop(heap))
