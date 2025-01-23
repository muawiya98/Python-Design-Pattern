

class Sorting:


    def swap(self, object:list, i: int, j: int):
        x1 = object[i]
        x2 = object[j]
        object[i] = x2
        object[j] = x1
        return object
    
    def compare_to(self, first, second):
        if first>second:return 1
        elif first<second:return 0
        else:return -1
    
    def merge_sort(self, src: list, dest: list, low: int, high: int, off: int):

        for i in range(low, high, 1):
            for j in range(i, low, -1):
                if self.compare_to(dest[j-1], dest[j])==1:
                    dest = self.swap(dest, j, j-1)
        return dest

    def sort(self, object: list):
        temp_object = object.copy()
        return self.merge_sort(temp_object, object, 0 , len(object), 0)

