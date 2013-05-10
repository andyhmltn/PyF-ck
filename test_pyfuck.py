import unittest
import os
import pyfuck


class TestPyFuck(unittest.TestCase):
    to_parse = ('++++++++++[>++++>++++++++>++++++++++>+++++++++++>++++++'
                '++++++<<<<<-]>>.>>>+.<<<----------.<++.>>-.>---.')
    test_file = '.test'

    def setUp(self):
        self.fd = open(self.test_file, 'w+')

    def tearDown(self):
        self.fd.close()
        os.remove(self.test_file)

    def assertion(self):
        # head to the start of the file for output
        self.fd.seek(0, 0)
        text = self.fd.read()
        self.assertEqual(text, 'PyF*ck\n')

    def test_evals_pyfuck(self):
        p = pyfuck.PyFuck(self.to_parse, outfile=self.fd)
        p.parse()
        self.assertion()

    def test_api(self):
        pyfuck.parse(self.to_parse, outfile=self.fd)
        self.assertion()


if __name__ == '__main__':
    unittest.main()
