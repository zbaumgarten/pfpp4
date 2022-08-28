def max_num(one, two, three):
    return max([one, two, three])

# print(max_num(45, 34, 58))

def multi_list(list):
    if len(list) == 0:
        return 0
    product = list[0]

    if len(list) > 1:
        for item in list[1:]:
            product = product * item
    return product

# print(multi_list([4, 8, 9]))

def rev_string(string):
    return string[::-1]

# print(rev_string("I have a banana"))

def num_within(one, two, three):
    return one in range(two, three + 1)

# print(num_within(3, 2, 4))

triangle = [[1], [1, 1]]
def pascal(number):
    if number < 1:
        print("number must be one or greater")
    elif number == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < number:
            row = []
            prev_row = triangle[row_number - 1]
            length = len(prev_row) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_number - 1][i - 1] + triangle[row_number - 1][i])
                else:
                    row.append(1)
        triangle.append(row)
        row_number += 1

    for row in triangle:
        print(row)


pascal(5)
            