import os

module = "PlanningTool"


def fix_path(module_name):
    cwd = os.getcwd().split(os.sep)

    path = []

    for p in cwd:
        path.append(p)
        if p == module_name:
            break

    path = os.path.join(path)

    os.chdir(path)
