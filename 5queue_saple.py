# FIFO (선입 선출)
# 큐 : 스택과 반대로 저장 순서대로 데이터를 꺼내는 구조
# 인큐 : 큐에 데이터 저장하는 것
# 디큐 : 큐에 데이터 꺼내는 것

import queue

q = queue.Queue()
q.put(3) # 큐에 '3'을 추가
q.put(5) # 큐에 '5'를 추가
q.put(2) # 큐에 '2'를 추가

temp = q.get() # 큐에서 꺼내기
print(temp)

temp = q.get() # 큐에서 꺼내기
print(temp)

q.put(4) # 큐에 '4'를 추가

temp = q.get() # 큐에서 꺼내기
print(temp)

# queue 모듈을 불러올 때 파일명을 queue.py처럼 지정하면 queue 모듈을 읽을 수 없고 오류 발생