import csv

def lastWord(string):
   
    # taking empty string
    newstring = ""
     
    # calculating length of string
    length = len(string)
     
    # traversing from last
    for i in range(length-1, 0, -1):
       
        # if space is occurred then return
        if(string[i] == " "):
           
            # return reverse of newstring
            return newstring[::-1]
        else:
            newstring = newstring + string[i]
 








def q1a(val):
    with open(f"{val}.csv", 'r') as csv_team:
        csv_reader = csv.reader(csv_team)

        for line in csv_reader:
            print(",".join(line))

    # 1b
def q1b(p, c, ind):
    rows = []
    indexes = []

    with open(f"{p}.csv") as csv_player:
        csv_reader = csv.reader(csv_player)

        #fields = next(csv_reader)

        for row in csv_reader:
            rows.append(row)
        n = len(rows[0])
        ind = ind.replace("'", '')
        p = p.replace("'", '')

        index = 0
        for i in range(0, n):
            if rows[0][i] == f"{c}":
                index = i
        count = 0

        for i in range(0, len(rows)):
            if rows[i][index] == f"{ind}":
                indexes.append(i)


        c = 0

        new_list = [rows[i] for i in indexes]


        #print(new_list)
        for li in new_list:
            print(",".join(li))
    #    index = 0
    #   for i in range(0, len(L)-1):
    #       if L[i] == 'country_name':
    #           index = i

    #   print(index)



 #1c

def q1c(printCol, playerm, role, cap):
    rows = []
    indexes = []

    with open(f"{playerm}.csv") as csv_player:
        csv_reader = csv.reader(csv_player)

        #fields = next(csv_reader)

        for row in csv_reader:
            rows.append(row)


        n = len(rows[0])
        index = 0
        for i in range(0, n):
            if rows[0][i] == f"{role}":
                index = i
        count = 0
        if type(cap) == str:
            cap = cap.replace("'", '')
        for i in range(0, len(rows)):
            if rows[i][index] == f"{cap}":
                indexes.append(i)

        c = 0

        indexCol = []
        for i in range(0, len(printCol)):
            for j in range(0, len(rows[0])):
                if printCol[i] == rows[0][j]:
                    indexCol.append(j)


        new_list = [rows[i] for i in indexes]


        #print(new_list)

        for i in indexes:
            newstr = []
            for j in indexCol:
                newstr.append(rows[i][j])
            print(",".join(newstr))     
#        for li in new_list:
#            
#            print(",".join(li))
    #    index = 0
    #   for i in range(0, len(L)-1):
    #       if L[i] == 'country_name':
    #           index = i

    #   print(index)

# 2


####################################################################

def q2(r1, r2, c1, c2):
    rows = []
    indexes = []

    rows2 = []


    with open(f"{r1}.csv") as csv_match:
        with open(f"{r2}.csv") as csv_team:
            csv_reader = csv.reader(csv_match)
            csv_reader_2 = csv.reader(csv_team)
            #fields = next(csv_reader)

            #indexCol1, indexCol2

            index = 0

        

            indexCol = 0
            indexCol2 = 0

            for row in csv_reader:
                rows.append(row)
                

            for row in csv_reader_2:
                rows2.append(row)

            for i in range(0, len(rows[0])):
                if rows[0][i] == f"{c1}":
                    indexCol = i
            for i in range(0, len(rows2[0])):
                if rows[0][i] == f"{c2}":
                    indexCol2 = i

            for i in range(0, len(rows)):
                for j in range(0, len(rows2)):
                    if rows[i][indexCol] == rows2[j][indexCol2]:
                        new_list = [*rows[i], *rows2[j]]
                        print(','.join(new_list))

#3
#########################################
def q3(r, c, val):
    rows = []
    indexCol = 0
    count = 0
    if type == str:
        val = val.replace("'", '')
    
    with open(f"{r}.csv") as csv_match:
        csv_reader = csv.reader(csv_match)
        for row in csv_reader:
            rows.append(row)
        
        for i in range(0, len(rows[0])):
            if rows[0][i] == f"{c}":
                indexCol = i
        for i in range(0, len(rows)):
            if rows[i][indexCol] == f"{val}":
                count = count + 1

        print(count)

