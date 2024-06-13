#!/usr/bin/env python3
""" Parameterize a unit test """


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
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        # Patch 'requests.get' in the 'utils' module to avoid actual HTTP calls
        with patch('utils.requests.get') as mocked_get:
            # Create a mock response object with a 'json' method that returns 'test_payload'
            mocked_response = Mock()
            mocked_response.json.return_value = test_payload
            # Set the return value of 'requests.get' to our mock response
            mocked_get.return_value = mocked_response

            # Call the function under test with the test URL
            result = get_json(test_url)
            
            # Assert that 'requests.get' was called exactly once with the correct URL
            mocked_get.assert_called_once_with(test_url)
            # Assert that the result of 'get_json' matches the expected payload
            self.assertEqual(result, test_payload)
