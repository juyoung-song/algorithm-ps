H, M = map(int, input().split())

# 분 변화 O(분 >= 45)
# 시 변화 X
if M>=45:
    print(H, M-45)

# 분 변화 O(분 < 45) 
else:
    # 시 변화 -1
    if H==0:
        print(23, M+15)
    # 시 변화 00->23(시 == 0)
    else:
        print(H-1, M+15)