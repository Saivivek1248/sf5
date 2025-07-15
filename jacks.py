total_jumping_jacks = 0

for i in range(10):
    total_jumping_jacks += 10
    print(f"You did {total_jumping_jacks} jumping jacks.")
    tired = input("Are you tired? (yes/no): ").lower()
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the rest? (yes/no): ").lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {total_jumping_jacks} jumping jacks.")
            break
else:
    print("Congratulations! You completed the workout.")
