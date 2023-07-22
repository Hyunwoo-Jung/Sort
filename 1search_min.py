# 1. 선택 정렬
# 리스트에서 가장 작은 요소의 위치 찾기

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
min = 0 # 최소값 위치의 초기값으로 맨 앞을 설정

for i in range(1, len(data)):
    if data[min] > data[i]:
        min = i # 최소값이 갱신되면 해당 위치를 저장

print(min)