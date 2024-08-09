def bubble_sort(arr):
    n = len(arr)
    # 모든 원소를 다 확인할 때까지 반복
    for i in range(n):
        # 이 플래그는 현재 패스에서 교환이 발생했는지 여부를 기록합니다
        swapped = False
        # 마지막 i개의 원소는 이미 정렬되었으므로 확인할 필요 없음
        for j in range(0, n - i - 1):
            # 인접한 두 원소를 비교
            if arr[j] > arr[j + 1]:
                # 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 만약 이번 패스에서 교환이 발생하지 않았다면, 배열은 이미 정렬되어 있는 것입니다
        if not swapped:
            break

# 사용 예제
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("정렬된 배열:", arr)