# 범용적인 힙 정렬 구현

def heapify(data, i):
    left = 2 * i + 1 # 왼쪽 아래에 위치
    right = 2 * i + 2 # 오른쪽 아래에 위치
    size = len(data) - 1
    min = i
    if left <= size and data[min] > data[left]: # 왼쪽 아래가 작을 때
        min = left
    if right <= size and data[min] > data[right]: # 왼쪽 아래가 작을 때
        min = right
    if min != i: # 교환이 발생하는 경우
        data[i], data[min] = data[min], data[i]
        heapify(data, min) # 힙을 재구성

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# 힙 구성
for i in reversed(range(len(data) // 2)):
    heapify(data, i)

# 정렬 실행
sorted_data = []
for _ in range(len(data)):
    data[0], data[-1] = data[-1], data[0] # 마지막 노드와 맨 앞 노드를 교체
    sorted_data.append(data.pop()) # 최소값인 노드를 꺼내 정렬된 상태로 표시
    heapify(data, 0) # 힙을 재구성

print(sorted_data)