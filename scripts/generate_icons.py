from pathlib import Path
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'android/app/src/main/res'
def icon(size,round_=False):
 im=Image.new('RGBA',(size,size),(255,151,15,255));d=ImageDraw.Draw(im);r=size//2 if round_ else size//5
 m=Image.new('L',(size,size));ImageDraw.Draw(m).rounded_rectangle((0,0,size,size),radius=r,fill=255);im.putalpha(m)
 d.rounded_rectangle((size*.14,size*.14,size*.86,size*.86),radius=size*.16,fill=(255,247,239,255))
 d.polygon([(size*.28,size*.42),(size*.36,size*.24),(size*.45,size*.39),(size*.55,size*.39),(size*.64,size*.24),(size*.72,size*.42)],fill=(255,255,255,255),outline=(50,40,33,255))
 d.ellipse((size*.28,size*.34,size*.72,size*.76),fill=(255,255,255,255),outline=(50,40,33,255),width=max(3,size//28))
 d.ellipse((size*.39,size*.49,size*.43,size*.55),fill=(50,40,33,255));d.ellipse((size*.57,size*.49,size*.61,size*.55),fill=(50,40,33,255))
 d.ellipse((size*.66,size*.65,size*.84,size*.83),fill=(215,215,215,255),outline=(50,40,33,255),width=max(2,size//32))
 return im
for f,s in {'mipmap-mdpi':48,'mipmap-hdpi':72,'mipmap-xhdpi':96,'mipmap-xxhdpi':144,'mipmap-xxxhdpi':192}.items():
 p=RES/f;p.mkdir(parents=True,exist_ok=True);icon(s).save(p/'ic_launcher.png');icon(s,True).save(p/'ic_launcher_round.png')
