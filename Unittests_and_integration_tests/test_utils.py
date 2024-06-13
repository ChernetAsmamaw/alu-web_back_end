#!/usr/bin/env python3
""" Parameterize a unit test, Mock HTTP calls,
and Parameterize and patch """


import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing Nested Map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test method returns output """
        self.assertEqual(access_nested_map(nested_map, path), expected)


    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])

    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ Test method raises correct exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)

class TestGetJson(unittest.TestCase):
    """ Class for testing get_json function """
    
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test that get_json returns the correct output """
        # Create a mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        
        # Patch 'requests.get' to return the mock response
        with patch('requests.get', return_value=mock_response) as mocked_get:
            # Call the function under test
            real_response = get_json(test_url)
            
            # Assert that the function returns the expected payload
            self.assertEqual(real_response, test_payload)
            
            # Assert that 'requests.get' was called exactly once with the correct URL
            mocked_get.assert_called_once_with(test_url)

class TestMemoize(unittest.TestCase):
    """ Class for testing memoization """

    def test_memoize(self):
        """ Tests memoize function """

        class TestClass:
            """ Test class """

            def a_method(self):
                """ Method to always return 42 """
                return 42

            @memoize
            def a_property(self):
                """ Returns memoized property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
