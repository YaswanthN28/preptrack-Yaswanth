print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)

# Step 1: Student Name Validation
while True:
    student_name = input("Enter student name: ").strip()
    if student_name != "":
        break
    print("Student name cannot be empty.")

# Registration Number
registration_number = input("Enter registration number: ")

# Step 2: Graduation Year Validation
while True:
    graduation_year = int(input("Enter graduation year: "))
    if 2024 <= graduation_year <= 2026:
        break
    print("Invalid graduation year. Must be between 2024 and 2026.")

# Step 3: Attendance Validation
while True:
    attendance = float(input("Enter attendance percentage: "))
    if 0 <= attendance <= 100:
        break
    print("Invalid attendance. Enter a value between 0 and 100.")

# Step 4: Project Validation
while True:
    project_input = input(
        "Has the student completed the required project? (yes/no): "
    ).lower()

    if project_input == "yes":
        project_completed = True
        break
    elif project_input == "no":
        project_completed = False
        break
    else:
        print("Invalid input. Enter yes or no.")

# Step 5: Profile Verification
while True:
    profile_input = input(
        "Is the student profile verified? (yes/no): "
    ).lower()

    if profile_input == "yes":
        profile_verified = True
        break
    elif profile_input == "no":
        profile_verified = False
        break
    else:
        print("Invalid input. Enter yes or no.")

# Variables
total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0

# Step 6: Practice for 7 Days
for day in range(1, 8):

    while True:
        score = int(
            input(
                f"Enter Day {day} score (0-100) or -1 for absent: "
            )
        )

        if score == -1 or (0 <= score <= 100):
            break

        print("Invalid score. Please enter -1 or a value from 0 to 100.")

    if score == -1:
        absent_days += 1
        print(f"Day {day} Result : Absent")
        continue

    attempted_days += 1
    total_score += score

    if not first_attempt_found:
        highest_score = score
        lowest_score = score
        highest_score_day = day
        lowest_score_day = day
        first_attempt_found = True
    else:
        if score > highest_score:
            highest_score = score
            highest_score_day = day

        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day

    if score >= 75:
        strong_days += 1
        passed_days += 1
        print(f"Day {day} Result : Strong")

    elif score >= 60:
        satisfactory_days += 1
        passed_days += 1
        print(f"Day {day} Result : Satisfactory")

    elif score >= 40:
        improvement_days += 1
        failed_days += 1
        print(f"Day {day} Result : Needs Improvement")

    else:
        critical_days += 1
        failed_days += 1
        print(f"Day {day} Result : Critical")

        if not critical_score_found:
            critical_score_found = True
            first_critical_day = day
            first_critical_score = score

# Step 7: Average
if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0

# Step 8: Eligibility
graduation_eligible = 2025 <= graduation_year <= 2027
attendance_eligible = attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)

# Step 9: Final Status
if attempted_days == 0:
    final_status = "Practice Not Evaluated"
    primary_blocker = "No practice attempted"
    next_action = "Attempt the required coding practices"

elif critical_score_found:
    final_status = "Critical Support Required"
    primary_blocker = (
        f"Critical score found on Day {first_critical_day}"
    )
    next_action = "Revise the concepts from the first critical day"

elif attempted_days < 6:
    final_status = "Practice Incomplete"
    primary_blocker = "Fewer than six practices attempted"
    next_action = "Complete at least six practice days"

elif passed_days < 4:
    final_status = "Insufficient Passed Practices"
    primary_blocker = "Less than four passed practices"
    next_action = "Pass at least four coding practices"

elif average_score < 70:
    final_status = "Practice Improvement Required"
    primary_blocker = "Average score below 70"
    next_action = "Improve the average score to at least 70"

elif attendance < 75:
    final_status = "Attendance Improvement Required"
    primary_blocker = "Attendance below 75%"
    next_action = "Improve attendance to at least 75 percent"

elif not graduation_eligible:
    final_status = "Graduation Criteria Not Met"
    primary_blocker = "Graduation year not eligible"
    next_action = "Check the eligible graduation-year requirement"

elif not project_completed:
    final_status = "Application On Hold"
    primary_blocker = "Required project not completed"
    next_action = "Complete the required project"

elif not profile_verified:
    final_status = "Application On Hold"
    primary_blocker = "Profile not verified"
    next_action = "Complete profile verification"

else:
    final_status = "Ready for Mock Interview"
    primary_blocker = "None"
    next_action = "Proceed to placement mock interviews"

# Step 10: Report
print()
print("=" * 50)
print("              PREPTRACK REPORT")
print("=" * 50)

print("\nSTUDENT PROFILE\n")

print(f"Student Name             : {student_name}")
print(f"Registration Number      : {registration_number}")
print(f"Graduation Year          : {graduation_year}")
print(f"Attendance               : {attendance}%")
print(f"Project Completed        : {'Yes' if project_completed else 'No'}")
print(f"Profile Verified         : {'Yes' if profile_verified else 'No'}")

print("\nPRACTICE SUMMARY\n")

print("Total Practice Days      : 7")
print(f"Attempted Days           : {attempted_days}")
print(f"Absent Days              : {absent_days}")
print(f"Passed Days              : {passed_days}")
print(f"Failed Days              : {failed_days}")

print(f"\nStrong Days              : {strong_days}")
print(f"Satisfactory Days        : {satisfactory_days}")
print(f"Needs Improvement Days   : {improvement_days}")
print(f"Critical Days            : {critical_days}")

print("\nPERFORMANCE ANALYSIS\n")

print(f"Total Score              : {total_score}")
print(f"Average Score            : {average_score:.2f}")

if attempted_days > 0:
    print(f"Highest Score            : {highest_score}")
    print(f"Highest Score Day        : Day {highest_score_day}")
    print(f"Lowest Score             : {lowest_score}")
    print(f"Lowest Score Day         : Day {lowest_score_day}")
else:
    print("Highest Score            : Not Available")
    print("Highest Score Day        : Not Available")
    print("Lowest Score             : Not Available")
    print("Lowest Score Day         : Not Available")

print("\nCRITICAL SCORE INFORMATION\n")

print(f"Critical Score Found     : {'Yes' if critical_score_found else 'No'}")

if critical_score_found:
    print(f"First Critical Day       : Day {first_critical_day}")
    print(f"First Critical Score     : {first_critical_score}")
else:
    print("First Critical Day       : Not Applicable")
    print("First Critical Score     : Not Applicable")

print("\nFINAL DECISION\n")

print(f"Final Status             : {final_status}")
print(f"Primary Blocker          : {primary_blocker}")
print(f"Next Action              : {next_action}")

print("=" * 50)
