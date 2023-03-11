# encoding:utf-8
import pizza_classes
import decorator_classes
import datetime
import csv


def main():
    print_menu()
    choose_pizza_choose_sauce_payment()



def print_menu():
    f = open("Menu.txt", "r", encoding="utf-8")
    print(f.read())
    print("Lütfen ekrandan pizza ve sos seçiniz")

def choose_pizza_choose_sauce_payment():

    while True:
        try:
            pizza_secimi = int(input("Lutfen bir pizza seciniz: "))
            if pizza_secimi < 1 or pizza_secimi > 4:
                raise ValueError
            break
        except ValueError:
            print("Gecersiz giris! Lutfen 1-4 arasinda bir sayi girin.")


    if pizza_secimi == 1:
        pizza = pizza_classes.Klasik()
    elif pizza_secimi == 2:
        pizza = pizza_classes.Margherita()
    elif pizza_secimi == 3:
        pizza = pizza_classes.TurkishPizza()
    elif pizza_secimi == 4:
        pizza = pizza_classes.Dominos()



    while True:
        try:
            sos_secimi = int(input("Ve seceneklerimizden bir sos seciniz: "))
            if sos_secimi < 11 or sos_secimi > 16:
                raise ValueError
            break
        except ValueError:
            print("Gecersiz giris. Lutfen 11-16 arasinda bir sayi girin.")

    if sos_secimi == 11:
        sos = decorator_classes.Zeytin(pizza)
    elif sos_secimi == 12:
        sos = decorator_classes.Mantarlar(pizza)
    elif sos_secimi == 13:
        sos = decorator_classes.KeciPeyniri( pizza)
    elif sos_secimi == 14:
        sos = decorator_classes.Et(pizza)
    elif sos_secimi == 15:
        sos = decorator_classes.Sogan(pizza)
    elif sos_secimi == 16:
        sos = decorator_classes.Misir(pizza)


    order_inf =print(f'Sipariş özeti: {sos.get_description()}li {pizza.get_description()}')
    total_cost = print(f'Ödenecek tutar:{sos.get_cost()}')
    name_surname = input("Lütfen ad soyad giriniz: ")

    while True:
        try:
            size = 11
            identity_num = input("11 haneli TC kimlik numaranızı giriniz: ")

            if len(identity_num) != size:
                raise ValueError
            break
        except ValueError:
            print("Eksik veya fazla sayı girdiniz, Lütfen tekrar deneyiniz")

    while True:
        try:
            size = 16
            card_num = input("Kredi kartı numaranızı giriniz: ")
            if len(card_num) != size:
                raise ValueError
            break
        except ValueError:
            print("Eksik veya fazla sayı girdiniz. Lütfen dikkatli giriniz")


    while True:
        try:
            size=4
            password = input("Kredi kartı şifrenizi giriniz: ")
            if len(password) != size:
                raise ValueError
            break
        except ValueError:
            print("Hatalı tuşlama yaptınız. Lütfen tekrar deneyiniz.")

    order_inf = f'{sos.get_description()}li {pizza.get_description()}'
    total_cost = (f'{sos.get_cost()}')

    date = datetime.datetime.strftime(datetime.datetime.now(), '%c')


    columns = ['kullanici adi', 'kullanici kimligi', 'kredi karti bilgileri','kredi karti sifresi','siparis aciklamasi','siparis tutari', 'siparis zamani']
    informations = [name_surname,identity_num,card_num,password,order_inf,total_cost,date]

    with open("Order_Database.csv", mode="w") as inf:
        printer = csv.writer(inf)
        printer.writerow(columns)
        printer.writerow(informations)


if __name__ == "__main__":
    main()
