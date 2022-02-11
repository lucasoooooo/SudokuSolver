#back track and generate new numbers
def genNumber(graph):
    l = [0,0]
    if not foundEmpty(graph, l):
        return True
    #unwrap new empty location
    i,j = l[0], l[1] 
    #number picker 1-9
    for num in range(1,10):
        if numWorks(graph, num, i, j):
            graph[i][j] = num
            if genNumber(graph):
                return True
            graph[i][j] = 0
    return False

def foundEmpty(graph, arr):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                arr[0] = i
                arr[1] = j
                return True
    return False

def numWorks(graph, num, row, column):
    #check horizontal
    checker = set()
    checker.add(num)
    for j in range(len(graph)):
        if graph[row][j] in checker:
            return False
        if graph[row][j] != 0:
            checker.add(graph[row][j])
    

    #checks vertical
    checker = set()
    checker.add(num)
    for i in range(len(graph)):
        if graph[i][column] in checker:
            return False
        if graph[i][column] != 0:
            checker.add(graph[i][column])

    #check box
    checker = set()
    checker.add(num)
    for i in range(len(graph)//3):
        for j in range(len(graph)//3):
            if graph[i + (row-row%3)][j + (column-column%3)] in checker:
                return False
            if graph[i + (row-row%3)][j + (column-column%3)] != 0:
                checker.add(graph[i + (row-row%3)][j + (column-column%3)])
    return True

#Check if solution could work
def isNotBroken(graph):
    #Check if number match horizontally
    for i in range(len(graph)):
        horizontal = set()
        for j in range(len(graph[i])):
            if graph[i][j] in horizontal:
                return False
            if graph[i][j] != 0:
                horizontal.add(graph[i][j])
    #Check if number match vertically
    for i in range(len(graph)):
        vertical = set()
        for j in range(len(graph[i])):
            if graph[j][i] in vertical:
                return False
            if graph[j][i] != 0:
                vertical.add(graph[j][i])
    #Check if number match in 3x3 box
    for l in range(len(graph)//3):
        for k in range(len(graph)//3):
            box = set()
            for i in range(len(graph)//3):
                
                for j in range(len(graph[i])//3):
                    if graph[i+3*k][j+3*l] in box:
                        return False
                    if graph[i+3*k][j+3*l] != 0:
                        box.add(graph[i+3*k][j+3*l])
    return True
def printGraph(graph):
    for i in range(len(graph)):
        if i%3 == 0:
            print(" ________________________")
        for j in range(len(graph[i])):
            if j%3 == 0 :
                print(f' | {graph[i][j]}', end="")
            else:
                print(f' {graph[i][j]}', end="")
            if j==len(graph)-1:
                print("|")
    print(" ________________________")
        
#Testing section
    #works
graph1 =[[4,3,5,2,6,9,7,8,1],
         [6,8,2,5,7,1,4,9,3],
         [1,9,7,8,3,4,5,6,2],
         [8,2,6,1,9,5,3,4,7],
         [3,7,4,6,8,2,9,1,5],
         [9,5,1,7,4,3,6,2,8],
         [5,1,9,3,2,6,8,7,4],
         [2,4,8,9,5,7,1,3,6],
         [7,6,3,4,1,8,2,5,9]   
        ]
    #doesnt work
graph2 =[[9,1,2,3,4,5,6,7,8],
         [9,1,2,3,4,5,6,7,8],
         [9,1,2,3,4,5,6,7,8],
         [9,1,2,3,4,5,6,7,8],
         [9,1,2,3,4,5,6,7,8],
         [9,1,2,3,4,5,6,7,8],
         [9,1,2,3,4,5,6,7,8],
         [9,1,2,3,4,5,6,7,8],
         [9,1,2,3,4,5,6,7,8],
        ]  
    #uncompleted
graph3 =[[0,0,0,2,6,0,7,0,1],
         [6,8,0,0,7,0,0,9,0],
         [1,9,0,0,0,4,5,0,0],
         [8,2,0,1,0,0,0,4,0],
         [0,0,4,6,0,2,9,0,0],
         [0,5,0,0,0,3,0,2,8],
         [0,0,9,3,0,0,0,7,4],
         [0,4,0,0,5,0,0,3,6],
         [7,0,3,0,1,8,0,0,0]
        ]
#Uncompleted
graph4 =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
		[5, 2, 0, 0, 0, 0, 0, 0, 0],
		[0, 8, 7, 0, 0, 0, 0, 3, 1],
		[0, 0, 3, 0, 1, 0, 0, 8, 0],
		[9, 0, 0, 8, 6, 3, 0, 0, 5],
		[0, 5, 0, 0, 9, 0, 6, 0, 0],
		[1, 3, 0, 0, 0, 0, 2, 5, 0],
		[0, 0, 0, 0, 0, 0, 0, 7, 4],
		[0, 0, 5, 2, 0, 6, 3, 0, 0]]

print(isNotBroken(graph1)) #should be True
print(isNotBroken(graph2)) # should be False
print(isNotBroken(graph3)) # should be True

if genNumber(graph3):
    printGraph(graph3)
else:
    print("Graph 4 DIDN'T WORK")

if genNumber(graph4):
    printGraph(graph4)
else:
    print("Graph 4 DIDN'T WORK")
