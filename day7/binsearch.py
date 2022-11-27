bin_list = [2, 53, 75, 3, 23, 64, 76, 8544, 78, 14, 46]
word_list = []
with open("british-english", "r") as file:
    words = file.readlines()
    for word in words:
        word_list.append(word.strip("\n"))
    # print(words)
# print(word_list)
# new_list = sorted(bin_list)
# print(new_list)
pos = -1


def search(lst, n):
    # set initial position for lower and upper bounds
    lower = 0
    upper = len(lst) - 1

    while lower <= upper:
        # floor of lower and upper bounds divided by 2 is the middle position
        mid = (lower + upper) // 2
        # if list[mid] is our number return true
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        # otherwise keep searching
        else:
            if lst[mid] < n:
                lower = mid
            else:
                upper = mid


print(search(word_list, 'zebra'))
print(pos)
