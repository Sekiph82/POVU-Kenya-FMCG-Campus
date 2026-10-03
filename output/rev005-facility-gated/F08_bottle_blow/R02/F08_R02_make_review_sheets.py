from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
root=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\output\rev005-facility-gated\F08_bottle_blow\R02')
for role in 'ABCD':
 files=sorted((root/'candidates'/role).glob(f'{role}_[0-9][0-9][0-9]_900x600.png'))
 assert len(files)==24,(role,len(files))
 w,h,lab,cols=200,133,22,6; sheet=Image.new('RGB',(cols*w,4*(h+lab)),(30,30,30));d=ImageDraw.Draw(sheet)
 try: font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',14)
 except:font=ImageFont.load_default()
 for n,p in enumerate(files):
  im=Image.open(p).convert('RGB').resize((w,h),Image.Resampling.LANCZOS);x=(n%cols)*w;y=(n//cols)*(h+lab);sheet.paste(im,(x,y));d.text((x+5,y+h+3),p.stem,fill='white',font=font)
 sheet.save(root/f'F08_R02_{role}_ALL24_REVIEW.png')
 print(role,len(files),sheet.size)
