import unittest
from completer import complete


class CompleterTest(unittest.TestCase):
    """
    select -> [field(s)]
    select field -> from
    select field from -> [table(s)]
    """

    def test_when_buffer_is_empty(self):
        current_buffer = ''
        self.assertEqual(complete(current_buffer), 'select')

    def test_when_buffer_have_select_word(self):
        current_buffer = 'select'
        self.assertEqual(complete(current_buffer), ['id', 'cpf'])

    def test_when_buffer_have_wrong_select_word(self):
        current_buffer = 'selecti'
        self.assertEqual(complete(current_buffer), 'select')

    def test_when_buffer_have_field_word(self):
        current_buffer = 'select id'
        self.assertEqual(complete(current_buffer), 'from')

    def test_get_table(self):
        current_buffer = 'select id from'
        self.assertEqual(complete(current_buffer), ['table1', 'table2'])


if __name__ == '__main__':
    unittest.main()
