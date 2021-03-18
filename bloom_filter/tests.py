import pytest

from .bloom_filter import BloomFilter


@pytest.fixture
def bloom():
    return BloomFilter(32)


@pytest.fixture
def test_strings():
    return [
        '0123456789',
        '1234567890',
        '2345678901',
        '3456789012',
        '4567890123',
        '5678901234',
        '6789012345',
        '7890123456',
        '8901234567',
        '9012345678',
    ]


def test_without_values_is_value_return_False_for_all_values(bloom, test_strings):
    for a_str in test_strings:
        assert not bloom.is_value(a_str)


def test_after_add_is_value_return_True(bloom, test_strings):
    for a_str in test_strings:
        bloom.add(a_str)
        assert bloom.is_value(a_str)
