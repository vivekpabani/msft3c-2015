#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'
import operator
from collections import defaultdict


def main():

    sentinel = ''
    paging_data = list()

    for line in iter(raw_input, sentinel):
        paging_data.append(line)

    for item in paging_data:

        line = item.split(',')
        current = int(line[0])
        rolling = int(line[2])
        last = int(line[1])
        first = 1

        answer = list()

        for i in range(0, last):
            answer.append('.')

        if last < current or last < 0 or current < 0:
            print 'ERR',
        else:
            answer[0] = first
            answer[current - 1] = current
            answer[last-1] = last

            for i in range(rolling):
                if current + i < len(answer):
                    answer[current + i] = current + i + 1
                if(current - i - 2) >= 0:
                    answer[current - i - 2] = current - i - 1

            i = 0

            while i < len(answer):
                if answer[i] != '.':
                    print(answer[i]),
                    i += 1
                else:
                    print("..."),
                    while i < len(answer) and answer[i] == ".":
                        i += 1

        print("")

if __name__ == '__main__':
    main()

