

import pandas as pd

from task import Material, Task

if __name__ == "__main__":
    mdf = pd.read_csv('material.csv', delimiter=";")
    jdf = pd.read_csv('jobs.csv', delimiter=';')

    materials = {}
    tasks = {}

    for _, job_number, material_number, qty, dd in jdf.itertuples():
        material = materials.get(material_number)
        if material is None:
            dur = int(mdf[mdf['Material'] == material_number]['Duration'])
            material = Material(material_number, dur)
            materials[material_number] = material

        task = Task(job_number, material, qty, dd)

        tasks[job_number] = task

    for task in sorted(tasks.values(), key=lambda x: x.due_date):
        task.set_predecessors()

    for task in sorted(tasks.values(), key=lambda x: x.due_date, reverse=True):
        task.set_successors()

    print(task for task in tasks)
