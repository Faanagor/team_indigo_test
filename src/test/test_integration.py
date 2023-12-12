import pytest
from src.indigo_app.data_capture import DataCapture


@pytest.fixture
def populated_data_capture():
    data_capture = DataCapture()
    data_capture.add(5)
    data_capture.add(7)
    data_capture.add(5)
    data_capture.add(10)
    return data_capture


def test_integration_less(populated_data_capture):
    stats = populated_data_capture.build_stats()
    assert stats.less(6) == 2


def test_integration_between(populated_data_capture):
    stats = populated_data_capture.build_stats()
    assert stats.between(5, 10) == 4


def test_integration_greater(populated_data_capture):
    stats = populated_data_capture.build_stats()
    assert stats.greater(7) == 1
