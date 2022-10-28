"""11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the
tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]"""


def quicksort(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        pivot = my_list.pop()
        element = pivot[1][2]
        lower_list = []
        greater_list = []

    for my_tuple in my_list:
        if my_tuple[1][2] > element:
            greater_list.append(my_tuple)
        else:
            lower_list.append(my_tuple)

    return quicksort(lower_list) + [pivot] + quicksort(greater_list)


def main():

    my_list = [('abc', 'bcd'), ('abc', 'zza'), ('abc', 'zzb'), ('abc', 'zze'), ('abc', 'zzc'), ('abc', 'zzf')]
    sorted_list = quicksort(my_list)
    print(sorted_list)


if __name__ == "__main__":
    main()
