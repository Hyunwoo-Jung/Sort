# 3. 버블 정렬
# 리스트에서 인접한 데이터를 비교해 대소 관계의 순서가 다르면 정렬해나가는 방법

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(len(data)):
    for j in range(len(data) - i - 1): # 정렬된 부분을 제외하고 반복 실행
        if data[j] > data[j + 1]: # 앞쪽이 큰 경우
            data[j], data[j + 1] = data[j + 1], data[j]

print(data)

# 복잡도 : O(n^2)