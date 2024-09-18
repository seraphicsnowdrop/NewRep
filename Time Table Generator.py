import tkinter as tk
from tkinter import messagebox, ttk
import random

# Function to generate a timetable for a given section
def generate_timetable_for_section(subjects, days_of_week, periods_per_day):
    timetable = {day: ['' for _ in range(periods_per_day)] for day in days_of_week}
    all_classes = []
    
    for subject, info in subjects.items():
        count = info['count']
        teacher = info['teacher']
        all_classes.extend([f"{subject} ({teacher})"] * count)
    
    random.shuffle(all_classes)
    
    for i in range(len(all_classes)):
        place_class_in_timetable(all_classes, timetable, days_of_week, periods_per_day)
    
    return timetable

# Helper function to place a class in the timetable ensuring no overlap and no more than 2 consecutive periods
def place_class_in_timetable(all_classes, timetable, days_of_week, periods_per_day):
    class_name = all_classes.pop(0)
    
    day = random.choice(days_of_week)
    period = random.choice(range(periods_per_day))
    
    attempts = 0
    max_attempts = 100
    
    while (timetable[day][period] != '' or
           (period > 0 and timetable[day][period-1] == class_name) or
           (period > 1 and timetable[day][period-2] == class_name)) and attempts < max_attempts:
        day = random.choice(days_of_week)
        period = random.choice(range(periods_per_day))
        attempts += 1
    
    if timetable[day][period] == '' and \
       not (period > 0 and timetable[day][period-1] == class_name) and \
       not (period > 1 and timetable[day][period-2] == class_name):
        timetable[day][period] = class_name

# Function to generate the full school timetable
def generate_full_school_timetable(subjects_by_section, days_of_week, periods_per_day):
    school_timetable = {}
    
    for section_name, subjects in subjects_by_section.items():
        school_timetable[section_name] = generate_timetable_for_section(subjects, days_of_week, periods_per_day)
    
    return school_timetable

# Function to display the timetable for each section
def display_timetable(timetable, section_name, days_of_week, periods_per_day):
    section_label = tk.Label(table_frame, text=f"{section_name} Timetable", font=("Arial", 12, "bold"))
    section_label.pack()
    
    table = ttk.Treeview(table_frame, columns=days_of_week, show='headings', height=periods_per_day)
    table.pack()
    
    for day in days_of_week:
        table.heading(day, text=day)
        table.column(day, width=150)
    
    for period in range(periods_per_day):
        row = [timetable[day][period] for day in days_of_week]
        table.insert("", "end", values=row)

# Function to get input and generate the timetables for the entire school
def generate():
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    periods_per_day = 8
    
    # Define the subjects and teachers for each section
    subjects_by_section = {
        'Section A': {
            'English': {'count': int(english_count_A_entry.get()), 'teacher': english_teacher_A_entry.get()},
            '2nd Language': {'count': int(language_count_A_entry.get()), 'teacher': language_teacher_A_entry.get()},
            'Work Education': {'count': int(worked_count_A_entry.get()), 'teacher': worked_teacher_A_entry.get()},
            'Math': {'count': int(math_count_A_entry.get()), 'teacher': math_teacher_A_entry.get()},
            'Social Science': {'count': int(social_count_A_entry.get()), 'teacher': social_teacher_A_entry.get()},
            'Physics': {'count': int(physics_count_A_entry.get()), 'teacher': physics_teacher_A_entry.get()},
            'Chemistry': {'count': int(chemistry_count_A_entry.get()), 'teacher': chemistry_teacher_A_entry.get()},
            'Biology': {'count': int(biology_count_A_entry.get()), 'teacher': biology_teacher_A_entry.get()},
            'Physical Education': {'count': int(pe_count_A_entry.get()), 'teacher': pe_teacher_A_entry.get()},
            'Library': {'count': int(library_count_A_entry.get()), 'teacher': library_teacher_A_entry.get()},
            'Art': {'count': int(art_count_A_entry.get()), 'teacher': art_teacher_A_entry.get()},
            'AI': {'count': int(ai_count_A_entry.get()), 'teacher': ai_teacher_A_entry.get()}
        },
        'Section B': {
            'English': {'count': int(english_count_B_entry.get()), 'teacher': english_teacher_B_entry.get()},
            '2nd Language': {'count': int(language_count_B_entry.get()), 'teacher': language_teacher_B_entry.get()},
            'Work Education': {'count': int(worked_count_B_entry.get()), 'teacher': worked_teacher_B_entry.get()},
            'Math': {'count': int(math_count_B_entry.get()), 'teacher': math_teacher_B_entry.get()},
            'Social Science': {'count': int(social_count_B_entry.get()), 'teacher': social_teacher_B_entry.get()},
            'Physics': {'count': int(physics_count_B_entry.get()), 'teacher': physics_teacher_B_entry.get()},
            'Chemistry': {'count': int(chemistry_count_B_entry.get()), 'teacher': chemistry_teacher_B_entry.get()},
            'Biology': {'count': int(biology_count_B_entry.get()), 'teacher': biology_teacher_B_entry.get()},
            'Physical Education': {'count': int(pe_count_B_entry.get()), 'teacher': pe_teacher_B_entry.get()},
            'Library': {'count': int(library_count_B_entry.get()), 'teacher': library_teacher_B_entry.get()},
            'Art': {'count': int(art_count_B_entry.get()), 'teacher': art_teacher_B_entry.get()},
            'AI': {'count': int(ai_count_B_entry.get()), 'teacher': ai_teacher_B_entry.get()}
        }
    }
    
    try:
        school_timetable = generate_full_school_timetable(subjects_by_section, days_of_week, periods_per_day)
        
        for section_name, timetable in school_timetable.items():
            display_timetable(timetable, section_name, days_of_week, periods_per_day)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for the subjects.")

