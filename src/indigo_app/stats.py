from typing import Dict


class Stats:
    """Class that builds statistics based on the captured data."""

    def __init__(self, max_value: int, dict_sorted_add_capture: Dict) -> None:
        """Initialize an instance of Stats with a given data list.

        Args:
            dict_capture (Dict): The list of data for which statistics will be
            calculated.
            dict_sorted_add_capture (Dict):
        """
        self.max_value = max_value
        self.dict_sorted_add_capture = dict_sorted_add_capture

    def less(self, num_less: int) -> int:
        """
        Count the number of elements less than a given value.

        Args:
            num_less (int): The threshold value.

        Returns:
            int: The count of elements less than the threshold.
        """
        if num_less > self.max_value:
            num_less = self.max_value + 1
        return self.dict_sorted_add_capture.get(num_less - 1, 0)

    def between(self, num_down_range: int, num_up_range: int) -> int:
        """
        Count the number of elements within a specified range.

        Args:
            num_down_range (int): The lower bound of the range.
            num_up_range (int): The upper bound of the range.

        Returns:
            int: The count of elements within the specified range.
        """
        if num_up_range > self.max_value:
            num_up_range = self.max_value

        return (self.dict_sorted_add_capture.get(num_up_range, 0) -
                self.dict_sorted_add_capture.get(num_down_range - 1, 0))

    def greater(self, num_greater: int) -> int:
        """
        Count the number of elements greater than a given value.

        Args:
            num_greater (int): The threshold value.

        Returns:
            int: The count of elements greater than the threshold.
        """
        if num_greater > self.max_value:
            return 0
        return (self.dict_sorted_add_capture.get(self.max_value, 0) -
                self.dict_sorted_add_capture.get(num_greater, 0))
