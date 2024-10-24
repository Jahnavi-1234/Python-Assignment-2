# Student information
name = "John"
surname = "Doe"
subjects = ['Math', 'Physics', 'Philosophy']
exams_passed = True
subjects_passed = {'Math': 5, 'Philosophy': 2}
# Print student's name and surname
print("Name:", name)
print("Surname:", surname)
print("All Subjects:", subjects)
# Check if exams have been passed
if exams_passed:
    # Find subjects not passed
    remaining_subjects = []
    for i in subjects:
        if i not in subjects_passed:
            remaining_subjects.append(i)
            if remaining_subjects:

                 print("Subjects left to pass:", remaining_subjects)
            else:
                print("All subjects passed!")
else:
    print("The student has not passed the session yet.")
