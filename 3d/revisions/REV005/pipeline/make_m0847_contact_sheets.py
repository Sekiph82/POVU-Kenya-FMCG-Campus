from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "output/rev005-facility-gated/F08_F15_combined"
FACILITIES = [f"F{i:02d}" for i in range(8, 16)]
CELL_W, IMAGE_H, HEADER_H = 400, 230, 30
FONT = ImageFont.load_default()


def main():
    for role in "ABC":
        sheet = Image.new("RGB", (CELL_W * 4, (IMAGE_H + HEADER_H) * 2), (242, 242, 242))
        draw = ImageDraw.Draw(sheet)
        for i, fid in enumerate(FACILITIES):
            path = OUT / fid / f"{fid}_{role}.png"
            with Image.open(path) as source:
                image = source.convert("RGB").resize((CELL_W, IMAGE_H))
            x, y = (i % 4) * CELL_W, (i // 4) * (IMAGE_H + HEADER_H)
            sheet.paste(image, (x, y + HEADER_H))
            draw.text((x + 8, y + 8), f"{fid} - view {role}", fill=(20, 20, 20), font=FONT)
        sheet.save(OUT / f"CONTACT_FINAL_{role}.jpg", quality=90)


main()
