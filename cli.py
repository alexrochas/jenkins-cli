from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings
from jenkins import status

word_completer = WordCompleter([
    'status', 'build'
], ignore_case=True)

kb = KeyBindings()


@kb.add('c-space')
def _(event):
    b = event.app.current_buffer
    if b.complete_state:
        b.complete_next()
    else:
        b.start_completion(select_first=False)


def _read_input():
    return prompt('>>> ', completer=word_completer, complete_while_typing=False, key_bindings=kb)


def main():
    print('Welcome to Jenkins CLI')
    while True:
        answer = _read_input()
        print('You said: ' + answer)


if __name__ == '__main__':
    main()
