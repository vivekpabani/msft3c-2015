#!/usr/bin/env python


__author__ = 'vivek'

import operator
from collections import defaultdict


def main():
    
    sentinel = ""
    attribute_data = list()
    
    for line in iter(raw_input, sentinel):
        attribute_data.append(line.split(','))
    
    temp_list = list()
    temp_dict = defaultdict(lambda: 0)

for item in attribute_data:
    temp_list.append(item[:-1])
        key = (item[0], item[1])
        if temp_dict[key] == "true":
            pass
    else:
        temp_dict[key] = item[-1]

temp_list = dict((x[0], x) for x in temp_list).values()
    attribute_data = sorted(temp_list, key=operator.itemgetter(3, 4, 1))
    
    levels = list()
    for item in attribute_data:
        if int(item[3]) == 0:
            if len(levels) <= 1:
                levels.append(1)
            else:
                new_level = levels[0] + 1
                levels = list(new_level)
        else:
            if len(levels) <= int(item[3]):
                levels.append(1)
            elif levels[int(item[3])] == 0:
                levels[int(item[3])] = 1
            else:
                levels[int(item[3])] += 1
                k = int(item[3])+1
                while k < len(levels):
                    levels[k] = 0
                    k += 1
        i = 0
        level_str = ""
        while len(levels) > i and levels[i] > 0:
            if len(level_str) != 0:
                level_str += '.'
            level_str += str(levels[i])
            i += 1
        
        if temp_dict[(item[0], item[1])] == "false":
            status_str = "(in progress)"
        elif temp_dict[(item[0], item[1])] == "true":
            status_str = "(done)"
        else:
            pass
    
        answer_str = level_str + " " + item[2] + " " + status_str

    print(answer_str)


if __name__ == '__main__':
    main()


