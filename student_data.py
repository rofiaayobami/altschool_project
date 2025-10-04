students = []

# Function to create a student dictionary   
def create_student(name, age, grade):
  student = {
        "name": name,
        "age": age,
        "grade": grade
    }

# Function to add a student to the list
def add_student():
    name =  str(input("Enter student name: "))
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade: "))
    student = create_student(name, age, grade)
    students.append({"name": name, "age": age, "grade": grade})
    print(f"Student {name} added successfully!")
    return  

# Function to display all students
def view_students():
    if not students:
        print("No students yet.")
        return
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
        return 

#Calculates the average of all grades.
def get_average_grade():
    if not students:
        print("No students registered.")
        return None
    total_grade = sum(student['grade'] for student in students)
    return total_grade / len(students)                 
    print(f"The average grade is: {average:.2f}")
    return




