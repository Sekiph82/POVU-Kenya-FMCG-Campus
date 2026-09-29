from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "output/rev005-interior-remediation-v08"

def sheet(files, output, columns, cell=(256, 176)):
    rows = (len(files) + columns - 1) // columns
    canvas = Image.new("RGB", (columns * cell[0], rows * cell[1]), (24, 28, 32))
    for i, path in enumerate(files):
        with Image.open(path).convert("RGB") as image:
            image.thumbnail((cell[0] - 8, cell[1] - 24), Image.Resampling.LANCZOS)
            tile = Image.new("RGB", cell, (24, 28, 32))
            x = (cell[0] - image.width) // 2
            y = 4 + (cell[1] - 20 - image.height) // 2
            tile.paste(image, (x, y))
            ImageDraw.Draw(tile).text((6, cell[1] - 18), path.stem[:34], fill=(235, 235, 235))
            canvas.paste(tile, ((i % columns) * cell[0], (i // columns) * cell[1]))
    canvas.save(output)

isolated = sorted((OUT / "qa_isolated").glob("*.png"))
qa = sorted((OUT / "qa").glob("*.png"))
sheet(isolated, OUT / "CONTACT_SHEET_ISOLATED.png", 5)
sheet(qa, OUT / "CONTACT_SHEET_INTEGRATED_AND_PRESERVATION.png", 6)
print({"isolated": len(isolated), "qa": len(qa)})
