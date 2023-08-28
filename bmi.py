import tkinter as tk
import ttkbootstrap as ttk


# Create the Window and add to Memory
window=ttk.Window(themename='cyborg')

# Add the Title
window.title('BMI Calculator')

# Add the icon
window.iconbitmap('xi.ico')

# Create the fixed size of our window
window.geometry("550x250")

# Create the Header
lbl_header=ttk.Label(text="BMI Calculator", bootstyle="danger", font=('Helvetica, 15'))
lbl_header.grid(row=0, column=1, padx=10)


lbl_feet=ttk.Label(text="Please Enter your Feet Value", bootstyle="success")
lbl_feet.grid(row=1, column=0, pady=10)

# Create the Entry
entry_feet=ttk.Entry()
entry_feet.grid(row=1, column=1, padx=10)

lbl_inches=ttk.Label(text="Please Enter your Inch Value", bootstyle="success")
lbl_inches.grid(row=2, column=0, pady=10)

entry_inches=ttk.Entry()
entry_inches.grid(row=2, column=1, padx=10)

lbl_weight=ttk.Label(text="Please Enter your Weight", bootstyle="success")
lbl_weight.grid(row=3, column=0, pady=10)

entry_weight=ttk.Entry()
entry_weight.grid(row=3, column=1, padx=10)

def calculate_bmi():
    try:
        entry1=int(entry_feet.get())
        entry2=int(entry_inches.get())
        entry3=int(entry_weight.get())

        new_height=(entry1 * 0.3048) + (entry2 * 0.0254)
        new_weight=(entry3 * 0.453592)

        bmi=round((new_weight/new_height), 2)

        if bmi <=18.5:
            lbl_answer.configure(text=f"Your BMI is: {bmi} you are underweight")
        elif bmi <=24.9:
            lbl_answer.configure(text=f"Your BMI is {bmi} and you are Healthy")
        elif bmi <=29.9:
            lbl_answer.configure(text=f"Your BMI is {bmi} and you are Overweight")
        else:
            lbl_answer.configure(text=f"Your BMI is {bmi}. Please, see a doctor")
    except ValueError:
        lbl_answer['text'] = "Alphanumeric Characters are not allowed!!"

btn_bmi=ttk.Button(text="Calculate BMI", bootstyle="danger", command=calculate_bmi)
btn_bmi.grid(row=4, column=1, pady=10, padx=20)


def clear_entry():
    entry_feet.delete(0, "end")
    entry_inches.delete(0, "end")
    entry_weight.delete(0, "end")
    lbl_answer['text']=""


btn_clear=ttk.Button(text="Clear", bootstyle="danger", command=clear_entry)
btn_clear.grid(row=4, column=2)


lbl_answer=ttk.Label(text="", bootstyle="success")
lbl_answer.grid(row=5, column=1, pady=10)

window.mainloop()