class Student_info:

    def __init__(self,name,age,grade):
        self.name = name
        self.age=age
        self.grade = grade

    def get_grade(self):
        return self.grade
    
class Course:

    def __init__(self,course_name,max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.student_list = []

    def add_student(self,student):
        if len(self.student_list) < self.max_students:
            self.student_list.append(student)
            return True, self.student_list
        return False
    
    def average_grade(self):
        val = 0
        for i in self.student_list:
            val += i.get_grade()
            
        return val/len(self.student_list)

s1 = Student_info("david", 24, 90)
s2 = Student_info('Tim', 22, 69)
s3 = Student_info('Jimmy', 23, 78)

course = Course("CSE", 2)
course.add_student(s1)
course.add_student(s2)
#print(course.add_student(s3))

for i in course.student_list:
    print(i.name)

print(course.average_grade())