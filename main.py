# main.pyfrom student_data import
from student_data import add_student, view_students, get_average_grade

def main():
    while True:
        print(" =====Student Management System=====")
        print("1. add Student")
        print("2. View Students")
        print("3. get Average Grade")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            avg = get_average_grade()
            if avg is not None:
                print(f"The average grade of all students is: {avg:.2f}")
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
