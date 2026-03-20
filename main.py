import json

class ToDo:
    def __init__(self, title):
        self.title = title
        self._done = False

    def done(self):
        self._done = True

    def is_done(self):
        return self._done

    def to_dict(self):
        return {"title":self.title,
                "done":self._done
                }

def save_file(tasks):
    with open("tasks.json", "w") as f:
        json.dump([task.to_dict() for task in tasks], f)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)  # json.load() сам прочитає файл
            tasks = []
            for item in data:
                task = ToDo(item["title"])
                if item["done"]:
                    task.done()
                tasks.append(task)
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def main():

    tasks = load_tasks()
    active = True

    while active:
        print("\n--------------------")
        print("1-Check your tasks")
        print("2-Add task")
        print("3-Delete task")
        print("4-Mark task as done")
        print("5-Exit")
        print("--------------------")

        user_input = input("Write your choice: ")

        if user_input == "1":
            if not tasks:
                print("Your list is empty")
            else:
                for task in tasks:
                    if task.is_done():
                        print(task.title, "✅")
                    else:
                        print(task.title, "❎")

        elif user_input == "2":
            inp = input("Enter your task to be added: ")
            task = ToDo(inp)
            tasks.append(task)
            save_file(tasks)

        elif user_input == "3":
            inp = input("Enter task to be deleted: ")
            for task in tasks:
                if task.title == inp:
                    tasks.remove(task)
                    save_file(tasks)

        elif user_input == "4":
            inp = input("Enter task to be marked as done: ")
            for task in tasks:
                if task.title == inp:
                    task.done()
                    save_file(tasks)

        elif user_input == "5":
            active = False


    print("Goodbye")


if __name__ == "__main__":
    main()