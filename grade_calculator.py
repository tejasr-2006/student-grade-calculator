def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def main():
    print("=== Student Grade Calculator ===")
    name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))

    marks = []
    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / num_subjects
    grade = calculate_grade(percentage)

    print("\n=== Result ===")
    print(f"Name: {name}")
    print(f"Total Marks: {total:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

    if grade == "F":
        print("Status: Fail")
    else:
        print("Status: Pass")

if __name__ == "__main__":
    main()
