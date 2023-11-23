from customtkinter import *

set_appearance_mode("dark")

# Function to handle the button click
def login():
    entered_email = email_entry.get()
    entered_password = password_entry.get()

    # Replace with your login logic here
    if entered_email == "@gmail.com":
        result.configure( text_color="green", text="Login successful!")
    else:
        result.configure(text_color="red",text="Login failed. Please check your credentials.")

    if len(entered_password) >= 8:
        save.configure(text_color="green", text="Your password is strong enough")
    else:
        save.configure(text_color="red",text="Your password is not strong enough")


goal = CTk()
goal.geometry("400x400")

label = CTkLabel(goal, text_color="green", text="Log In", font=('Arial', 30))
label.place(x=150, y=10)

label = CTkLabel(goal, font=('Arial', 15), text="Email:")
label.place(x=55, y=70)
email_entry = CTkEntry(goal, width=300, height=45, placeholder_text="Enter your email", border_color="#fff886", corner_radius=10,)
email_entry.place(x=50, y=95)


label = CTkLabel(goal, font=('Arial', 15), text="Password:")
label.place(x=55, y=165)
password_entry = CTkEntry(goal, width=300, height=45, placeholder_text="Enter your password", border_color="#fff886", corner_radius=10)
password_entry.place(x=50, y=190)

button = CTkButton(goal, text="Submit", width=100, height=40, command=login)
button.place(x=150, y=260)

result = CTkLabel(goal, text="",)
result.place(x=60, y=140)  


save = CTkLabel(goal, text="",)
save.place(x=60, y=235) 


goal.mainloop()
