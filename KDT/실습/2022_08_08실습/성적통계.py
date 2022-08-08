import sys

input = sys.stdin.readline

for test_case in range(1, int(input()) + 1):
    nums = list(map(int, input().split()))
    # 입력 중 처음 부분이 리스트의 길이
    k = nums.pop(0)
    # 문제에서 내림차순 했을때 서로의 gap를 원했기 때문에 진행.
    nums.sort(reverse=True)
    gap = 0
    for i in range(k - 1):
        # 갭 차이의 최대를 찾기
        gap = max(gap, nums[i] - nums[i + 1])
    print(f"{'Class'} {test_case}")
    print(f"{'Max'} {max(nums)}, {'Min'} {min(nums)}, {'Largest gap'} {gap}")