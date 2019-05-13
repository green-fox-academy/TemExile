class teacher(object):
    def teach(self):
        return student.learn(self)
    def answer(self):
        return 'teacher answer'

class student(object):
    def learn(self):
        return 'student learn'
    def question(self):
        return teacher.answer(self)

s = student()
t = teacher()

print(s.question())
print(t.teach())