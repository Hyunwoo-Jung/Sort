# 처리 중 교환이 일어났는지 저장, 교환이 일어나지 않았으면 이후 처리를 하지 않음

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

change = True
for i in range(len(data)):
    if not change: # 요소 교환이 일어나지 않으면 종료
        break
    change = False
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            change = True # 요소 교환이 발생

print(data)