from src.indigo_app.data_capture import DataCapture
from src.indigo_app.stats import Stats


def test_add():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    assert len(capture.list_capture) == 2


def test_build_stats():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    stats = capture.build_stats()
    assert isinstance(stats, Stats)


def test_stats_less():
    data = [3, 9, 3, 4, 6]
    stats = Stats(data)
    result = stats.less(4)
    assert result == 2


def test_stats_between():
    data = [3, 9, 3, 4, 6]
    stats = Stats(data)
    result = stats.between(3, 6)
    assert result == 4


def test_stats_greater():
    data = [3, 9, 3, 4, 6]
    stats = Stats(data)
    result = stats.greater(4)
    assert result == 2
