#!/usr/bin/env python

__author__ = 'vivek'


def main():
    num_str = int(raw_input())

    print(num_str)

    for k in xrange(num_str):
        str1 = raw_input()
        result = ""
        length = len(str1)

        i = 0

        while i < length:
            ch = str1[i]
            count = 0

            while i < length and str1[i] == ch:
                count += 1
                i += 1

            if count > 1:
                result += str(count)

            result = result + ch

        print(result)

if __name__ == '__main__':
    main()
