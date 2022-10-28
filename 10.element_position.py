"""10. Write a function that receives a variable number of lists and returns a list of tuples as follows: the first
tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists, etc.
Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].

Note: If input lists do not have the same number of items, missing items will be replaced with None to be able to
generate max ([len(x) for x in input_lists]) tuples."""


def position(*lists):
    final_list = []
    max_val = 0
    for list in lists:
        if len(list) > max_val:
            max_val = len(list)
    temp_list = [() for i in range(max_val)]

    for index, my_tuple in enumerate(temp_list):
        for el_list in lists:
            if index + 1 <= len(el_list):
                temp = (el_list[index],)
                my_tuple += temp
            else:
                my_tuple += (None,)
        final_list.append(my_tuple)

    return final_list


def main():
    list0 = []
    list1 = [1, 2, 3]
    list2 = [5, 6, 7, 8]
    list3 = ["a", "b", "c"]
    list4 = []
    pos = position(list0, list1, list2, list3, list4)
    print(pos)


if __name__ == "__main__":
    main()
