class DataCapture:
    def __init__(self):
        self.data = []
        self.counts = {}  # Dictionary to store counts of each value
        self.cumulative_counts = {}  # Dictionary to store cumulative counts

    def add(self, value):
        self.data.append(value)
        self.counts[value] = self.counts.get(value, 0) + 1

    def build_stats(self):
        total = 0
        for value, count in sorted(self.counts.items()):
            total += count
            self.cumulative_counts[value] = total
        return Stats(self.counts, self.cumulative_counts)


class Stats:
    def __init__(self, counts, cumulative_counts):
        self.counts = counts
        self.cumulative_counts = cumulative_counts

    def less(self, threshold):
        return self.cumulative_counts.get(threshold - 1, 0)

    def between(self, low, high):
        return self.cumulative_counts.get(high, 0) - self.cumulative_counts.get(low - 1, 0)

    def greater(self, threshold):
        return len(self.counts) - self.cumulative_counts.get(threshold, 0)


# Example Usage
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()

result1 = stats.less(4)
result2 = stats.between(3, 6)
result3 = stats.greater(4)

print(result1)  # Should return 2
print(result2)  # Should return 4
print(result3)  # Should return 2
