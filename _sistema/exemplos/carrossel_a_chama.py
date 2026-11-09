import sys; import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from templates import *
A={k:f'file:///home/claude/tpl/assets/{v}' for k,v in {'avatar':'julio-avatar.jpg'}.items()}
OUT='/home/claude/posts/chama-5-formas'
N=7
def dots(active):
    return '<div style="position: absolute; left: 80px; bottom: 108px; display: flex; gap: 10px">'+''.join(
        f'<div style="width: {36 if i==active else 12}px; height: 12px; border-radius: 6px; background: {INK if i==active else "#DADADA"}"></div>' for i in range(N))+'</div>'
def foot(active, dark=False):
    c='#A9A193' if dark else MUTE_W
    return dots(active)+f'<p style="position: absolute; right: 80px; bottom: 96px; margin: 0; font-size: 24px; font-weight: 700; color: {c}">@juliopalhoto</p>'
slides=[]
# capa
slides.append(frame(label('A Chama', GOLDTXT, y=96) +
  f'<p style="position: absolute; right: 50px; top: 40px; margin: 0; font-family: {SERIF}; font-size: 600px; font-weight: 600; line-height: 1; {gt(GD)}">5</p>'
  f'<p style="position: absolute; left: 80px; top: 640px; width: 920px; margin: 0; font-size: 96px; font-weight: 800; letter-spacing: -3px; line-height: 1.02; color: {INK}">formas de sair da igreja <span style="font-family: {SERIF}; font-style: italic; font-weight: 600; letter-spacing: -1px; color: {GOLDTXT}">sem perceber</span></p>'
  f'<p style="position: absolute; left: 80px; top: 1000px; width: 820px; margin: 0; font-size: 36px; line-height: 1.45; color: {SOFT_W}">Ninguém abandona a fé de uma vez. A saída quase sempre é silenciosa.</p>'
  f'<div style="position: absolute; left: 80px; right: 80px; bottom: 96px; display: flex; justify-content: space-between; align-items: center"><p style="margin: 0; font-size: 24px; font-weight: 700; color: {MUTE_W}">@juliopalhoto</p><p style="margin: 0; font-size: 24px; font-weight: 700; letter-spacing: 4px; color: {INK}">ARRASTE &#8594;</p></div>',
  f'background: {WHITE}'))
items=[
 ('Aos poucos','Começa com “só este domingo”. Depois vira costume. Ninguém sai de uma vez: sai um domingo de cada vez.'),
 ('Pela ferida','Uma decepção com pessoas virou distância de Deus. Trate a ferida, mas não entregue a sua fé junto com ela.'),
 ('Pela agenda','Trabalho, cansaço, compromissos. Nada disso é errado. Mas, quando tudo cabe na semana menos Deus, a prioridade já mudou.'),
 ('Pelo coração','O corpo continua no banco, mas o coração já saiu. Cantar sem adorar, ouvir sem obedecer. É a saída mais difícil de notar.'),
 ('Pelo isolamento','Brasa fora do braseiro esfria. Fé sem comunhão também. Você não foi feito para caminhar sozinho.'),
]
for i,(t,b) in enumerate(items):
    slides.append(frame(
      f'<p style="position: absolute; left: 70px; top: 190px; margin: 0; font-family: {SERIF}; font-size: 240px; font-weight: 600; line-height: 1; {gt(GD)}">0{i+1}</p>'
      f'<div style="position: absolute; left: 80px; top: 470px; width: 120px; height: 4px; background: {G}"></div>'
      f'<p style="position: absolute; left: 80px; top: 520px; width: 920px; margin: 0; font-size: 96px; font-weight: 800; letter-spacing: -3px; line-height: 1.02; color: {INK}">{t}</p>'
      f'<p style="position: absolute; left: 80px; top: 700px; width: 900px; margin: 0; font-size: 50px; line-height: 1.45; color: {SOFT_W}">{b}</p>'
      + foot(i+1), f'background: {WHITE}'))
# fechamento escuro
slides.append(frame(
  f'<div style="position: absolute; left: 540px; top: 675px; width: 1000px; height: 1000px; margin: -500px 0 0 -500px; border-radius: 50%; border: 2px solid rgba(244,192,79,0.18)"></div>'
  + label('Se você se reconheceu', GOLD5, y=96) +
  f'<p style="position: absolute; left: 80px; top: 230px; width: 920px; margin: 0; font-size: 88px; font-weight: 800; letter-spacing: -2.5px; line-height: 1.04; color: #FFFFFF">A chama ainda pode ser <span style="{gt(G)}">reacesa.</span></p>'
  f'<p style="position: absolute; left: 80px; top: 560px; width: 900px; margin: 0; font-family: {SERIF}; font-style: italic; font-size: 54px; font-weight: 500; line-height: 1.2; color: #F2EEE6">“Não deixemos de congregar-nos, como é costume de alguns.”</p>'
  f'<p style="position: absolute; left: 80px; top: 720px; margin: 0; font-size: 26px; font-weight: 700; letter-spacing: 4px; color: {GOLD5}">HEBREUS 10.25 · ARA</p>'
  f'<p style="position: absolute; left: 80px; top: 860px; width: 900px; margin: 0; font-size: 40px; font-weight: 600; line-height: 1.4; color: #FFFFFF">Envie para alguém que precisa voltar.</p>'
  + handle_personal(A, dark=True, bottom=96), DARKBG))
fam=[('manrope','Manrope','normal',[300,400,500,600,700,800]),('cormorant-garamond','Cormorant Garamond','normal',[500,600]),('cormorant-garamond','Cormorant Garamond','italic',[500,600])]
faces=''.join(f"@font-face{{font-family:'{n}';font-style:{st};font-weight:{w};src:url(file:///home/claude/tpl/fonts/{f}-latin-{w}-{st}.woff2)}}" for f,n,st,ws in fam for w in ws)
from playwright.sync_api import sync_playwright
from PIL import Image
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,h in enumerate(slides):
        open(f'{OUT}/_tmp.html','w').write(f"<!doctype html><html><head><meta charset='utf-8'><style>{faces}body{{margin:0}}</style></head><body>{h}</body></html>")
        pg.goto(f'file://{OUT}/_tmp.html'); pg.wait_for_timeout(500)
        pg.screenshot(path=f'{OUT}/s.png'); Image.open(f'{OUT}/s.png').convert('RGB').save(f'{OUT}/a-chama-5-formas-{i+1:02d}.jpg',quality=93,optimize=True)
    b.close()
import os; os.remove(f'{OUT}/_tmp.html'); os.remove(f'{OUT}/s.png')
tw,th=360,450; s=Image.new('RGB',(4*(tw+16)+16,2*(th+16)+16),(120,120,120))
for i in range(N):
  s.paste(Image.open(f'{OUT}/a-chama-5-formas-{i+1:02d}.jpg').resize((tw,th),Image.LANCZOS),(16+(i%4)*(tw+16),16+(i//4)*(th+16)))
s.save('/home/claude/posts/chama-preview.png')
