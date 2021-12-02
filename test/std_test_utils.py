from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class STDIOTest(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdin_n_out(self, function, string_input, expected_output, mock_stdout):
        with patch('sys.stdin', StringIO(string_input)):
            function()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
