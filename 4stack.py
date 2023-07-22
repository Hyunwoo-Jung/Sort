# 리스트의 맨 앞이나 끝에서 데이터를 꺼내거나 넣어서 효율적으로 처리하는 것을 고려

# LIFO (후입 선출)
# 스택 : 리스트에 추가 및 제거를 반복할 때 마지막에 저장한 데이터부터 꺼내는 구조
# 푸시 : 스택에 데이터 저장하는 것
# 팝 : 스택에 데이터 꺼내는 것

stack = []

stack.append(3) # 스택에 '3'을 추가
stack.append(5) # 스택에 '5'를 추가
stack.append(2) # 스택에 '2'를 추가

temp = stack.pop() # 스택에서 꺼내기
print(temp)

temp = stack.pop() # 스택에서 꺼내기
print(temp)

stack.append(4) # 스택에 '4'를 추가

temp = stack.pop() # 스택에서 꺼내기
print(temp)