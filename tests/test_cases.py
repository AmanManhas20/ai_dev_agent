"""
Test cases for generated solution code.

Executed by TesterAgent using pytest.
"""


def test_basic_sort():
    """
    Test simple sorting behavior
    """

    from generated_code.solution import example_function

    result = example_function()

    assert result == [1, 2, 3]


def test_non_empty_output():
    """
    Ensure function returns a list
    """

    from generated_code.solution import example_function

    result = example_function()

    assert isinstance(result, list)


def test_list_length():
    """
    Ensure output length is correct
    """

    from generated_code.solution import example_function

    result = example_function()

    assert len(result) == 3