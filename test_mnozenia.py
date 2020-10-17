from random import randint
from datetime import datetime

# testing if a string can be an INT
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# variables
correct = 0
total = 0
total_time = 0 # in sekundach
numbers_a = []
numbers_b = []
answers = []
points = []
times = []

#main body of program
for i in range(10):

    # randomly generating 2 numbers
    a = randint(1,16)
    b = randint(1,16)

    # timer start anc core function
    start = datetime.now()
    w = input(f'Give the result of multiplication: {a} * {b} > ')
    end = datetime.now()

    # calculating time for each question
    temp_time = end - start
    times.append(temp_time)
    calculated_seconds = str(temp_time.seconds)
    calculated_ms = f'{temp_time.microseconds}'
    calculated_time = calculated_seconds + '.' + calculated_ms
    total_time += float(calculated_time)
    print(total_time)
    wynik = str(a * b)
    if w == wynik:
        print('You are correct, +1')
        correct += 1
        points.append(1)
    else:
        print('Wrong answer, +0')
        points.append(0)

    total += 1
    numbers_a.append(a)
    numbers_b.append(b)
    answers.append(w)
    print(f'Your temporary result is: {correct} / {total} = {correct / total * 100 :.2f}%')

#RAPORT W KONSOLI
for i in range(10): # 0 1 2 3 4 5 6 7 8 9
    print(f'{i+1}. Drawn numbers a : {numbers_a[i]} b : {numbers_b[i]} | Answer : {answers[i]} | Points {points[i]} | Answer time: {times[i].seconds}.{times[i].microseconds} sec')
print(f'Summary: Points : {correct} / {total} = {correct / total * 100 :.2f}% | Total time : {total_time:.2f} sek')

# SAVING INTO LEADERBOARD.TXT
f = open("Leaderboard.txt", "a")
f.write(f'Summary: Points : {correct} / {total} = {correct / total * 100 :.2f}% | Total time : {total_time:.2f} sek \n')
f.close()

# SAVING INTO HIGHSCORE.TXT

# checking if the current result is better than the highscore
def isNewHighscore(highscore,highscore_time,result_score,result_time):
    if result_score > highscore:
        return True
    elif result_score == highscore:
        if result_time < highscore_time:
            return True
        else:
            return False
    else:
        return False

# error handling if file doesn't exist yet
try:
    file = open("highscore.txt", "r")
    words = file.readlines()
except :
    file = open("highscore.txt", "x")
    words = []

words_final = []
# checking if the file isn't empty
if words == []:
    words_final = ["Highscore","0","0.0"]
    print(words_final)

# refactoring the output
for line in words:
    words_final.append(line.strip("\n").strip())
file.close()
print(words_final)

file = open("highscore.txt", "w")
# checking if we have new highscore
if isNewHighscore(int(words_final[1]), float(words_final[2]), correct, total_time):
    file.truncate(0)
    file.write(f'Highscore:\n{correct}\n{total_time:.2f}')
else:
    print(f'''Unfortunately you didnt beat the highscore.
You had {correct} points in {total_time} seconds.
The record is {words_final[1]} points in {words_final[2]:.2f} seconds''')

    file.write(f'Highscore:\n{words_final[1]}\n{words_final[2]}') # so we leave the previous hs
file.close()
