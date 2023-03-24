import sys

str1=['']+list(input())
str2=['']+list(input())

# print(str1)
# print(str2)

graph=[[0 for _ in range(len(str1))] for _ in range(len(str2))]

# for i in graph:
#     print(i)

for col in range(1, len(str1)):
    for row in range(1, len(str2)):
        if str1[col]==str2[row]:
            graph[row][col]=graph[row-1][col-1]+1
        elif str1[col]!=str2[row]:
            if graph[row-1][col]>=graph[row][col-1]:
                graph[row][col]=graph[row-1][col]
            elif graph[row-1][col]<graph[row][col-1]:
                graph[row][col]=graph[row][col-1]


# for i in graph:
#     print(i)

print(graph[len(str2)-1][len(str1)-1])