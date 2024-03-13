import tkinter as tk
import random

class MultipleChoiceGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Multiple Choice Game")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "choices": [("London", "London"), ("Paris", "Paris"), ("Berlin", "Berlin"), ("Rome", "Rome")],
                "correct_answer": "Paris",
                "hint": "It's known as the City of Light."
            },
            {
                "question": "What is the largest ocean on Earth?",
                "choices": [("Pacific Ocean", "Pacific Ocean"), ("Atlantic Ocean", "Atlantic Ocean"), ("Indian Ocean", "Indian Ocean"), ("Arctic Ocean", "Arctic Ocean")],
                "correct_answer": "Pacific Ocean",
                "hint": "It stretches from the western shores of the Americas to the eastern shores of Asia and Australia."
            },
            {
                "question": "What is the chemical symbol for water?",
                "choices": [("W", "W"), ("H2O", "H2O"), ("O2", "O2"), ("H2", "H2")],
                "correct_answer": "H2O",
                "hint": "It consists of two hydrogen atoms and one oxygen atom."
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "choices": [("Venus", "Venus"), ("Mars", "Mars"), ("Jupiter", "Jupiter"), ("Saturn", "Saturn")],
                "correct_answer": "Mars",
                "hint": "It's the fourth planet from the Sun in our solar system."
            },
            {
                "question": "Who wrote 'To Kill a Mockingbird'?",
                "choices": [("Harper Lee", "Harper Lee"), ("Mark Twain", "Mark Twain"), ("J.K. Rowling", "J.K. Rowling"), ("George Orwell", "George Orwell")],
                "correct_answer": "Harper Lee",
                "hint": "The author's first name is Nelle."
            }
        ]

        self.current_question_index = -1
        self.hint_shown = False

        self.question_label = tk.Label(master, text="", font=("Helvetica", 16))
        self.question_label.pack()

        self.choice_radios = []
        for _ in range(4):
            choice_radio = tk.Radiobutton(master, text="", variable=tk.StringVar(), value="", font=("Helvetica", 14))
            self.choice_radios.append(choice_radio)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer, font=("Helvetica", 14))
        self.submit_button.pack()

        self.hint_button = tk.Button(master, text="Hint", command=self.show_hint, font=("Helvetica", 14))
        self.hint_button.pack()

        self.next_question()

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            choices = question_data["choices"]
            random.shuffle(choices)
            for i in range(4):
                self.choice_radios[i].config(text=choices[i][0], value=choices[i][1])
                self.choice_radios[i].pack()
            self.hint_shown = False
        else:
            self.question_label.config(text="End of questions!")

    def check_answer(self):
        selected_answer = None
        for choice_radio in self.choice_radios:
            if choice_radio.cget("variable").get():
                selected_answer = choice_radio.cget("variable").get()
                break

        if selected_answer:
            correct_answer = self.questions[self.current_question_index]["correct_answer"]
            if selected_answer == correct_answer:
                result_text = "Correct!"
            else:
                result_text = f"Incorrect. The correct answer is {correct_answer}."
            result_label = tk.Label(self.master, text=result_text, font=("Helvetica", 14))
            result_label.pack()
            self.master.after(2000, result_label.destroy)  # Remove result label after 2 seconds
            self.master.after(2000, self.next_question)  # Move to the next question after 2 seconds
        else:
            error_label = tk.Label(self.master, text="Please select an answer!", font=("Helvetica", 14))
            error_label.pack()
            self.master.after(2000, error_label.destroy)  # Remove error label after 2 seconds

    def show_hint(self):
        if self.current_question_index < len(self.questions) and not self.hint_shown:
            hint_text = self.questions[self.current_question_index]["hint"]
            hint_label = tk.Label(self.master, text=hint_text, font=("Helvetica", 14))
            hint_label.pack()
            self.hint_shown = True


def main():
    root = tk.Tk()
    game = MultipleChoiceGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
