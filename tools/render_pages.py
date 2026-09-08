"""Render katalog.pdf into pages/pNNN.jpg + pages.json for the web viewer."""
import json, os, shutil, sys
import pymupdf

SRC = "katalog.pdf"
OUT = "pages"
WIDTH = 1400      # px, wide enough that product tables stay readable when zoomed
QUALITY = 74

if not os.path.exists(SRC):
    print("katalog.pdf not found; nothing to render"); sys.exit(0)

doc = pymupdf.open(SRC)
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)
meta = {"count": len(doc), "pdf_size": os.path.getsize(SRC), "width": None, "height": None, "files": []}
for i, page in enumerate(doc, 1):
    zoom = WIDTH / page.rect.width
    pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), alpha=False)
    name = f"p{i:03d}.jpg"
    pix.pil_save(os.path.join(OUT, name), format="JPEG", quality=QUALITY, optimize=True, progressive=True)
    if i == 1:
        meta["width"], meta["height"] = pix.width, pix.height
    meta["files"].append(name)
json.dump(meta, open("pages.json", "w"), indent=0)
total = sum(os.path.getsize(os.path.join(OUT, f)) for f in meta["files"])
print(f"rendered {len(doc)} pages, {total/1e6:.2f} MB")
