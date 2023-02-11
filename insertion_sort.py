class Insertion_sort:
    def __init__(self, array: list):
        self.array = array

    def run_crescent(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1

            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j = j - 1

            self.array[j + 1] = key

        print(self.array)

    def run_decrescent(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1

            while j >= 0 and self.array[j] < key:
                self.array[j + 1] = self.array[j]
                j = j - 1

            self.array[j + 1] = key

        print(self.array)


list = list((3, 4, 2, 8, 9))
insertion_sort = Insertion_sort(list)
insertion_sort.run_crescent()
insertion_sort.run_decrescent()
