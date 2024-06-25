import csv
import os

from mania.domainmodel.model import Question, Answer

class CSVReader:
    def __init__(self, filename):
        self.__filename = filename
        
    def read_file(self):
        if not os.path.exists(self.__filename):
            print(f"path {self.__filename} does not exist!")
            return
        with open(self.__filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            question_answer = []
            for row in reader:
                question = Question(row["Q/N"], row["Question"])
                answer = Answer(row["Q/N"], [row["A1"], row["A1P"]], [row["A2"], row["A2P"]],
                                 [row["A3"], row["A3P"]], [row["A4"], row["A4P"]], 
                                 [row["A5"], row["A5P"]], [row["A6"], row["A6P"]]
                                 , [row["A7"], row["A7P"]], [row["A8"], row["A8P"]])
                question_answer.append((question, answer))
            return question_answer
            print(question_answer[22][1].a7)

                
                
                
                
                
                
                
                
                
        #         temp_dict = dict(number=row["Q/N"], question=row['Question'],
        #                         a1=row["A1"], a2=row["A2"], a3=row["A3"], a4=row["A4"], 
        #                         a5=row["A5"], a6=row["A6"], a7=row["A7"], a8=row["A8"], 
        #                         a1p=row["A1P"], a2p=row["A2P"], a3p=row["A3P"], a4p=row["A4P"], 
        #                         a5p=row["A5P"], a6p=row["A6P"], a7p=row["A7P"], a8p=row["A8P"])
        #         self.__questions_answers.append(temp_dict)
        # print(self.__questions_answers[0])
        # return self.__questions_answers
                