import pytest

from .generate_bbst_array import GenerateBBSTArray


@pytest.mark.parametrize(
    'orig_list,expected_list',
    [
        (
            [1, 3, 2],
            [2, 1, 3],
        ),
        (
            [3, 1, 9, 6, 4, 12, 7, 2, 11],
            [6, 3, 11, 2, 4, 9, 12, None, None, None, 1, None, None, None, 7],
        ),
        (
            [],
            []
        )
    ]
)
def test_generate_bbst_array(orig_list, expected_list):
    bst = GenerateBBSTArray(orig_list)
