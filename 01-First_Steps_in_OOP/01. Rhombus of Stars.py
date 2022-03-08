#n = 3

'''
  *   # spaces: n-1, stars: 1
 * *  # spaces: n-2, stars: 2
* * * # spaces: 0, stars: 3 (n)
 * *
  *
'''


def print_line(spaces_count, stars_count):
    line_spaces = ''.join([' '] * spaces_count)
    line_stars = ' '.join(['*'] * stars_count)
    print(line_spaces + line_stars)


def print_rhombus(n):
    for i in range(n):
        spaces = n - i - 1
        stars = i + 1
        print_line(spaces, stars)

    for i in range(n-2, -1, -1):
        spaces = n - i - 1
        stars = i + 1
        print_line(spaces, stars)


n = int(input())
print_rhombus(n)