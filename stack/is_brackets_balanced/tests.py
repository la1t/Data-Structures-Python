from .is_brackets_balanced import is_brackets_balanced


def test_return_True_if_brackets_are_balanced():
    assert is_brackets_balanced('(()())')


def test_return_True_if_string_is_empty():
    assert is_brackets_balanced('')


def test_return_False_if_closing_bracket_before_opening():
    assert not is_brackets_balanced('())(')


def test_return_False_if_closing_bracket_in_the_start():
    assert not is_brackets_balanced(')')


def test_return_False_if_there_is_no_closing_bracket():
    assert not is_brackets_balanced('(')
