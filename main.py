import random
import tkinter as tk
from diccionariodepruebas import concepts
import copy 

copy_dictionary = copy.deepcopy(concepts) # copying the dictionary to avoid modifying the original one

random_key = random.choice(list(copy_dictionary.keys())) # turning the dictionary into a list and choosing a random key
root = tk.Tk()
root.title("CQ: Concept Quiz")
root.geometry("850x230")  
root.resizable(False, False) 

total_concepts = len(concepts)
correct_answers = 0
wrong_answers = 0

my_font = ("Terminal", 10)

# Defining the function check_answer 

def check_answer(event=None):
    global random_key, correct_answers, wrong_answers, button_result, label_result, label_end_of_quiz, random_key, copy_dictionary

    # Obtaining user answer
    user_answer = entry_answer.get().lower()    

    # Verifying answer
    if user_answer == random_key:        
                 
        label_answer.config(text="Correct!")
        correct_answers += 1  # Increment correct answers

    else:        
        label_answer.config(text=f'''Wrong Answer!
The Correct Answer is: {random_key}''')
        wrong_answers += 1  # Increment wrong answers

    del copy_dictionary[random_key] # deleting already asked item to empty the dictionary and not repeat it
         
    # Generating new question
    random_key = random.choice(list(copy_dictionary.keys()))
    label_question.config(text=copy_dictionary[random_key])
    label_previous_answer.config(text=f"Previous Answer: {entry_answer.get()}")
    entry_answer.delete(0, tk.END)
    
    # Binding result button to result page
    if correct_answers + wrong_answers == total_concepts -1:

        label_question.pack_forget()
        entry_answer.pack_forget()
        button_send.pack_forget()
        label_previous_answer.pack_forget()
        label_answer.pack_forget()
        
        # Create a button to show the result page and showing it
        label_end_of_quiz = tk.Label(root)
        label_end_of_quiz.config(text="End of quiz", font=("Terminal", 13))
        label_end_of_quiz.pack(padx=20, pady=40)
        button_result = tk.Button(root, text="Show Results", command=show_result_page, font=my_font)
        button_result.pack(padx=0, pady=5)
        copy_dictionary = copy.deepcopy(concepts) # resetting the dictionary to its original state

    
# Creating function Result Page and its elements elements + hiding main quiz ones

def show_result_page():
    global correct_answers, wrong_answers, label_question, label_previous_answer, entry_answer, button_send, label_answer, label_result, button_result, button_restart, copy_dictionary, main_quiz

    # Hide main quiz elements
    label_question.pack_forget()
    label_previous_answer.pack_forget()
    entry_answer.pack_forget()
    button_send.pack_forget()
    label_answer.pack_forget()
    label_end_of_quiz.pack_forget()
    button_result.pack_forget()

    # Create result page elements
    label_result = tk.Label(root)
    label_result.config(text=f"Correct Answers: {correct_answers}\nWrong Answers: {wrong_answers}", font=("Terminal", 12))       
    label_result.pack(padx=20, pady=40)
    
    button_restart = tk.Button(root, text="Restart Quiz", command=restart_quiz, font=my_font)
    button_restart.pack()


# Creating main quiz

def main_quiz():
    global label_question, label_previous_answer, entry_answer, button_send, label_answer, button_restart, label_result, copy_dictionary         
       
    label_welcome.pack_forget()
    button_start.pack_forget()  
       
    # Showing main quiz elements

    label_question.pack(padx=20, pady=10) 
    entry_answer.pack(expand=False, ipadx=20, ipady=1, padx=0, pady=5)
    button_send.pack(padx=0, pady=5)
    label_previous_answer.config(text="") # Resetting previous answer label
    label_previous_answer.pack()
    label_answer.pack()

    entry_answer.bind("<Return>", check_answer) 

def restart_quiz():
    global correct_answers, wrong_answers, random_key, copy_dictionary

    button_restart.pack_forget()
    label_result.pack_forget()

    # Reset variables
    correct_answers = 0
    wrong_answers = 0
    random_key = random.choice(list(copy_dictionary.keys()))
    label_answer.config(text="")
    label_previous_answer.config(text="")

    # Show main quiz elements again
    label_question.pack(padx=20, pady=10)
    entry_answer.pack(expand=False, ipadx=20, ipady=1, padx=0, pady=5)
    button_send.pack(padx=0, pady=5)
    label_previous_answer.pack()
    label_answer.pack()

    # Update question and previous answer labels
    label_question.config(text=copy_dictionary[random_key])

    entry_answer.delete(0, tk.END)  # Clear entry


# Creating main quiz elements

entry_answer = tk.Entry(root, font=my_font)
label_question = tk.Label(root, text=copy_dictionary[random_key], font=my_font)
label_previous_answer = tk.Label(root, text=f"Previous Answer: {entry_answer.get()}", font=my_font)
label_answer = tk.Label(root, font=my_font)
button_send = tk.Button(root, text="Send", command=check_answer, font=my_font) 
    

# Creating welcome page

label_welcome = tk.Label(root, text="Welcome to CQ!", font=("Terminal", 13))
button_start = tk.Button(root, text="Start Here", command=main_quiz, font=my_font)


# Showing welcome page elements

button_restart = tk.Button(root, text="Restart Quiz", command=main_quiz, font=my_font)
label_result = tk.Label(root)

label_welcome.pack(padx=20, pady=40)
button_start.pack(padx=0, pady=1)


# Starting main loop

root.mainloop()


