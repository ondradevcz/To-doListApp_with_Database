from tinydb import TinyDB, Query

db = TinyDB('db4.json')
Database = Query()

def start_conversation():
    while True:
        command = input("What do you wish to do?\nYou can delete or make a new note, to end just type 'end'\nType here: ")

        # COMMANDS
        t_delete = ("delete", "Delete", "erase")
        t_new_note = ("new note", "newnote", "new", "New", "New note", "New Note", "Newnote")
        t_end = ("end", "End", "Ending", "ending", "Stop", "stop")

        if any(action in command for action in t_new_note):
            title = input("Enter the title of the note: ")
            content = input("Enter the content of the note: ")
            db.insert({"title": title, "content": content})
            print("Note created!")
        elif any(action in command for action in t_delete):
            all_notes = db.search(Database.title.exists())
            if all_notes:
                print(all_notes)
                title = input("Enter the title of the note you want to delete: ")
                db.remove(Database.title == title)
                print("Deleted")
            else:
                print("No notes to delete.")
        elif any(action in command for action in t_end):
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

# Start the conversation
start_conversation()
