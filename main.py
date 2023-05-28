from sys import argv

file = argv[1]#remove//rename

def delete():
    f = open(file, "a")
    f.truncate(0)
    f.close()
def Prim(matrix, size):
    no_edge = 0
    anser = []
    visit = [False for i in range(size)]
    visit[0] = True
    while(no_edge < size - 1):
        minn = 999999999
        x = 0
        y = 0
        for i in range(size):
            if(visit[i] == True):
                for j in range(size):
                    if(visit[j] == False and matrix[i][j]):
                        if (minn > matrix[i][j]):
                            minn = matrix[i][j]
                            x = i
                            y = j
        anser.append([x,y,minn])
        visit[y] = True
        no_edge += 1
    return anser
                        
with open(file, "r+") as f:
    size = int(f.readline())
    matrix = []
    for i in range(size):
        line = (f.readline()).split()
        line = [int(i) for i in line]
        matrix.append(line)
    pos = f.readlines()
    ans = Prim(matrix, size)
    print(ans)
    delete()
with open(file, "w") as f:
    f.write(str(size) + "\n")
    matrix = [[0 for j in range(size)] for i in range(size)]
    for i in range(len(ans)):
        matrix[ans[i][0]][ans[i][1]] = ans[i][2]
        matrix[ans[i][1]][ans[i][0]] = ans[i][2]
    for i in range(size):
        line = [str(matrix[i][j]) for j in range(size)]
        s = " ".join(line)
        f.write(s + "\n")
    s = ""
    res = 0
    for i in range(len(ans)):
        res+= ans[i][2]
        s += f"{i+1}. {ans[i][0]} - {ans[i][1]}: {ans[i][2]}\n"
    s +="Sum: " + str(res) + "\n"
    f.write("".join(pos))
    f.write("<Text>\n"+ s)
