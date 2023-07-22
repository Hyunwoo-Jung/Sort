# 2. 삽입 정렬
# 정렬된 리스트에 추가할 데이터를 순서대로 비교하여 저장할 위치 찾아 추가

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(1, len(data)):
    temp = data[i] # 현재의 요소를 일시적으로 저장
    j = i - 1
    while (j >= 0) and (data[j] > temp):
        data[j + 1] = data[j] # 요소를 하나씩 뒤로 옮김
        j -= 1
    data[j + 1] = temp #임시 공간에서 되돌림

print(data)