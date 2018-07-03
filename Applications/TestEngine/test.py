questions = [
    "Ques.1 Which keyword is used to skip current iteration ?",
    "Ques.2 Python is successor of which language ?",
    "Ques.3 Which module is used for game development ?",
    "Ques.4 Which module is used get random numbers ?",
    "Ques.5 Which file mode is wrong ?"
]

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
    print(questions[i])
    print("1. {}           2. {}".format(options[i][0], options[i][1]))
    print("3. {}           4. {}".format(options[i][2], options[i][3]))
    user_ans = int(input(">> : "))
    if options[i][user_ans-1] == answers[i]:
        counter += 1
print("Final Score is",counter)