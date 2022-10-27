from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button, END, messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_value = website_entry.get()
    username_value = username_entry.get()
    pass_value = password_entry.get()

    if website_value == "":
        messagebox.showerror(title="Field is empty", message="The website field should not be empty")
        return
    if username_value == "":
        messagebox.showerror(title="Field is empty", message="The username/email field should not be empty")
        return
    if pass_value == "":
        messagebox.showerror(title="Field is empty", message="The password field should not be empty")
        return

    isOk = messagebox.askokcancel(title="Confirmation", message=f"These are the credentials you've entered: \n\n"
                                                                f"Website: {website_value} \nUsername/Email: {username_value}\nPassword: {pass_value}\n\n"
                                                                f"Is it Ok ?")
    if isOk:
        with open("creds.txt", "a") as f:
            f.write(f"{website_value}  | {username_value} | {pass_value}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(10, 10, image=photo, anchor="nw")
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=("Arial", 12))
website_label.grid(column=0, row=1, sticky="EW")

username_label = Label(text="Email/Username: ", font=("Arial", 12))
username_label.grid(column=0, row=2, sticky="EW")

password_label = Label(text="Password: ", font=("Arial", 12))
password_label.grid(column=0, row=3, sticky="EW")

website_entry = Entry(window, width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

username_entry = Entry(window, width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(0, "jrsylvester2000@gmail.com")

password_entry = Entry(window, width=21)
password_entry.grid(column=1, row=3, sticky="EW")

generate_button = Button(text="Generate Password", command=generate_pass)
generate_button.grid(column=2, row=3, sticky="EW", padx=5)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
