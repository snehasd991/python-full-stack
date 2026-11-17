
class student:
    def __init__(self, usn, name, marks):
        self.usn = usn
        self.name = name
        self.marks = marks

    def display(self):
        print("USN:", self.usn)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("------------------------")

class studentmanagement:
    def __init__(self):
        self.students = []

    def add_students(self):
        usn = input("enter USN:")

        for student in self.students:
            if student.usn == usn:
                print("USN already exists!")
                return

        name = input("Enter student name:")
        marks = float(input("enter marks"))

        student = student(usn, name, marks)

        self.students.append(student)
        print("Student added successfully!")

    def display_students(self):
        if len(self.student) == 0:
            print("No student found!")
        return

        for student in self.students:
            student.display

    def search_student(self):
        usn = input("Enter USN to search:")
        for student in self.student:
            if student.usn == usn:
                student.display()
                return
        print("Student not found!")

        for student in self.student:
            if student.usn == usn:
                print("Student found!")
                student.display()
                return

            print("Student not found!")

        def delete_student(self):
            usn = input("Enter USN to delete:")

            for student in self.students:
                if student.usn == usn:
                    self.student.remove(student)
                    print("Student deleted successfully!")
                    return
            print("Student not found!")

app = studentmanagement()

while True:

    print("\n======= Student Management System =======")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")
s
    if choice == "1":
        app.add_student()
    elif choice == "2":
        app.view_student()
    elif choice == "3":
        app.search_student()
    elif choice == "4":
        app.delete_student()
    elif choice == "5":
        print("Thank you for using the application")
        break

    else:
        print("Invalid choice! Please try again.")
