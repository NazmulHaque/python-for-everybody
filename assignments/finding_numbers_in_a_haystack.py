x = '''
Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative
7 and rewarding activity.  You can write programs for
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that
everyone needs to know how to program ...
'''

import re

full_text = open('regex_sum_269164.txt').read()

numbers = [int(num) for num in re.findall('[0-9]+', full_text)]

print 'There are {} numbers and the sum of the numbers is {}'.format(str(len(numbers)), str(sum(numbers)))
