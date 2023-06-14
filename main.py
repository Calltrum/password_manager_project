from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    pass_letter = [password_list.append(choice(letters)) for char in range(randint(8, 10))]
    pass_symbol = [password_list.append(choice(symbols)) for har in range(randint(2, 4))]
    pass_num = [password_list.append(choice(numbers)) for cha in range(randint(2, 4))]
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    if len(web_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title='oops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web_text, message=f'These are the details entered: \nEmail: {email_text} '
                                                               f'\nPassword: {password_text} \nIs it okay to save?')

        if is_ok:
            with open('data.txt', 'a') as data_collector:
                data_collector.write(f'{web_text} | {email_text} | {password_text}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image_name = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image_name)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky='EW')
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky='EW')
email_entry.insert(0, 'Chideraomeje190@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='EW')

password_gen_button = Button(text='Generate Password', command=generate_password)
password_gen_button.grid(row=3, column=2, sticky='EW')

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()
