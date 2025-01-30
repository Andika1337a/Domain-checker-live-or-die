# Domain-checker-live-or-die
### Penjelasan:
1. **Library `aiohttp`**:
   - Digunakan untuk melakukan HTTP requests secara asynchronous.
   - Memungkinkan pengecekan domain secara bersamaan (concurrent).

2. **Fungsi `check_domain_status`**:
   - Mengecek status domain dengan mengirim request HTTP ke domain.
   - Jika respons status code adalah `2xx` atau `3xx`, domain dianggap "Live".
   - Jika terjadi error (misalnya timeout atau domain tidak ditemukan), domain dianggap "Dead".

3. **Fungsi `check_domains_from_file`**:
   - Membaca file `domain.txt` dan membuat list domain.
   - Menggunakan `aiohttp.ClientSession` untuk membuat session HTTP.
   - Membuat task untuk setiap domain dan menjalankannya secara bersamaan menggunakan `asyncio.gather`.

4. **Output**:
   - Menampilkan status setiap domain beserta kode HTTP atau pesan error.
   - Menampilkan list domain yang mati.

### Cara Menggunakan:
1. **Install Library `aiohttp`**:
   Jika belum memiliki library `aiohttp`, install menggunakan pip:
   ```bash
   pip install aiohttp
   ```

2. **Buat File `domain.txt`**:
   Buat file `domain.txt` dan masukkan list domain yang ingin dicek (satu domain per baris). Contoh:
   ```
   example.com
   google.com
   nonexistentdomain123.com
   thisshouldnotexist.com
   ```

3. **Jalankan Script**:
   Simpan script di atas sebagai `domain_checker.py` dan jalankan menggunakan Python:
   ```bash
   python Pengecek_handal.py
   ```

### Contoh Output:
```
Domain: example.com - Status: Live (HTTP Code: 200)
Domain: google.com - Status: Live (HTTP Code: 301)
Domain: nonexistentdomain123.com - Status: Dead (HTTP Code: Cannot connect to host)
Domain: thisshouldnotexist.com - Status: Dead (HTTP Code: Cannot connect to host)

Dead Domains:
nonexistentdomain123.com
thisshouldnotexist.com
```

### Keuntungan:
- **Cepat**: Menggunakan asynchronous programming, sehingga pengecekan domain dilakukan secara bersamaan.
- **Akurat**: Mengecek kode HTTP untuk menentukan status domain.
- **Mudah Dikembangkan**: Anda bisa menambahkan fitur seperti pengecekan HTTPS atau timeout yang lebih fleksibel.

### Catatan:
- Pastikan file `domain.txt` ada di direktori yang sama dengan script Python.
- Jika Anda ingin mengecek domain dengan HTTPS, ubah `http://` menjadi `https://` di fungsi `check_domain_status`.
- Untuk pengecekan yang lebih cepat, Anda bisa menyesuaikan timeout atau menggunakan server dengan bandwidth yang lebih besar.
