A = list(map(int, input("Enter the first sequence of integers: ").split()))
B = list(map(int, input("Enter the second sequence of integers: ").split()))
length = 0
common_elements = []

common_elements_1 = None

for i in range(len(A)):
    for j in range(len(B)):
        elements = []
        x = i
        y = j
        while x < len(A) and y < len(B) and A[x] == B[y]:
            elements.append(A[x])
            x += 1
            y += 1
        if len(elements) > length:
            length = len(elements)
            common_elements = elements

            if common_elements_1 is None:
                common_elements_1 = elements

print("Longest common subsequence length:", length)

if common_elements_1:
    print("First common subsequence length:", len(common_elements_1))
else:
    print("No common subsequence found.")