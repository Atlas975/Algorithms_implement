
class ADT_tool:
    def __init__(self):
        self.algorithm={
            "insertion": lambda: self.insertion_sort(data),
            "selection": lambda: self.selection_sort(data),
            "merge": lambda: self.merge_sort(data),
        }

    def convert_to(self,data,choice="set"):
        pass
