import csv

class Note:
    def __init__(self, title, message):
        self.title = title
        self.message = message

def get_notes():
    notes = []
    with open('notes.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            n = Note(row[0], row[1])
            notes.append(n)
    return notes

def add_note():
    note = Note("", "")
    note.title = input("Enter Title: ")
    note.message = input("Enter Message: ")
    notes = get_notes()
    notes.append(note)

    with open('notes.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')

        for line in notes:
            csv_writer.writerow([line.title, line.message])
    print("Note added successfully.")

def edit_note():
    message_title = input("Enter Title of Message to Edit: ")
    new_message = input("Enter New Message: ")
    notes = get_notes()

    for note in notes:
        if note.title == message_title:
            note.message = new_message

    with open('notes.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')

        for line in notes:
            csv_writer.writerow([line.title, line.message])
    print("Note edited successfully.")

def remove_note():
    note_to_remove = input("Enter Title of Note to Remove: ")
    notes = get_notes()

    for note in notes:
        if note.title == note_to_remove:
            notes.remove(note)

    with open('notes.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')

        for line in notes:
            csv_writer.writerow([line.title, line.message])
    print("Note removed successfully.")

def view_notes():
    notes = get_notes()

    for note in notes:
        print(f"Title: {note.title}, Message: {note.message}")

    if not notes:
        print("No notes found.")

user_choice = ""
while user_choice != "q":
    print("Enter [q] at anytime to quit")
    user_choice = input("(1) Add Note (2) Edit Note (3) Delete Note (4) View Notes: ")

    if user_choice == "1":
        add_note()

    elif user_choice == "2":
        edit_note()

    elif user_choice == "3":
        remove_note()

    elif user_choice == "4":
        view_notes()

    elif user_choice == "q":
        print("Goodbye")

    else:
        print("Please make a valid selection")
