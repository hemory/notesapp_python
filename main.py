from Note import Note
import NotesAction
import csv

# MAIN
def getNotes():
    notes = []
    with open('notes.csv',) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        n = Note("", "")
        for row in csv_reader:
            n.title = row[0]
            n.message = row[1]
            notes.append(n)
    return notes

userChoice = ""

while userChoice != "q":
    print("Enter [q] at anytime to quit")
    userChoice = input("(1)Add Note (2)Edit Note (3)Delete Note (4)View Notes: ".lower())

    if userChoice == "1":
        note = Note("", "")
        note.title = input("Enter Title: ")
        note.message = input("Enter Message: ")
        notes = getNotes()
        notes.append(note)

        with open('notes.csv', 'w',) as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')

            for line in notes:
                spamwriter.writerow([line.title,line.message])

    elif userChoice == "2":
        messageTitle = input("Enter Title of Message to Edit: ")
        newMessage = input("Enter New Message: ")

        isSuccessful = NotesAction.editNote(notes, messageTitle, newMessage)

        if isSuccessful:
            print("Message has been updated")
        else:
            print("Unsuccessful, please try again")

    elif userChoice == "3":
        noteToRemove = input("Enter Title of Note to Remove:")

        isSuccessful = NotesAction.removeNote(notes, noteToRemove)

        if isSuccessful:
            print("Message has been removed.")
        else:
            print("Unsuccessful, please try again.")

    elif userChoice == "4":

        f = open('path/to/csv_file', encoding='UTF8')

        csv_reader = open("notes.csv", encoding='UTF8')

        for line in csv_reader:
            print(f"Title: {line[0]}, Message: {line[1]}")
        f.close()

    elif userChoice == "q":
        print("Goodbye")
    else:
        print("Please make a valid selection")
