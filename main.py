from Task import Task


tasks_dict = {"high":[],
              "low":[]}

def read_tasks():
    lines = []
    with open("tasks_list.txt", "r+") as f:
        lines = f.readlines()

    in_main_task = False
    in_sub_task = False

    for line in lines:
        if line == "Main Tasks":
            in_main_task = True
            in_sub_task = False
        elif line.strip() == "":
            continue
        elif line == "Sub Tasks":
            in_sub_task = True
            in_main_task = False

        if in_main_task:
            tasks_dict["high"].append(line)
        elif in_sub_task:
            tasks_dict["low"].append(line)


def get_dict(priority):
    return "high" if priority == 1 else "low"


def add_task(name, priority):
    t = Task(name, priority)
    tasks_dict[get_dict(priority)].append(t)


def remove_task(name, priority):
    t = Task(name, priority)
    dict_choice = get_dict(priority)
    for task in tasks_dict[dict_choice]:
        if task.name == t.name:
            tasks_dict[dict_choice].remove(task)

def print_tasks():
    for p, t in tasks_dict.items():
        for n in t:
            print(p, (n.name, n.priority))

def save_tasks():
    with open("tasks_list.txt", "w+") as f:
        f.write("Main Tasks\n")
        for task in tasks_dict["high"]:
            f.write(task.name)
            f.write('\n')
        f.write("\nSub Tasks\n")
        for task in tasks_dict["low"]:
            f.write(task.name)
            f.write('\n')


def main():
    pass


if __name__ == "__main__":
    add_task("Homework", 1)
    add_task("Minecraft", 2)
    add_task("Library", 1)
    add_task("Work", 1)
    add_task("Basketball", 2)
    add_task("Soccer", 2)
    remove_task("Minecraft", 2)
    print_tasks()
    print('------------------------')
    save_tasks()
    read_tasks()
    add_task("Cricket",2 )
    print_tasks()
