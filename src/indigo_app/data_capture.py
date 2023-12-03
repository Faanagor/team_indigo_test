from .stats import Stats


class DataCapture:
    """ Class 
    """

    def __init__(self) -> None:
        """Initialize an instance of DataCapture with an empty data list
        (list_capture).
        """
        self.list_capture = []

    def add(self, num: int) -> None:
        """Add a value to the data list.

        Args:
            num: The value to be added to list_capture list.
        """
        self.list_capture.append(num)

    def build_stats(self) -> int:
        """Build and return an instance of Stats using the current data.

        Returns:
            Stats: An instance of the Stats class with the current data.
        """
        return Stats(self.list_capture)
