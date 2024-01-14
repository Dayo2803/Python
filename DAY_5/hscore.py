high_score = input("Give a list of the student scores\n").split()
for n in range(0, len(high_score)):
    high_score[n] = int(high_score[n])
# print(high_score)

student_score = 0
for score in high_score:
    if score > student_score:
        student_score = score
print(f"The heighest score is {student_score}")