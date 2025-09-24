#Survive the semester game

#input
student_name = "Charlestone Mayenga"
current_gpa = 3.75
study_hours = int(10)
social_points = int(50)
stress_level = int(5)


print("Welcome to College Life Simulator!")
print("Your goal: Finish the semester without burning out and keep your GPA strong.")
print("Student Name:", student_name)
print("Current GPA:", current_gpa)
print("Study Hours:", study_hours)
print("Social Points:", social_points)
print("Stress Level:", stress_level)

#Decision 1

print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice (A/B/C): ")
if choice == "A":
    if current_gpa < 2.5:
        print("You took it easy, but your GPA doesn’t rise enough. Professors warn you to step up.")
        study_hours += 5
        stress_level += 1
    else:
        print("Smart choice! You balance study and rest. GPA improves slowly.")
        current_gpa += 0.2
        study_hours += 8
        stress_level += 2

elif choice == "B":
    if current_gpa >= 3.0:
        print("Balanced course load. You grind steadily.")
        current_gpa += 0.1
        study_hours += 10
        stress_level += 3
    else:
        print("You struggle to keep up but survive.")
        study_hours += 7
        stress_level += 4

elif choice == "C":
    if current_gpa >= 3.5:
        print("You thrive under pressure! Professors praise your effort.")
        current_gpa += 0.2
        study_hours += 15
        stress_level += 5
    else:
        print("Too heavy! You burn out, miss deadlines, and grades slip.")
        current_gpa -= 0.3
        study_hours += 12
        stress_level += 7

else:
    print("BInvalid choice. You waste time deciding, stress rises!")
    stress_level += 2

# Show updated stats
print("\n📊 End of Round Stats:")
print(f"GPA: {round(current_gpa, 2)}")
print(f"Study Hours: {study_hours}")
print(f"Stress Level: {stress_level}")

# Game Over checks
if stress_level > 10:
    print("\n⚠️ You burned out. Game Over.")
elif current_gpa < 2.0:
    print("\n⚠️ Academic probation. Game Over.")
else:
    print("\n✅ You survived this round! Keep going next semester...")
        

