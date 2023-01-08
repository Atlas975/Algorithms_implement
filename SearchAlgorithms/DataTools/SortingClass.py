from random import randrange


class Sort:
    def __init__(self):
        self.algorithm = {
            "i": lambda data: self.insertion_sort(data),
            "s": lambda data: self.selection_sort(data),
            "m": lambda data: self.merge_sort(data),
            "h": lambda data: self.heap_sort(data),
            "q": lambda data: self.quick_sort(data),
            "b": lambda data: self.bogo_sort(data),
            "r": lambda data: self.radix_sort(data),
            "0": lambda data: self.just_use_whatever_sort(data),
        }

    def sort(self, data, choice):
        choice = choice[0].lower()
        algorithm = self.algorithm[choice]
        return algorithm(data)

    def selection_sort(self, data):
        for i in range(len(data)):
            minimum = i
        for j in range(i + 1, len(data)):
            if data[j] < data[minimum]:
                minimum = j
        if minimum != i:
            data[minimum], data[i] = data[i], data[minimum]
        return data

    def insertion_sort(self, data):
        for i in range(1, len(data)):
            temp = i
            for j in range(i - 1, -1, -1):
                if data[j] > data[temp]:
                    data[j], data[temp] = data[temp], data[j]
                    temp -= 1
                else:
                    break
        return data

    def merge_sort(self, data):
        if len(data) == 1:
            return data
        split = round(len(data) / 2)
        left_segment = data[:split]
        right_segment = data[split:]
        left_segment = self.merge_sort(left_segment)
        right_segment = self.merge_sort(right_segment)
        return self.merge_segement(left_segment, right_segment)

    def merge_segement(self, leftSegment, rightSegment):
        result = []
        while len(leftSegment) > 0 and len(rightSegment) > 0:
            if leftSegment[0] < rightSegment[0]:
                result.append(leftSegment[0])
                leftSegment.pop(0)
            else:
                result.append(rightSegment[0])
                rightSegment.pop(0)
        if len(leftSegment) != 0:
            result.extend(leftSegment)
        else:
            result.extend(rightSegment)
        return result

    def max_heap(self, data, n, root):
        new_root = root
        left = 2 * root + 1
        if left >= n:
            return data
        right = 2 * root + 2
        if right >= n:
            return data

        if data[left] > data[new_root]:
            new_root = left
        if data[right] > data[new_root]:
            new_root = right
        if new_root != root:
            data[root], data[new_root] = data[new_root], data[root]
            self.max_heap(data, n, new_root)
        return data

    def heap_sort(self, data):
        n = len(data)
        for parent in range(n // 2 - 1, -1, -1):
            data = self.max_heap(data, n, parent)
        for i in range(n - 1, 0, -1):
            data[0], data[i] = data[i], data[0]
            data = self.max_heap(data, i, 0)
        return data

    def quick_sort(self, data, low=0, high=None):
        if high == None:
            high = len(data) - 1
        if low < high:
            pivot_idx = self.quick_sort_partition(data, low, high)
            self.quick_sort(data, low, pivot_idx - 1)
            self.quick_sort(data, pivot_idx + 1, high)
        return data

    def print_data(self, data):
        return data

    def quick_sort_partition(self, data, low, high):
        start = low
        if data[high] < data[low]:
            data[high], data[low] = data[low], data[high]
            start += 1
            low += 1
        pivot = data[high]
        for i in range(low, high):
            if data[i] <= pivot:
                data[start], data[i] = data[i], data[start]
                start += 1
        data[start], data[high] = data[high], data[start]
        return start

    def bogo_sort(self, data):
        isSorted = True
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                isSorted = False
        if isSorted:
            return data
        else:
            for i in range(len(data)):
                new_spot = randrange(len(data))
                data[i], data[new_spot] = data[new_spot], data[i]
        return self.bogo_sort(data)

    def radix_sort(self, data):
        return

    def just_use_whatever_sort(self, data):
        return data
