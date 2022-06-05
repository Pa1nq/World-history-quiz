import time

import psycopg2

conn = psycopg2.connect(dbname='quiz_game', user='postgres', password='txcplaya228nevPly)')

curs = conn.cursor()


def start():
    started_gaming = False
    print('Hello to the quiz game about World history!', end='\n')
    time.sleep(1)
    print('Today you are going to answer 25 interesting questions about world history. You need to choose one option '
          'from 4. How much of them can you ask?')
    time.sleep(2)
    while not started_gaming:
        command = input(
            'Okay, please, enter the command that you want to be shown:\n start_game for starting the game,\n help for '
            'more information about game:\n')
        if command == 'start_game':
            start_game()
            started_gaming = True
        elif command == 'help':
            help_gamer()
            started_gaming = True
        else:
            print('Unknown command.')


def help_gamer():
    print('Here\'s help for you: ', end='\n')
    print('In this quiz about world\'s history 20 questions and for each of them 4 options. You can take only\n one '
          'option and enter "next" to get to the next question. There\'s timer that shows in which time you need to '
          'answer the question. \nIf you answered correctly, you gain 1 point, '
          'if wrong - nothing. Please, don\'t cheat and play honestly. You can start the quiz again after it finishes')
    started = False
    while not started:
        command = input(
            'Hope, you understood the rules of game. please, enter the command start_game for starting the game: ')
        if command == 'start_game':
            start_game()
            started = True
        else:
            print('You wrote unknown command.')


def start_game():
    dot = 3
    points = 0
    t = 30
    question = 1
    is_again = False
    print('You started the game. Ready? We are starting in 3 secs')
    time.sleep(1)
    print('3', end='')
    while dot > 0:
        time.sleep(0.3)
        print('.', end='')
        dot -= 1
    dot = 3
    print('2', end='')
    while dot > 0:
        time.sleep(0.3)
        print('.', end='')
        dot -= 1
    dot = 3
    print('1', end='')
    while dot > 0:
        time.sleep(0.3)
        print('.', end='')
        dot -= 1
    print('Started!')
    curs.execute('SELECT COUNT(question) FROM quizgame')
    count = curs.fetchone()
    whole_questions = count[0]
    while whole_questions >= question:

        print(f'Question {question}: ', end='')

        curs.execute(f'SELECT question FROM quizgame WHERE question_id = {question}')
        ques = curs.fetchall()
        quest = ques[0][0]
        print(quest)

        curs.execute(f'SELECT first_answer FROM quizgame WHERE question_id = {question}')
        first_q = curs.fetchall()
        fst_q = first_q[0][0]
        print(f'1. {fst_q}', end='\n')
        curs.execute(f'SELECT second_answer FROM quizgame WHERE question_id = {question}')
        second_q = curs.fetchall()
        sec_q = second_q[0][0]
        print(f'2. {sec_q}', end='\n')
        curs.execute(f'SELECT third_answer FROM quizgame WHERE question_id = {question}')
        third_q = curs.fetchall()
        thrd_q = third_q[0][0]
        print(f'3. {thrd_q}', end='\n')
        curs.execute(f'SELECT fourth_answer FROM quizgame WHERE question_id = {question}')
        fourth_q = curs.fetchall()
        frth_q = fourth_q[0][0]
        print(f'4. {frth_q}', end='\n')
        # print('Timer (30 secs) started')
        answer = int(input('Your answer (1/2/3/4): '))

        curs.execute(f'SELECT right_answer FROM quizgame WHERE question_id = {question}')
        get_correct = curs.fetchall()
        correct = get_correct[0][0]
        if answer == correct:
            print('Your answer is correct! You\'ve gained 1 point')
            points += 1
        else:
            print('Your answer is wrong! You didn\'t gained the point')
        print(f'Your current points: {points}')

        nexted = False
        while not nexted:
            wait_next = input('Lets go for next question, write "next" if you want to continue: ')
            if wait_next == 'next':
                question += 1
                nexted = True
            else:
                print('Unknown command, please enter the word "next"')
        continue

    print('The test have finished. Your results: ', end='\n')
    time.sleep(0.2)
    if points == 0:
        print('You\'ve gained 0 points, maybe you just took random answers? Please, do it with enthusiasm :)')
    elif 5 > points > 0:
        print(f'Oh oh, it seems like you know a little bit about world history, because you gained {points} points '
              f'You can learn more about it, '
              'it is really interesting')
    elif 5 < points < 10:
        print(f'{points} points. You know some things in world history, but not so deep. Maybe, you forgot most of '
              f'information which you learned at school')
    elif 10 < points < 15:
        print(f'Wow, you gained {points} points. This is good result, it seems like you can talk about history with '
              f'someone and it would be interesting')
    elif 15 < points < 20:
        print(f'Very good results, you\'ve gained {points} points. Your knowledge about world is so big!')
    elif points == 20:
        print('20/20. That\'s maximum. You are genius of World\'s History')

    while not is_again:
        again = input('Do you want to play again this quiz? Type "yes" if yes, or "no" if don\'t want: ')
        if again.lower() == 'yes':
            start_game()
            is_again = True
        elif again.lower() == 'no':
            exit(0)
            is_again = True
        else:
            print('Please, write yes or no to the console')
            time.sleep(1)


start()
