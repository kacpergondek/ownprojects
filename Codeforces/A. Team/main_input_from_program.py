while True:
    tasks = input('How many tasks are to be completed?')
    try:
        tasks = int(tasks)
        break
    except ValueError:
        print ("Please enter a number")

tasks_to_complete = 0
while tasks >= 1:
    decision = str(input('Enter the decisions. 1 for agree, 0 for disagree, for example: 101'))
    tasks -= 1
    x = sum([int(d) for d in str(decision)])
    if x == 2 or x == 3:
        tasks_to_complete += 1

new_file = open('answer',"x")
new_file.write(f"Overall, there will be {tasks_to_complete} tasks to do")
