from .stats import Stats


class DataCapture:
    """
    Class that adds elements to list_capture, calls to Stat Class and
    return its result
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the DataCapture class.

        Attributes:
        - list_capture (list): List to capture data.
        - dict_capture (dict): Dictionary to store counts of each value.
        - dict_sorted_add_capture (dict): Dictionary to store cumulative counts.
        """
        self.list_capture = []
        self.dict_capture = {}  # Dictionary to store counts of each value
        self.dict_sorted_add_capture = {}  # Dictionary to store cumulative counts

    def add(self, num: int) -> None:
        """
        Adds a number to the data capture.

        Parameters:
        - num (int): The number to be added.
        """
        self.list_capture.append(num)
        self.dict_capture[num] = self.dict_capture.get(num, 0) + 1

    def build_stats(self) -> int:
        """
        Builds statistics based on the captured data.

        Returns:
        - int: The value result from the Stats Class.
        """
        total = 0
        max_value = max(self.list_capture)
        for i in range(1, max_value + 1):
            if i not in self.dict_capture:
                self.dict_capture[i] = 0
        for value, count in sorted(self.dict_capture.items()):
            total += count
            self.dict_sorted_add_capture[value] = total
        return Stats(max_value, self.dict_sorted_add_capture)
