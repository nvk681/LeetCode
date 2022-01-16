def convert(s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lenght_of_string = len(s)
        new_list = [[None for x in range(lenght_of_string)] for y in range(numRows)] 
        # new_list = [[None]*lenght_of_string]*numRows
        index_row, index_col = 0,0
        down = True
        for i in range(len(s)):
            if down:
                new_list[index_row][index_col] = s[i]
                index_row += 1
                if index_row == numRows:
                    index_row -= 2
                    index_col += 1
                    down = False
                    continue
            if not down:
                new_list[index_row][index_col] = s[i]
                index_col += 1
                index_row -= 1
                if index_row == 0 and numRows != 2:
                    down = True
                if index_row == -1 and numRows == 2:
                    down = True
                    index_row = 0
        print("Hello")
convert("ABCDF",2)
# convert("PAYPALISHIRING",3)