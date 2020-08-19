# 프로그래머스 카카오 2019 여름 인턴십
# 이분탐색: 기준 값에 대해 반으로 나누어 기준보다 크거나 작으면 반으로 자르고 다시 탐색
# 효율성때문에 알고리즘이 생각이 나지 않아 인터넷을 참고했음...

def bin_search(left, right, k,stones):
    mid = (left + right) // 2
    cnt = 0
    for i in stones:
        if i < mid:
            cnt += 1
        else:
            cnt = 0
        if cnt >= k:
            return False
    return True

def solution(stones, k):
    left = 1
    right = max(stones) + 1

    while (left < right-1):
        if bin_search(left, right, k,stones):
            left = (left + right) // 2
        else:
            right = (left + right) // 2

    return left
