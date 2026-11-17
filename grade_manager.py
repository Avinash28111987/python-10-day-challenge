"""
Student Grade Manager

Indha program student-oda marks-a store panni,
mark-ku correct grade calculate pannum.
Terminal-la run panna vendiya simple Python program.
"""

def get_grade(mark):
    # Indha function mark-a check panni grade return pannum.
    # 90-100 -> A
    # 80-89  -> B
    # 70-79  -> C
    # 60-69  -> D
    # 60-ku keela -> E
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark < 90:
        return "B"
    elif 70 <= mark < 80:
        return "C"
    elif 60 <= mark < 70:
        return "D"
    else:
        return "E"


def get_valid_mark():
    # User kitta mark vaangura function.
    # User correct mark kudukkura varaikkum loop continue aagum.
    while True:
        value = input("Enter mark (0-100): ").strip()

        # User edhuvum type pannama Enter press pannina,
        # empty value reject pannuvom.
        if value == "":
            print("Mark cannot be empty. Please try again.")
            continue

        try:
            # User kudutha value-a number-a convert panna try pannuvom.
            mark = float(value)
        except ValueError:
            # "abc" madhiri number illaadha value kudutha,
            # program crash aagama error message kaattuvom.
            print("Invalid mark. Please enter a number.")
            continue

        # Mark 0-100 range-kulla irukka nu check pannuvom.
        # Example: 105 or -5 kudutha reject pannuvom.
        if not 0 <= mark <= 100:
            print("Mark must be between 0 and 100.")
            continue

        # Correct mark kidaichuduchu.
        # Adha calling function-ku return pannuvom.
        return mark


def add_student(students):
    # Indha function oru pudhu student-a add pannum.

    # First student name vaanguvom.
    name = input("Enter student name: ").strip()

    # Name empty-aa irundha student-a add panna maatom.
    if name == "":
        print("Name cannot be empty.")
        return

    # Valid mark vaangura function-a call pannuvom.
    mark = get_valid_mark()

    # Mark based on grade calculate pannuvom.
    grade = get_grade(mark)

    # Oru student-ku name, mark, grade nu 3 information irukku.
    # Adhanala dictionary use pannrom.
    student = {
        "name": name,
        "mark": mark,
        "grade": grade
    }

    # Student dictionary-a students list-kulla add pannuvom.
    students.append(student)

    print(f"{name} added successfully.")


def show_results(students):
    # Indha function students-oda complete result-a display pannum.

    # Yaarum add pannala na result show panna mudiyadhu.
    # Program crash aagama message display pannuvom.
    if not students:
        print("\nNo students have been added yet.")
        return

    # Table heading print pannuvom.
    print("\n" + "=" * 42)
    print(f"{'Name':<20}{'Mark':>10}{'Grade':>10}")
    print("-" * 42)

    # List-la irukkura each student-a one by one process pannuvom.
    for student in students:
        mark = student["mark"]

        # 92.0 madhiri display aagama 92 nu kaatta,
        # :g formatting use pannuvom.
        mark_display = f"{mark:g}"

        # Name, mark, grade-a neatly aligned table-la print pannuvom.
        print(
            f"{student['name']:<20}"
            f"{mark_display:>10}"
            f"{student['grade']:>10}"
        )

    # Ella students-oda marks mattum oru separate list-la eduppom.
    # Example: [92, 78, 59]
    marks = [student["mark"] for student in students]

    # Average = total marks / number of students.
    average = sum(marks) / len(marks)

    # max() highest mark-a find pannum.
    highest = max(marks)

    # min() lowest mark-a find pannum.
    lowest = min(marks)

    # Final statistics display pannuvom.
    print("-" * 42)
    print(f"Average: {average:.1f}")
    print(f"Highest: {highest:g}")
    print(f"Lowest: {lowest:g}")
    print("=" * 42)


def main():
    # Idhu program-oda main control function.

    # Starting-la empty list create pannuvom.
    # Ella student records-um indha list-kulla store aagum.
    students = []

    # User Quit select pannura varaikkum menu repeat aagum.
    while True:
        print("\nStudent Grade Manager")
        print("1. Add student")
        print("2. Show results")
        print("3. Quit")

        # User kitta menu choice vaanguvom.
        choice = input("Choose an option: ").strip()

        # 1 select pannina student add pannuvom.
        if choice == "1":
            add_student(students)

        # 2 select pannina results display pannuvom.
        elif choice == "2":
            show_results(students)

        # 3 select pannina program-a stop pannuvom.
        elif choice == "3":
            print("Goodbye!")
            break

        # 1, 2, 3 thavira vera value kudutha,
        # program crash aagama error message kaattuvom.
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Indha file-a direct-aa run pannumbodhu mattum main() call aagum.
# Example: python grade_manager.py
if __name__ == "__main__":
    main()
