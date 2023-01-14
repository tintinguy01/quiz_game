def new_game():

    guesses = []
    correct_answer = 0
    question_num = 1

    for qes in questions:
        print('----------------------------------------------------------')
        print(qes)
        for choices in options[question_num-1]:
            print(choices)

        guess = input('What is your answer? (A, B, C, or D): ').upper()
        guesses.append(guess)

        correct_answer += check_answer(questions.get(qes), guess)
        question_num += 1

    display_score(correct_answer, guesses)
    play_again()

# -------------------------------------------------------------------------------------------------------------------------------------------------------


def check_answer(answer, guess):

    if answer == guess:
        print('Correct!!')
        return 1
    else:
        print('Wrong!!')
        return 0


def display_score(correct_answer, guesses):
    print('----------------------------------------------------------')

    print('Correct Answer for all question: ', end='')
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print('Your Answer for all question: ', end='')
    for i in guesses:
        print(i, end=" ")
    print()

    print('----------------------------------------------------------')

    print("Your score is " + str(correct_answer) +
          " out of " + str(len(questions)) + '.')
    print('Which is ' + str(round(correct_answer / (len(questions)) * 100)) + "%")

    print('----------------------------------------------------------')


def play_again():
    while True:
        again = input('Do you want to play again? (YES, NO): ').lower()
        if again == 'yes':
            new_game()
        elif again == 'no':
            quit('Thanks for playing')
        else:
            continue


questions = {
    'Who created Python?: ': 'A',
    'What year was Python created?: ': 'B',
    'Python is tributed to which comedy group?: ': 'C',
    'Is the Earth round?: ': 'A'
}

options = [
    ['A. Guido van Rossum', 'B. Elon Musk', 'C. Bill Gates', 'D. Mark Zuckerburg'],
    ['A. 1989', 'B. 1991', 'C. 2000', 'D. 2016'],
    ['A. Lonely Island', 'B. Smosh', 'C. Monty Python', 'D. SNL'],
    ['A. True', 'B. False', 'C. sometimes', "What's Earth?"]
]

new_game()
