# You will need to install Python Poetry.
#This is still in progress.

from PyInquirer import prompt
from platform import system
from subprocess import call

questions = [
    dict(type='input', name='ip', message='What is the IP of the machine you are trying to ping?'
    dict(type='input', name='pings', message+"How many times do you want to ping?'
]

def clear():
    pass

def ping(address, n=1):
    pass

def main():
    clear()
    answers = prompt(questions)
    success = ping(answers['ip'], answers['pings'])
    if not success:
        print("Had some issues pinging {}.".format(answers["ip"]))


if __name__ == "__main__":
    main()
