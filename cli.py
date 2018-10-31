from prompt_toolkit import prompt
from jenkins import status

def hello_world(name):
    print('Hello ' + name + ' :)')

if __name__ == '__main__':
    print('Welcome to Jenkins CLI')
    while True:
        answer = prompt('>>> ')
        status()