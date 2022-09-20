
class ManageFile:
    def __init__(self, filename):
        print("init")
        self.filename = filename

    def __enter__(self):
        print("enter")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("exception has been handled ")
        print("traceback:", exc_traceback)
        print("exc:", exc_type, exc_value)
        print("exit")


with ManageFile("notes.txt") as file:
    print("do some stuff...")
    file.write("some todo...")
    file.some_method()
print("continuing...")
