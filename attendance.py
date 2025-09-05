import datetime

class AttendanceRegister:
    def __init__(self):
        self.attendance = {}
        self.student_id = 0

    def register(self, *students):
        """Register students quickly"""
        for student in students:
            self.student_id += 1
            self.attendance[self.student_id] = {
                "name": student,
                "present": [],
                "absent": []
            }

    def mark(self, status, *ids):
        """Mark present/absent"""
        today = str(datetime.date.today())
        for id in ids:
            if id in self.attendance:
                self.attendance[id][status].append(today)

    def report(self, id, only_present=False, only_absent=False):
        """Show report"""
        student = self.attendance.get(id)
        if not student:
            return "Student not found"

        if only_present:
            return {student["name"]: student["present"]}
        if only_absent:
            return {student["name"]: student["absent"]}

        return {
            student["name"]: {
                "present": student["present"],
                "absent": student["absent"]
            }
        }

register = AttendanceRegister()

register.register("Jon", "Leo", "Kenan")
register.mark("present", 1, 2)
register.mark("absent", 3)

print(register.report(1))
print(register.report(2, only_present=True))
print(register.report(3, only_absent=True))
