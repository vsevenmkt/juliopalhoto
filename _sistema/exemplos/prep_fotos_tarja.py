import sys
from PIL import Image, ImageOps, ImageEnhance, ImageDraw
# name: (file, eye_y, face_cx, crop_h)
P = {
 'julio':   ('julio.jpg',   284, 300, 560),
 'gabriel': ('gabriel.png', 137, 170, 320),
 'abner':   ('abner.png',   124, 150, 290),
 'evellyn': ('evellyn.png', 440, 470, 900),
}
EYE = 0.42
for k,(f,ey,cx,ch) in P.items():
    im = Image.open(f'fotos_in/{f}').convert('RGB')
    cw = int(ch*5/6); top = int(ey - EYE*ch); left = int(cx - cw/2)
    im = im.crop((left, top, left+cw, top+ch)).resize((800,960), Image.LANCZOS)
    g = ImageOps.grayscale(im); g = ImageOps.autocontrast(g, cutoff=1); g = ImageEnhance.Contrast(g).enhance(1.15)
    g.save(f'fotos/{k}.jpg', quality=90)
    t = g.convert('RGB'); d = ImageDraw.Draw(t); y = int(EYE*960); d.rectangle((144, y-67, 656, y+67), fill='black')
    t.resize((267,320)).save(f'fotos/_check_{k}.jpg')
