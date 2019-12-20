from random import randint

def get_names ():
    with open("names.txt", "r") as names_file:
        names = names_file.readlines()

    names = [name.rstrip() for name in names]
    return names


def get_lucky ():
    names = get_names()
    lucky_number = randint(0,len(names)-1)
    print("Congrats", names[lucky_number]+"!")

    
def get_questions ():
    with open("questions.txt", "r") as questions_file:
        questions = questions_file.readlines()
    questions = [question.rstrip() for question in questions]
    bank = {}
    for question in questions:
        idx = question.find("/")
        category = question[:idx]
        try:
            bank[category].append(question[idx+1:])
        except KeyError:
            bank[category] = [question[idx+1:]]

    return bank


def ask_questions ():
    bank = get_questions()
    categories = [category for category in bank.keys()]
    number_of_questions = 0
    for category in categories:
        number_of_questions += len(bank[category])
        
    with open ("asked_questions.txt", "r") as asked_questions_file:
        asked_questions = asked_questions_file.readlines()
        
    asked_questions = [aq.rstrip() for aq in asked_questions]
    counter = 0
    while True:
        category = randint(0, len(categories)-1)
        category = categories[category]
        question = randint(0, len(bank[category])-1)
        
        given = bank[category][question]
        counter += 1
        if given not in asked_questions:
            with open ("asked_questions.txt", "a") as asked_questions_file:
                asked_questions_file.write(given)
                asked_questions_file.write("\n")
            print(given)
            print("-"*50)
            break
        if counter > number_of_questions:
            print("No more questions!")
            print("-"*50)
            return False
        

while True:
    print("Let's choose a lucky person!")
    print("-"*50)
    get_lucky()
    print("Let's give you a question: ", end="")
    result = ask_questions()
    if not result:
        break
    cmd = input("Next lucky person [Y/N] \t")
    if cmd.upper() != "Y":
        break
        
