import json
import pyperclip as clip
from datetime import datetime


def get_tasks(path: str):
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def save_tasks(path, data):
    with open(path, 'w') as f:
        json_object = json.dumps(data, indent=4)
        f.write(json_object)


def translate_day(day: str):
    days_week = {
        "Monday": "Segunda",
        "Tuesday": "Terça",
        "Wednesday": "Quarta",
        "Thursday": "Quinta",
        "Friday": "Sexta",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }

    if not day in days_week.keys():
        return day 

    return days_week[day]


def find_by_date(tasks, date):
    filtered = [] # filtered lmao
    for task in tasks:
        if task["date"] == date:
            filtered.append(task)

    return filtered


tasks = get_tasks('tasks.json')
today = datetime(2018, 6, 1)

# Working with dates here, nothing to see
x = datetime.strptime(tasks["tasks"][0]["date"], '%Y-%m-%d')
print(x.strftime("%d/%m/%Y"))  # 30/12/2022
print(x.strftime("%A"))  # Friday
print("Sexta" if x.strftime("%A") == "Friday" else "Seggs")

message = "_*Tarefas dessa Semana!*_"
for task in tasks["tasks"]:
    message += "\n*Data*: " + task["date"]
    message += "\n*Matéria*: " + task["subject"]
    message += "\n*Descrição*: " + task["description"]


clip.copy(message)
print("Copied to clipboard!")
