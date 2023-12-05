from src.indigo_app.stats import Stats

# Mock data for testing
mock_dict_sorted_add_capture = {1: 1, 2: 3, 3: 6, 4: 10, 5: 11}
max_value = max(mock_dict_sorted_add_capture.keys())


def test_less():
    stats = Stats(max_value, mock_dict_sorted_add_capture)
    assert stats.less(3) == 3
    assert stats.less(5) == 10
    assert stats.less(2) == 1


def test_between():
    stats = Stats(max_value, mock_dict_sorted_add_capture)
    assert stats.between(2, 4) == 9
    assert stats.between(1, 3) == 6
    assert stats.between(3, 5) == 8


def test_greater():
    stats = Stats(max_value, mock_dict_sorted_add_capture)
    assert stats.greater(2) == 8
    assert stats.greater(5) == 0
    assert stats.greater(1) == 10
