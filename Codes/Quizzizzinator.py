import tkinter as tk
questions = [
    {"question":"How many pounds are there in one kilogram?",
    "options":["2","2.2046","2.5","2.2"],
    "answer":"2.2046"},
    {"question":"In which country did the Metric System come from?",
    "options":["Spain","Britain","France","Germany"],
    "answer":"France"},
    {"question":"How many SI units are there?",
    "options":["5","6","7","8"],
    "answer":"7"}
]
class QuizApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Quiz App")
        self.score = 0
        self.q_index = 0
        self.question_label = tk.Label(root,text = "",font = ("Arial",14),wraplength = 400)
        self.question_label.pack(pady = 20)
        self.var = tk.StringVar()
        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(root,text = "",variable = self.var,value = "",font = ("Arial",12))
            rb.pack(anchor = "w")
            self.options.append(rb)
        self.submit_button = tk.Button(root,text = "Submit",command = self.check_answer)
        self.submit_button.pack(pady = 20)
        self.result_label = tk.Label(root,text = "",font = ("Arial",12))
        self.result_label.pack(pady = 10)
        self.next_btn = tk.Button(root,text = "Next",command = self.next_question)
        self.next_btn.pack_forget()
        self.load_question()
    def load_question(self):
        if self.q_index < len(questions):
            q = questions[self.q_index]
            self.question_label.config(text = q["question"])
            self.var.set(None)
            for i,option in enumerate(q["options"]):
                self.options[i].config(text = option,value = option)
            self.result_label.config(text = "")
            self.submit_button.pack(pady = 20)
            self.next_btn.pack_forget()
        else:
            self.show_score()
    def check_answer(self):
        selected = self.var.get()
        if not selected:
            self.result_label.config(text = "Please select an object!",fg = "yellow")
            return
        if selected == questions[self.q_index]["answer"]:
            self.score += 1
            self.result_label.config(text = "Correct",fg = "green")
        else:
            self.result_label.config(text = f"Wrong! Correct answer : {questions[self.q_index]['answer']}",fg = "red")
        self.submit_button.pack_forget()
        self.next_btn.pack(pady = 20)
    def next_question(self):
        self.q_index += 1
        self.load_question()
    def show_score(self):
        self.question_label.config(text = "Quiz Completed!")
        for rb in self.options:
            rb.pack_forget()
        self.submit_button.pack_forget()
        self.next_btn.pack_forget()
        self.result_label.config(text = f"Your Score : {self.score}/{len(questions)}",fg = "blue")
root = tk.Tk()
app = QuizApp(root)
root.mainloop()