#2024-08-10과제

#스택이란??

#스택은 한쪽 끝에서만 데이터를 넣고 뺼수있는 후입선출 형태의 선형 자료구조이다.
#제공연산 종류: 
#pop():스택에서 가장위에 있는 항목을 제거
#push(item):item 하나를 스택의 가장 윗부분에 추가
#peek():스택의 가장위에 있는항목을 반환한다
#isEmpty():스택이 비어있떄 true를 반환한다

#스택의 활용 예시:

#웹 브라우저 방문기록(뒤로가기)
#실행 취소(undo) (되돌리기기능)
#역순 문자열 만들기
#후위 표기법 계산

class ListStack:
    def __init__(self):
        # 스택을 구현하기 위해 빈 리스트를 초기화합니다.
        self.items = []

    def is_empty(self):
        # 스택이 비어 있는지 확인합니다.
        return len(self.items) == 0

    def push(self, item):
        # 스택의 상단에 항목을 추가합니다.
        self.items.append(item)

    def pop(self):
        # 스택의 상단에서 항목을 제거하고 반환합니다.
        if not self.is_empty():
            return self.items.pop()
        else:
            # 스택이 비어 있으면 예외를 발생시킵니다.
            raise IndexError("pop from empty stack")

    def peek(self):
        # 스택의 상단에 있는 항목을 제거하지 않고 반환합니다.
        if not self.is_empty():
            return self.items[-1]
        else:
            # 스택이 비어 있으면 예외를 발생시킵니다.
            raise IndexError("peek from empty stack")

    def size(self):
        # 스택에 있는 항목의 개수를 반환합니다.
        return len(self.items)

# 리스트를 사용한 스택 사용 예제
stack = ListStack()
stack.push(1)  # 스택에 1을 추가합니다.
stack.push(2)  # 스택에 2를 추가합니다.
stack.push(3)  # 스택에 3을 추가합니다.
stack.push(4)
stack.push(5)
stack.push(6)
print(stack.pop())  # 출력: 3 (스택의 상단에서 3을 제거하고 반환합니다.)
print(stack.peek()) # 출력: 2 (스택의 상단에 있는 2를 제거하지 않고 반환합니다.)
print(stack.size()) # 출력: 2 (스택에 있는 항목의 개수를 반환합니다.)
