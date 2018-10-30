from prompt_toolkit import prompt

if __name__ == '__main__':
    print('Welcome to Jenkins CLI')
    while True:
        answer = prompt('>>> ')
        print('Command %s not implemented yet..sorry' % answer)