#4
##########################################
def q4(colx, column, relation):
    indexX = 0
    indexC = 0 
    ro = []

    runsX = []
    strik = []
    mylist = []

    filename = open(f"{relation}.csv", 'r')

    file = csv.DictReader(filename)
    for col in file:
        mylist.append(tuple((col[f"{colx}"], col[f"{column}"])))
        

    thisdict = {}

    ind = 0
    indexList = []



    sums = {}
    for a, b in mylist:
        if b not in sums: sums[b] = int(a)
        else: sums[b] += int(a)
    #print (list(sums.items()))

    
    for k,v in sorted(sums.items(),key=lambda x:(x[0],-x[1])): #ans
        print("{},{}".format(v,k))


#########################################
#5

def q5(cols, r, colX, value1, colY, value2):
    filename = open(f"{r}.csv")
    file = csv.DictReader(filename)

    if type(value1) == str:
        value1 = value1.replace("'", '')
    if type(value2) == str:
        value2 = value2.replace("'", '')




    mylist = []
    list2 = []
    Indexes = []
    countss = 0
    for col in file:
        if col[colX] == str(value1):
            if col[colY] == value2:
                
                Indexes.append(countss)
        countss = countss + 1

    rows = []
    with open(f"{r}.csv") as csv_player:
        csv_reader = csv.reader(csv_player)

        #fields = next(csv_reader)

        for row in csv_reader:
            rows.append(row)

        indexCol = []
        for i in range(0, len(cols)):
            for j in range(0, len(rows[0])):
                if cols[i] == rows[0][j]:
                    indexCol.append(j)


        for i in Indexes:
            newstr = []
            for j in indexCol:
                newstr.append(rows[i+1][j])
            print(",".join(newstr))

while 1:
    q = input("Query Type? ")
    if q == '0':
        break
    if q == 0:
        break
    q = q.strip()
    if q == '1a':
        sql = input()
        sql = sql.strip(";")
        sql = lastWord(sql)
        q1a(sql)
    if q == '1b':
        sql = input()
        sql = sql.strip(";")
        sql = sql.split()
        #print(sql[3], sql[5], sql[7])
        q1b(sql[3], sql[5], sql[7])
        
    if q == '1c':
        sql = input()
        sql = sql.strip(";")
        sql = sql.replace(',', ' ')
        sql = sql.split()
        fromi = 0
        for i in range(0, len(sql)):
            if sql[i] == 'from':
                fromi = i
        mylist = []
        for i in range(1, fromi):
            mylist.append(sql[i])

        q1c(mylist, sql[fromi+1], sql[fromi+3], sql[fromi+5])

        
    if q == '2':
        sql = input()
        sql = sql.strip(";")
        sql = sql.replace(',', ' ')
        sql = sql.replace(',', '')
        sql = sql.replace('.', ' ')
        sql = sql.split()
        fromi = 0
        #3 4 r1, r2
        #7 10 c1 c2
        q2(sql[3], sql[4], sql[7], sql[10])

    if q == '3':
        sql = input()
        sql = sql.strip(";")
        sql = sql.split()
        q3(sql[3], sql[5], sql[7])
        

    if q == '4':
        sql = input()
        sql = sql.strip(";")
        sql = sql.replace('(', ' ')
        sql = sql.replace(')', ' ')
        sql = sql.replace(',', ' ')
        sql = sql.split()
        q4(sql[2], sql[3], sql[5])

    if q == '5':
        sql = input()
        sql = sql.strip(";")
        fromi = 0
        sql = sql.replace(',', ' ')
        sql = sql.replace('(', ' ')
        sql = sql.replace(')', ' ')

        sql = sql.split()
        for i in range(0, len(sql)):
            if sql[i] == 'from':
                fromi = i
                break
        coln = []
        for i in range(1, fromi):
            coln.append(sql[i])
        wherei = 0
        for i in range(0, len(sql)):
            if sql[i] == 'where':
                wherei = i
                break

        q5(coln, sql[wherei-1], sql[wherei+1], sql[wherei+3], sql[wherei + 5], sql[wherei + 7])


print('exiting...')