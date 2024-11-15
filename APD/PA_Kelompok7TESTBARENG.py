import os
import csv

def clear():
    os.system("cls" if os.name == "nt" else "clear")

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

def register(username, password, nama, alamat, no_hp, tanggal_lahir, role = "Pengunjung"):
    try:
        with open("./APD/akun.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password, nama, alamat, no_hp, tanggal_lahir, role])
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

def lihat_pesanan():
    try:
        with open("./APD/pesanan.csv", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)

            if lines:
                for index, line in enumerate(lines):
                    jumlah = harga_total(line[1],line[2])
                    print(f"""
Pesanan Ke-{index + 1}
Nama Menu: {line[1]}
Jumlah Pesanan: {line[2]}
Jumlah Total : Rp.{jumlah}
""")
            else:
                print("Tidak Ada Pesanan")
                
    except FileNotFoundError:
        print("File Tidak Ditemukan")

def tambah_pesanan(username, nama_menu, jumlah_pesanan):
    try:
        with open("./APD/menu.csv", "r") as file:
            reader = list(csv.reader(file))
            if 0 <= nama_menu < len(reader):
                nama_menu = reader[nama_menu][0] 

                with open("./APD/pesanan.csv", "a", newline='') as file_pesanan:
                    writer = csv.writer(file_pesanan)
                    writer.writerow([username, nama_menu, jumlah_pesanan])
                    print("Pesanan Berhasil Ditambahkan")

            else:
                print("Menu yang dipilih tidak valid.")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def ubah_pesanan(index, nama_menu, jumlah_pesanan):
    try:
        with open("./APD/pesanan.csv", "r") as file:
            lines = list(csv.reader(file))

            if 0 <= index < len(lines): 
                lines[index][2] = jumlah_pesanan
                with open("./APD/menu.csv", "r") as file:
                    lines2 = list(csv.reader(file))
                    menubaru = lines2[nama_menu][0]
                    lines[index][1] = menubaru
                with open("./APD/pesanan.csv", "w", newline='') as file:
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
Menu ke-{index+1}
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
        with open("./APD/akun.csv", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)
            if lines:
                for index, line in enumerate(lines):
                    print(f"""
Akun ke-{index+1}
Username : {line[0]}
Nama : {line[1]}
Alamat : {line[2]}
No.HP : {line[3]}
Password : {line[4]}
Role Akun : {line[5]}
Tanggal Lahir : {line[6]}
""")
            else:
                print("Data Masih Kosong")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def tambah_data(username_baru, password_baru, nama_baru, alamat_baru, no_hp_baru, tanggal_lahir_baru, role_baru):
    try:
        with open("./APD/akun.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username_baru, password_baru, nama_baru, alamat_baru, no_hp_baru, tanggal_lahir_baru, role_baru])
            print("Data Berhasil Ditambahkan")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def ubah_data(index, username_baru, password_baru, nama_baru, alamat_baru, no_hp_baru, tanggal_lahir_baru, role_baru):
    try:
        with open("./APD/akun.csv", "r") as file:
            lines = list(csv.reader(file))

        if 0 <= index < len(lines):
            lines[index][0] = username_baru
            lines[index][1] = password_baru
            lines[index][2] = nama_baru
            lines[index][3] = alamat_baru
            lines[index][4] = no_hp_baru
            lines[index][5] = tanggal_lahir_baru
            lines[index][6] = role_baru
            
            with open("./APD/akun.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)
                print("Data Berhasil Diubah")

        else:
            print("Pilihan Tidak Valid")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def hapus_data(index):
    try:
        with open("./APD/akun.csv", "r") as file:
            lines = list(csv.reader(file))

        if 0 <= index < len(lines):
            del lines[index]
            with open("./APD/akun.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)
            print("Data Berhasil Dihapus")

        else:
            print("Pilihan Tidak Valid")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def liat_pesanan_pengguna():
    try:
        with open("./APD/pesanan.csv", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)
            if lines:
                for index, line in enumerate(lines):
                    print(f"""
Akun ke-{index+1}
Username : {line[0]}
Pesanan : {line[1]}
""")
            else:
                print("Data Masih Kosong")

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
    print("| 3. Kembali                   |")
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
            nama_baru = input("Masukkan Nama: ")
            alamat_baru = input("Masukkan Alamat: ")
            no_hp_baru = input("Masukkan Nomor HP: ")
            tanggal_lahir_baru = input("Masukkan Tanggal Lahir: ")
            register(username_baru, password_baru, nama_baru, alamat_baru, no_hp_baru, tanggal_lahir_baru)
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
                
# ================================== [ PIlIHAN ADMIN MENGATUR MENU ] ==================================

                if pilih2 == "1":
                    while True:
                        menu_admin2()
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

                            except ValueError:
                                print("Input tidak valid")
                            print("\n<====================================>")

                        elif pilih3 == "5":
                            clear()
                            kembali_ke_menu()
                            break

                        else:
                            print("\nPilihan Invalid")

# ================================== [ PIlIHAN ADMIN MENGATUR DATA ] ===============================
                    
                elif pilih2 == "2":
                    while True:
                        menu_data()
                        pilih4 =  input("\nMasukkan Pilihan Anda: ")
                        clear()
                        if pilih4 == "1":
                            clear()
                            print("<========== DAFTAR DATA ==========>")
                            liat_data()
                            print("<=================================>")

                        elif pilih4 == "2":
                            clear()
                            print("<========== MENAMBAHKAN DATA ==========>")
                            nambah_username = input("Masukkan Username Baru Pengguna: ")
                            nambah_password = input("Masukkan Password Baru Pengguna: ")
                            nambah_nama = input("Masukkan Nama Baru Pengguna: ")
                            nambah_alamat = input("Masukkan Alamat Baru Pengguna : ")
                            nambah_NoHP = input("Masukkan No.HP Baru Pengguna: ")
                            nambah_tanggallahir = input("Masukkan Tanggal Lahir Baru Pengguna: ")
                            nambah_Role = input("Masukkan Role Baru Pengguna: ")
                            try:
                                tambah_data(nambah_username, nambah_password, nambah_nama, nambah_alamat, nambah_NoHP, nambah_tanggallahir, nambah_Role)

                            except ValueError:
                                print("Harga harus berupa angka")
                            print("\n<======================================>")

                        elif pilih4 == "3":
                            clear()
                            print("<========== MENGUBAH DATA ==========>")
                            liat_data()
                            try:
                                index_baru = int(input("Masukkan Nomor Data Yang Ingin Diubah: ")) - 1 # habis mmasukkan index nanti dia milih mau data bagian mana yang diubah
                                username_baru = input("Masukkan Username Baru: ")
                                password_baru = input("Masukkan Password Baru: ")
                                nama_baru = input("Masukkan Nama Baru: ")
                                alamat_baru = input("Masukkan Alamat Baru: ")
                                no_hp_baru = input("Masukkan No.HP Baru: ")
                                tanggal_lahir_baru = input("Masukkan Tanggal Lahir Baru: ")
                                role_baru = input("Masukkan Role Baru: ") # role_baru bisa dihapus karena role admin cuma bisa satu
                                ubah_data(index_baru, username_baru, password_baru, nama_baru, alamat_baru, no_hp_baru, tanggal_lahir_baru, role_baru) #role_baru dihapus aja nanti

                            except ValueError:
                                print("Input tidak valid")
                            print("\n<===================================>")

                        elif pilih4 == "4":
                            clear()
                            print("<========== MENGHAPUS DATA ==========>")
                            liat_data()
                            try:
                                index_hapus = int(input("Masukkan Nomor Data Yang Ingin Dihapus: ")) - 1
                                hapus_data(index_hapus)

                            except ValueError:
                                print("Input tidak valid")
                            print("\n<====================================>")

                        elif pilih4 == "5":
                            clear()
                            liat_pesanan_pengguna()

                        elif pilih4 == "6":
                            clear()
                            kembali_ke_menu()
                            break

                        else:
                            print("\nPilihan Invalid")

            
                elif pilih2 == "3":
                    kembali_ke_menu()
                    break

# ================================== [ PROGRAM PENGGUNA ] ===============================

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
                            tambah_pesanan(username,index_pesanan,jumlah_pesanan)

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
                        liat_menu()
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
