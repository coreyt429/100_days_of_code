student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
sum_of_scores = 0
min_of_scores = 10**9
max_of_scores = 0
for score in student_scores:
    sum_of_scores += score
    if score > max_of_scores:
        max_of_scores = score
    if score < min_of_scores:
        min_of_scores = score
print(f"sum a: {sum_of_scores}")
print(f"sum b: {sum(student_scores)}")
assert(sum_of_scores == sum(student_scores))
print(f"min a: {min_of_scores}")
print(f"min b: {min(student_scores)}")
print(f"max a: {max_of_scores}")
print(f"max b: {max(student_scores)}")