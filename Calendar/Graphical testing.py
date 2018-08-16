# Example: File: pack-entry-form-1.py

from tkinter import *
import CalendarUploader

root = Tk()


def update_reminder():
    storage = open("reminders.txt", "r")
    reminder_listbox.delete(0, END)
    for line in storage:
        reminder_listbox.insert(END, line)
    storage.close()


def remind(entry_box):
    storage = open("reminders.txt", "a")
    reminder = entry_box.get()
    # print (reminder)
    if reminder != '':
        reminder_listbox.insert(END, reminder)
        entry_box.delete(0, END)
        storage.write(reminder+'\n')
    storage.close()


def remove(self):
    if reminder_listbox.curselection() != ():

        storage = open("reminders.txt", "r")

        content = storage.readlines()  # reads line by line and out puts a list of each line

        content.remove(content[reminder_listbox.curselection()[0]])

        storage = open('reminders.txt', 'w')
        storage.writelines(content)

        reminder_listbox.delete(reminder_listbox.curselection())
        clear_selection(self)

        storage.close()


def clear_selection(self):
    reminder_listbox.selection_clear(0, END)


def update_clock(master):
    # print "Update!"
    # print now
    event_listbox.delete(0, END)
    events = CalendarUploader.get_events()
    for x, event in enumerate(events):
        event = event[5:]
        event = event.replace('T', ' ')
        event = event.replace('-', '/', 1)
        event = event.replace(':00', '', 1)
        time = event[:17]
        time = time[:-6]
        event = "---" + event[17:]
        event_listbox.insert(END, time)
        event_listbox.insert(END, event)
    master.after(60000, update_clock, master)


# ------------------ Add a Tag and Text Field ------------------------------------
def add_entry(master, text, **options):

    frame = Frame(master, bg='grey8')

    if options.__contains__('width'):
        entry = Entry(frame, width=options.get("width"), bg='grey8', fg='white', highlightthickness=1)
        entry.bind('<Return>', (lambda event: remind(entry)))
    else:
        entry = Entry(frame, bg='grey8', fg='white', highlightthickness=1)

    entry.pack(side=RIGHT)

    label = Label(frame, text=text, bg='grey8', fg='white')
    label.pack(side=RIGHT)

    frame.pack(fill=X)


# ----------------- Start Of Button Frame ----------------------------------------
button_frame = Frame(root, bg='grey8')
entry_label = Label(button_frame, text="New Event!", font=("Helvetica", 25), bg='grey8', fg='white')
entry_label.pack()
add_entry(button_frame, "Summary")
add_entry(button_frame, "Location")
add_entry(button_frame, "Date")
add_entry(button_frame, "Duration")
button_frame.pack(side=LEFT, fill=Y)

# ----------------- Start Of Events Frame ----------------------------------------
events_frame = Frame(root, bg='grey8')
event_list = ["thing #1", "thing #2", "thing #3", "thing #5"]

scrollbar = Scrollbar(events_frame, width=2)
scrollbar.pack(side=RIGHT, fill=Y)

event_listbox = Listbox(events_frame, bg='grey8', fg='white')
event_listbox.pack()


for thing in event_list:
    event_listbox.insert(END, thing)

event_listbox.config(yscrollcommand=scrollbar.set, height=12)
scrollbar.config(command=event_listbox.yview)

events_frame.pack(side=LEFT, fill=Y)

# ----------------- Start of Reminder Frame --------------------------------------
reminder_frame = Frame(root, bg='grey8')
reminder_list = ["remember #1", "remember #2", "remember #3", "remember #5"]

# ----------------- Start of Reminder List Frame ---------------------------------
reminder_list_frame = Frame(reminder_frame, bg='grey8')

scrollbar = Scrollbar(reminder_list_frame, width=2)
scrollbar.pack(side=RIGHT, fill=Y)

reminder_listbox = Listbox(reminder_list_frame, width=35, bg='grey8', fg='white')
reminder_listbox.pack()
reminder_listbox.bind('<Return>', remove)
reminder_listbox.bind('<Escape>', clear_selection)

for thing in reminder_list:
    reminder_listbox.insert(END, thing)

reminder_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=reminder_listbox.yview)

# ----------------- Start of Add Reminder Frame ----------------------------------
add_reminder_frame = Frame(reminder_frame, bg='grey8')

add_entry(add_reminder_frame, "Reminder", width=13)


# ----------------- Main Reminder Frame ------------------------------------------
reminder_list_frame.pack(side=BOTTOM)
add_reminder_frame.pack(side=BOTTOM)
reminder_frame.pack(side=LEFT, fill=Y)

# storage = open("reminders.txt", "r+")
update_reminder()
update_clock(reminder_frame)
mainloop()
