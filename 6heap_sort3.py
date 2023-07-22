# 라이브러리 활용

import heapq

def heap_sort(array):
    h = array.copy()
    heapq.heapify(h) # 힙 구성
    return [heapq.heappop(h) for _ in range(len(array))] # 데이터를 꺼내면서 정렬된 리스트를 작성

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

print(heap_sort(data))