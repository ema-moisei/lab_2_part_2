"""12. Write a function that will receive a list of words  as parameter and will return a list of lists of words,
grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
Example:
group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'],
['arme']] """


def group_by_rhyme(words):
    rhyme_list = []
    last_letters = []
    for word in words:
        if word[-2:] not in last_letters:
            last_letters.append(word[-2:])
            rhyme_list.append([word])
        else:
            for group in rhyme_list:
                if word[-2:] == group[0][-2:]:
                    group.append(word)
    return rhyme_list


def main():

    words = ['ana', 'banana', 'carte', 'arme', 'parte']
    rhyme_list = group_by_rhyme(words)
    print(rhyme_list)


if __name__ == "__main__":
    main()
