def rezultats(sk1, sk2):

    if sk1<6 and sk2<6:

        rez = sk1*sk2

    else:

        rez = sk1+sk2

    return rez

for skaitlis in range(1, 11, 2):        #range - funkcija, kas skaita skaitļus

    for otrs in range(2, 11, 2):

        print("pirmais skaitlis:", skaitlis,"otrais skaitlis:", otrs, "rezultāts: ", rezultats(skaitlis, otrs))

def zvaigznites1(skaits):

    for rindasNr in range(1, skaits+1):

        for zvaigzne in range(rindasNr):

            print("*", end="")

        print("")

def zvaigznites2(skaits):

    for rindasNr in range(1, skaits+1):

        print("*"*rindasNr)

zvaigznites1(7)

saraksts1 = [1, 7, 5, 9, 35, 2]

saraksts2 = [4, 2, 2, 39, 6, 4]

for skaititajs in range(len(saraksts1)):

    print("skaititajs:", skaititajs, "pirmais skaitlis:", saraksts1[skaititajs],"otrais skaitlis:", saraksts2[skaititajs], "rezultāts: ", rezultats(saraksts1[skaititajs], saraksts2[skaititajs]))

skaitlu_pari = [2,5], [4,7], [3,4], [7,9]

print("---------------------------------")

for i in range(len(skaitlu_pari)):

     print("skaititajs:", i, "pirmais skaitlis:", skaitlu_pari[i][0],"otrais skaitlis:", skaitlu_pari[i][1], "rezultāts: ", rezultats(skaitlu_pari[i][0], skaitlu_pari[i][1]))

print("---------------------------------")

for elements in skaitlu_pari[:-1]:

    print("pirmais skaitlis:", elements[0],"otrais skaitlis:", elements[1], "rezultāts: ", rezultats(elements[0], elements[1]))

print("---------------------------------")