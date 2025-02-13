import tkinter as tk
from tkinter import messagebox
import random

class Question:
    def __init__(self, prompt, answer, distractors):
        self.prompt = prompt
        self.answer = answer
        self.distractors = distractors

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.score = 0
        self.question_index = 0
        
        # Set up main window
        self.root.title("Quiz App")
        self.root.geometry("600x400")
        self.root.configure(bg='#2c3e50')  # Background color
        self.root.resizable(True, True)

        # Question label
        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 16), wraplength=500, bg='#2c3e50', fg='#ecf0f1')
        self.question_label.pack(pady=20)

        # Frame for answer buttons
        self.answers_frame = tk.Frame(self.root, bg='#2c3e50')
        self.answers_frame.pack(pady=20)

        # Create answer buttons dynamically
        self.buttons = []
        button_colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']  # Button colors
        for i in range(4):
            button = tk.Button(self.answers_frame, text="", font=("Helvetica", 14), width=30, bg=button_colors[i], fg='#ecf0f1', command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.buttons.append(button)

        self.update_widgets()

    def update_widgets(self):
        # Update question and answer buttons
        current_question = self.questions[self.question_index]
        self.question_label.config(text=current_question.prompt)

        # Shuffle and display answer choices
        answers = [current_question.answer] + random.sample(current_question.distractors, 3)
        random.shuffle(answers)
        for i in range(4):
            self.buttons[i].config(text=answers[i])

    def check_answer(self, idx):
        current_question = self.questions[self.question_index]
        selected_answer = self.buttons[idx].cget("text")
        if selected_answer == current_question.answer:
            self.score += 1
            messagebox.showinfo("Correct", "Correct answer!", parent=self.root)
        else:
            messagebox.showerror("Incorrect", f"Wrong answer! The correct answer is: {current_question.answer}", parent=self.root)

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.update_widgets()
        else:
            messagebox.showinfo("Quiz Complete", f"Quiz completed!\nYour score: {self.score}/{len(self.questions)}", parent=self.root)
            self.root.destroy()

def main():
    # Sample questions
    questions = [
        Question("What is the capital of France?", "Paris", ["London", "Berlin", "Madrid"]),
        Question("Who wrote 'Romeo and Juliet'?", "Shakespeare", ["Jane Austen", "William Wordsworth", "Charles Dickens"]),
        Question("What is 2 + 2?", "4", ["3", "5", "6"]),
        Question("Which planet is known as the Red Planet?", "Mars", ["Venus", "Jupiter", "Saturn"]),
        Question("What is the largest mammal?", "Blue whale", ["Elephant", "Giraffe", "Lion"])
    ]

    random.shuffle(questions)  # Shuffle questions

    root = tk.Tk()
    app = QuizApp(root, questions)

    root.mainloop()

if __name__ == "__main__":
    main()
    