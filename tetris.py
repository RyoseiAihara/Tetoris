import random

field = [[0 for i in range(12)] for j in range(21)]
for i in range(21):
    field[i][0] = 1
    field[i][11] = 1
for i in range(11):
    field[20][i] = 1
#for i in range(20):
   # print(field[i])
point = [0,3]
block_L1 = [[]]
block_L2 = [[]]
block_L3 = [[]]
block_L4 = [[]]
block_L5 = [[]]
block_L6 = [[]]
block_L7 = [[]]
block_field = [[0 for i in range(4)] for j in range(4)]
block_L1[0] = [(2, 2, 2, 0), (2, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
block_L1.append([(2, 2, 0, 0), (0, 2, 0, 0), (0, 2, 0, 0), (0, 0, 0, 0)])
block_L1.append([(0, 0, 2, 0), (2, 2, 2, 0), (0, 0, 0, 0), (0, 0, 0, 0)])
block_L1.append([(2, 0, 0, 0), (2, 0, 0, 0), (2, 2, 0, 0), (0, 0, 0, 0)])
block_L2[0] = [(2, 2, 2, 0), (0, 0, 2, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
block_L2.append([(0, 2, 0, 0), (0, 2, 0, 0), (0, 2, 0, 0), (0, 0, 0, 0)])
block_L2.append([(2, 0, 0, 0), (2, 0, 0, 0), (2, 2, 0, 0), (0, 0, 0, 0)])
block_L2.append([(2, 2, 2, 0), (0, 0, 0, 0), (0, 2, 0, 0), (0, 0, 0, 0)])
block_L3[0] = [(2, 2, 2, 0), (0, 2, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
block_L3.append([(0, 2, 0, 0), (2, 2, 0, 0), (0, 2, 0, 0), (0, 0, 0, 0)])
block_L3.append([(0, 0, 0, 0), (0, 2, 0, 0), (2, 2, 2, 0), (0, 0, 0, 0)])
block_L3.append([(0, 0, 2, 0), (0, 2, 2, 0), (0, 0, 2, 0), (0, 0, 0, 0)])
block_L4[0] = [(2, 0, 0, 0), (2, 2, 0, 0), (0, 2, 0, 0), (0, 0, 0, 0)]
block_L4.append([(0,2, 2, 0),(2, 2, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)])
block_L5[0] = [(0, 2, 0, 0), (2, 2, 0, 0), (2, 0, 0, 0), (0, 0, 0, 0)]
block_L5.append([(2, 2, 0, 0), (0, 2, 2, 0), (0, 0, 0, 0), (0, 0, 0, 0)])
block_L6[0] = [(2, 0, 0, 0), (2, 0, 0, 0), (2, 0, 0, 0), (2, 0, 0, 0)]
block_L6.append([(0, 0, 0, 0), (2, 2, 2, 2), (0, 0, 0, 0), (0, 0, 0, 0)])
block_L7[0] = [(2, 2, 0, 0), (2, 2, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]


def rotate_block(block, next_block):
    counter = 0
    for i in range(4):
        for j in range(4):
            if (next_block[i][j] == 2):
                if (field[point[0]+i][point[1]+j] != 1):
                    counter = counter + 1

    if (counter == 4):
        print ('rotate')
        for i in range(4):
            for j in range(4):
                if(block[i][j] == 2):
                    field[point[0]+i][point[1]+j] = 0
        for i in range(4):
            for j in range(4):
                if(next_block[i][j]==2):
                    field[point[0]+i][point[1]+j] = 2


def rise_bottom(ba):
    j = random.randint(3, 5)
    new_line = [0 for n in range(12)]
    new_line[0] = 1
    new_line[11] = 1
    for k in range(j):
        i = random.randint(0, 9)
        if (0 < i < 11):
            new_line[i] = 1
    del ba[0]
    ba.insert(19,new_line)

def fall_block(block):
    counter = 0
    for i in range(4):
        for j in range(4):
            if(block[i][j] == 2):
                if(field[point[0]+i][point[1]+j+1] != 1):
                    counter = counter + 1
    if(counter == 4):
        apply_field(block,'fall')
        point[0] += 1
        return 1
    printf('error')
    return 0

def next_block():
    i = random.randint(1,7)
    return block_L + str(i)

def apply_field(block,char):
    param = (0,0)
    if(char == 'fall'):
        print('fall')
        param = (1,0)
    if(char == 'first'):
        print('first')
        param = (0,0)
    for i in (3,2,1,0):
        for j in (3,2,1,0):
            if(block[i][j] == 2):
                field[point[0]+i+param[0]][point[1]+j+param[1]] = block[i][j]
                if (char != 'first'):
                    field[point[0]+i][point[1]+j] = 0
               # print_field()
               # print ()

def print_field():
    for i in range(21):
        print(field[i])

def delete_line():
    for i in range(12):
        if(field[i] == [1,1,1,1,1,1,1,1,1,1,1,1]):
            del field[i]

def put_block(block):
    for i in range(4):
        for j in range(4):
            if(block[i][j] == 2):
                field[point[0]+i][point[1]+j] = 1

def search_point(block):
    for m in range(-2,8):
        for n in range(20):
            for i in range(4):
                for j in range(4):
                    if(block[i][j]==2):
                        print(point[0]+i+1+n,point[1]+j+m)
                        if(field[point[0]+i+1+n][point[1]+j+m] == 1):
                            #print('///')
                            print(point[0]+n,point[1]+m)
                            print()
        break

for i in range(5):
    rise_bottom(field)

apply_field(block_L1[0],'first')
#nall_block(block_L1[0])
print_field()
search_point(block_L1[0])
#rotate_block(block_L1[0],block_L1[1])






