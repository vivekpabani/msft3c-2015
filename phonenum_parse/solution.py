#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'


def main():

    sentinel = ''
    number_data = list()

    for line in iter(raw_input, sentinel):
        number_data.append(line)

    dialing_pad = dict.fromkeys(['a', 'b', 'c', 'A', 'B', 'C'], '2')
    dialing_pad.update(dict.fromkeys(['d', 'e', 'f', 'D', 'E', 'F'], '3'))
    dialing_pad.update(dict.fromkeys(['g', 'h', 'i', 'G', 'H', 'I'], '4'))
    dialing_pad.update(dict.fromkeys(['j', 'k', 'l', 'J', 'K', 'L'], '5'))
    dialing_pad.update(dict.fromkeys(['m', 'n', 'o', 'M', 'N', 'O'], '6'))
    dialing_pad.update(dict.fromkeys(['p', 'q', 'r', 's', 'P', 'Q', 'R', 'S'], '7'))
    dialing_pad.update(dict.fromkeys(['t', 'u', 'v', 'T', 'U', 'V'], '8'))
    dialing_pad.update(dict.fromkeys(['w', 'x', 'y', 'z', 'W', 'X', 'Y', 'Z'], '9'))

    for line in number_data:
        answer_str = ""
        number_count = 0
        index_count = 0
        while index_count < len(line):
            if number_count < 4:
                if str.isdigit(line[index_count]):
                    answer_str += line[index_count]
                    number_count += 1
            else:
                if str.isdigit(line[index_count]):
                    answer_str += line[index_count]
                    number_count += 1
                elif str.isalpha(line[index_count]):
                    answer_str += dialing_pad[line[index_count]]
                    number_count += 1

            index_count += 1

        if number_count == 10:
            final_answer = '+1' + answer_str
        elif number_count == 11:
            final_answer = '+' + answer_str
        else:
            final_answer = "Fleshling follow-up needed"

        print(final_answer)

if __name__ == '__main__':
    main()
