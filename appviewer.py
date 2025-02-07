import tkinter as tk
import csv

def display_csv():
    try:
        with open('app_tracking.csv', 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

        text_box.delete(1.0, tk.END)  # Clear the text box
        for row in data:
            text_box.insert(tk.END, ",".join(row) + "\n")
    except FileNotFoundError:
        text_box.insert(tk.END, "No CSV file found.")

root = tk.Tk()
root.title("CSV Viewer")

text_box = tk.Text(root, width=80, height=20)
text_box.pack()

display_csv()  # Display the CSV file initially
root.after(1000, display_csv)  # Update the display every 1 second

root.mainloop()

