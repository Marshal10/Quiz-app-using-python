from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT=("Arial",20,"italic")
class QuizInterface:
    
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.score_lbl=Label(text=f"Score: 0",bg=THEME_COLOR,fg="white",font=("Arial",14,"normal"))
        self.score_lbl.grid(column=1,row=0)
        
        self.canvas=Canvas(width=400,height=250,bg="white")
        self.question_text=self.canvas.create_text(200,125,width=380,text="Question will come here",font=FONT)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=20)
        
        true_img=PhotoImage(file="images/true.png")
        self.true_btn=Button(image=true_img,highlightthickness=0,command=self.answer_true)
        self.true_btn.grid(column=0,row=2,pady=20)
        
        false_img=PhotoImage(file="images/false.png")
        self.false_btn=Button(image=false_img,highlightthickness=0,command=self.answer_false)
        self.false_btn.grid(column=1,row=2,pady=20)
        
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.configure(bg="white")
        self.true_btn.config(state="normal")
        self.false_btn.config(state="normal")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text=f"You have completed the quiz.Your final score was: {self.quiz.score}/{self.quiz.question_number} ")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
        self.update_score()
        
    def answer_true(self):
        correct_answer=self.quiz.check_answer("True")
        self.canvas_change_color(correct_answer)
    
    def answer_false(self):
        correct_answer=self.quiz.check_answer("False")
        self.canvas_change_color(correct_answer)
        
    def canvas_change_color(self,bool_val):
        if bool_val:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")
        self.window.after(1000,self.get_next_question)
            
    def update_score(self):
        self.score_lbl.config(text=f"Score: {self.quiz.score}")