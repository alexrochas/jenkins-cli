from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings
from actions import status, deploy
from prompt_toolkit.completion import Completer, Completion
from setup import setup, build_dictionary


class MyCustomCompleter(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        action = document.text.split(' ')[0]
        line = document.text.split(' ')

        if line[0] is '':
            last_word = 'empty'
        else:
            key_word_index = len(line) - 2
            last_word = line[key_word_index]

        for i in build_dictionary(last_word):
            yield Completion(i, start_position=-len(word_before_cursor))


kb = KeyBindings()


@kb.add('c-space')
def _(event):
    b = event.app.current_buffer
    if b.complete_state:
        b.complete_next()
    else:
        b.start_completion(select_first=False)


def _read_input():
    return prompt('>>> ',
                  completer=MyCustomCompleter(),
                  complete_while_typing=False,
                  key_bindings=kb)


def main():
    setup()
    print('Welcome to Jenkins CLI')
    while True:
        answer = _read_input()
        if answer.startswith('status'):
            status(answer)
        elif answer.startswith('build'):
            deploy(answer)
        else:
            print('action n0t found')


if __name__ == '__main__':
    main()
