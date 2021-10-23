# METHODS

def editNote(notes, title, newMessage):
    noteToUpdate = getNoteByTitle(notes, title)

    if noteToUpdate != "":
        noteToUpdate.message = newMessage
        return True
    return False

def removeNote(notes, title):
    noteToRemove = getNoteByTitle(notes, title)

    if noteToRemove != "":
        notes.remove(noteToRemove)
        return True
    return False

def getNoteByTitle(notes, title):
    for note in notes:
        if note.title.lower() == title.lower():
            return note
    return ""