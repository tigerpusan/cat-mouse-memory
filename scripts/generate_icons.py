from pathlib import Path
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'android/app/src/main/res'
def icon(size,round_=False):
 im=Image.new('RGBA',(size,size),(255,151,15,255));d=ImageDraw.Draw(im);r=size//2 if round_ else size//5
 m=Image.new('L',(size,size),0);ImageDraw.Draw(m).rounded_rectangle((0,0,size,size),radius=r,fill=255);im.putalpha(m)
 d.rounded_rectangle((size*.10,size*.10,size*.90,size*.90),radius=size*.16,fill=(255,247,239,255))
 # puzzle grid background
 for q in (.28,.50,.72):
  d.line((size*.18,size*q,size*.82,size*q),fill=(242,210,173,255),width=max(2,size//48))
  d.line((size*q,size*.18,size*q,size*.82),fill=(242,210,173,255),width=max(2,size//48))
 # cat face
 d.polygon([(size*.25,size*.42),(size*.34,size*.23),(size*.43,size*.39),(size*.57,size*.39),(size*.66,size*.23),(size*.75,size*.42)],fill=(255,255,255,255),outline=(50,40,33,255))
 d.ellipse((size*.27,size*.32,size*.73,size*.75),fill=(255,255,255,255),outline=(50,40,33,255),width=max(3,size//28))
 d.ellipse((size*.39,size*.48,size*.43,size*.54),fill=(50,40,33,255));d.ellipse((size*.57,size*.48,size*.61,size*.54),fill=(50,40,33,255))
 d.arc((size*.43,size*.53,size*.57,size*.64),10,170,fill=(50,40,33,255),width=max(2,size//40))
 # mouse badge
 d.ellipse((size*.63,size*.63,size*.85,size*.84),fill=(215,215,215,255),outline=(50,40,33,255),width=max(2,size//32))
 d.ellipse((size*.62,size*.60,size*.70,size*.68),fill=(215,215,215,255),outline=(50,40,33,255),width=max(2,size//40));d.ellipse((size*.78,size*.60,size*.86,size*.68),fill=(215,215,215,255),outline=(50,40,33,255),width=max(2,size//40))
 d.ellipse((size*.72,size*.70,size*.75,size*.73),fill=(50,40,33,255));d.line((size*.85,size*.74,size*.92,size*.69),fill=(50,40,33,255),width=max(2,size//48))
 return im
for f,s in {'mipmap-mdpi':48,'mipmap-hdpi':72,'mipmap-xhdpi':96,'mipmap-xxhdpi':144,'mipmap-xxxhdpi':192}.items():
 p=RES/f;p.mkdir(parents=True,exist_ok=True);icon(s).save(p/'ic_launcher.png');icon(s,True).save(p/'ic_launcher_round.png')