def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\nNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def hitung_nilai_akhir(uts, uas):
    # Hitung nilai akhir berdasarkan rumus tertentu, misalnya (0.4 * uts + 0.6 * uas)
    return 0.4 * uts + 0.6 * uas

def main():
    data_mahasiswa = {
        "Rudi": {"UTS": 85, "UAS": 90},
        "Excel": {"UTS": 70, "UAS": 75},
        "Daffa": {"UTS": 95, "UAS": 88},
        # Tambahkan data mahasiswa lainnya sesuai kebutuhan
    }

    data_nilai_akhir = {}

    for nama, nilai in data_mahasiswa.items():
        uts = nilai["UTS"]
        uas = nilai["UAS"]
        nilai_akhir = hitung_nilai_akhir(uts, uas)
        data_nilai_akhir[nama] = nilai_akhir

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()