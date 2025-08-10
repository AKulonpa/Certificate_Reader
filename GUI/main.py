import tkinter
from tkinter import filedialog
import customtkinter
from tkinterdnd2 import DND_FILES, TkinterDnD
from Certificate_Reader.Reader.Analysis.DocAnalyze import AnalyzeCertificate

lang_code = "eng"

def SelectFile():
    filepaths = filedialog.askopenfilenames(title="Select files", filetypes=[("All files", "*.*")])
    if filepaths:
        file.delete(0, tkinter.END)
        file.insert(0, "; ".join(filepaths))

def SelectedLang(value):
    global lang_code
    if value == "English":
        lang_code = "eng"
    elif value == "Finnish":
        lang_code = "fin"
    else:
        lang_code = "eng"  # Default to English if no valid selection is made
    print(f"Selected language code: {lang_code}")

def SaveAnswers():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("Sample answers saved.")

def RunAnalysis():
    filepaths = file.get().split("; ")
    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    for filepath in filepaths:
        if filepath:
            response = AnalyzeCertificate(filepath, lang_code)
            output_box.insert("end", f"File {filepath}:\n{response}\n\n")
    output_box.configure(state="disabled")

def Drop(event):
    file.delete(0, tkinter.END)
    file.insert(0, event.data.strip('{}'))

#App frame
app = TkinterDnD.Tk()
#System settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app.geometry("800x800")
app.title("Certificate Reader")

#UI elements
title = customtkinter.CTkLabel(app, text="Insert the files you want to analyze and select the correct language", font=("Arial", 20))
title.pack(pady=20)
title = customtkinter.CTkLabel(app, text="Insert the files you want to analyze and select the correct language", font=("Arial", 20))
title.pack(pady=20)
file = customtkinter.CTkEntry(app, placeholder_text="File path or drag and drop here", width=400)
file.pack(pady=10)
file.drop_target_register(DND_FILES)
file.dnd_bind('<<Drop>>', Drop)

#Frame for buttons
button_frame = customtkinter.CTkFrame(app)
button_frame.pack(pady=10)

select = customtkinter.CTkButton(button_frame, text="Browse files", command=SelectFile, width=100)
select.pack(side="left", padx=5)
lang = customtkinter.CTkOptionMenu(button_frame, values=["English", "Finnish"], command=SelectedLang, width=100)
lang.pack(side="left", padx=5)
analyze_button = customtkinter.CTkButton(app, text="Analyse", command=RunAnalysis)
analyze_button.pack(pady=10)
output_box = customtkinter.CTkTextbox(app, width=700, height=300, state ="disabled")
output_box.pack(pady=20)
analyze_button = customtkinter.CTkButton(app, text="Save answers", command=SaveAnswers)
analyze_button.pack(pady=10)

app.configure(bg="#2b2b2b")

#Run app
app.mainloop()