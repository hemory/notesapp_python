from Note import Note
import NotesAction


# MAIN
notes = [Note("Greet", "Hello"), Note("Depart", "Bye")]
userChoice = ""

while userChoice != "q":
    print("Enter [q] at anytime to quit")
    userChoice = input("(1)Add Note (2)Edit Note (3)Delete Note (4)View Notes: ".lower())

    if userChoice == "1":
        note = Note("", "")
        note.title = input("Enter Title: ")
        note.message = input("Enter Message: ")

        notes.append(note)

    elif userChoice == "2":
        messageTitle = input("Enter Title of Message to Edit: ")
        newMessage = input("Enter New Message: ")

        isSuccessful = editNote(notes, messageTitle, newMessage)

        if isSuccessful:
            print("Message has been updated")
        else:
            print("Unsuccessful, please try again")

    elif userChoice == "3":
        noteToRemove = input("Enter Title of Note to Remove:")

        isSuccessful = removeNote(notes, noteToRemove)

        if isSuccessful:
            print("Message has been removed.")
        else:
            print("Unsuccessful, please try again.")

    elif userChoice == "4":
        for note in notes:
            print(note.toString())
    elif userChoice == "q":
        print("Goodbye")
    else:
        print("Please make a valid selection")












