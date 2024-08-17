import random

def hill_climbing(schedule):
    while True:
        neighbors = get_neighbors(schedule)
        if not neighbors:
            break         
        next_schedule = min(neighbors, key=conflict)
        if conflict(next_schedule) >= conflict(schedule):
            break
        schedule = next_schedule
    return schedule

def generate_random_schedule(classes):
    for class_name in classes:
        random.shuffle(classes[class_name])
    return classes

def get_random_neighbors(neighbors:list, schedule: dict) ->list:
    
    class_names = list(schedule.keys())
    random_time = random.randint(0, 1)
    for i in range(random_time):
        
        class_name1, class_name2 = random.sample(class_names, 2)
        
        class_list1, class_list2 = schedule[class_name1], schedule[class_name2]

        random_cls_one = random.randint(0, len(class_list1)-1)
        random_cls_two = random.randint(0, len(class_list2)-1)
        
        
        schedule_new = {k: v[:] for k, v in schedule.items()}
        schedule_new[class_name1][random_cls_one], schedule_new[class_name2][random_cls_two] = schedule_new[class_name2][random_cls_two], schedule_new[class_name1][random_cls_one]
        neighbors.append(schedule_new)
            
    return neighbors
            
def get_neighbors(schedule:dict):
    neighbors = []
    
    for class_name, class_list in schedule.items():
        
        for i in range(len(class_list)):
        
            for j in range(i+1, len(class_list)):
            
                schedule_new = {k: v[:] for k, v in schedule.items()}
                schedule_new[class_name][i], schedule_new[class_name][j] = schedule_new[class_name][j], schedule_new[class_name][i]
                neighbors.append(schedule_new)
    get_random_neighbors(neighbors, schedule_new)
   
    return neighbors

def conflict(schedule:dict):
    
    total_conflicts = 0
    for class_name, class_list in schedule.items():
        for i in range(len(class_list)):
            for j in range(i+1, len(class_list)):
                if schedule[class_name][i]['Time'] == schedule[class_name][j]['Time']: 
                    total_conflicts += 1
        
                if set(schedule[class_name][i]['Students']) & set(schedule[class_name][j]['Students']):
                    total_conflicts += 1
                
                if set(schedule[class_name][i]['Master']) & set(schedule[class_name][j]['Master']):
                    total_conflicts += 1
                        
    return total_conflicts

def random_restart_hill_climbing(schedule, restarts=100):
    best_schedule = hill_climbing(schedule)
    num_iteration = 0
    for _ in range(restarts):
        
        new_schedule = generate_random_schedule(best_schedule)
        solution = hill_climbing(new_schedule)
        if conflict(solution) < conflict(best_schedule):
            best_schedule = solution
        num_iteration += 1
    return best_schedule, num_iteration

def run(schedule):
    print(random_restart_hill_climbing(schedule))

# class_uni = {"class1": 
#     [
#         {"Master": "Ali",'Time': '10:00', 'Students': ['Meow', 'Losi']},
#         {"Master": "JAfAR",'Time': '10:00', 'Students': ['H', 'FIFI']}
#     ],
#     'RTI': 
#         [
#         {'Master': 'REZA', 'Time': '8:00', 'Students': ['H', "V"]}
#         ]
# }
    
if __name__ == "__main__":
    class_uni = {}
    num_class = int(input("Enter the number of Classess: "))
   
    for i in range(num_class):
        
        class_schedule = []
        class_info = {}
        class_name = input("Enter your class name: ")
        num_a_class = int(input(f"Enter the number of classes in {class_name}:"))
        
        for j in range(num_a_class):
            
            master_name = input("Enter the master name: ")
            time = input("Enter the time: ")
            class_info["Master"] = master_name
            class_info["Time"] = time
        
            num_students = int(input("Number of Student: "))
            stu = []
            
            for k in range(num_students):
                student_name = input("Enter the student name: ")
            
            class_info["Students"] = student_name
            class_schedule.append(class_info)
        
        class_uni[class_name] = class_schedule
            
    run(class_uni)