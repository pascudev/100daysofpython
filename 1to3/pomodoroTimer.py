import datetime
from datetime import timedelta
from datetime import date


def pomodoroTimer(minutes):

    setToInt = int(minutes)
    currentTime = datetime.datetime.now()
    userTime = datetime.timedelta(minutes=setToInt)
    finalTime = currentTime + userTime
    parsedFinalTime = finalTime.strftime('%H:%M:%S')

    return parsedFinalTime

print('Hi! Please enter a the minutes to set your Pomodoro Timer: ')
getUserInput = input()

print(pomodoroTimer(getUserInput))
