import datetime
import os

def lapor_bug(nama_bug, deskripsi, tingkat_keparahan):
    # Mengambil waktu saat bug ditemukan
    waktu_ditemukan = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Merakit desain pesan notifikasi
    pesan_slack = f"""
    🚨 *Bug Baru Ditemukan!* 🚨
    waktu= {waktu_ditemukan}
    bug_id = {nama_bug}
    keparahan= {tingkat_keparahan}
    detail= {deskripsi}
    Tindakan : Mohon tim Frontend segera mengecek kode HTML terkait.
    """

    # 1. Tampilkan peringatan berwarna merah di Terminal (Simulasi Slack)
    print(f"\033[91m{pesan_slack}\033[0m")

    # 2. Simpan jejak bug ke dalam file bukti (Bug Report)
    with open("bug_report.text","a" ,encoding="utf-8") as file_log:
        file_log.write(pesan_slack + "\n")

    # Catatan Engineer: 
    # Di dunia kerja sungguhan, baris ini akan diaktifkan menggunakan library 'requests' 
    # untuk mengirim pesan ke aplikasi chat kantor:
    # requests.post("https://hooks.slack.com/services/TOKEN_RAHASIA", json={"text": pesan_slack})
