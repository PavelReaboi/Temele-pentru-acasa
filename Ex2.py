x = [[5,13,19,6,-10], 
    [41,0,17,21,8], 
    [-33,32,39,26,18], 
    [19,-40,11,22,31], 
    [16,20,-38,8,7]]
print('Suma primului rand este', sum(x[0]))
print('Suma randului al doilea este', sum(x[1]))
print('Suma randului al treile este', sum(x[2]))
print('Suma randulului al patrulea este', sum(x[3]))
print('Suma randului al cincelea este', sum(x[4]))
col1=0
col2=0
col3=0
col4=0
col5=0
for i in x:
    col1+=i[0]
    col2+=i[1]
    col3+=i[2]
    col4+=i[3]
    col5+=i[4]
print('Suma primei coloane este', col1)
print('Suma coloanei a doua este', col2)
print('Suma coloanei a treia este', col3)
print('Suma coloanei a patra este', col4)
print('Suma coloanei a cincea este', col5)
diprin = x[0][0]+x[1][1]+x[2][2]+x[3][3]+x[4][4]
disec = x[0][4]+x[1][3]+x[2][2]+x[3][1]+x[4][0]
print('Suma diagonalei principale este', diprin)
print('Suma diagonalei secundare este', disec)