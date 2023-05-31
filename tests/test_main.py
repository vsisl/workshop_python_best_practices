"""This is a module containing unit tests for the main.py module.

We are using the pytest framework for unit tests. See https://docs.pytest.org/en/7.3.x/.

Note that alternative testing frameworks exist - e.g. unittest https://docs.python.org/3/library/unittest.html
"""
import pytest

from utilities.math_utils import add_two_numbers


class TestAddTwoNumbers:
    def test_on_two_integers(self):
        actual = add_two_numbers(a=2, b=3)              # actual result of the tested function
        expected = 5                                    # expected (reference) result

        assert actual == expected

    # see https://docs.pytest.org/en/7.3.x/how-to/skipping.html#xfail-mark-test-functions-as-expected-to-fail
    @pytest.mark.xfail
    def test_on_floats_wrong_approach(self):
        """This test is SUPPOSED TO FAIL because some floats cannot be represented as exact binary fractions."""
        actual = add_two_numbers(a=0.1, b=0.2)
        expected = 0.3

        assert actual == expected                       # avoid using == when comparing floats!

    def test_on_floats_correct_approach(self):
        actual = add_two_numbers(a=0.1, b=0.2)
        expected = 0.3

        # use this to compare float values
        #  see https://docs.pytest.org/en/7.3.x/reference/reference.html#pytest.approx
        assert actual == pytest.approx(expected)
