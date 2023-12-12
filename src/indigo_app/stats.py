from typing import Dict


class Stats:
    """Class that builds statistics based on the captured data."""

    def __init__(self, max_value: int, dict_sorted_add_capture: Dict) -> None:
        """Initialize an instance of Stats with a given data list.

        Args:
            max_value (int): The maximum value in the data.
            dict_sorted_add_capture (Dict): Dictionary with sorted cumulative counts.
        """
        self.max_limit = 1000
        self._validate_input(max_value, dict_sorted_add_capture)
        self.max_value = max_value
        self.dict_sorted_add_capture = dict_sorted_add_capture

    def _validate_input(self, max_value: int, dict_sorted_add_capture: Dict) -> None:
        """Validate the input parameters for the Stats class.

        Args:
            max_value (int): The maximum value in the data.
            dict_sorted_add_capture (Dict): Dictionary with sorted cumulative counts.

        Raises:
            TypeError: If max_value is not an integer or dict_sorted_add_capture is not a dictionary.
        """
        if not isinstance(max_value, int):
            raise TypeError("max_value must be an integer.")
        if not isinstance(dict_sorted_add_capture, dict):
            raise TypeError("dict_sorted_add_capture must be a dictionary.")
        if max_value > self.max_limit:
            raise ValueError(
                f"Input must be an integer less than or equal to {self.max_limit}.")

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
