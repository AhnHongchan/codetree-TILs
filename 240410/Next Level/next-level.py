class Student:
    def __init__(self, ID='codetree', lv=10):
        self.ID = ID
        self.lv = lv

student = Student()
print(f'user {student.ID} lv {student.lv}')
a, b = input().split()
student2 = Student(a, b)
print(f'user {student2.ID} lv {student2.lv}')