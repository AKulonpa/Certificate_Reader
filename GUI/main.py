import tkinter
from tkinter import filedialog
import customtkinter
from tkinterdnd2 import DND_FILES, TkinterDnD
from Certificate_Reader.Reader.Analysis.DocAnalyze import AnalyzeCertificate

lang_code = "eng"
education_field = ""

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

def SelectedEducation():
    global education_field
    education_field = education_entry.get()
    if education_field:
        print(f"Selected education field: {education_field}")
    else:
        print("No education field selected.")

def RunAnalysis():
    SelectedEducation()
    filepaths = file.get().split("; ")
    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    for filepath in filepaths:
        if filepath:
            response = AnalyzeCertificate(filepath, lang_code, education_field)
            output_box.insert("end", f"File {filepath}:\n{response}\n\n")
    output_box.configure(state="disabled")

def Drop(event):
    file.delete(0, tkinter.END)
    file.insert(0, event.data.strip('{}'))

def SaveAnswers():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filepath:
        output_text = output_box.get("1.0", "end-1c")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(output_text)

#App frame
app = TkinterDnD.Tk()
#System settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app.geometry("800x720")
app.title("Certificate Reader")

#UI elements
title = customtkinter.CTkLabel(app, text="Certificate analyser 3000", font=("Arial", 30), text_color="#68ad8b")
title.pack(pady=30)
title = customtkinter.CTkLabel(app, text="insert the files you want to analyze and select the correct language", font=("Arial", 18))
title.pack(pady=10)
file = customtkinter.CTkEntry(app, placeholder_text="File path or drag and drop here", width=400)
file.pack(pady=10)
file.drop_target_register(DND_FILES)
file.dnd_bind('<<Drop>>', Drop)

#Frame for buttons
button_frame1 = customtkinter.CTkFrame(app)
button_frame1.pack(pady=10)

select = customtkinter.CTkButton(button_frame1, text="Browse files", command=SelectFile, width=70)
select.pack(side="left", padx=5)
lang = customtkinter.CTkOptionMenu(button_frame1, values=["English", "Finnish"], command=SelectedLang, width=70)
lang.pack(side="left", padx=5)
education_entry = customtkinter.CTkEntry(app, placeholder_text="What is your education field?", width=400)
education_entry.pack(pady=10)
education_entry.bind("<FocusOut>", lambda e: SelectedEducation())

#Frame for buttons
button_frame2 = customtkinter.CTkFrame(app)
button_frame2.pack(pady=10)

analyze_button = customtkinter.CTkButton(button_frame2, text="Analyse files", font=("Arial", 25), width=220, height=60, command=RunAnalysis)
analyze_button.pack(side="left", padx=5)
save_button = customtkinter.CTkButton(button_frame2, text="Save answers", font=("Arial", 25), width=220, height=60, command=SaveAnswers)
save_button.pack(side="left", padx=5)
output_box = customtkinter.CTkTextbox(app, width=700, height=300, state ="disabled", wrap="word")
output_box.pack(pady=20)

app.configure(bg="#2b2b2b")

#Run app
app.mainloop()