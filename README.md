# Karteya Katalog

Bu site https://alterwayapp-create.github.io/karteya-katalog/ adresinde yayınlanır. QR kod bu adrese sabitlidir; adres hiçbir zaman değişmez.

## Kataloğu güncellemek

1. Yeni kataloğun PDF dosyasının adını **katalog.pdf** yapın (küçük harf).
2. Bu depoda **Add file → Upload files** ile katalog.pdf dosyasını yükleyin. Eski dosya üzerine yazılır.
3. **Commit changes** deyin.

Yükleme sonrası sistem sayfaları kendiliğinden resme çevirir (`pages/` klasörü ve `pages.json`, "Actions" sekmesinden izlenebilir) ve site 2-3 dakika içinde yeni kataloğu gösterir. Başka hiçbir dosyaya dokunmanız gerekmez.

## Dosyalar

- `katalog.pdf` – yayındaki katalog (PDF indir düğmesi bunu verir)
- `pages/`, `pages.json` – otomatik üretilen sayfa görselleri (elle düzenlemeyin)
- `index.html`, `lib/` – görüntüleyici
- `tools/render_pages.py`, `.github/workflows/render.yml` – otomatik dönüştürme
