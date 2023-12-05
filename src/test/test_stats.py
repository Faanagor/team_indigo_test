import pytest

from src.indigo_app.stats import Stats

# Mock data for testing
mock_dict_sorted_add_capture = {1: 1, 2: 3, 3: 6, 4: 10, 5: 11}
max_value = max(mock_dict_sorted_add_capture.keys())


@pytest.mark.parametrize(
    "num_input, num_output",
    [
        (3, 3),
        (5, 10),
        (2, 1),
        (0, 0),
        (-5, 0),
        (8, 11)
    ]
)
def test_less(num_input: int, num_output: int) -> None:
    stats = Stats(max_value, mock_dict_sorted_add_capture)
    assert stats.less(num_input) == num_output


@pytest.mark.parametrize(
    "num_low_input, num_high_input, num_output",
    [
        (2, 4, 9),
        (1, 3, 6),
        (3, 5, 8),
        (-3, 5, 11),
        (5, 15, 1),
        (-2, 18, 11)
    ]
)
def test_between(num_low_input: int,
                 num_high_input: int,
                 num_output: int) -> None:
    stats = Stats(max_value, mock_dict_sorted_add_capture)
    assert stats.between(num_low_input, num_high_input) == num_output


@pytest.mark.parametrize(
    "num_input, num_output",
    [
        (2, 8),
        (5, 0),
        (1, 10),
        (0, 11),
        (15, 0),
        (11, 0),
        (-4, 11)
    ]
)
def test_greater(num_input: int, num_output: int) -> None:
    stats = Stats(max_value, mock_dict_sorted_add_capture)
    assert stats.greater(num_input) == num_output
