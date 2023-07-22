# 선택 정렬의 구현

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(len(data)):
    min = i # 최소값의 위치를 설정
    for j in range(i + 1, len(data)):
        if data[min] > data[j]:
            min = j # 최소값이 갱신되면 그 위치를 설정

    #최소값의 위치에 현재의 요소를 교환
    data[i], data[min] = data[min], data[i]

print(data)

# 복잡도 : O(n^2)