# GUI setup
root = tk.Tk()
root.title("Full School Timetable Generator")

# Entry for subjects and teachers for Section A and Section B
tk.Label(root, text="Subject").grid(row=0, column=0)
tk.Label(root, text="Periods (Section A)").grid(row=0, column=1)
tk.Label(root, text="Teacher (Section A)").grid(row=0, column=2)
tk.Label(root, text="Periods (Section B)").grid(row=0, column=3)
tk.Label(root, text="Teacher (Section B)").grid(row=0, column=4)

tk.Label(root, text="English:").grid(row=1, column=0)
english_count_A_entry = tk.Entry(root)
english_count_A_entry.grid(row=1, column=1)
english_teacher_A_entry = tk.Entry(root)
english_teacher_A_entry.grid(row=1, column=2)
english_count_B_entry = tk.Entry(root)
english_count_B_entry.grid(row=1, column=3)
english_teacher_B_entry = tk.Entry(root)
english_teacher_B_entry.grid(row=1, column=4)

tk.Label(root, text="2nd Language:").grid(row=2, column=0)
language_count_A_entry = tk.Entry(root)
language_count_A_entry.grid(row=2, column=1)
language_teacher_A_entry = tk.Entry(root)
language_teacher_A_entry.grid(row=2, column=2)
language_count_B_entry = tk.Entry(root)
language_count_B_entry.grid(row=2, column=3)
language_teacher_B_entry = tk.Entry(root)
language_teacher_B_entry.grid(row=2, column=4)

tk.Label(root, text="Work Education:").grid(row=3, column=0)
worked_count_A_entry = tk.Entry(root)
worked_count_A_entry.grid(row=3, column=1)
worked_teacher_A_entry = tk.Entry(root)
worked_teacher_A_entry.grid(row=3, column=2)
worked_count_B_entry = tk.Entry(root)
worked_count_B_entry.grid(row=3, column=3)
worked_teacher_B_entry = tk.Entry(root)
worked_teacher_B_entry.grid(row=3, column=4)

tk.Label(root, text="Math:").grid(row=4, column=0)
math_count_A_entry = tk.Entry(root)
math_count_A_entry.grid(row=4, column=1)
math_teacher_A_entry = tk.Entry(root)
math_teacher_A_entry.grid(row=4, column=2)
math_count_B_entry = tk.Entry(root)
math_count_B_entry.grid(row=4, column=3)
math_teacher_B_entry = tk.Entry(root)
math_teacher_B_entry.grid(row=4, column=4)

