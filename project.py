# SMART CAMPUS INFORMATION SYSTEM
# Short Version (~200 Lines)

import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# =====================================================
# STUDENT CLASS
# =====================================================

class Student:

    def __init__(self, sid, name, age, dept):

        self.sid = sid
        self.name = name
        self.age = age
        self.dept = dept
        self.courses = {}

    def add_course(self, course, marks):

        self.courses[course] = marks

    def grade(self):

        if not self.courses:
            return "No Grade"

        avg = sum(self.courses.values()) / len(self.courses)

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "Fail"

    def display(self):

        print("\n----------------------------")
        print("ID :", self.sid)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Department :", self.dept)

        print("\nCourses & Marks")

        for c, m in self.courses.items():
            print(c, ":", m)

        print("Grade :", self.grade())
        print("----------------------------")


# =====================================================
# STUDENT MANAGEMENT SYSTEM
# =====================================================

class SMS:

    def __init__(self):

        self.students = []

    # 1. REGISTER STUDENT
    def register(self):

        sid = int(input("Enter Student ID : "))
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        dept = input("Enter Department : ")

        s = Student(sid, name, age, dept)

        n = int(input("How many courses? "))

        for i in range(n):

            course = input("Course Name : ")
            marks = int(input("Marks : "))

            s.add_course(course, marks)

        self.students.append(s)

        print("\nStudent Added Successfully!")

    # 2. DISPLAY STUDENTS
    def display(self):

        if not self.students:
            print("\nNo Records Found!")
            return

        for s in self.students:
            s.display()

    # 3. SEARCH STUDENT
    def search(self):

        sid = int(input("Enter Student ID : "))

        for s in self.students:

            if s.sid == sid:
                s.display()
                return

        print("Student Not Found!")

    # 4. SORT STUDENTS
    def sort_students(self):

        print("\n1. Sort by Name")
        print("2. Sort by Grade")

        ch = int(input("Enter Choice : "))

        if ch == 1:

            self.students.sort(key=lambda x: x.name)

        elif ch == 2:

            self.students.sort(
                key=lambda x:
                sum(x.courses.values()) / len(x.courses),
                reverse=True
            )

        print("\nSorting Completed!")

    # 5. FEE CALCULATION
    def fee(self):

        credits = int(input("Enter Credits : "))

        total = credits * 1500 + 1000 + 2000

        print("\nTotal Fee :", total)

    # 6. SAVE FILE
    def save(self):

        if not self.students:
            print("\nNo Data To Save!")
            return

        data = []

        for s in self.students:

            data.append({
                "ID": s.sid,
                "Name": s.name,
                "Age": s.age,
                "Department": s.dept,
                "Courses": s.courses
            })

        with open("students.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\nRecords Saved!")

    # 7. DIRECTORY SCAN
    def scan(self):

        path = input("Enter Directory Path : ")

        try:

            files = os.listdir(path)

            print("\nFiles:")

            for file in files:
                print(file)

        except Exception as e:
            print("Error :", e)

    # 8. ANALYTICS
    def analytics(self):

        if not self.students:
            print("\nNo Data Available!")
            return

        names = []
        avgs = []

        for s in self.students:

            avg = np.mean(list(s.courses.values()))

            names.append(s.name)
            avgs.append(avg)

        print("\nAverage Marks :", np.mean(avgs))
        print("Highest Marks :", np.max(avgs))
        print("Lowest Marks :", np.min(avgs))

        df = pd.DataFrame({
            "Student": names,
            "Average": avgs
        })

        print("\n", df)

        plt.bar(names, avgs, color="blue")

        plt.title("Student Performance")
        plt.xlabel("Students")
        plt.ylabel("Average Marks")

        plt.show()


# =====================================================
# MAIN PROGRAM
# =====================================================

sms = SMS()

while True:

    print("\n========= SMART CAMPUS MENU =========")
    print("1. Student Registration")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Sort Students")
    print("5. Fee Calculation")
    print("6. Save Records")
    print("7. Directory Scan")
    print("8. Analytics")
    print("9. Exit")

    choice = int(input("\nEnter Choice : "))

    if choice == 1:
        sms.register()

    elif choice == 2:
        sms.display()

    elif choice == 3:
        sms.search()

    elif choice == 4:
        sms.sort_students()

    elif choice == 5:
        sms.fee()

    elif choice == 6:
        sms.save()

    elif choice == 7:
        sms.scan()

    elif choice == 8:
        sms.analytics()

    elif choice == 9:

        print("\nExiting Program...")
        break

    else:
        print("\nInvalid Choice!")