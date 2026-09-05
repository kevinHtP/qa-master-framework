import pytest
from playwright.sync_api import Page , Route
from axe_playwright_python.sync_playwright import Axe

# Impor fungsi helper yang sudah kita buat
from utils.db_helper import database_master, ambil_harga
from utils.notifier import lapor_bug


def test_flow(page: Page):

    # ---------------------------------------------------------
    # ILMU 0: SETUP DATABASE EKSPLISIT
    # ---------------------------------------------------------
    print("\n[SYSTEM] Menyiapkan Master Database...")
    database_master() # Kita panggil langsung di sini agar PASTI jalan!
    
    # ---------------------------------------------------------
    # ILMU 1: NETWORK INTERCEPTION (Blokir Gambar agar Web Super Cepat)
    # ---------------------------------------------------------
    print("Blokir gambar agar loading instan")
    def blokir_gambar(route:Route):
        if route.request.resource_type =="image":
            route.abort()
        else :
            route.continue_()

    page.route("**/*", blokir_gambar)

    # ---------------------------------------------------------
    # ILMU 2: UI AUTOMATION (Login POM-style)
    # ---------------------------------------------------------
    print("[LOGIN]Login ke Web")
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # ---------------------------------------------------------
    # ILMU 3: CROSS-LAYER DATABASE VALIDATION
    # ---------------------------------------------------------
    print("[VALIDATION] harga di website dengan di database")
    nama_barang = "Sauce Labs Backpack"

    # Ambil harga dari DB (Backend)
    harga_db = ambil_harga(nama_barang)

    # Ambil harga dari Layar (Frontend)
    text_harga_ui = page.locator(f".inventory_item:has-text('{nama_barang}') .inventory_item_price").inner_text()
    harga_ui = float(text_harga_ui.replace("$", ""))

    # Assertion (Pencocokan)
    assert harga_ui == harga_db, f"Mismatched! UI: {harga_ui} | DB: {harga_db}"
    print(f"✅ Validasi Sukses: Harga UI (${harga_ui}) SINKRON dengan DB (${harga_db})")

    # ---------------------------------------------------------
    # ILMU 4: ACCESSIBILITY (a11y) TESTING
    # ---------------------------------------------------------
    print("[A11Y] memindai cacat aksessibilitas di halaman produk")
    results = Axe().run(page)
    pelanggaran = results.response.get("violations", [])

    isu_kritis = [isu for isu in pelanggaran if isu.get("impact") == "critical"]

    # Logika Cerdas: Jika ada bug, lapor! Jika tidak ada, puji!
    if len(isu_kritis)>0:
        print(f"\n[SISTEM] Ditemukan {len(isu_kritis)} bug kritis! Mengirim notifikasi ke tim...")
        for isu in isu_kritis:
            lapor_bug(isu.get("id"), isu.get("description"), isu.get("impact"))
            print("[INFO] Laporan telah dikirim. Melanjutkan sisa pengujian agar pipeline CI/CD tidak macet...")
    else:
        print("✅ Pemindaian Sukses: Bebas dari pelanggaran aksesibilitas kritis.")


