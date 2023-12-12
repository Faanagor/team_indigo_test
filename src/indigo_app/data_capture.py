from collections import defaultdict

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
        self.sorted_dict_capture = {}
        self.max_limit = 1000
        self.max_value = -1000

    def _validate_input(self, num: int) -> None:
        """
        Validates the input parameter for the add method.

        Parameters:
        - num (int): The number to be validated.

        Raises:
        - ValueError: If the input is not an integer or is not within a specific range.
        """
        if not isinstance(num, int):
            raise ValueError("Input must be an integer.")
        if num > self.max_limit:
            raise ValueError(
                f"Input must be an integer less than or equal to {self.max_limit}.")

    def add_new_zero_value_to_dict(self) -> None:
        """ Add value to key in dict, when the value of key is 0. """
        for i in range(1, self.max_value + 1):
            if i not in self.dict_capture:
                self.dict_capture[i] = 0

    def add(self, num: int) -> None:
        """
        Adds a number to the data capture.

        Parameters:
        - num (int): The number to be added.
        """
        self._validate_input(num)
        self.list_capture.append(num)
        self.dict_capture[num] = self.dict_capture.get(num, 0) + 1
        self.max_value = max(self.max_value, num)
        self.add_new_zero_value_to_dict()
        self.sorted_dict_capture = dict(sorted(self.dict_capture.items()))

    def build_stats(self) -> int:
        """
        Builds statistics based on the captured data.

        Returns:
        - Stats: An instance of the Stats class.
        """
        total = 0
        dict_added_capture = {}
        for value, count in (self.sorted_dict_capture.items()):
            total += count
            dict_added_capture[value] = total
        return Stats(self.max_value, dict_added_capture)
