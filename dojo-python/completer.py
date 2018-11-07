def _fetch_fields():
    return ['id', 'cpf']


def _fetch_tables():
    return ['table1', 'table2']


def complete(current_buffer):
    current_dict = sql_syntax
    if current_buffer is '':
        return [*current_dict.keys()][0]

    for word in current_buffer.split(' '):
        if word in [*current_dict.keys()][0]:
            current_dict = current_dict.get([*current_dict.keys()][0])
            if current_dict.get([*current_dict.keys()][0]) is None:
                return list([*current_dict.keys()][0])

    if isinstance([*current_dict.keys()][0], tuple):
        return list([*current_dict.keys()][0])
    return [*current_dict.keys()][0]


sql_syntax = {
    'select': {
        tuple(_fetch_fields()): {
            'from': {
                tuple(_fetch_tables()): None
            }
        }
    },
}