tk.Label(root, text="Social Science:").grid(row=5, column=0)
social_count_A_entry = tk.Entry(root)
social_count_A_entry.grid(row=5, column=1)
social_teacher_A_entry = tk.Entry(root)
social_teacher_A_entry.grid(row=5, column=2)
social_count_B_entry = tk.Entry(root)
social_count_B_entry.grid(row=5, column=3)
social_teacher_B_entry = tk.Entry(root)
social_teacher_B_entry.grid(row=5, column=4)

tk.Label(root, text="Physics:").grid(row=6, column=0)
physics_count_A_entry = tk.Entry(root)
physics_count_A_entry.grid(row=6, column=1)
physics_teacher_A_entry = tk.Entry(root)
physics_teacher_A_entry.grid(row=6, column=2)
physics_count_B_entry = tk.Entry(root)
physics_count_B_entry.grid(row=6, column=3)
physics_teacher_B_entry = tk.Entry(root)
physics_teacher_B_entry.grid(row=6, column=4)

tk.Label(root, text="Chemistry:").grid(row=7, column=0)
chemistry_count_A_entry = tk.Entry(root)
chemistry_count_A_entry.grid(row=7, column=1)
chemistry_teacher_A_entry = tk.Entry(root)
chemistry_teacher_A_entry.grid(row=7, column=2)
chemistry_count_B_entry = tk.Entry(root)
chemistry_count_B_entry.grid(row=7, column=3)
chemistry_teacher_B_entry = tk.Entry(root)
chemistry_teacher_B_entry.grid(row=7, column=4)

tk.Label(root, text="Biology:").grid(row=8, column=0)
biology_count_A_entry = tk.Entry(root)
biology_count_A_entry.grid(row=8, column=1)
biology_teacher_A_entry = tk.Entry(root)
biology_teacher_A_entry.grid(row=8, column=2)
biology_count_B_entry = tk.Entry(root)
biology_count_B_entry.grid(row=8, column=3)
biology_teacher_B_entry = tk.Entry(root)
biology_teacher_B_entry.grid(row=8, column=4)

tk.Label(root, text="Physical Education:").grid(row=9, column=0)
pe_count_A_entry = tk.Entry(root)
pe_count_A_entry.grid(row=9, column=1)
pe_teacher_A_entry = tk.Entry(root)
pe_teacher_A_entry.grid(row=9, column=2)
pe_count_B_entry = tk.Entry(root)
pe_count_B_entry.grid(row=9, column=3)
pe_teacher_B_entry = tk.Entry(root)
pe_teacher_B_entry.grid(row=9, column=4)

tk.Label(root, text="Library:").grid(row=10, column=0)
library_count_A_entry = tk.Entry(root)
library_count_A_entry.grid(row=10, column=1)
library_teacher_A_entry = tk.Entry(root)
library_teacher_A_entry.grid(row=10, column=2)
library_count_B_entry = tk.Entry(root)
library_count_B_entry.grid(row=10, column=3)
library_teacher_B_entry = tk.Entry(root)
library_teacher_B_entry.grid(row=10, column=4)

tk.Label(root, text="Art:").grid(row=11, column=0)
art_count_A_entry = tk.Entry(root)
art_count_A_entry.grid(row=11, column=1)
art_teacher_A_entry = tk.Entry(root)
art_teacher_A_entry.grid(row=11, column=2)
art_count_B_entry = tk.Entry(root)
art_count_B_entry.grid(row=11, column=3)
art_teacher_B_entry = tk.Entry(root)
art_teacher_B_entry.grid(row=11, column=4)

tk.Label(root, text="AI:").grid(row=12, column=0)
ai_count_A_entry = tk.Entry(root)
ai_count_A_entry.grid(row=12, column=1)
ai_teacher_A_entry = tk.Entry(root)
ai_teacher_A_entry.grid(row=12, column=2)
ai_count_B_entry = tk.Entry(root)
ai_count_B_entry.grid(row=12, column=3)
ai_teacher_B_entry = tk.Entry(root)
ai_teacher_B_entry.grid(row=12, column=4)

# Button to generate the timetable
generate_button = tk.Button(root, text="Generate Timetable", command=generate)
generate_button.grid(row=13, column=0, columnspan=5)

# Frame to display the generated timetable
table_frame = tk.Frame(root)
table_frame.grid(row=14, column=0, columnspan=5, pady=20)

root.mainloop()

