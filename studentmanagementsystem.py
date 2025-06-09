class Student:
    def __init__(self, student_id, name, grade_level):
        self.student_id = student_id
        self.name = name
        self.grade_level = grade_level
        self.attendance = []
        self.grades = {}

    def mark_attendance(self, date, present=True):
        self.attendance.append({'date': date, 'present': present})

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_attendance(self):
        return self.attendance

    def get_grades(self):
        return self.grades

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.messages = []

    def enroll_student(self, student_id, name, grade_level):
        if student_id in self.students:
            print(f"Student with ID {student_id} already enrolled.")
            return
        self.students[student_id] = Student(student_id, name, grade_level)
        print(f"Student {name} enrolled successfully.")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with ID {student_id} removed.")
        else:
            print(f"Student with ID {student_id} not found.")

    def mark_attendance(self, student_id, date, present=True):
        if student_id in self.students:
            self.students[student_id].mark_attendance(date, present)
            print(f"Attendance marked for student ID {student_id} on {date}.")
        else:
            print(f"Student with ID {student_id} not found.")

    def add_grade(self, student_id, subject, grade):
        if student_id in self.students:
            self.students[student_id].add_grade(subject, grade)
            print(f"Grade added for student ID {student_id} in {subject}.")
        else:
            print(f"Student with ID {student_id} not found.")

    def send_message(self, sender, receiver, message):
        self.messages.append({'from': sender, 'to': receiver, 'message': message})
        print(f"Message sent from {sender} to {receiver}.")

    def view_messages(self, user):
        user_messages = [msg for msg in self.messages if msg['to'] == user]
        for msg in user_messages:
            print(f"From: {msg['from']} - Message: {msg['message']}")

    def list_students(self):
        for student_id, student in self.students.items():
            print(f"ID: {student_id}, Name: {student.name}, Grade Level: {student.grade_level}")

def main():
    sms = StudentManagementSystem()
    while True:
        print("\nStudent Management System")
        print("1. Enroll Student")
        print("2. Remove Student")
        print("3. Mark Attendance")
        print("4. Add Grade")
        print("5. Send Message")
        print("6. View Messages")
        print("7. List Students")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            grade_level = input("Enter grade level: ")
            sms.enroll_student(student_id, name, grade_level)
        elif choice == '2':
            student_id = input("Enter student ID to remove: ")
            sms.remove_student(student_id)
        elif choice == '3':
            student_id = input("Enter student ID: ")
            date = input("Enter date (YYYY-MM-DD): ")
            present_input = input("Is the student present? (y/n): ")
            present = True if present_input.lower() == 'y' else False
            sms.mark_attendance(student_id, date, present)
        elif choice == '4':
            student_id = input("Enter student ID: ")
            subject = input("Enter subject: ")
            grade = input("Enter grade: ")
            sms.add_grade(student_id, subject, grade)
        elif choice == '5':
            sender = input("Enter sender name: ")
            receiver = input("Enter receiver name: ")
            message = input("Enter message: ")
            sms.send_message(sender, receiver, message)
        elif choice == '6':
            user = input("Enter your name to view messages: ")
            sms.view_messages(user)
        elif choice == '7':
            sms.list_students()
        elif choice == '8':
            print("Exiting Student Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
