# 🎓 Smart Campus Information System

A Python-based **Smart Campus Information System** designed to simplify student information management and academic performance tracking through an interactive menu-driven application.

The system provides essential student management operations, automated grade calculation, fee estimation, JSON-based data storage, and academic performance analytics with graphical visualization.

## 🚀 Features

### 👨‍🎓 Student Management
- Register students with Student ID, Name, Age, and Department.
- Add multiple courses and corresponding marks.
- Display complete student information.
- Search students using their unique Student ID.

### 📊 Academic Performance Management
- Automatically calculate grades based on average marks.
- Sort students alphabetically by name.
- Sort students according to academic performance.
- Calculate average, highest, and lowest student marks.

### 💰 Fee Management
- Calculate student fees based on credit hours.
- Include additional fixed charges in the total fee calculation.

### 💾 Data Management
- Store student records in JSON format.
- Save student information for future access.
- Scan and display files from a specified directory.

### 📈 Data Analytics & Visualization
- Generate student performance summaries.
- Calculate individual student averages.
- Display academic performance through bar charts using Matplotlib.
- Present analytical results using Pandas DataFrames.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application development |
| NumPy | Numerical and statistical calculations |
| Pandas | Student performance data management |
| Matplotlib | Graphical data visualization |
| JSON | Student record storage |
| OS Module | Directory and file operations |

## 📂 Project Structure

```text
smart_campus_system/
│
├── project.py
│   └── Main application containing student
│       management and analytics functionality
│
├── students.json
│   └── Stores student records in JSON format
│
└── README.md
    └── Project documentation
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Brunda-tech/smart_campus_system.git
```

### 2. Navigate to the Project Directory

```bash
cd smart_campus_system
```

### 3. Install Required Libraries

```bash
pip install numpy pandas matplotlib
```

### 4. Run the Application

```bash
python project.py
```

## 🖥️ Application Menu

The application provides the following menu-driven operations:

```text
========= SMART CAMPUS MENU =========

1. Student Registration
2. Display Students
3. Search Student
4. Sort Students
5. Fee Calculation
6. Save Records
7. Directory Scan
8. Analytics
9. Exit

Enter Choice:
```

Select the required option to perform the corresponding operation.

## 🎯 Grade Calculation System

The application calculates grades based on the average marks obtained across registered courses.

| Average Marks | Grade |
|---|---|
| 90 and above | A+ |
| 80 – 89 | A |
| 70 – 79 | B |
| 60 – 69 | C |
| Below 60 | Fail |

## 📊 Academic Analytics

The analytics module provides:

- Average marks across registered students.
- Highest individual student average.
- Lowest individual student average.
- Tabular performance summaries.
- Bar chart visualization of student performance.

## 💡 Future Enhancements

The system can be further improved by introducing:

- Student login and administrator authentication.
- Database integration using MySQL or SQLite.
- Student attendance management.
- Timetable and course scheduling.
- Fee payment tracking.
- Graphical user interface using Tkinter or a web framework.
- Automated academic reports and downloadable PDF summaries.
- Improved input validation and duplicate student ID detection.

## 👥 Team Members

This project was collaboratively developed by:

| Team Member | GitHub Profile |
|---|---|
| **Brunda S** | [@Brunda-tech](https://github.com/Brunda-tech) |
| **Chandhan Kumar** | [@chandhankumargv](https://github.com/chandhankumargv) |

## 🤝 Collaboration

We developed this project collaboratively, applying Python programming concepts, data management techniques, and analytical methods to build a practical campus management solution.

## 📜 License

This project is developed for educational and learning purposes.
