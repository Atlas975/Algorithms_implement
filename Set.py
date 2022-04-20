class Set:

    def __init__(self, data = [], convert = True):
        if(convert):
            self.data = self.convert_to(data)
        else:
            self.data = data
        self.get_data()

    def is_in(self, element, data):
        for i in data:
            if i == element:
                return True
        return False

    def convert_to(self, data):
        i = 0
        while i != len(data):
            if(self.is_in(data[i], data[:i])):
                data.pop(i)
                i -= 1
            else:
                i += 1
        return data

    def add_elem(self, element):
        if(not self.is_in(element, self.data)):
            self.data.append(element)
        self.data

    def is_empty_set(self):
        return len(self.data) == 0

    def is_valid_set(self):
        i = 0
        while i != len(self.data):
            if(self.is_in(self.data[i], self.data[:i])):
                return False
            else:
                i += 1
        return True

    def is_set_equal(self, set2):
        print(self.data)
        print(set2)
        if len(self.data) != len(set2):
            return False
        for i in self.data:
            if(not self.is_in(i, set2)):
                return False
        return True

    def merge_set(self, data1, data2):
        self.data = self.convert_to(data1)
        data2 = self.convert_to(data2)
        for i in data2:
            if (not self.is_in(i, self.data)):
                self.data.append(i)
        return self.data

    def set_intersect(self, data2):
        intersection = []
        set2 = self.convert_to(data2)
        for i in self.data:
            if(self.is_in(i, set2)):
                intersection.append(i)
        return intersection

    def set_difference(self, data2):
        difference = []
        for i in self.data:
            if(not self.is_in(i, data2)):
                difference.append(i)
        for i in data2:
            if(not self.is_in(i, self.data)):
                difference.append(i)
        return difference

    def is_subset(self, data2):
        for i in range(len(self.data)):
            if(not self.is_in(self.data[i], data2)):
                return False
        return True

    def get_data(self):
        return self.data
