class Note:
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def toString(self):
        return f"Title: {self.title} Message: {self.message}"

