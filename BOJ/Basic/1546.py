# 과목 수
N = int(input())

# 점수 입력
score_list = list(map(int, input().split()))

# 본인 점수의 최댓값 저장
M = max(score_list)

sum = 0
for i in range(len(score_list)):
    sum += score_list[i]/M*100

print(sum/len(score_list))