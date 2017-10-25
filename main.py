#add apenas os valores de x's e const

m = [[-4,-5,-9,-11,0],
     [1,1,1,1,15],
     [7,5,3,2,120],
     [3,5,10,15,100]]

"""
m = [[2,-4,0],
     [-1,2,2],
     [1,1,7]]



m = [[-5,-4,-3,0],
     [2,3,1,5],
     [4,2,2,11],
     [3,2,2,8]]

m = [[-5,-2,0],
     [1,0,3],
     [0,1,4],
     [1,2,9]]

m = [[-1,-2,0],
     [-1,3,6],
     [1,-1,2]]
"""


size = len(m)

l = [0]
j = len(m[0])


for i in range(len(m)):
    l.append(j)
    j += 1


imatrix = lambda n: [[1 if j == i else 0 for j in range(1,n)] for i in range(n)]


def legenda():
    print("      Z   ",end= "")
    for i in range(len(matriz[0])-2):
        print("    X%d  " %(i+1), end="")
    print("    C")

def printMatriz(matriz,contTable,idIn,idOut):

    l[idOut] = idIn
     
    line = len(matriz)
    column = len(matriz[0])
    print("\nTable: %d"%contTable)
    legenda()
    for i in range(line):
        if (i==0):
            print("Z " ,end="  ")
        else:
            print("X%d" %l[i], end="  ")
        for j in range(column):
            if(matriz[i][j]<0):
                print("%.3f" % matriz[i][j],end="  ")
            elif(matriz[i][j]<=10):
                print("%.4f" % matriz[i][j],end="  ")
            elif(matriz[i][j]<=100):
                print("%.3f" % matriz[i][j],end="  ")
            elif(matriz[i][j]>=100):
                print("%.3f" % matriz[i][j],end="  ")
        print()
    
def MatrizF(size):

    matrizAux = imatrix(size)

    #cria matriz identidade
    for i in range(size):
        if(i==0):
            aux = m[i].pop(-1)
            print(aux)
            m[i].insert(0,1)
            m[i] += matrizAux[i]
            m[i].append(aux)
        else:
            aux = m[i].pop(-1)
            m[i].insert(0,0)
            m[i] += matrizAux[i]
            m[i].append(aux)
            
    return(m)


def Pivo():

    matriz = m
    small = -1
    contTable = 1

    printMatriz(matriz,contTable,0,0)

    while(small<0):

        small = 0
        idPivo = 0
        linePivo = 0
        columnPivo = 1000000
        
        #pega o menor valor        
        for i in range(len(matriz[0])):
            if (matriz[0][i]<small and matriz[0][i] != small):
                idPivo = i
                small = matriz[0][i]

        #escolhe o pivo
        for i in range(len(matriz)):
            
            if(matriz[i][idPivo]==0):
               continue
            elif(matriz[i][-1]/matriz[i][idPivo] > 0 and matriz[i][-1]/matriz[i][idPivo] < columnPivo):
                linePivo = i
                columnPivo = matriz[i][-1]/matriz[i][idPivo]

        #arruma a linha do pivo e atualiza caso seja diferente de 1
        if (matriz[linePivo][idPivo] != 1):
            divisorPivo = matriz[linePivo][idPivo]
            
            for i in range(len(matriz[linePivo])):
                matriz[linePivo][i] /= divisorPivo
                
        mAux = matriz

        #arrumar restante das linhas
        for i in range(len(matriz)):
            
            if(i == linePivo):
                    continue
            else:
                multAux = matriz[i][idPivo]
                for j in range(len(matriz[i])):
                    matriz[i][j] = mAux[i][j] - (multAux * mAux[linePivo][j])

        if(small != 0):
            contTable += 1 
            printMatriz(matriz,contTable,idPivo,linePivo)


matriz = MatrizF(size)
Pivo()
exit = input()

