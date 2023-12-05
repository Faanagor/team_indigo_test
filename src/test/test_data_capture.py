from src.indigo_app.data_capture import DataCapture


def test_add():
    data_capture = DataCapture()

    # Test add method
    data_capture.add(1)
    data_capture.add(2)
    assert data_capture.list_capture == [1, 2]
    assert data_capture.dict_capture == {1: 1, 2: 1}


def test_build_stats():
    data_capture = DataCapture()
    data_capture.add(1)
    data_capture.add(2)

    # Test build_stats method
    stats = data_capture.build_stats()
    assert stats.max_value == 2
    assert stats.dict_sorted_add_capture == {1: 1, 2: 2}
