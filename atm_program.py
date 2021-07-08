import random
import datetime
from customer import Customer

atm = Customer(id)

while True:

    id = int(input('Masukkan pin anda: '))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input('Pin Anda salah. Silakan masukkan lagi: '))

        trial += 1
        
        if trial == 3:
            print("Error. Silakan ambil kartu dan coba lagi..")
            exit()
        
    while True:
        print("Selamat Datang di ATM Khalid!")
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar ")
        select_menu = int(input("\nSilakan pilih menu: "))

        if select_menu == 1:
            print("\nSaldo anda sekarang: Rp",str(atm.checkBalance()), "\n")

        elif select_menu == 2:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut? {} (y/n) ".format(nominal))
            
            if verify_withdraw == "y":
                print("Saldo awal anda: Rp",str(atm.checkBalance()), "")
            else:
                break
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil!")
                print("Sisa saldo: Rp",str(atm.checkBalance()), "")
            else:
                print("Maaf, saldo Anda tidak cukup untuk melakukan debet.")
                print("Silakan lakukan penambahan nominal saldo!")

        elif select_menu == 3:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut? {} (y/n) ".format(nominal))
            
            if verify_deposit == "y":
                atm.depositBalance(nominal)
                print("Saldo anda sekarang: Rp",str(atm.checkBalance()), "\n")
            else:
                break

        elif select_menu == 4:
            verify_pin = int(input("Masukkan pin anda: "))

            while verify_pin != int(atm.checkPin()):
                print("Pin Anda salah. silakan masukkan pin: ")

            updated_pin = int(input("Masukkan pin baru: "))
            print("Pin Anda berhasil diganti.")

            verify_newpin = int(input("Coba masukkan pin baru: "))

            if verify_newpin == updated_pin:
                print("Pin baru Anda sukses.")
            else:
                print("Maaf, pin Anda salah.")

        elif select_menu == 5:
            print("Resi tercetak otomatis saat Anda keluar. \nHarap simpan tanda terima ini \nsebagai bukti transaksi Anda.")
            print()
            print("No. Record: ",random.randint(100000, 1000000))
            print("Tanggal: ",datetime.datetime.now())
            print("Saldo akhir: ",atm.checkBalance())
            print("Terima kasih telah menggunakan ATM Khalid!")
            exit()

        else:
            print("Error. \nMaaf, menu tidak tersedia.")