"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:

print('Welcome to the Quizz !')

questions_liste = open('085_questions.txt', 'r')
questions = [q.strip() for q in questions_liste.readlines()]
questions_liste.close()

n = 0
m = 0
for question in questions:
    question_display = question.split('=')[0]
    answer = input(question_display+'=')
    if answer == question.split('=')[1]:
        n += 1
    m += 1

result_file = open('085_result.txt', 'w')
result_file.write(f'Your final score is {n}/{m}.')
result_file.close()
