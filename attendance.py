"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime

attendance = {}
ID = {"student_id": 0}
def register_student(student_id, *name):
    """Register a student in the system."""
    for students in name:
        ID["student_id"] += 1
        attendance[ID["student_id"]] = {"name": students, "present_days": [], "absent_days": []}
    print(attendance)
register_student(ID["student_id"], "Jon", "Leo", "Kenan")
def mark_present(*student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    # implement logic
    for ids in student_ids:
        if ids in attendance:
            attendance[ids]["present_days"].append(today)
    print(attendance)
mark_present(1, 2)
def mark_absent(*student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    #implement logic
    for ids in student_ids:
        if ids in attendance:
            attendance[ids]["absent_days"].append(today)
    print(attendance)
mark_absent(1, 2)


def get_report(SID = 1, **details):
    """Generate attendance report with optional filters."""
    report = {}
    # implement logic
    report["REPORT"] = details
    return report
print(get_report(Days_absent = attendance[1]["absent_days"], Days_present = attendance[1]["present_days"]))