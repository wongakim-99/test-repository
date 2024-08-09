def myfunction():
    print("Hello World")
# 분할 함수 정의 (by Lomuto)
def partition(A, low, high):
    pivot_idx = low  # 피벗의 인덱스를 임의의 값으로 설정 (현재는 제일 왼쪽 값으로 설정)
    pivot = A[pivot_idx]

    A[pivot_idx], A[high] = A[high], A[pivot_idx]  # 비교를 위해 피벗을 가장 오른쪽 값과 swap

    i = low
    for j in range(low, high):
        if A[j] < pivot:  # 인덱스 j는 피벗보다 작은 값을 찾아서, A[i]와 swap
            A[i], A[j] = A[j], A[i]
            i += 1

    pivot_idx = i  # 반복문을 마친 배열에서 i는 피벗의 인덱스가 되어야 함.
    A[pivot_idx], A[high] = A[high], A[pivot_idx]

    return pivot_idx


# 퀵 정렬 함수 정의
def quick_sort(A, low, high):
    if low < high:
        pivot_idx = partition(A, low, high)  # 분할 함수를 진행하여 피벗을 기준으로 분할을 진행
        quick_sort(A, low, pivot_idx - 1)  # 분할의 왼쪽 부분에 대해서 재귀
        quick_sort(A, pivot_idx + 1, high)  # 분할의 오른쪽에 대해서 재귀
        
# 테스트 코드
if __name__ == "__main__":
    A = [5, 6, 4, 0, 2, 1, 7, 9, 3, 8]
    low, high = 0, len(A)-1

    print(f"BEFORE QUICK_SORT : {A}")
    quick_sort(A, low, high)
    print(f"AFTER QUICK_SORT  : {A}")