import unittest
from completer import complete
from completer import _add_elements_into_list


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
        self.assertEqual(complete(current_buffer), ['id', 'cpf', 'from'])

    def test_get_table(self):
        current_buffer = 'select id from'
        self.assertEqual(complete(current_buffer), ['table1', 'table2'])

    def test_when_buffer_have_a_invalid_word_positioned_word(self):
        current_buffer = 'id from'
        self.assertEqual(complete(current_buffer), 'select')

    def test_append_list(self):
        self.assertEqual(_add_elements_into_list(['id', 'cpf'], 'from'), ['id', 'cpf', 'from'])

if __name__ == '__main__':
    unittest.main()
