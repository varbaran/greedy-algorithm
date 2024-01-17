def swap_count(a):
    swap = 0
    count = 0
    for i in range(len(a)):
        if a[i] == "[":
            count += 1
        else:
            count -= 1
        if count < 0:
            for j in range(i + 1, len(a)):
                if a[j] == "[":
                    swap += j - i
                    a.insert( i , a[j])
                    a.pop(j + 1)
                    count = 1
                    break


    return swap, a


a = "[][][][][]]["
print(swap_count(list(a)))


# def swapCount(s):
#     # Keep track of '['
#     pos = []
#
#     for i in range(len(s)):
#         if (s[i] == '['):
#             pos.append(i)
#
#     # To count number
#     # of encountered '['
#     count = 0
#
#     # To track position
#     # of next '[' in pos
#     p = 0
#
#     # To store result
#     sum = 0
#     s = list(s)
#
#     for i in range(len(s)):
#
#         # Increment count and
#         # move p to next position
#         if (s[i] == '['):
#             count += 1
#             p += 1
#         elif (s[i] == ']'):
#             count -= 1
#
#         # We have encountered an
#         # unbalanced part of string
#         if (count < 0):
#             # Increment sum by number
#             # of swaps required
#             # i.e. position of next
#             # '[' - current position
#             sum += pos[p] - i
#             s[i], s[pos[p]] = (s[pos[p]],
#                                s[i])
#             p += 1
#
#             # Reset count to 1
#             count = 1
#     return sum
#
#
# # Driver code
s = "[]][]["
print(swap_count(list(s)))

s = "[[][]]"
print(swap_count(list(s)))

s = "[]"
print(swap_count(list(s)))

s = "]["
print(swap_count(list(s)))

s = "][][[][]]["
print(swap_count(list(s)))