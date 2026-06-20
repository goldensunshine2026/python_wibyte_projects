subjects = ["English", "Maths", "Science", "Computer", "Hindi"]

choice = "yes"

while choice == "yes":

    print("      STUDENT REPORT CARD SYSTEM    ")
    name = input("Enter student name: ")

    student_id = name[:3].upper()

    marks = []

    for subject in subjects:

        while True:
            mark = int(input(f"Enter marks in {subject}: "))

            if mark >= 0 and mark <= 100:
                marks.append(mark)
                break
            else:
                print("Invalid marks! Please enter marks between 0 and 100.")

    total = sum(marks)

    percentage = total / len(subjects)

    fail = False

    for mark in marks:
        if mark < 33:
            fail = True

    if fail:
        grade = "Fail"

    elif percentage >= 90:
        grade = "A+"

    elif percentage >= 75:
        grade = "A"

    elif percentage >= 60:
        grade = "B"

    elif percentage >= 40:
        grade = "C"

    else:
        grade = "Fail"


    print("\n========== REPORT CARD ==========")
    print("Student Name :", name)
    print("Student ID   :", student_id)
    print("---------------------------------")

    for i in range(len(subjects)):
        if marks[i] >= 33:
            status = "Pass"
        else:
            status = "Fail"

        print(subjects[i], ":", marks[i], "-", status)

    print("Total Marks  :", total, "/ 500")
    print("Percentage   :", percentage, "%")
    print("Grade        :", grade)


    # Final result
    if grade == "Fail":
        print("Result       : FAIL")
    else:
        print("Result       : PASS")

    choice = input("\nDo you want to enter another student report? (yes/no): ").lower()
