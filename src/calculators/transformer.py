import tkinter as tk


def show_transformer_calculator(content_frame):
    """Display the Transformer Calculator page."""

    # remove any existing widgets
    for widget in content_frame.winfo_children():
        widget.destroy()

    # create a new title
    title = tk.Label(
        content_frame,
        text='Transformer Calculator',
        font=('Arial', 20, 'bold'),
        bg='white'
    )
    title.pack(pady=20)

    # create a label and entry for primary turns
    primary_turns_label = tk.Label(
        content_frame,
        text='Primary turns:',
        font=('Arial', 12)
    )
    primary_turns_label.pack(pady=5)

    primary_turns_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12)
    )
    primary_turns_entry.pack(pady=5)

    # create a label and entry for secondary turns
    secondary_turns_label = tk.Label(
        content_frame,
        text='Secondary turns:',
        font=('Arial', 12)
    )

    secondary_turns_label.pack(pady=5)

    secondary_turns_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12)
    )

    secondary_turns_entry.pack(pady=5)

    # create a label and entry for primary voltage

    primary_voltage_label = tk.Label(
        content_frame,
        text='Primary Voltage (V):',
        font=('Arial', 12)
    )

    primary_voltage_label.pack(pady=5)

    primary_voltage_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12)
    )

    primary_voltage_entry.pack(pady=5)

    # create a result label for displaying the secondary voltage
    result_label = tk.Label(
        content_frame,
        text='',
        font=('Arial', 12),
        bg='white'
    )
    result_label.pack(pady=10)

    def calculate_secondary_voltage():
        try:
            primary_turns = float(primary_turns_entry.get())
            secondary_turns = float(secondary_turns_entry.get())
            primary_voltage = float(primary_voltage_entry.get())
            if primary_turns == 0:
                raise ValueError('Primary turns must be non-zero')
            secondary_voltage = (
                secondary_turns / primary_turns) * primary_voltage
            result_label.config(
                text=f'Secondary Voltage: {secondary_voltage:.2f} V')
        except ValueError:
            result_label.config(text='Please enter valid numeric values.')

    calculate_button = tk.Button(
        content_frame,
        text='Calculate',
        font=('Arial', 12),
        command=calculate_secondary_voltage
    )
    calculate_button.pack(pady=10)
