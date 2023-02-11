class Fusion_sort:
    def run(self, arr: list):
        if len(arr) > 1:
            middle_of_array = len(arr) // 2
            left_array = arr[:middle_of_array]
            right_array = arr[middle_of_array:]

            self.run(right_array)
            self.run(left_array)

            i = j = k = 0

            while i < len(left_array) and j < len(right_array):
                if left_array[i] <= right_array[j]:
                    arr[k] = left_array[i]
                    i += 1
                else:
                    arr[k] = right_array[j]
                    j += 1
                k += 1

            while i < len(left_array):
                arr[k] = left_array[i]
                i += 1
                k += 1

            while j < len(right_array):
                arr[k] = right_array[j]
                j += 1
                k += 1


list = list((3, 4, 2, 8, 9))
insertion_sort = Fusion_sort()
insertion_sort.run(list)
print(list)
