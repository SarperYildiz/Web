class Students():

    def __init__(self, students_id, name, last_name):
        self.__students_id = students_id
        self.name = name
        self.last_name = last_name

    def getID(self):
        return self.__students_id

    def __str__(self):
        return self.name + " " + self.last_name


File = open("student.txt", "r", encoding="utf-8")
List = []
for i in File:
    i = i.rstrip()
    kayit = i.split(" ")
    List.append(kayit)
File.close()

ogrenci_inf = []
for i in List:
    ogrenci_inf.append(Students(i[0], i[1], i[2]))

s = ogrenci_inf
while True:
    print("""
1) Search for a student with a given id and display his/her name and lastname
2) List the universities/departmens sorted by their base point
3) Create a file named "results.txt" for each students
4) List the students information sorted by their score
5) List the student placed in every university/department
6) List of studetns who were not be able to placed anywhere
7) List of all the departments
8) Exit
    """)

    Q = int(input("Please enter the option:"))

    if Q == 1:
        num = input("Please enter the ID of the student:")

        x = 0
        y = 1
        while x < len(s):
            if s[x].getID() == num:
                print(s[x])
                break
            elif y == len(s):
                print("öğrenci bulunamadı")
                break

            else:
                x += 1
                y += 1

    if Q == 2:
        file1 = open("university.txt", "r", encoding="utf-8")
        List1 = []
        for i in file1:
            i = i.rstrip()
            kayit = i.split(",")
            List1.append(kayit)
        file1.close()

        rankingdict = {}
        for i in List1:
            rankingdict[i[2]] = i[1]
        sortedlist = (list(rankingdict.items()))
        sortedlist.sort()
        sortedlist.reverse()
        for i in sortedlist:
            print(*i)


    if Q == 3:
        List3 = []  # cevap anahtarları
        List4 = []  # öğrenci bilgileri
        List5 = []  # kitapçık türü
        students_answers = []
        List6 = []  # score
        List7 = []  # dogru
        List8 = []  # yanlıs
        List9 = []  # bos
        List10 = []  # net
        List15 = []  # ilktercih
        List16 = []  # ikincitercih
        List17 = [] #3.tercih
        List18 = [] #4.tercih
        List19 = [] #5.tercih
        okullar = open("university.txt", "r", encoding="utf-8")
        List11 = []  # okullar
        for i in okullar:
            i = i.rstrip()
            kayit = i.split(",")
            List11.append(kayit)
        okullar.close()

        anahtar = open("key.txt", "r")
        for i in anahtar:
            i = i.rstrip()

            List3.append(i)
        anahtar.close()
        cevap = open("answers.txt", "r")
        for i in cevap:
            i = i.rstrip()
            cevaplar = i.split(" ")
            List4.append(cevaplar)
        cevap.close()
        for i in List4:
            students_answers.append((i)[2])
        for i in List4:
            List5.append((i)[1])
        l = 0
        for i in List5:
            score = 0
            dogru_sayilari = 0
            yanlis_sayilari = 0
            bos_sayilari = 0
            net_sayilari = 0
            answer = students_answers[l]
            if i == "A":
                for z in range(40):
                    if answer[z] == List3[0][z]:
                        score += 15
                        dogru_sayilari += 1
                    elif answer[z] == "-":
                        bos_sayilari += 1
                    else:
                        score -= 3.75
                        yanlis_sayilari += 1
                l += 1
                net_sayilari = dogru_sayilari - (yanlis_sayilari / 4)
                List6.append(score)
                List7.append(dogru_sayilari)
                List8.append(yanlis_sayilari)
                List9.append(bos_sayilari)
                List10.append(net_sayilari)
            elif i == "B":
                for z in range(40):
                    if answer[z] == List3[1][z]:
                        score += 15
                        dogru_sayilari += 1
                    elif answer[z] == "-":
                        bos_sayilari += 1
                    else:
                        score -= 3.75
                        yanlis_sayilari += 1
                l += 1
                net_sayilari = dogru_sayilari - (yanlis_sayilari / 4)
                List6.append(score)
                List7.append(dogru_sayilari)
                List8.append(yanlis_sayilari)
                List9.append(bos_sayilari)
                List10.append(net_sayilari)
        for p in List4:
            ilk_tercih = ""
            ikinci_tercih = ""
            ucuncu_tercih = ""
            dorduncu_tercih = ""
            besinci_tercih = ""
            for k in List11:
                if p[3] == k[0]:
                    ilk_tercih += k[1]
            List15.append(ilk_tercih)
            for m in List11:
                if p[4] == m[0]:
                    ikinci_tercih += m[1]
            List16.append(ikinci_tercih)
            for l in List11:
                if p[5] == l[0]:
                    ucuncu_tercih += l[1]
            List17.append(ucuncu_tercih)
            for n in List11:
                if p[6] == n[0]:
                    dorduncu_tercih += n[1]
            List18.append(dorduncu_tercih)
            for o in List11:
                if p[7] == o[0]:
                    besinci_tercih += o[1]
            List19.append(besinci_tercih)
        cs=0
        #for i in range(len(List4)):
        ask=(List[cs][0],List[cs][1],List[cs][2],List5[cs],List7[cs],List8[cs],List9[cs],List10[cs],List6[cs],List15[cs],List16[cs],List17[cs],List18[cs],List19[cs])
        muz=str(ask)
        dota=open("results.txt","w")

        for i in range(len(List4)):


            ask = str(List[cs][0])+", "+ str(List[cs][1])+", "+ str(List[cs][2])+", "+ str(List5[cs])+", "+ str(List7[cs])+", "+ str(List8[cs])+", "+ str(List9[cs])+", "+ str(List10[cs])+", "+ str(List6[cs])+", "+str(List15[cs])+", "+ str(List16[cs])+", "+ str(List17[cs])+", "+ str(List18[cs])+", "+ str(List19[cs])

            dota.write(ask+"\n")
            cs+=1







    if Q == 4:
        List3 = []  # cevap anahtarları
        List4 = []  # öğrenci bilgileri
        List5 = []  # kitapçık türü
        students_answers = []
        List6 = []  # score

        anahtar = open("key.txt", "r")

        for i in anahtar:
            i = i.rstrip()

            List3.append(i)

        anahtar.close()

        cevap = open("answers.txt", "r")
        for i in cevap:
            i = i.rstrip()
            cevaplar = i.split(" ")
            List4.append(cevaplar)
        cevap.close()

        for i in List4:
            students_answers.append((i)[2])

        for i in List4:
            List5.append((i)[1])

        l = 0
        for i in List5:

            score = 0
            answer = students_answers[l]

            if i == "A":
                for z in range(40):
                    if answer[z] == List3[0][z]:
                        score += 15
                        z += 1



                    elif answer[z] == "-":
                        z += 1


                    else:

                        score -= 3.75
                        z += 1

                    if z == 40:
                        break
                l += 1
                List6.append(score)

            elif i == "B":
                for z in range(40):
                    if answer[z] == List3[1][z]:
                        score += 15
                        z += 1


                    elif answer[z] == "-":
                        z += 1


                    else:

                        score -= 3.75
                        z += 1

                    if z == 40:
                        break
                l += 1
                List6.append(score)

        studentrankingdict = {}
        m = 0
        for i in List:
            studentrankingdict[i[0] + " " + i[1] + " " + i[2]] = List6[m]
            m += 1
        import operator

        kucuktenbuyuge = sorted(studentrankingdict.items(), key=operator.itemgetter(1))  # birden çok öğrencinin aynı puanı olabildiği için keyleri öğrenci aldık value leri sıralamak için böyle bir yöntem kullandım
        kucuktenbuyuge.reverse()
        for i in kucuktenbuyuge:
            print(i[0], " ", i[1])

    if Q == 5:
        print(5)

    if Q == 6:
        print(6)

    if Q == 7:
        file1 = open("university.txt", "r", encoding="utf-8")
        List = []
        y = []
        for i in file1:
            i = i.rstrip()
            kayit = i.split("University")
            for i in kayit:
                s = i.split(",")
            List.append(s[0])
        file1.close()
        for j in List:
            if j not in y:
                y.append(j)
        for k in y:
            print(k)

    if Q == 8:
        break