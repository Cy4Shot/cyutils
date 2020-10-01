from cyutils.io import colored_text as ct

class CustomError:

    def __init__(self, title, exitOnError=True):
        self.title = title
        self.exitOnError = exitOnError
    
    def __str__(self):
        return self.title
    
    def throw(self, message):
        ct.clrprint(self.title + ": " + message, "red")
        if self.exitOnError:
            exit()

def throw(error, message):
    error.throw(message)
