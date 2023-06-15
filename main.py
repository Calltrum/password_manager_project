from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
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
    web_text = website_entry.get().title()
    email_text = email_entry.get()
    password_text = password_entry.get()
    new_data = {
        web_text: {'email': email_text,
                   'password': password_text
                   }
    }
    if len(web_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title='oops', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as data_collector:
                # Reading old data
                data = json.load(data_collector)
        except FileNotFoundError:
            with open('data.json', 'w') as data_collector:
                # Saving the updated data
                json.dump(new_data, data_collector, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open('data.json', 'w') as data_collector:
                # Saving the updated data
                json.dump(data, data_collector, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    try:
        with open('data.json', 'r') as data_file:
            json_dict = json.load(data_file)
            web_name = website_entry.get().title()
            # codes in comment are by me
            # web_dict = json_dict[web_name]
            # email_pick = web_dict['email']
            # pass_pick = web_dict['password']
    except FileNotFoundError:
        messagebox.showinfo(title='Oops', message='No Data File Found.')
    # except KeyError:
        # messagebox.showinfo(title='Oops', message='No details for the website exists.')
    else:
        # messagebox.showinfo(title=web_name, message=f"Email: {email_pick}\nPassword: {pass_pick}")
        if web_name in json_dict:
            email = json_dict[web_name]['email']
            password = json_dict[web_name]['password']
            messagebox.showinfo(title=web_name, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='Oops', message=f'No detail for {web_name} exists.')


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
website_entry.grid(row=1, column=1, sticky='EW')
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

search_button = Button(text='Search', width=18, command=find_password)
search_button.grid(row=1, column=2, sticky='EW')

window.mainloop()
