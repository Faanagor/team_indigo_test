import pytest

from src.indigo_app.data_capture import DataCapture, Stats


def test_add_integer_less_than_1000():
    data_capture = DataCapture()
    data_capture.add(1)
    data_capture.add(2)
    data_capture.add(5)
    assert data_capture.list_capture == [1, 2, 5]
    assert data_capture.dict_capture == {1: 1, 2: 1, 3: 0, 4: 0, 5: 1}
    assert data_capture.max_value == 5


def test_add_duplicate_values():
    data_capture = DataCapture()
    data_capture.add(3)
    data_capture.add(3)
    assert data_capture.list_capture == [3, 3]
    assert data_capture.dict_capture == {1: 0, 2: 0, 3: 2}
    assert data_capture.max_value == 3


def test_add_integer_greater_than_1000():
    data_capture = DataCapture()
    with pytest.raises(ValueError, match=(f"Input must be an integer less than or equal to 1000.")):
        data_capture.add(25000)


def test_add_non_integer():
    data_capture = DataCapture()
    with pytest.raises(ValueError, match="Input must be an integer."):
        data_capture.add("not_an_integer")


def test_build_stats():
    data_capture = DataCapture()
    data_capture.add(1)
    data_capture.add(2)

    # Test build_stats method
    stats = data_capture.build_stats()
    assert stats.max_value == 2
    assert stats.dict_sorted_add_capture == {1: 1, 2: 2}
    assert isinstance(stats, Stats)


def test_build_stats_no_data():
    data_capture = DataCapture()
    stats = data_capture.build_stats()
    assert isinstance(stats, Stats)
    assert stats.max_value == data_capture.max_value
    assert stats.dict_sorted_add_capture == {}
