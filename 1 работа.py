class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def __str__(self):
        return f"[{'X' if self.completed else ' '}] {self.title}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f'Задача "{title}" добавлена.')

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Задача "{removed_task.title}" удалена.')
        else:
            print("Некорректный индекс.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f'Задача "{self.tasks[index].title}" выполнена.')
        else:
            print("Некорректный индекс.")

    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index}: {task}")


def main():
    todo_list = TodoList()

    while True:
        print("\nДобро пожаловать в To-Do List!")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Завершить задачу")
        print("4. Показать задачи")
        print("5. Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            title = input("Введите название задачи: ")
            todo_list.add_task(title)

        elif choice == '2':
            todo_list.show_tasks()
            index = int(input("Введите индекс задачи для удаления: "))
            todo_list.remove_task(index)

        elif choice == '3':
            todo_list.show_tasks()
            index = int(input("Введите индекс задачи для завершения: "))
            todo_list.complete_task(index)

        elif choice == '4':
            todo_list.show_tasks()

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()