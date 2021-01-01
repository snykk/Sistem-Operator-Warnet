import os
import json
from datetime import datetime
menu = ["[1] Login"," [2] Logout"," [3] Warnet Tutup"]
try:
    with open ("ListKursi.json", "r") as jsonKursi:
            data_user = json.load(jsonKursi)
except IOError:
    data_user = []
def login(user_login):
    while True:
        angka = ["1","2","3","4","5","6","7","8","9","10"]
        number = input("Ingin login pada kursi nomor berapa? ")
        for a in angka:
            if number == a:
                number = int(number)
                number -= 1
                if user_login[number]["Status"] == 'Ready':
                    name = input("Nama User: ")
                    time_start = str(datetime.now().strftime("%H:%M:%S"))
                    user_login[number]["Username"] = name
                    user_login[number]["Mulai"] = time_start
                    user_login[number]["Status"] = "Running"
                    break
                elif user_login[number]["Status"] == 'Running':
                    dislogin(user_login, number)
        break


def dislogin(data_dislogin, number):
    os.system("cls")
    print('Maaf kursi nomor', (number+1), 'saat ini sedang dipakai')
    print(f"{'Kursi':7} {'Status':9} {'Username':12} {'Mulai':12}")
    print("{0:^5} {1:1} {2:9} {3:12} {4:12}".format(data_dislogin[number]["Kursi"]," ",data_dislogin[number]["Status"],data_dislogin[number]["Username"],data_dislogin[number]["Mulai"]))
    enter = input("Tekan [Enter] untuk kembali")
    print(enter)


def dislogout(data_dislogout, number):
    os.system("cls")
    print('Maaf, tidak ada user pada kursi nomer', (number+1))
    print(f"{'Kursi':7} {'Status':9} {'Username':12} {'Mulai':12}")
    print("{0:^5} {1:1} {2:9} {3:12} {4:12}".format(data_dislogout[number]["Kursi"]," ",data_dislogout[number]["Status"],data_dislogout[number]["Username"],data_dislogout[number]["Mulai"]))
    enter = input("Tekan [Enter] untuk kembali")
    print(enter)


def common():
    os.system("cls")
    print(f"{'SISTEM OPERATOR WARNET NAZI':^50}")
    print("-"*50)
    print(f"{'Kursi':9} {'Status':11} {'Username':20s}")
    print("-"*50)
    for table in data_user:
        print("{0:^5} {1:3} {2:11} {3:20}".format(table["Kursi"]," ",table["Status"],table["Username"]))


def logout(data_logout):
    number = int(input("Ingin logout pada kursi nomor berapa? "))
    number -= 1
    if data_logout[number]["Status"] == "Ready":
        dislogout(data_logout, number)
    else:
        final = input("Apakah anda yakin untuk logout di kursi ke-"+str(number+1)+"?[y/t] ")
        if final == "y":
            time_end = str(datetime.now().strftime("%H:%M:%S"))
            data_logout[number]["Berhenti"] = time_end
            elapsed(data_logout, number)
            viewlogout(data_logout, number)
            enter = input("Tekan [Enter] apabila telah selesai melakukan pembayaran")
            if enter == "":
                write(data_logout, number)
                restart(data_logout, number)


def restart(data_restart, number):
    data_restart[number]["Status"] = "Ready"
    data_restart[number]["Username"] = "-----"
    data_restart[number]["Mulai"] = "-----"
    data_restart[number]["Berhenti"] = "-----"
    data_restart[number]["Lama"] = "-----"
    data_restart[number]["Harga"] = 0


def write(data_write, number):
    with open("Data Warnet.json", "a") as jsonfile:
        json.dump(data_write[number], jsonfile, indent=4)


def elapsed(data_elapsed, number):
    lama = 0
    for i in range(len(data_elapsed[number]["Mulai"])):
        if i == 0:
            jam = int(data_elapsed[number]["Berhenti"][i:i+2]) - int(data_elapsed[number]["Mulai"][i:i+2])
            detik = jam*3600
            lama += detik
        elif i == 3:
            menit = int(data_elapsed[number]["Berhenti"][i:i+2]) - int(data_elapsed[number]["Mulai"][i:i+2])
            detik = menit*60
            lama += detik
        elif i == 6:
            detik = int(data_elapsed[number]["Berhenti"][i:i+2]) - int(data_elapsed[number]["Mulai"][i:i+2])
            lama += detik
    dalamJam = lama/3600
    if dalamJam  < 1/6:
        harga = 1000
    elif dalamJam-int(dalamJam) > 1/6:
        harga = (int(dalamJam)+1)*5000
    else:
        harga = int(dalamJam)*5000
    data_elapsed[number]["Lama"] = "{:.3f}".format(dalamJam) + " jam"
    data_elapsed[number]["Harga"] = harga


def viewlogout(view_logout, number):
    os.system("cls")
    print(f"{'Kursi':7} {'Status':9} {'Username':12} {'Mulai':12} {'Berhenti':12} {'Lama':12} {'Harga':20}")
    total = int(view_logout[number]["Harga"])
    print("{0:^5} {1:1} {2:9} {3:12} {4:12} {5:12} {6:12} {7:20}".format(view_logout[number]["Kursi"]," ",view_logout[number]["Status"],view_logout[number]["Username"],view_logout[number]["Mulai"],view_logout[number]["Berhenti"],view_logout[number]["Lama"],"Rp {:,}".format(total)))


while True:
    common()
    print("\nPilih Integer:","".join(menu))
    ask = input("[1][2][3]~~~> ")
    if ask == "1":
        login(data_user)
    elif ask == "2":
        logout(data_user)
    elif ask == "3":
        break