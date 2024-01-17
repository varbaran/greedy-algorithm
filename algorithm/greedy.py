# from operator import itemgetter

# def sort_tuples(w):
#     return sorted(w , key=itemgetter(1))

works = [(9,10),(8,13),(9,12),(12,13),(12,14)]
works.sort(key=lambda x: x[1])
# soon_end = sort_tuples(works)
print(works)
selected = []
selected.append(works[0])
for j in range (1,len(works)):
    if works[j][0] >= selected[-1][1]:
        selected.append(works[j])
print(selected)

# lambda input:output, میتونه هر چیزی باشهو لیست و تاپل
# f = lambda x: [x[3], "hello"]
# print(f(works))
# works.sort(key=lambda x: (x[1] , x[0]))
# print(works)

# def MaxActivities(arr, n):
#     selected = []
#
#     # Sort jobs according to finish time
#     activity.sort(key=lambda x: x[1])
#
#     # The first activity always gets selected
#     i = 0
#     selected.append(arr[i])
#
#     for j in range(1, n):
#
#         '''If this activity has start time greater than or
#            equal to the finish time of previously selected
#            activity, then select it'''
#         if arr[j][0] >= arr[i][1]:
#             selected.append(arr[j])
#             i = j
#     return selected
#
#
# activity = [[11,13],[9,10],[11,12],[12,13],[12,14],[13,14]]
# n = len(activity)
# selected = MaxActivities(activity, n)
# print(selected)
#
