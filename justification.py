def fullJustify(words, maxWidth: int):
        current_leght = 0
        current_list = []
        all_lines = []
        while len(words) > 0:
            if current_leght+len(words[0]) < maxWidth:
                current_leght += len(words[0])
                current_list.append(words.pop(0))
            else:
                string = ""
                total_lenght = len(string.join(current_list))
                spaces_required = maxWidth - total_lenght
                one_set_of_space = spaces_required//len(current_list)
                extra = spaces_required%len(current_list)
                current_line = []
                while len(current_list) > 0:
                    current_line.append(current_list.pop(0)+(" "*(one_set_of_space+extra)))
                    extra = 0
                all_lines.append(string.join(current_line))
                current_list.clear()
                current_leght = 0
        if len(current_list) > 0:
            string = ""
            total_lenght = len(string.join(current_list))
            spaces_required = maxWidth - total_lenght
            one_set_of_space = spaces_required//len(current_list)
            extra = spaces_required%len(current_list)
            current_line = []
            spaces_added = len(current_list)
            while len(current_list) > 0:
                current_line.append(current_list.pop(0)+" ")
            current_line.append(" "*(spaces_required-spaces_added))
            all_lines.append(string.join(current_line))
            current_list.clear()
            current_leght = 0
        return all_lines

fullJustify(["What","must","be","acknowledgment","shall","be"], 16)