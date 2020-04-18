# define pupil class with it's properties (avarage mark, marks, home work (done, not done), e. t. c.).
#  Spread the idea
class Pupil:

    def __init__ (self,in_name,in_age,in_marks):
        self.name = in_name
        self.age = in_age
        self.marks = in_marks
        self.amark = 0

    def set_mark(self, current_mark):
        self.marks.append(current_mark)
        
    def average_mark(self):
        return sum(self.marks) / len(self.marks)
          
    def __str__(self):
        s = "pupil " + self.name + " aged " + str(self.age) + " has marks " + str(self.marks)
        return s