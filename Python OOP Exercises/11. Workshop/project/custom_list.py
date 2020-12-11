class CustomList:

    def __init__(self, *args):
        self.custom_list = [el for el in args]

    def __getitem__(self, item):
        return self.custom_list[item]

    def __repr__(self):
        return f"{', '.join(str(n) for n in self.custom_list)}"

    def __len__(self):
        return len(self.custom_list)

    # def __str__(self):
    #     return f"{', '.join(str(n) for n in self.custom_list)}"

    def check_index(self, index):
        if not index > len(self.custom_list):
            return True
        raise IndexError

    def append(self, value):
        self.custom_list += [value]

    def remove(self, index):
        if self.check_index(index):
            del(self.custom_list[index])

    def get(self, index):
        if self.check_index(index):
            return self.__getitem__(index)

    def extend(self, iterable):
        return self.custom_list + iterable

    def insert(self, index, value):
        if self.check_index(index):
            self.custom_list = self.custom_list[:index] + [value] + self.custom_list[index:]
            return self.custom_list

    def pop(self):
        val = self.custom_list[-1]
        del (self.custom_list[-1])
        return val

    def clear(self):
        self.custom_list = []

    def index(self, value):
        counter = 0
        for num in self.custom_list:
            if num == value:
                return counter
            counter += 1

    def count(self, value):
        counter = 0
        for num in self.custom_list:
            if num == value:
                counter += 1
        return counter

    def reverse(self):
        return self.custom_list[::-1]

    def copy(self):
        new_list = [num for num in self.custom_list]
        return new_list

# =========== CUSTOM FUNCTIONALITIES ====================
    def size(self):
        return len(self.custom_list)

    def add_first(self, value):
        self.custom_list = [value] + self.custom_list

    def dictionize(self):
        new_dict = {}
        new_list = [num for num in self.custom_list]
        if len(new_list) % 2 != 0:
            new_list.extend([" "])
        even_list = CustomList()
        odd_list = CustomList()
        for num in range(len(new_list)):
            if num % 2 == 0:
                even_list.append(new_list[num])
            else:
                odd_list.append(new_list[num])

        for key, value in zip(even_list, odd_list):
            new_dict[key] = value
        return new_dict

    def move(self, amount):
        to_move = self.custom_list[:amount]
        self.custom_list = self.custom_list[amount:] + to_move
        return self.custom_list

    def sum(self):
        total = 0
        for value in self.custom_list:
            if isinstance(value, int) or isinstance(value, float):
                total += value
            else:
                total += len(value)
        return total

    def overbound(self):
        counter = 0
        max_num = 0
        for elem in self.custom_list:
            if isinstance(elem, int) or isinstance(elem, float):
                if elem > max_num:
                    max_num = elem
                    counter = self.index(elem)
            else:
                if len(elem) > max_num:
                    max_num = len(elem)
                    counter = self.index(elem)
        return counter

    def underbound(self):
        new_list = CustomList()
        for elem in self.custom_list:
            if isinstance(elem, int) or isinstance(elem, float):
                new_list.append(elem)
            else:
                new_list.append(len(elem))

        return self.index(min(new_list))


#
# my_list = CustomList()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# my_list.append(6)
# my_list.append(7)
# my_list.append("This")
# my_list.append("Homegrown")
# my_list.remove(5)
# my_list.remove(3)
# print(my_list.get(3))
# print(my_list.extend([1, 2, 3, 4]))
#
# print(my_list.insert(3, 1444))
# print(my_list.insert(3, 777))
# print(my_list.insert(1, 267))
#
# print(my_list)
# print(my_list.pop())
# # print(my_list.clear())
# print(my_list)
#
# print(my_list.index(444))
# print(my_list.count(444))
# print(my_list.reverse())
# # my_list.append(4)
# # my_list.append(4)
# print(my_list.copy())
# print(my_list.size())
# print(my_list)
# my_list.add_first(123)
# print(my_list.dictionize())
# print(my_list.index("Homegrown"))
# print(my_list.move(5))
# print(my_list.sum())
# print(my_list.overbound())
# print(my_list.underbound())