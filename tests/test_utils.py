import unittest

from utils import InputError
from utils import find_all_tags, partition_and_replace


class TestPartionAndReplace(unittest.TestCase):
    """
    Test cases for `partion_and_replace` function.
    """

    def test_standard_string(self):
        test_string = '''
        <html>
          <head>
          </head>
          <body>
          </body>
        </html>
        '''
        all_tags = find_all_tags(test_string)
        new_string = partition_and_replace(test_string, all_tags)
        self.assertEqual(test_string, new_string)

    def test_non_standard_string(self):
        test_string = '''
        <html>
          <head>
          </>
          <body>
          </>
        </html>
        '''
        expected_new_string = '''
        <html>
          <head>
          </head>
          <body>
          </body>
        </html>
        '''
        all_tags = find_all_tags(test_string)
        new_string = partition_and_replace(test_string, all_tags)
        self.assertEqual(new_string, expected_new_string)

    def test_nested_non_standard_string(self):
        test_string = '''
        <html>
          <head></>
        </>
        '''
        expected_new_string = '''
        <html>
          <head></head>
        </html>
        '''
        all_tags = find_all_tags(test_string)
        new_string = partition_and_replace(test_string, all_tags)
        self.assertEqual(new_string, expected_new_string)

    def test_nested_non_standard_string2(self):
        test_string = '''
        <html>
          <head>
            <title>test case</>
          </>
        </>
        '''
        expected_new_string = '''
        <html>
          <head>
            <title>test case</title>
          </head>
        </html>
        '''
        all_tags = find_all_tags(test_string)
        new_string = partition_and_replace(test_string, all_tags)
        self.assertEqual(new_string, expected_new_string)

    def test_standard_string2(self):
        test_string = '''
        <img src="www.example.com" />
        '''
        all_tags = find_all_tags(test_string)
        new_string = partition_and_replace(test_string, all_tags)
        self.assertEqual(test_string, new_string)

    def test_wrong_string(self):
        test_string = '''
        </html>
        '''
        all_tags = find_all_tags(test_string)
        with self.assertRaises(InputError):
            new_string = partition_and_replace(test_string, all_tags)

    def test_wrong_string2(self):
        test_string = '''
        <html></a></html>
        '''
        all_tags = find_all_tags(test_string)
        with self.assertRaises(InputError):
            new_string = partition_and_replace(test_string, all_tags)

    def test_wrong_string3(self):
        test_string = '''<html></></html>'''
        all_tags = find_all_tags(test_string)
        with self.assertRaises(InputError):
            new_string = partition_and_replace(test_string, all_tags)
