import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Tests that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_single_streak():
    """Tests a simple case with a single streak."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_multiple_streaks_longest_is_last():
    """Tests multiple streaks where the longest streak is at the end."""
    assert longest_positive_streak([1, 2, -1, 3, 4, 5]) == 3

def test_multiple_streaks_longest_is_first():
    """Tests multiple streaks where the longest streak is at the beginning."""
    assert longest_positive_streak([1, 2, 3, 4, -5, 1, 2]) == 4

def test_with_zeros():
    """Tests that zeros break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4]) == 2

def test_with_negatives():
    """Tests that negative numbers break the streak."""
    assert longest_positive_streak([1, 2, -3, 4, 5]) == 2

def test_all_non_positive():
    """Tests a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_example_from_prompt():
    """Tests the example provided in the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_same_positive_number():
    """Tests a streak of identical positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_single_element_positive():
    """Tests a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_element_non_positive():
    """Tests a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0