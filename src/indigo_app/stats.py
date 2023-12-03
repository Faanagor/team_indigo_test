from typing import List


class Stats:
    def __init__(self, list_capture: List) -> None:
        """Initialize an instance of Stats with a given data list.

        Args:
            data (list): The list of data for which statistics will be
            calculated.
        """
        self.data = list_capture

    def less(self, num_less: int) -> int:
        return len([x for x in self.data if x < num_less])

    def between(self, num_down_range: int, num_up_range: int) -> int:
        return len([
            x for x in self.data if num_down_range <= x <= num_up_range])

    def greater(self, num_greater: int) -> int:
        return len([x for x in self.data if x > num_greater])
