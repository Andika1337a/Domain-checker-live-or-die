import aiohttp
import asyncio

# Fungsi untuk mengecek status domain
async def check_domain_status(session, domain):
    try:
        async with session.get(f"http://{domain}", timeout=10) as response:
            if response.status < 400:  # Jika status code 2xx atau 3xx
                return domain, "Live", response.status
            else:
                return domain, "Dead", response.status
    except Exception as e:
        return domain, "Dead", str(e)

# Fungsi untuk membaca file domain.txt dan mengecek status domain
async def check_domains_from_file(filename):
    try:
        with open(filename, "r") as file:
            domains = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan!")
        return []

    dead_domains = []
    async with aiohttp.ClientSession() as session:
        tasks = [check_domain_status(session, domain) for domain in domains]
        results = await asyncio.gather(*tasks)

        for domain, status, http_code in results:
            print(f"Domain: {domain} - Status: {status} (HTTP Code: {http_code})")
            if status == "Dead":
                dead_domains.append(domain)

    return dead_domains

# Nama file yang berisi list domain
filename = "domain.txt"

# Jalankan pengecekan domain
dead_domains = asyncio.run(check_domains_from_file(filename))

# Tampilkan hasil domain mati
print("\nDead Domains:")
for dead_domain in dead_domains:
    print(dead_domain)
