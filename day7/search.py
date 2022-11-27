# binary search
# lst = [23,4,76,87,8,93,569,7]

# O(1)
# O(n)
word_list = []

with open('british-english', 'r') as file:
    file = file.readlines()
    for word in file:
        word_list.append(word.strip("\n"))

pos = 0


def search(lst, item):
    lower = 0
    upper = len(lst) - 1


    while lower <= upper:
        # floor of lower and upper bounds divided by 2 is the middle position
        mid = (lower + upper) // 2
        # if list[mid] is our number return true
        if lst[mid] == item:
            globals()['pos'] = mid
            return True
        # otherwise keep searching
        else:
            if lst[mid] < item:
                lower = mid
            else:
                upper = mid


item = "Agrippa"


if __name__ == "__main__":
    print(search(word_list, item))
    print(pos)
