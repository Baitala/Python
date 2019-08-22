# define pupil class with it's properties (avarage mark, marks, home work (done, not done), e. t. c.).
#  Spread the idea
class pupil:

    def __init__ (self):
        self.name = ""
        self.year = 0
        self.marks = []
        self.amark = 0

    def set_mark(self, current_mark):
        self.marks.append(current_mark)
        
    def average_mark(self):
        return sum(self.marks) / len(self.marks)
          