class Material:
    def __init__(self, number, duration):
        self.number = number
        self.duration = duration
        self.tasks = []

    def __repr__(self):
        return f'Material({self.number}, {self.duration})'

    def add_task(self, task):
        self.tasks.append(task)


class Task:
    def __init__(self, number, material, quantity, due_date):
        self.number = number
        self.material = material
        self.quantity = quantity
        self.due_date = due_date

        self.predecessors = []
        self.successors = []
        self.early_start = None
        self.early_finish = None
        self.late_start = None
        self.late_finish = None

        material.add_task(self)

    def __repr__(self):
        return f'Task({self.number}, {self.material}, {self.quantity}, {self.due_date})'

    def set_early(self):
        self.early_start = 0
        for pred in self.predecessors:
            if pred.early_finish > self.early_start:
                self.early_start = pred.early_finish

        self.early_finish = self.early_start + (self.quantity * self.material.duration)

    def set_late(self):
        if len(self.successors) == 0:
            if len(self.predecessors) == 0:
                self.late_finish = self.quantity * self.material.duration
            else:
                self.late_finish = max(task.early_finish for task in self.predecessors) + self.quantity * self.material.duration
        else:
            lf = None
            for succ in self.successors:
                if lf is None or succ.late_start > lf:
                    self.late_finish = succ.late_start

        self.late_start = self.late_finish - (self.quantity * self.material.duration)

    def set_predecessors(self):
        sorted_tasks = sorted(self.material.tasks, key=lambda x: x.due_date)
        self.predecessors = [task for task in sorted_tasks if task.due_date < self.due_date]
        self.set_early()

    def set_successors(self):
        sorted_tasks = sorted(self.material.tasks, key=lambda x: x.due_date, reverse=True)
        self.successors = [task for task in sorted_tasks if task.due_date > self.due_date]
        self.set_late()
