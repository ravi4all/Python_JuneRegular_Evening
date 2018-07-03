import random

file = open('questions.txt')
questions = file.readlines()

options = [
    ['pass', 'skip', 'break', 'continue'],
    ['C', 'C++', 'B', 'ABC'],
    ['pandas', 'pygame', 'numpy', 'none'],
    ['random', 'rand', 'randomize', 'randomNumber'],
    ['r+', 'rb', 'wb', 'rw']
]
answers = ['continue', 'ABC', 'pygame', 'random', 'rw']
counter = 0

for i in range(len(questions)):
    index = random.randrange(len(questions))
    print(questions[index])
    opt_index = index
    opt = options[opt_index]
    print("1", opt[0], "2", opt[1])
    print("3", opt[2], "4", opt[3])
    user_input = int(input("Enter your choice : [1/2/3/4] : "))
    if opt[user_input - 1] == answers[opt_index]:
        counter += 1
    del questions[index]
    del options[opt_index]

print("Final Score is",counter)