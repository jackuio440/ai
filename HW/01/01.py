from random import random, randint, choice
from solution import Solution
import numpy as np
import random

courses = [
{'teacher': '甲', 'name':'機率', 'hours': 2},
{'teacher': '甲', 'name':'線代', 'hours': 3},
{'teacher': '甲', 'name':'離散', 'hours': 3},
{'teacher': '乙', 'name':'視窗', 'hours': 3},
{'teacher': '乙', 'name':'科學', 'hours': 3},
{'teacher': '乙', 'name':'系統', 'hours': 3},
{'teacher': '乙', 'name':'計概', 'hours': 3},
{'teacher': '丙', 'name':'軟工', 'hours': 3},
{'teacher': '丙', 'name':'行動', 'hours': 3},
{'teacher': '丙', 'name':'網路', 'hours': 3},
{'teacher': '丁', 'name':'媒體', 'hours': 3},
{'teacher': '丁', 'name':'工數', 'hours': 3},
{'teacher': '丁', 'name':'動畫', 'hours': 3},
{'teacher': '丁', 'name':'電子', 'hours': 4},
{'teacher': '丁', 'name':'嵌入', 'hours': 3},
{'teacher': '戊', 'name':'網站', 'hours': 3},
{'teacher': '戊', 'name':'網頁', 'hours': 3},
{'teacher': '戊', 'name':'演算', 'hours': 3},
{'teacher': '戊', 'name':'結構', 'hours': 3},
{'teacher': '戊', 'name':'智慧', 'hours': 3}
]

teachers = ['甲', '乙', '丙', '丁', '戊']

rooms = ['A', 'B']

slots = [
'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37',
'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47',
'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57',
'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27',
'B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37',
'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47',
'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57',
]

slots2 = [
'A11', 'A12', 
'A21', 'A22', 
'A31', 'A32', 
'A41', 'A42', 
'A51', 'A52', 
'B11', 'B12', 
'B21', 'B22', 
'B31', 'B32', 
'B41', 'B42',
'B51', 'B52',
]
T2=[
    3,4,3,5,5
]

def schedule_courses(courses, slots):
    random.shuffle(courses)
    schedule = {time: None for time in slots}
    slots_with_one = [time for time in slots if time[-1] == '1']

    for course in courses:
        teacher = course['teacher']
        name = course['name']
        if course['hours'] == 4:
            random.shuffle(slots_with_one)  
            for time in slots_with_one:
                if schedule[time] is None:
                    schedule[time] = {'teacher': teacher, 'course': name}
                    break
            else:
                print(f"Cannot schedule {name} with teacher {teacher} in any slot with '1'.")

        else:
            random.shuffle(slots)  
            for time in slots:
                if schedule[time] is None:
                    schedule[time] = {'teacher': teacher, 'course': name}
                    break
            else:
                print(f"Cannot schedule {name} with teacher {teacher} in any slot.")

    return schedule

schedule = schedule_courses(courses, slots2)

for time, info in schedule.items():
    print(f"{time}: {info['course']} with {info['teacher'] if info else 'No class'}")

