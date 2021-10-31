
import tkinter as tk
import time
import random
import string
import numpy as np
from tkinter import messagebox
import pyperclip

def generate_password():
    password_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    '''for char in range(nr_letters):
      password_list.append(random.choice(letters))'''

    '''for char in range(nr_symbols):
      password_list += random.choice(symbols)
    
    for char in range(nr_numbers):
      password_list += random.choice(numbers)'''

    letter_append = [random.choice(letters) for i in range(nr_letters)]
    symbols_append = [random.choice(numbers) for i in range(nr_symbols)]
    numbers_append = [random.choice(symbols) for i in range(nr_numbers)]

    password_list = letter_append + symbols_append + numbers_append

    random.shuffle(password_list)

    password = "".join(password_list)
    '''for char in password_list:
      password += char'''

    password_entry.insert(0, password)
    pyperclip.copy(password)
    return password


def random_password():
    password_entry.delete(0, 'end')
    generated_password = []
    len_password = random.choice(range(8, 11))
    for i in range(0, len_password-1):
        random_choice_alpha = random.choice(string.ascii_letters)
        generated_password.append(random_choice_alpha)
    random_choice_digit = random.choice(range(0, 10))
    generated_password.append(str(random_choice_digit))
    true_password = ''
    for i in range(0, len(generated_password)):
        x = random.choice(generated_password)
        true_password += x
        generated_password.remove(x)
    password_entry.insert(0, true_password)


with open('passwords.txt', mode='r+') as text:
    first_line = text.readline()
    print('first_line is', first_line )
    if first_line == '':
        print(True)
        text.writelines(f'Website | Email | Password\n')
    elif first_line == f'Website | Email | Password\n':
        pass
    else:
        pass

entry = 0


def add():
    global entry
    entry += 1
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    all_right = tk.messagebox.askokcancel(title='Check please',
                                          message=f'Please check all the input you are going to save\n'
                                                  f'Website: {website}\n'
                                                  f'Email: {email}\nPassword: {password}')

    if website == '':
        no_website = tk.messagebox.showwarning(title='No website error', message='Website empty')
    if email == '':
        no_email = tk.messagebox.showwarning(title='No email error', message='Email empty')
    if password == '':
        no_password = tk.messagebox.showwarning(title='No password error', message='Password empty')

    if all_right:
        if len(password) < 7:
            no_password = tk.messagebox.showwarning(title='No password error',
                                                    message='Password too small, minimum length of password is 8')
        elif len(password) > 7:
            with open('passwords.txt', mode='a') as password_text:
                password_text.writelines(f'{entry} | {website} | {email} | {password} \n')
                password_entry.delete(0, 'end')
                website_entry.delete(0, 'end')



window = tk.Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, highlightthickness=0)

'''timer_label = tk.Label(text='Timer', fg='blue', bg='yellow', highlightthickness=0, font=("Times", 35, 'bold'))
timer_label.grid(column=1, row=0)'''

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
'''timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=("Times", 35, 'bold'))'''
canvas.grid(column=1, row=0)

website_label = tk.Label(text='Website:', fg='blue', highlightthickness=0, font=("Times", 11, 'bold'))
website_label.grid(column=0, row=1)


email_label = tk.Label(text='Email/Username:', fg='blue', highlightthickness=0, font=("Times", 11, 'bold'))
email_label.grid(column=0, row=2)

password_label = tk.Label(text='Password:', fg='blue', highlightthickness=0, font=("Times", 11, 'bold'))
password_label.grid(column=0, row=3)

website_entry = tk.Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = tk.Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'shanudengre82@mail.com')

password_entry = tk.Entry(width=32)
password_entry.grid(column=1, row=3)

generate_password = tk.Button(width=14, text='Generate password', command=generate_password)
generate_password.config(padx=1, pady=1)
generate_password.grid(column=2, row=3)

add_password = tk.Button(width=43, text='Add', command=add)
add_password.grid(column=1, row=4, columnspan=2)

window.mainloop()