from tkinter import *


root = Tk()
root.title("Riddle Quiz")
root.geometry("500x300")

quiz_data = []


def load_quiz(filename):
    global quiz_data
    quiz_data = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                question_answer = line.strip().split(":")
                if len(question_answer) == 2:
                    quiz_data.append((question_answer[0], question_answer[1]))
    except FileNotFoundError:
        print("The file was not found.")
        exit()

def check_answer():
    user_answer = answer_entry.get()
    correct_answer = quiz_data[0][1]
    if user_answer.strip().lower() == correct_answer.strip().lower():
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Incorrect. Try again.", fg="red")

question_label = Label(root, text="What is middle of Paris?", font=("Helvetica", 14))
question_label.pack(pady=20)

answer_entry = Entry(root, font=("Helvetica", 12))
answer_entry.pack(pady=10)

result_label = Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

check_button = Button(root, text="Check Answer", font=("Helvetica", 12), command=check_answer)
check_button.pack(pady=20)


load_quiz("quizans.txt")


root.mainloop()
