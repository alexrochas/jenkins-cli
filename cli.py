from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings
from actions import status, deploy
from prompt_toolkit.completion import Completer, Completion
import pdb


class MyCustomCompleter(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        action = document.text.split(' ')[0]
        line = document.text.split(' ')
        last_word = line[-1]

        if len(line) == 2 and action == 'build':
            yield Completion('dev', start_position=0)
            yield Completion('hlg', start_position=0)
            yield Completion('prod', start_position=0)
        elif len(line) >= 2:
            yield Completion('cartoes-core-adapter', start_position=0)
            yield Completion('cartoes-pagamento-service', start_position=0)
        else:
            if action.startswith('b'):
                yield Completion('build', start_position=-len(word_before_cursor))
            elif action.startswith('s'):
                yield Completion('status', start_position=-len(word_before_cursor))
            else:
                yield Completion('build', start_position=0)
                yield Completion('status', start_position=0)


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
