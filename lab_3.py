A = list(map(int, input("Enter the first sequence of integers: ").split()))
B = list(map(int, input("Enter the second sequence of integers: ").split()))
common_elements = []

count_A = {}
count_B = {}

for x in A:
    if x in count_A:
        count_A[x] += 1
    else:
        count_A[x] = 1

for x in B:
    if x in count_B:
        count_B[x] += 1
    else:
        count_B[x] = 1

for key in count_A:
    if key in count_B:
         common_elements.extend([key] * min(count_A[key], count_B[key]))

print(len(common_elements))