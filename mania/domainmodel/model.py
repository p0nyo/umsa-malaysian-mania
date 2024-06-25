class Question:
    def __init__(self, number, question):
        self.number = number
        self.question = question
        
    def __str__(self):
        return f"Question {self.number}: {self.question}"
        
# Answer and Points are stored within a list
# self.a1 = ["a1", 48]
class Answer:
    def __init__(self, number, a1=[], a2=[], a3=[], a4=[], a5=[], a6=[], a7=[], a8=[]):
        self.number = number
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.a8 = a8
    
        