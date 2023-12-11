A, B = map(int, input().split())
C = int(input())

T_h = A + C//60
T_m = B + C%60

# T_m < 60
if T_m < 60:
    # T_h >= 24
    if T_h >= 24:
        print(T_h-24, T_m)
    # T_h < 24
    else:
        print(T_h, T_m)
# T_m >= 60
else:
    # T_h+1 >= 24
    if T_h+1 >= 24:
        print(T_h-23, T_m-60)
    # T_h+1 < 24
    else:
        print(T_h+1, T_m-60)