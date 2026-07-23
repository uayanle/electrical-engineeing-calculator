import tkinter as tk


def show_voltage_drop_calculator(content_frame):
    """Display the Voltage Drop Calculator page."""

    # removing any existing widgets in the content frame
    for widget in content_frame.winfo_children():
        widget.destroy()

        # create a new title
    title = tk.Label(
        content_frame,
        text='Voltage Drop Calculator',
        font=('Arial', 20, 'bold'),
        bg='white'
    )
    title.pack(pady=20)

    # create a label and entry for current
    current_label = tk.Label(
        content_frame,
        text='Current (A):',
        font=('Arial', 12)
    )
    current_label.pack(pady=5)

    current_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12)
    )

    current_entry.pack(pady=5)

    # create a label for resistance
    resistance_label = tk.Label(
        content_frame,
        text='Resistance (Ω):',
        font=('Arial', 12)
    )

    resistance_label.pack(pady=5)

    resistance_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12)
    )

    resistance_entry.pack(pady=5)

    # calculation function

    def calculate_voltage_drop():
        try:
            current = float(current_entry.get())
            resistance = float(resistance_entry.get())
            voltage_drop = current * resistance
            result_label.config(text=f'Voltage Drop: {voltage_drop:.2f} V')
        except ValueError:
            result_label.config(
                text='Invalid input. Please enter valid numbers.')

    # create a label to display the result
    result_label = tk.Label(
        content_frame,
        text='Voltage Drop: 0.00 V',
        font=('Arial', 12),
        fg='blue'
    )

    result_label.pack(pady=20)

    # create a button to calculate
    calculate_button = tk.Button(
        content_frame,
        text='Calculate',
        font=('Arial', 12),
        command=calculate_voltage_drop
    )

    calculate_button.pack(pady=10)
