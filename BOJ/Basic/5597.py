student_list = []

for i in range(28):
    student_list.append(int(input()))

non_list = []
for j in range(1,31):
    if j not in student_list:
        non_list.append(j)

print(min(non_list), max(non_list), sep='\n')