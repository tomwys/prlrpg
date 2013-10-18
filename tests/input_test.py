from unittest import TestCase
from input import Input


class TestInput(TestCase):

    def __make_input(self, lines):
        def input():
            return lines.pop()
        return input
    def __make_output(self, result):
        def output(line):
            result.append(line)
        return output

    def test_wrong_input(self):
        result = []
        input = Input(self.__make_input(['dupa']), self.__make_output(result))
        self.assertEqual(input.next_move(), None)
        self.assertEqual(result, ['Wrong move. Try: look.'])

    def test_look(self):
        result = []
        input = Input(self.__make_input(['look']), self.__make_output(result))
        self.assertEqual(input.next_move(), ("look", []))

    def test_move(self):
        result = []
        input = Input(self.__make_input(['move north']), self.__make_output(result))
        self.assertEqual(input.next_move(), ("move", ['north']))
