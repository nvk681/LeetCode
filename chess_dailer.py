'''We are interested in getting 7 digit phone number by watching a chess piece (rook) traverse a board with numbers on each board position.

Given a 3 by 3 board that looks like this.

1 2 3
4 5 6
7 8 9

'''
dailer_map = {
    '1' : ['2','4'],
    '2' : ['1', '3', '5'],
    '3' : ['2', '6'],
    '4' : ['1', '5', '7'],
    '5' : ['4', '2', '6', '8'],
    '6' : ['5', '3', '9'],
    '7' : ['4', '8'],
    '8' : ['7', '5', '9'],
    '9' : ['8', '6']
}

def make_my_number(num):
    list_of_numbers = []
    def make_one(current):
        if len(current) == 7:
            list_of_numbers.append("".join(current))
            return
        for i in dailer_map[current[-1]]:
            current.append(i)
            make_one(current)
            current.pop()
    temp = list(num)
    make_one(temp)
    return list_of_numbers

for i in make_my_number('4'):
    print(i)