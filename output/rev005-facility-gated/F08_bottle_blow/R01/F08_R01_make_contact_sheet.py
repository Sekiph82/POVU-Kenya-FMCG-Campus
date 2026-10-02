from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
import sys
root=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\output\rev005-facility-gated\F08_bottle_blow\R01')
role=sys.argv[1]; folder=root/'candidates'/role
files=sorted(folder.glob(f'{role}_[0-9][0-9][0-9]_900x600.png'))
thumbw,thumbh=300,200; lab=28; cols=6; rows=(len(files)+cols-1)//cols
sheet=Image.new('RGB',(cols*thumbw,rows*(thumbh+lab)),(28,28,28)); d=ImageDraw.Draw(sheet)
try: font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17)
except: font=ImageFont.load_default()
for i,p in enumerate(files):
 im=Image.open(p).convert('RGB').resize((thumbw,thumbh),Image.Resampling.LANCZOS)
 x=(i%cols)*thumbw;y=(i//cols)*(thumbh+lab);sheet.paste(im,(x,y));d.text((x+8,y+thumbh+4),p.stem,fill='white',font=font)
out=root/f'F08_R01_{role}_CANDIDATE_CONTACT_SHEET.png';sheet.save(out)
print(out, len(files), sheet.size)
