from ascii import yoda, vadar, starwars
from rich.console import Console
starwars()
namea=input("Hello there! what is you name ")
print(f"welcome {namea}/ncomplete this quiz to find out if you are a jedi or sith") 

console =Console()


class Question:
    
    def __init__(self, quiz_text, quiz_answers, wrong_answers):
        
        self.text = quiz_text
        self.answer = quiz_answers
        self.wrong = wrong_answers  
        

class Questionaire:
    
    
         
           
    def __init__(self, question_data):
        
        
        self.question_number = 0
        self.counter = 0
        self.question_list = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            wrong_answers = question["incorrect_answers"]    
            new_question = Question(question_text, question_answer, wrong_answers)
        
            self.question_list.append(new_question)
        
    
    def check_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        
        while True:
            user_answer = console.input(f"\n[blue]Q:{self.question_number}/10[/]\n{current_question.text}   \n[blue]Enter [[/]A[blue]] or [[/]B[blue]][/]:\n")
            console.rule("")
            user_answer =user_answer.upper()
            if user_answer != "A" and user_answer != "B":
                    console.print(f"[red][{user_answer}] ****INVALID INPUT****[/] [blue]Enter [[/]A[blue]] or [[/]B[blue]][/]")
                    continue
            else:
                break
                       
        self.check_answer(user_answer, current_question.answer, current_question.wrong)
        
    def check_answer(self, user_answer, correct_answer, wrong_answers):
        
        pass
            
   
    def final(self):
        
        print(f"not implemented")
        
    def run(self):
       while self.check_questions():
                     
        self.next_question()
        
        self.final()   
        

class Quiz(Questionaire):     
        

    def check_answer(self, user_answer, correct_answer,wrong_answers):
        
        if user_answer == correct_answer:
            self.counter += 1
            print(f"{self.counter}")
            
   
    def final(self):
        
        
        if self.question_number == 10:
            if self.counter>6:
                print("\nYou've completed the quiz")
                print(f"\n Goodness i sense in you  , Jedi story you begin")
                yoda()
                print(f"{namea}")
            else:
                print(f"\nYou've completed the quiz")
                print(f"\nThe darks side it strong with you , you are a sith  ")
                vadar()
                print(f"{namea}")
                
class Story(Questionaire):
        
    def check_answer(self, user_answer, correct_answer, wrong_answers):
        
            if user_answer == correct_answer:
                
                print("correct")
            else:
                print(wrong_answers)
                self.question_number =0  
                
    def final(self):
        pass
        
      
                  
                
         
                


            
