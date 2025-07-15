import random

rolls = [random.randint(1, 6) for _ in range(20)]

count_6 = rolls.count(6)
count_1 = rolls.count(1)
two_6s_in_row = sum(1 for i in range(len(rolls) - 1) if rolls[i] == 6 and rolls[i + 1] == 6)

print("Rolled a 6:", count_6, "times")
print("Rolled a 1:", count_1, "times")
print("Rolled two 6s in a row:", two_6s_in_row, "times")
