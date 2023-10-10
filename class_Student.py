class student:
    #constructor
    def __init__(self, name, student_id, age, gender):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.gender = gender

    #set grade
    def set_grade(self, grade):
        self.grade = grade

    #get grade
    def get_grade(self):
        return self.grade
    
    #student info
    def display_student_info(self):
        print('name : '+ self.name)
        print('student_id : '+ str(self.student_id))
        print('age : '+ str(self.age))
        print('gender : '+ self.gender)
        print('grade : '+ str(self.grade))
