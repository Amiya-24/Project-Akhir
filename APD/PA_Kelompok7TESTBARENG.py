import os
import csv

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def harga_total(nama_menu, jumlah_pesanan):
    try:
        with open("./APD/menu.csv", "r") as file:
            reader = csv.reader(file)
            for line in reader:
                if line[0] == nama_menu:
                    harga = int(line[1]) * int(jumlah_pesanan)
                    return harga
        return "Error"
    
    except FileNotFoundError:
        print("File Tidak Ditemukan")

# ================================== [ LOGIN/REGISTER ] ==================================

def cek_username(username):
    try:
        with open("./APD/akun.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == username:
                    print("Username Sudah Terdaftar")
                    return True
            return False
                
    except FileNotFoundError:
        print("File Tidak Ditemukan")
        return False

def register(username, password, nama, alamat, no_hp, role = "Pengunjung"):
    try:
        with open("./APD/akun.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password, nama, alamat, no_hp, role])
            print("Register Berhasil")
    
    except FileNotFoundError:
        print("File Tidak Ditemukan")

def login(username, password):
    try:
        with open("./APD/akun.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == username and row[1] == password:
                    print("Login Berhasil")
                    return row[6]

            print("Username atau Password Salah")
            return None
        
    except FileNotFoundError:
        print("File Tidak Ditemukan")
        return None

def keluar_dari_program():
    print("\nTerima Kasih Telah Datang")
    exit()

# ================================== [ PENGGUNA PESAN MANAGEMENT ] ==================================

def lihat_pesanan():
    try:
        with open("./APD/pesanan.csv", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)

            if lines:
                for index, line in enumerate(lines):
                    jumlah = harga_total(line[0],line[1])
                    print(f"""
Pesanan Ke-{index + 1}
Nama Menu: {line[0]}
Jumlah Pesanan: {line[1]}
Jumlah Total : Rp.{jumlah}
""")

            else:
                print("Tidak Ada Pesanan")
    except FileNotFoundError:
        print("File Tidak Ditemukan")

def tambah_pesanan(nama_menu, jumlah_pesanan):
    try:
        with open("./APD/menu.csv", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)

            if lines:
                for index, line in enumerate(lines):
                    nama_menu = line[0]

        with open("./APD/pesanan.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nama_menu, jumlah_pesanan])
            print("Pesanan Berhasil Ditambahkan")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def ubah_pesanan(index, nama_menu, jumlah_pesanan):
    try:
        with open("./APD/pesanan.csv", "r") as file:
            lines = list(csv.reader(file))

            if 0 <= index < len(lines):
                lines[index][0] = nama_menu
                lines[index][1] = jumlah_pesanan
                with open("/APD/pesanan.csv", "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(lines)
                    print("Pesanan Berhasil Diubah")
            else:
                print("Pilihan Tidak Valid")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def hapus_pesanan(index):
    try:
        with open("./APD/pesanan.csv", "r") as file:
            lines = list(csv.reader(file))

        if 0 <= index < len(lines): 
            del lines[index]
            with open("./APD/pesanan.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)
                print("Pesanan Berhasil Dihapus")
        else:
            print("Pilihan Tidak Valid")
    
    except FileNotFoundError:
        print("File Tidak Ditemukan")

# ================================== [ ADMIN MENU MANAGEMENT ] ==================================

def liat_menu():
    try:
        with open("./APD/menu.csv", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)

            if lines:
                for index, line in enumerate(lines):
                    print(f"""
Ak-{index+1}
Nama Menu : {line[0]}
Harga Menu : Rp.{line[1]}
""")
            else:
                print("Menu Masih Kosong")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def tambah_menu(nama_menu, harga_menu):
    try:
        with open("./APD/menu.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nama_menu, harga_menu])
            print("Menu Berhasil Ditambahkan")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def ubah_menu(index, menu_baru, harga_baru):
    try:
        with open("./APD/menu.csv", "r") as file:
            lines = list(csv.reader(file))

        if 0 <= index < len(lines):
            lines[index][0] = menu_baru
            lines[index][1] = harga_baru
            with open("./APD/menu.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)
                print("Menu Berhasil Diubah")

        else:
            print("Pilihan Tidak Valid")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def hapus_menu(index):
    try:
        with open("./APD/menu.csv", "r") as file:
            lines = list(csv.reader(file))

        if 0 <= index < len(lines):
            del lines[index]
            with open("./APD/menu.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)
            print("Menu Berhasil Dihapus")

        else:
            print("Pilihan Tidak Valid")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

# ================================== [ ADMIN DATA MANAGEMENT ] ==================================
def liat_data():
    try:
        with open("./APD/menu.csv", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)
            if lines:
                for index, line in enumerate(lines):
                    print(f"""
Akun ke-{index+1}
Username : {line[0]}
Nama : Rp.{line[1]}
Alamat : Rp.{line[2]}
No.HP : Rp.{line[3]}
Password : Rp.{line[4]}
""")
            else:
                print("Menu Masih Kosong")

    except FileNotFoundError:
        print("File Tidak Ditemukan")


# ================================== [ MENU ] ==================================

def kembali_ke_menu():
    print("\nKembali Ke Halaman Utama")

def tampilan_menu_utama():
    print("""
<============================================================>
|             SELAMAT DATANG DI WARUNG MAKAN ABL             | 
<============================================================>
| 1. Register                                                |
| 2. Login                                                   |
| 3. Keluar                                                  |
<============================================================>
""")

def menu_admin1():
    print("\n<==============================>")
    print("|     SELAMAT DATANG ADMIN     |")
    print("<==============================>")
    print("| 1. Mengatur Menu             |")
    print("| 2. Mengatur Data Pengguna    |")
    print("| 3. Keluar                    |")
    print("<==============================>")

def menu_admin2():
    print("\n<==============================>")
    print("|        SELAMAT DATANG        |")
    print("<==============================>")
    print("| 1. Liat Menu                 |")
    print("| 2. Tambah Menu               |")
    print("| 3. Ubah Menu                 |")
    print("| 4. Hapus Menu                |")
    print("| 5. Kembali                   |")
    print("<==============================>")

    
def menu_pengunjung():
    print("\n<==============================>")
    print("|        SELAMAT DATANG        |")
    print("<==============================>")
    print("| 1. Liat Menu                 |")
    print("| 2. Tambah Pesanan            |")
    print("| 3. Ubah Pesanan              |")
    print("| 4. Hapus Pesanan             |")
    print("| 5. Lihat Pesanan             |")
    print("| 6. Kembali                   |")
    print("<==============================>")

def menu_data():
    print("\n<==============================>")
    print("|        SELAMAT DATANG        |")
    print("<==============================>")
    print("| 1. Liat Data Pengguna        |")
    print("| 2. Tambah Data Pengguna      |")
    print("| 3. Ubah Data Pengguna        |")
    print("| 4. Hapus Data Pengguna       |")
    print("| 5. Lihat Pesanan Pengguna    |")
    print("| 6. Kembali                   |")
    print("<==============================>")

# ================================== [ PROGRAM ] ==================================

def program():
    tampilan_menu_utama()
    pilih1 = input("\nMasukkan Pilihan Anda: ")

    if pilih1 == "1":
        clear()
        print("<========== REGISTER ==========>")
        username_baru = input("Masukkan Username Baru: ")
        if not cek_username(username_baru):
            password_baru = input("Masukkan Password Baru: ")
            nama_baru = input("Masukkan Password Baru: ")
            no_hp_baru = input("Masukkan Password Baru: ")
            alamat_baru = input("Masukkan Password Baru: ")
            register(username_baru, password_baru, nama_baru, alamat_baru, no_hp_baru)
        print("<==============================>")

    elif pilih1 == "2":
        clear()
        print("<=============== LOGIN ===============>")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        role = login(username,password)
        print("<=====================================>")

        if role == "ADMIN":
            while True:
                menu_admin1()
                pilih2 = input("\nMasukkan Pilihan Anda: ")
                clear()
                
                if pilih2 == "1":
                    menu_admin2
                    pilih3 =  input("\nMasukkan Pilihan Anda: ")
                    clear()
                    if pilih3 == "1":
                        clear()
                        print("<========== DAFTAR MENU ==========>")
                        liat_menu()
                        print("<=================================>")

                    elif pilih3 == "2":
                        clear()
                        print("<========== MENAMBAHKAN MENU ==========>")
                        nama_menu = input("Masukkan Nama Menu: ")
                        harga_menu = input("Masukkan Harga Menu: Rp.")
                        try:
                            harga_menu = int(harga_menu)
                            tambah_menu(nama_menu, harga_menu)
                            print("Menu Berhasil Ditambahkan")

                        except ValueError:
                            print("Harga harus berupa angka")
                        print("\n<======================================>")

                    elif pilih3 == "3":
                        clear()
                        print("<========== MENGUBAH MENU ==========>")
                        liat_menu()
                        try:
                            index_baru = int(input("Masukkan Nomor Menu Yang Ingin Diubah: ")) - 1
                            menu_baru = input("Masukkan Menu Baru: ")
                            harga_baru = int(input("Masukkan Harga Baru: Rp."))
                            ubah_menu(index_baru, menu_baru, harga_baru)
                            print("Menu Berhasil Diubah")

                        except ValueError:
                            print("Input tidak valid")
                        print("\n<===================================>")

                    elif pilih3 == "4":
                        clear()
                        print("<========== MENGHAPUS MENU ==========>")
                        liat_menu()
                        try:
                            index_hapus = int(input("Masukkan Nomor Menu Yang Ingin Dihapus: ")) - 1
                            hapus_menu(index_hapus)
                            print("Menu Berhasil Dihapus")

                        except ValueError:
                            print("Input tidak valid")
                        print("\n<====================================>")

                    elif pilih3 == "5":
                        kembali_ke_menu()
                        break

                    elif pilih3 == "6":
                        kembali_ke_menu()
                        break

                    else:
                        print("\nPilihan Invalid")
                
                if pilih2 == "2":
                    print("Data masih proses")
        
                if pilih2 == "3":
                    print("tes")

        elif role == "Pengunjung":
            while True:
                menu_pengunjung()
                pilih2 = input("\nMasukkan Pilihan Anda: ")
                clear()

                if pilih2 == "1":
                    clear()
                    print("<========== DAFTAR MENU ==========>")
                    liat_menu()
                    print("\n<=================================>")
                
                elif pilih2 == "2":
                    clear()
                    print("<========== MENAMBAHKAN PESANAN ==========>")
                    liat_menu()
                    try:
                        index_pesanan = int(input("Masukkan Nomor Menu Yang Ingin Dipesan: ")) - 1
                        try:
                            jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
                            print("Pesanan Berhasil Ditambahkan")
                            tambah_pesanan(index_pesanan,jumlah_pesanan)

                        except ValueError:
                            print("Jumlah Pesanan harus berupa angka")
                
                    except ValueError:
                        print("Input Tidak Valid")
                
                elif pilih2 == "3":
                    clear()
                    print("<========== MENGUBAH PESANAN ==========>")
                    lihat_pesanan()
                    try:
                        index_pesanan = int(input("Masukkan Nomor Menu Yang Ingin Diubah: ")) - 1
                        index_baru = int(input("Masukkan Nomor Menu Baru: ")) - 1
                        jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
                        ubah_pesanan(index_pesanan, index_baru, jumlah_pesanan)

                    except ValueError:
                        print("Jumlah Pesanan harus berupa angka")
                
                elif pilih2 == "4":
                    clear()
                    print("<========== MENGHAPUS PESANAN ==========>")
                    lihat_pesanan()
                    try:
                        index_pesanan = int(input("Masukkan Nomor Menu Yang Ingin Dihapus: ")) - 1
                        hapus_pesanan(index_pesanan)
                        

                    except ValueError:
                        print("Input Tidak Valid")

                elif pilih2 == "5":
                    clear()
                    print("<========== LIHAT PESANAN ==========>")
                    lihat_pesanan()
                    print("\n<=================================>")
                
                elif pilih2 == "6":
                    kembali_ke_menu()
                    break
                
                else:
                    print("\nPilihan Invalid")
            
        else:
            print("Login Gagal!")


    elif pilih1 == "3":
        clear()
        keluar_dari_program()

    else:
        clear()
        print("\nPilihan Tidak Valid!")

while (True):
    program()
    