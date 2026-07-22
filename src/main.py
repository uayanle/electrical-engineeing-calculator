import tkinter as tk

root = tk.Tk()  # creates the main application window

# window title
root.title("Electrical Engineering Calculator")

# window size
root.geometry("1000x600")

# prevention of window becoming too small
root.minsize(800, 500)

# creating the left menu
menu_frame = tk.Frame(root, width=250, bg="#2C3E50")
menu_frame.pack(side='left', fill='y')

# creating the menu title because we want label inside the menu frame
menu_title = tk.Label(
    menu_frame,
    text='Calculators',
    font=('Arial', 16, 'bold'),
    fg='white',
    bg='#2C3E50',
)
# adding padding to the menu title to make it look better
menu_title.pack(pady=20)

# adding the first button
three_phase_button = tk.Button(
    menu_frame,
    text='Three Phase Calculator',
    width=20,
)
three_phase_button.pack(pady=5)

# adding the second button
voltage_drop_button = tk.Button(
    menu_frame,
    text='Voltage Drop Calculator',
    width=20,

)
voltage_drop_button.pack(pady=5)

# adding the third button
power_factor_button = tk.Button(
    menu_frame,
    text='Power Factor Calculator',
    width=20,

)
power_factor_button.pack(pady=5)

# adding the fourth button
transformer_button = tk.Button(
    menu_frame,
    text='Transformer Calculator',
    width=20,

)
transformer_button.pack(pady=5)

# adding the fifth button
motor_current_button = tk.Button(
    menu_frame,
    text='Motor Current Calculator',
    width=20,
)

motor_current_button.pack(pady=5)

# adding the sixth button
cable_sizing_button = tk.Button(
    menu_frame,
    text='Cable sizing Calculator',
    width=20
)
cable_sizing_button.pack(pady=5)

# adding the seventh button
short_circuit_button = tk.Button(
    menu_frame,
    text='Short Circuit Calculator',
    width=20
)

short_circuit_button.pack(pady=5)

# creating my main content workspace
content_frame = tk.Frame(root, bg='white')
content_frame.pack(side='right', expand=True, fill='both')

# welcome message
welcome_label = tk.Label(
    content_frame,
    text='Welcome to the Electrical Engineering Calculator!',
    font=('Arial', 18),
    bg='white',

)

# adding padding to the welcome message to make it look better
welcome_label.pack(pady=40)


# keep the application running
root.mainloop()
