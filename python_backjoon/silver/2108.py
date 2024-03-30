# 산술평균 : round(sum(N) / N, 1)
# 중앙값 : sum(N).sort[N//2]
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값   여러 개 있을 때는 두 번째로 작은 값 출력
# 범위 : max - min
N = int(input())
num_lst = [int(input()) for _ in range(N)]
num_lst.sort()

num_dict = {i: 0 for i in num_lst}
for k in num_lst:
    num_dict[k] += 1

print(int(round(sum(num_lst)/N, 0)))
print(num_lst[N//2])
mk = []
mv = 0
for k, v in num_dict.items():
    if v > mv:
        mv = v
for k in num_dict:
    if num_dict[k] == mv:
        mk.append(k)

if len(mk) > 1:
    print(mk[1])
else:
    print(mk[0])

print(num_lst[-1] - num_lst[0])


# # 산술 평균 계산
# average = int(round((sum(num_lst)) / N, 0))
#
# # 중앙값 계산
# mid = num_lst[N // 2]
#
# # 최빈값 계산
# num_cnt = {}
# mx_frq = 0
# mn = None
# scnd = None
# for num in num_lst:
#     num_cnt[num] = num_cnt.get(num, 0) + 1
#     if num_cnt[num] > mx_frq:  # 최빈값 젤 작은 숫자
#         mx_frq = num_cnt[num]
#         mn = num
#     elif num_cnt[num] == mx_frq and (scnd is None or mn < num < scnd):  # 최빈값 두 번째
#         scnd = num
#
# # 범위계산
# rng = num_lst[-1] - num_lst[0]
#
# print(average)
# print(mid)
# if scnd is None:
#     print(mn)
# else:
#     print(scnd)
# print(rng)
# print()