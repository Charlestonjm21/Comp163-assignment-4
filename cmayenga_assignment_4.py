#Survive the semester game
#All code was written by me, But I used ChatGPT to help me understand complex nested if statements, also help me find the error on my code

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
    
#Decision 2
study_options = ["Programming", "Math", "English", "History"]
user_choice = input("\nChoose a subject to focus your study hours on (Programming/Math/English/History): ")
current_gpa = float(current_gpa)
social_points = int(social_points)


#Used chatGPT to help unserstand if statements below
if user_choice in study_options:
    print(f"You chose to focus on {user_choice}. That's a valid study area.")
else:
    print("Invalid choice. Please choose a valid subject next time.")

if user_choice not in study_options:
    print(f"'{user_choice}' is not a valid option. please choose correctly.")
            
if (current_gpa < 3.0 or social_points < 20) and (user_choice == "Programming" or user_choice == "Math"):
    print("Decision 2: High priority on focused studying in the chosen area due to GPA/social points concerns.")
elif current_gpa >= 3.8 and social_points >= 80 and not (user_choice == "Programming" or user_choice == "Math"):
    print("Decision 2: Balanced approach to studying and socializing, maintaining strong GPA and social life.")
else:
    print("Decision 2: Moderate focus on studying with some social activities to keep stress in check.")
        

# Step 4: Final Semester Assessment

print("\n🎓 Final Semester Assessment...")

# Type check using identity operators
if type(current_gpa) is float and type(study_hours) is int and type(stress_level) is int:
    print("✅ Stats are valid for final evaluation.")
else:
    print("❌ Invalid stat types detected. Ending simulation early.")
    exit()

# Nested conditions with multiple endings, Used ChatGPT to help me understand why my code wasn't working
if current_gpa >= 3.8:
    if stress_level <= 6:  # Nested condition
        print("🏆 Ending: Dean’s List! You balanced everything brilliantly.")
    else:
        print("😓 Ending: Great grades but at the cost of your mental health. Be careful next semester!")
elif 2.5 <= current_gpa < 3.8:
    if stress_level < 10:  # Nested inside GPA range
        print("😊 Ending: Balanced Success! You passed with decent grades and kept stress manageable.")
    else:
        print("⚠️ Ending: You passed but nearly burned out. Recovery is needed before next semester.")
else:
    if stress_level is not 0:  # Identity operator example
        print("📉 Ending: You barely made it. GPA too low and stress took its toll.")
    else:
        print("😶 Ending: Somehow stress-free, but academics weren’t enough to succeed.")

# Display Final Statistics
print("\n📊 Final Semester Statistics:")
print(f"Student: {student_name}")
print(f"Final GPA: {round(current_gpa, 2)}")
print(f"Total Study Hours: {study_hours}")
print(f"Final Stress Level: {stress_level}")
print(f"Social Points: {social_points}")



