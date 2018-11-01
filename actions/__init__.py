from jenkins import get_status
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings

word_completer = WordCompleter([
    'cartoes-pagamento-service',
    'cartoes-core-adapter'
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
    return prompt('>>> Select your service >>> ',
                  completer=word_completer,
                  complete_while_typing=False,
                  key_bindings=kb)


def status():
    answer = _read_input()
    get_status(answer)
