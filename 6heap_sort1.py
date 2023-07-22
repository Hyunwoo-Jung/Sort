# 4. 힙 정렬
# 스택과 큐는 한방향을 데이터 꺼낼 수 있음
# 힙은 트리 구조로 구성
# 힙에 요소 추가 : 트리의 마지막에 요소 추가, 추가된 요소와 부모 요소 비교, 
# 부모보다 작으면 부모와 교환, 부모 쪽이 작으면 교환 하지 않고 종료
# 복잡도 : O(logn)

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# 힙 구성
for i in range(len(data)):
    j = i
    while (j > 0) and (data[(j - 1) // 2] < data[j]):
        data[(j - 1) // 2], data[j] = data[j], data[(j - 1) // 2] # 부모 노드와 교환
        j = (j - 1) // 2 # 부모 노드의 위치로 이동

# 정렬 실행
for i in range(len(data), 0, -1):
    # 힙의 맨 앞과 교환
    data[i - 1], data[0] = data[0], data[i - 1]
    j = 0 # 힙의 맨 앞부터 시작
    while ((2 * j + 1 < i - 1) and (data[j] < data[2 * j + 1])) \
        or ((2 * j + 2 < i - 1) and (data[j] < data[2 * j + 2])):
        if (2 * j + 2 == i - 1) or (data[2 * j + 1] > data[2 * j + 2]):
            # 왼쪽 아래와 교환
            data[j], data[2 * j + 1] = data[2 * j + 1], data[j]
            # 왼쪽 아래로 이동
            j = 2 * j + 1
        else:
            # 오른쪽 아래와 교환
            data[j], data[2 * j + 2] = data[2 * j + 2], data[j]
            # 오른쪽 아래로 이동
            j = 2 * j + 2

print(data)

# 복잡도 : O(nlogn)