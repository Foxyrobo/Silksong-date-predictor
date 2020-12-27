#Time Predictor
import random, time

def zeroStuff(timeType):
    if timeType >= 1 and timeType < 10:
        timeType = "0" + str(timeType)
    return timeType

while True:
    print("Fill in the blank")
    print("When will ______________?")
    answer = input()
    month = random.randint(1, 12)
    day = random.randint(1, 31)
    year = random.randint(2020, 2099)
    hour = random.randint(1, 24)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    AM = True
    showAnswer = True

    #Day shenanigans
    if day == 31:
        if month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
            day = random.randint(1, 30)
    if day > 28 and month == 2:
        day = random.randint(1, 28)

    #Hour shenanigans
    if hour > 12:
        AM = False
        hour -= 12

    #Shenanigans involving adding 0s to things
    month = zeroStuff(month)
    day = zeroStuff(day)
    hour = zeroStuff(hour)
    minute = zeroStuff(minute)
    second = zeroStuff(second)

    #Extra interactions
    if answer == 'the universe end':
        month = 1
        day = 1
        year = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        hour = 12
        minute = 0
        second = 0
        AM = True

    if answer == 'my youtube channel hit 1 million subscribers':
        showAnswer = False
        print('"my youtube channel hit 1 million subscribers" will happen on')
        print('Well, I hate to break it to you')
        print()
        print('Never')
        print()
        time.sleep(5)
        print("Don't be rude")
        print()

    if answer == 'thanks' or answer == 'thank you' or answer == 'thank' or answer == 'wow, thanks':
        showAnswer = False
        print('You are welcome')
        print()

    if answer == 'that was sarcastic':
        showAnswer = False
        print('I know')
        print('Just like I (might) know the release date for silksong')
        print()

    if answer == 'I die' or answer == 'i die':
        showAnswer = False
        print('Yesterday')
        time.sleep(3)
        print()
        print('Good luck')
        time.sleep(1)
        print('Goodbye')
        time.sleep(4)
        print('Hi')
        time.sleep(1)
        print('I was just kidding earlier')
        time.sleep(2.5)
        print('Or was I?')
        time.sleep(1)
        print('Nah, I was')
        time.sleep(1)
        print()
    
    #Display Answer
    if showAnswer:
        print('"' + answer + '" will happen on ' + str(month) + '/' + str(day) + '/' + str(year))
        if AM:
            print("The time will be " + str(hour) + ":" + str(minute) + ":" + str(second) + " AM")
        if not AM:
            print("The time will be " + str(hour) + ":" + str(minute) + ":" + str(second) + " PM")
        print()
