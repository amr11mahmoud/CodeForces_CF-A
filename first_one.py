# first_line,second_line = input().split()
# first_line = int(first_line)
# second_line = int(second_line)
#
# i_height = input().split()
#
# normal_width = 1
# bit_width = 2
#
# min_width_of_the_road = 0
#
# for i in i_height:
#     if int(i) > second_line:
#         min_width_of_the_road += 2
#     elif int(i) <= second_line:
#         min_width_of_the_road += 1
#
# print(min_width_of_the_road)

# first_line=input()
# second_line = input()
# Anton_win = second_line.count('A')
# Danik_win = second_line.count('D')
#
# if Anton_win > Danik_win:
#     print("Anton")
# elif Anton_win < Danik_win:
#     print("Danik")
# else:
#     print("Friendship")


# limak,bob = input().split()
# limak = int(limak)
# bob = int(bob)
# i = 0
#
# while limak <= bob:
#     limak = limak*3
#     bob = bob*2
#     i += 1
#     # if limak > bob:
#     #     break
#
# print(i)


# first_line = int(input())
#
# max_num = 0
# for i in range(first_line):
#    t = input().split()
#    if (int(t[0])+int(t[1])+int(t[2])) >=2:
#        max_num +=1
#
# print(max_num)


# first_line = input().split()
# second_line = input().split()
# third_line = input().split()
# fourth_line = input().split()
# fifth_line = input().split()
# matrix = [first_line, second_line, third_line, fourth_line, fifth_line]
# max_moves = 0
# for i in range(0, 5):
#     if "1" in matrix[i]:
#         found = matrix[i].index("1")
#         while (found != 2):
#             if found > 2:
#                 found -= 1
#                 max_moves += 1
#             else:
#                 found += 1
#                 max_moves += 1
#         while (i != 2):
#             if i > 2:
#                 i -= 1
#                 max_moves += 1
#             else:
#                 i += 1
#                 max_moves += 1
# print(max_moves)


# n = int(input())
# s = input().split()
# s = list(map(int, s))
# Sereja = 0
# Dima = 0
# i = 0
#
# while (len(s)-1 >=0):
#     if (i %2 == 0):
#         m = max(s[0],s[len(s)-1])
#         s.remove(m)
#         Sereja +=m
#         i+=1
#
#     else:
#         m = max(s[0],s[len(s)-1])
#         s.remove(m)
#         Dima +=m
#         i+=1
#
# print(Sereja)
# print(Dima)


# n = int(input())
# s = input().split()
# s = list(map(int, s))
#
# crimes = 0
# officers = 0
#
# for i in s :
#     if i > 0:
#         officers += i
#     if ( i <0 ) and(officers<=0):
#         crimes += 1
#     elif ( i <0 ) and( officers>0 ):
#         officers -=1
#
# print(crimes)

# calories = 0
# a1,a2,a3,a4 = input().split()
# a1 = int(a1)
# a2 = int(a2)
# a3 = int(a3)
# a4 = int(a4)
# s = input()
# for i in s :
#     if i == "1":
#         calories +=a1
#     elif i == "2" :
#         calories += a2
#     elif i == "3" :
#         calories += a3
#     else:
#         calories += a4
# print(calories)

import string

chars = string.ascii_lowercase
word = input()
list_of_chars = []
max_moves = 0
initial_pos = 0
found = 0
next_char = 0

for i in word:
    list_of_chars.append(i)

for i in list_of_chars:
    found = abs(chars.find(i) - initial_pos)
    if 26 - found >= found:
        found = found
        initial_pos = found
        max_moves += found
        print(chars[found])
    else:
        found = 26 - found
        initial_pos = found
        max_moves += found
        print(chars[found])

print(max_moves)