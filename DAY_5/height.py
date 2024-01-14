# std_heights = input("Input a list of student heights ").split()
# for n in range(0, len(std_heights)):
#     std_heights[n] = int(std_heights[n])
# print(std_heights)


# std_heights_sum = sum(std_heights)
# avg_height = std_heights_sum / len(std_heights)
# print(avg_height)

std_heights = input("Input a list of student heights ").split()
for n in range(0, len(std_heights)):
    std_heights[n] = int(std_heights[n])

std_heights_sum = 0
for height in std_heights:
    std_heights_sum += height
print(std_heights_sum)
avg_height = std_heights_sum / len(std_heights)
print(int(avg_height))