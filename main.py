import json
import os.path
from datetime import datetime


def save_in_json(notebook):
    with open("notebook.json", "w") as file:
        json.dump(notebook, file)


def load_from_json():
    if os.path.exists("notebook.json"):
        with open("notebook.json", "r") as file:
            note = json.load(file)
            return note
    else:
        return []


def create_note():
    notebook = load_from_json()
    new_note = {}
    new_note["id"] = len(notebook) + 1
    new_note["title"] = input("Title: ")
    new_note["msg"] = input("Message: ")
    new_note["date"] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    notebook.append(new_note)
    save_in_json(notebook)
    print("Note created successfully.")


def delete_note(id):
    notebook = load_from_json()
    for note in notebook:
        if note["id"] == id:
            notebook.remove(note)
            save_in_json(notebook)
            print("Note deleted successfully.")
            return
    print("Invalid note id.")


def change_note(id):
    notebook = load_from_json()
    for note in notebook:
        if note["id"] == id:
            note["title"] = input("Enter new title: ")
            note["msg"] = input("Enter new message: ")
            note["date"] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            save_in_json(notebook)
            print("Note changed successfully.")
            return
    print("Invalid note id.")


def show_notebook():
    notebook = load_from_json()
    for note in notebook:
        print(f"{note['id']}. {note['title']}: {note['msg']} ---> {note['date']}")


while True:
    print("\nOptions:")
    print("1. Create new note")
    print("2. Change note")
    print("3. Delete note")
    print("4. Show all notes")
    print("5. Exit\n")

    prompt = input("Choose option: \n")

    match prompt:
        case "1":
            create_note()
        case "2":
            try:
                id = int(input("Enter note id: "))
            except ValueError:
                print("Please, enter number, not a sign!")
            else:
                change_note(id)
        case "3":
            try:
                id = int(input("Enter note id: "))
            except ValueError:
                print("Please, enter number, not a sign!")
            else:
                delete_note(id)
        case "4":
            show_notebook()
        case "5":
            break
        case _:
            print("Invalid option, try again.")
