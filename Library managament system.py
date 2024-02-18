import time


class library():

    def __init__(self,kitap,yazar,yayin,sayfa):
        self.file = open('books.txt' , 'a+' )
        self.kitap = kitap
        self.yazar = yazar
        self.yayin = yayin
        self.sayfa = sayfa

def kitap_ekleme():
    kitap = input("Kitap adini yaziniz: ")
    yazar = input("Kitap yazarini yaziniz: ")
    yayin = input("kitapin yayinlanma tarihini yaziniz: ")
    sayfa = input("Kitapin sayfa sayisini yaziniz: ")

    with open('books.txt', 'a+') as file:
        file.write(f"{kitap},{yazar},{yayin},{sayfa}\n")

def kitap_silme():
    kitap = input("Silmek istediginiz kitabin ismini giriniz: ")
    kitapliste =[]
    with open('books.txt','r' ) as file :
        for line in file:
            if kitap not in line:
                kitapliste.append(line)  # kullanicinin girdigi kitap satirda varsa  listeye eklemiyor

    with open('books.txt' , 'w' ) as file :  # w modunda acinca dosyanin icerigi silinip tekrardan yaziliyor
        file.writelines(kitapliste)
    print("Kitap silindi. ")

def listele():
    kitaplar= []
    with open('books.txt' , 'r' ) as file :
        for line in file:
            kitapliste= line.strip().split(",")
            if len(kitapliste) !=4:
                print("Eksik öge bilgisi ", line)
                continue
            kitaplar.append(kitapliste)

    for book in kitaplar:
        print("Kitap:", book[0],"Yazar:", book[1])


def bul():
    bulmak = input("Bulmak istediğiniz kitabın ismini giriniz: ")
    kitaplar = []

    with open('books.txt', 'r') as file:
        for line in file:
            kitapliste = line.strip().split(",")
            if len(kitapliste) != 4:
                print("Eksik öge bilgisi ", line)
                continue
            kitaplar.append(kitapliste)
            if bulmak == kitapliste[0]:
                print("Kitap bulundu: ", kitapliste)
                return

    print("Kitap bulunamadi. ")

while True:
    print("Menu aciliyor lutfen bekleyiniz... ")
    time.sleep(3)
    break

while True:
    print("""
    *** MENU ***
    1)Kitap listesi
    2)Kitap ekle
    3)Kitap sil
    4)Kitap ara 
    5)Cik (Eger cikmak isityorsaniz q tusuna basiniz. )""")
    cevap = input("Hangi islemi gerceklestirmek istiyorsunuz? ")
    if (cevap == '1'):
        listele()

    elif (cevap == '2'):
        kitap_ekleme()

    elif (cevap == '3'):
        kitap_silme()

    elif (cevap == '4'):
        bul()

    elif (cevap == 'q'):
        print("Cikis yapiliyor...")
        time.sleep(3)
        print("Cikildi. ")
        quit()

    else:
        print("Gecersiz format girdiniz lutfen tekrar deneyiniz. ")
