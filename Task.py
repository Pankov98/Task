class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # False означает, что задача не выполнена

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        status_str = 'Выполнено' if self.status else 'Не выполнено'
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status_str}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Задача '{description}' добавлена  '{deadline}'.")

    def mark_task_as_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_done()


    def get_unfinished_tasks(self):
        return [task for task in self.tasks if not task.status]

    def __str__(self):
        return '\n'.join(str(task) for task in self.tasks)


# Пример использования
if __name__ == "__main__":
    task_manager = TaskManager()

    # Добавление задач с использованием функции add_task
    task_manager.add_task("Сходить на тренировку", "понедельник")
    task_manager.add_task("Помыть машину", "вторник")
    task_manager.add_task("Встретиться с друзьями", "пятница")

    # Отметим одну задачу как выполненную
    task_manager.mark_task_as_done(1)

    print("\nВсе задачи:")
    print(task_manager)

    print("\nТекущие задачи (не выполненные):")
    unfinished_tasks = task_manager.get_unfinished_tasks()
    for task in unfinished_tasks:
        print(task)