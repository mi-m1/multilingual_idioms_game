import tkinter as tk
from tkinter import Button
from tkinter import messagebox, ttk
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap import Style
# form ttkbootstrap.dialogs import Messagebox
from quiz_data import quiz_data

# Function to display the current question and choices
def show_question():
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to display the hints from AI models
# def show_hints():
#     gpt3_hint = quiz_data['gpt3-5turbo']
#     gpt4_hint = quiz_data["gpt4"]
    
def custom_messagebox(font_family, font_size, model, question):
    top = tk.Toplevel()

    x,y = root.winfo_rootx(), root.winfo_rooty()
    width, height = root.winfo_width(),root.winfo_height()
    top.geometry("%dx%d+%d+%d" % (width,height,x,y))
    

    # top.geometry("600x300")
    # top.title(f"{model} explanation")
    # message = tk.Label(top, text=question[model], font=(font_family, font_size))
    # message.pack(paddy=10)

    # ok_button = tk.Button(top, text="OK", command=top.destroy)
    # ok_button.pack(paddy=10)

    mb = Messagebox.ok(question[model], f"{model} explanation")


def show_hint_gpt3():
    question = quiz_data[current_question]
    # messagebox.showinfo("Hint", question["gpt3-5turbo"])
    print(question["gpt3-5turbo"])
    
    # tk.messagebox.showinfo("GPT 3.5 Turbo", question["gpt3-5turbo"])
    messagebox.showinfo("Hint", text="", command=custom_messagebox("Times", 16, "gpt3-5turbo", question))
    
def show_hint_gpt4():
    question = quiz_data[current_question]
    # messagebox.showinfo("Hint", question["gpt3-5turbo"])
    print(question["gpt4"])

    # tk.messagebox.showinfo("GPT 4", question["gpt4"])

    messagebox.showinfo("Hint", text="", command=custom_messagebox("Times", 16, "gpt4", question))

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text=f"Incorrect! The right answer is: {question['answer']}", foreground="red")
    
    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question +=1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style = Style(theme="superhero")

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Times", 24))
style.configure("TButton", font=("Times", 20))

# Create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled",
)
next_btn.pack(pady=10)

# Create GPT-3.5-Turbo button
# gpt3_btn = ttk.Button(
#     root,
#     text="GPT-3.5-Turbo",
#     command=show_hint,
#     padding=10
# )
# # gpt3_btn.pack(paddy=10)

cus_msgbox_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)

gpt3_btn = Button(root, text="GPT 3.5 Turbo", font=("Times", 20), command=show_hint_gpt3)
# gpt3_btn = Button(root, text="GPT 3.5 Turbo", font=("Times", 20), command=custom_messagebox("Times", 12, "gpt3-5turbo", quiz_data[current_question]))
gpt3_btn.pack()

gpt4_btn = Button(root, text="GPT4", font=("Times", 20), command=show_hint_gpt4)
gpt4_btn.pack()

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

# Start the main event loop
root.mainloop()