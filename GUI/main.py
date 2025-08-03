import tkinter
from tkinter import filedialog
import customtkinter


def select_file():
    filepath = filedialog.askopenfilename(title="Select a file", filetypes=[("All files", "*.*")])
    if filepath:
        file.delete(0, tkinter.END)
        file.insert(0, filepath)

def save_answers():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("Sample answers saved.")

def run_analysis():
    pass


#System settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#App frame
app = customtkinter.CTk()
app.geometry("800x600")
app.title("Certificate Reader")

#UI elements
title = customtkinter.CTkLabel(app, text="Insert the files you want to analyze and select the correct language", font=("Arial", 20))
title.pack(pady=20)
file = customtkinter.CTkEntry(app, placeholder_text="File path or drag and drop here", width=400)
file.pack(pady=10)
select = customtkinter.CTkButton(app, text="Browse", command=select_file)
select.pack(pady=10)
lang = customtkinter.CTkOptionMenu(app, values=["English", "Finnish"], variable=selected_lang, width=200)
lang.pack(pady=10)
analyze_button = customtkinter.CTkButton(app, text="Analyze", command=run_analysis)
analyze_button.pack(pady=10)
analyze_button = customtkinter.CTkButton(app, text="Save answers", command=save_answers)
analyze_button.pack(pady=10)

#Run app
app.mainloop()