# 🚀 Unified E2E Automation Framework (Master Quality Gate)

Framework otomatisasi terpadu (*Unified Framework*) ini dirancang sebagai *Quality Gate* tingkat Enterprise. Repositori ini menggabungkan lima lapisan pengujian dan pemantauan ke dalam satu alur eksekusi (*single pipeline execution*), membuktikan bahwa pengujian E2E dapat berjalan cepat, tangguh (*resilient*), dan mencakup seluruh aspek perangkat lunak (UI, Backend, Data, dan Aksesibilitas).

## 🌟 Arsitektur & Fitur Utama

Framework ini tidak sekadar menguji UI, melainkan mengorkestrasi validasi lintas lapisan (*Cross-Layer Validation*):

1. **⚡ Network Interception & Traffic Optimization:** 
   Memanfaatkan kapabilitas Playwright untuk mencegat (*intercept*) lalu lintas jaringan dan memblokir *resource* berat (seperti gambar/media) secara *on-the-fly*. Menghasilkan waktu eksekusi UI yang ultra-cepat dan menghemat *bandwidth* CI/CD.
2. **🤖 Robust UI Automation:** 
   Navigasi antarmuka dan interaksi DOM yang stabil menggunakan Playwright Sync API.
3. **🗄️ Cross-Layer Database Validation:** 
   Tidak hanya memvalidasi tampilan visual (Frontend), skrip secara aktif menembak *query* ke Database SQLite (Backend) untuk memastikan integritas data (contoh: kecocokan harga di layar UI dengan harga *Source of Truth* di DB).
4. **♿ Automated Accessibility (a11y) Auditing:** 
   Injeksi mesin pemindai **Axe-Core** ke dalam DOM untuk mendeteksi pelanggaran standar WCAG/ADA tingkat kritis secara otomatis di latar belakang.
5. **🚨 Smart Alerting & Auto-Notifier:** 
   Sistem penanganan *error* cerdas (menggunakan standar *encoding UTF-8*). Alih-alih merusak *pipeline* saat menemukan anomali aksesibilitas, sistem akan secara otomatis membuat dan menyimpan tiket *bug* ke dalam `bug_report.txt` (terstruktur untuk integrasi *webhook* Slack/Teams di masa depan).

## 🛠️ Tech Stack
*   **Core Engine:** Python 3 & Playwright
*   **Test Runner:** Pytest
*   **A11y Engine:** Axe-Core (`axe-playwright-python`)
*   **Database:** SQLite3

## 📁 Struktur Direktori
```text
qa-master-framework/
├── tests/
│   └── test_master_e2e.py  # Eksekutor utama (Otak dari framework)
├── utils/
│   ├── db_helper.py        # Modul jembatan koneksi & query Database
│   └── notifier.py         # Kurir sistem notifikasi dan pembuatan Bug Report
├── master_toko.db          # (Generated) Database lokal untuk validasi E2E
├── bug_report.txt          # (Generated) Log otomatis temuan anomali/bug
└── README.md


🚀 Panduan Eksekusi (Local Setup)
1. Instalasi Dependensi
Pastikan Python 3 sudah terpasang, lalu jalankan:

Bash
pip install pytest playwright axe-playwright-python
playwright install chromium
2. Menjalankan Master Pipeline
Eksekusi perintah di bawah ini untuk melihat keajaiban dari 5 teknologi yang berjalan secara paralel dalam hitungan detik:

Bash
python -m pytest -s -v --headed tests/test_master_e2e.py
Hasil yang Diharapkan:
Sistem akan memblokir gambar web, melakukan login otomatis, mencocokkan data UI dengan tabel SQL, memindai pelanggaran HTML/A11y, dan jika ditemukan anomali kritis, sistem akan mencetak peringatan merah di terminal serta merekam detailnya ke dalam file bug_report.txt.

Built with passion to demonstrate that Software Quality is not just about finding bugs, but designing a resilient safety net.