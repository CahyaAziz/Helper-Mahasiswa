def penambahan(tugas):
    
    tanggal = input("Masukkan tanggal (YYYY-MM-DD):")
    matkul = input("Masukkan nama mata kuliah: ")
    judul = input("Masukkan judul tugas: ")
    deskripsi = input("Masukkan deskripsi  tugas: ")
    kesulitan = input("Masukkan Tingkat kesulitan (Mudah/Sedang/Sulit): ")
    tenggat = input("Masukkan tanggal tenggat tugas (YYYY-MM-DD):")


    if tanggal not in tugas:
        tugas[tanggal] = []
    
    tugas[tanggal].append({
        'mata_kuliah': matkul, 
        'judul': judul,
        'deskripsi': deskripsi,
        'tingkat_kesulitan': kesulitan,
        'tenggat': tenggat,
        'status':'Belum Selesai'
        })
    
    print("Tugas berhasil ditambahkan!\n")

def tampilan(tugas):
    if not tugas:
        print("Cie lagi gak ada tugas.\n")
        return

    for tanggal, tugasHari in tugas.items():
        print(f"Tugas untuk tanggal {tanggal}:")
        for jadwalTugas in tugasHari:
            print(f"  Mata Kuliah: {jadwalTugas['mata_kuliah']}")
            print(f"  Judul: {jadwalTugas['judul']}")
            print(f"  Deskripsi: {jadwalTugas['deskripsi']}")
            print(f"  Tingkat Kesulitan: {jadwalTugas['tingkat_kesulitan']}")
            print(f"  Tenggat: {jadwalTugas['tenggat']}")
            print(f"  Status: {jadwalTugas['status']}")
        print()

def selesaikanTugas(tugas):
    tanggal = input("Masukkan tanggal tugas yang ingin diselesaikan (YYYY-MM-DD): ")
    if tanggal not in tugas:
        print("Tidak ada tugas pada tanggal tersebut.\n")
        return
    
    print("Tugas yang tersedia untuk tanggal tersebut:")
    for i, isiTugas in enumerate(tugas[tanggal]):
        print(f"{i + 1}. {isiTugas['judul']} - Status: {isiTugas['status']}")

    pilihan = int(input("Pilih nomor tugas yang ingin diselesaikan: ")) - 1
    if 0 <= pilihan < len(tugas[tanggal]):
        tugasPilihan = tugas[tanggal][pilihan]
        print(f"Status tugas '{tugasPilihan['judul']}' saat ini: {tugasPilihan['status']}")
        
        statusBaru = input("Apakah tugas ini sudah selesai? (ya/tidak): ").strip().lower()
        if statusBaru == 'ya':
            tugasPilihan['status'] = 'Selesai'
            print("Status berhasil diubah menjadi 'Selesai'!\n")
        elif statusBaru == 'tidak':
            tugasPilihan['status'] = 'Belum Selesai'
            print("Status berhasil diubah menjadi 'Belum Selesai'!\n")
        else:
            print("Input tidak valid. Masukkan 'ya' atau 'tidak'.\n")
    else:
        print("Pilihan tidak valid.\n")

def main_tugas():
    tugas = {}
    
    while True:
        print("1. Menambah Tugas")
        print("2. Menampilkan Tugas")
        print("3. Selesaikan Tugas")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == "1":
            penambahan(tugas)
        elif pilihan == "2":
            tampilan(tugas)
        elif pilihan == "3":
            selesaikanTugas(tugas)
        elif pilihan == "4":
            print("Terima kasih!, Program selesai.")
            return
        else:
            print("Invalid. Silakan pilih 1, 2, 3, atau 4.")

main_tugas()