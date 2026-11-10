import sys, json
sys.path.insert(0, '/home/claude/juliopalhoto/_sistema')
from render import render_slides, ASSETS

G = "linear-gradient(135deg, #E9A23B 0%, #FFD45E 45%, #FFEB8A 65%, #F2AE3F 100%)"
GT = f"background: {G}; -webkit-background-clip: text; background-clip: text; color: transparent"
DARK = "background: #0C0B09; background-image: radial-gradient(circle at 88% 8%, #3A2A0E 0%, #17120A 30%, #0C0B09 60%)"
PAPER = "background: #F3ECDD; background-image: linear-gradient(160deg, #FAF7F0 0%, #EFE6D2 100%)"
MONO = "'Liberation Mono', 'Courier New', monospace"
SANS = "'Manrope', Arial, sans-serif"; SERIF = "'Cormorant Garamond', Georgia, serif"

def frame(inner, bg):
    return f'<div style="position: relative; width: 1080px; height: 1350px; overflow: hidden; {bg}; font-family: {SANS}; font-variant-numeric: lining-nums">{inner}</div>'

def head(dark, page):
    logo = "{LOGO_GOLD}" if dark else "{LOGO_INK}"
    c = "#FAF7F0" if dark else "#14120D"; m = "#8C8578" if dark else "#6E675A"
    return (f'<div style="position: absolute; left: 88px; right: 88px; top: 80px; display: flex; justify-content: space-between; align-items: center">'
            f'<div style="display: flex; align-items: center; gap: 14px"><img src="{logo}" alt="" style="width: 64px; height: 64px"><span style="font-size: 28px; font-weight: 800; color: {c}">VSeven</span></div>'
            f'<span style="font-family: {MONO}; font-size: 22px; letter-spacing: 3px; color: {m}">ARQUIVO Nº 07 · {page}/10</span></div>')

def stamp(text, color, rot=-8, size=30, x=None, y=None, right=None):
    pos = f'left: {x}px;' if x is not None else f'right: {right}px;'
    return (f'<div style="position: absolute; {pos} top: {y}px; transform: rotate({rot}deg); border: 4px solid {color}; color: {color}; '
            f'font-family: {MONO}; font-weight: 700; font-size: {size}px; letter-spacing: 6px; padding: 10px 22px; border-radius: 6px; opacity: .9">{text}</div>')

def silhouette(w, fill, bar):
    h = int(w * 1.2)
    return (f'<div style="position: relative; width: {w}px; height: {h}px">'
            f'<svg width="{w}" height="{h}" viewBox="0 0 200 240" aria-hidden="true" style="position: absolute; left: 0; top: 0"><circle cx="100" cy="86" r="48" fill="{fill}"/><path d="M14 240 C14 176 56 144 100 144 C144 144 186 176 186 240 Z" fill="{fill}"/></svg>'
            f'<div style="position: absolute; left: {int(w*0.2)}px; width: {int(w*0.6)}px; top: {int(h*0.33)}px; height: {int(h*0.085)}px; background: {bar}; display: flex; align-items: center; justify-content: center">'
            f'<span style="font-family: {MONO}; font-size: {max(10,int(w*0.045))}px; letter-spacing: 3px; color: #F4C04F">CONFIDENCIAL</span></div></div>')

import os
FOTOS = '/home/claude/caso07/fotos'
def photo(w, key, label_bar=True):
    h = int(w * 1.2); y = int(h * 0.43); bh = int(h * 0.14)
    f = f'{FOTOS}/{key}.jpg'
    if key and os.path.exists(f):
        img = f'<img src="file://{f}" alt="" style="position: absolute; left: 0; top: 0; width: {w}px; height: {h}px; object-fit: cover">'
    else:
        img = (f'<div style="position: absolute; inset: 0; background: #2A251C; display: flex; align-items: flex-end; justify-content: center; padding-bottom: {int(h*0.12)}px; box-sizing: border-box">'
               f'<span style="font-family: {MONO}; font-size: {max(12,int(w*0.05))}px; letter-spacing: 3px; color: #8C8578">FOTO PENDENTE</span></div>')
    txt = f'<span style="font-family: {MONO}; font-size: {max(10,int(w*0.045))}px; letter-spacing: 3px; color: #F4C04F">CONFIDENCIAL</span>' if label_bar else ''
    return (f'<div style="position: relative; width: {w}px; height: {h}px; overflow: hidden; box-shadow: 0 24px 60px rgba(0,0,0,.45)">{img}'
            f'<div style="position: absolute; left: {int(w*0.12)}px; width: {int(w*0.76)}px; top: {y-bh//2}px; height: {bh}px; background: #0C0B09; display: flex; align-items: center; justify-content: center">{txt}</div></div>')

def mugboard(dark):
    bg = "#17140F" if dark else "#E6DCC6"; line = "#2B261C" if dark else "#CDBF9F"; num = "#5A5244" if dark else "#9C8E70"
    lines = "".join(f'<div style="position: absolute; left: 0; right: 0; top: {i*70}px; border-top: 2px solid {line}"><span style="position: absolute; left: 12px; top: 4px; font-family: {MONO}; font-size: 18px; color: {num}">{(19-i)*10}</span></div>' for i in range(1,9))
    return f'<div style="position: absolute; left: 88px; right: 88px; top: 200px; height: 600px; background: {bg}; border-radius: 16px; overflow: hidden">{lines}</div>'

KEYS = ["julio","evellyn","abner","gabriel"]
slides = []
SUSP = [  # key, area, nome, funcao, assinatura
 ("julio","GESTÃO","JÚLIO PALHOTO","Define a estratégia e conecta as frentes.","Toda decisão começa pelo resultado."),
 ("evellyn","OPERAÇÃO","EVELLYN MALHEIROS","Transforma cada plano em entrega.","Prazo, processo e padrão em cada projeto."),
 ("abner","BRANDING","MATHEUS ABNER","Dá nome, voz e valor à marca.","Marcas que as pessoas reconhecem e lembram."),
 ("gabriel","RELACIONAMENTO","GABRIEL JAVEX","Cuida do cliente do primeiro contato à parceria.","Cada cliente acompanhado de perto."),
]
KEYS = [k for k,*_ in SUSP]
arrow = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#F4C04F" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M13 6l6 6-6 6"/></svg>'

# 1 Capa
slides.append(frame(
    head(True, "01") +
    f'<div style="position: absolute; left: 88px; right: 88px; top: 190px; display: flex; justify-content: space-between">{"".join(photo(214, k, False) for k in KEYS)}</div>' +
    stamp("CONFIDENCIAL", "#F4C04F", rot=-6, size=34, x=640, y=440) +
    f'<p style="position: absolute; left: 88px; top: 560px; width: 920px; margin: 0; font-size: 104px; font-weight: 800; letter-spacing: -4px; line-height: 1; color: #FAF7F0">Eles diziam ser uma agência.</p>'
    f'<p style="position: absolute; left: 88px; top: 790px; margin: 0; font-family: {SERIF}; font-style: italic; font-weight: 600; font-size: 130px; line-height: 1; {GT}; padding-right: 24px">Não eram.</p>'
    f'<p style="position: absolute; left: 88px; top: 960px; width: 820px; margin: 0; font-size: 34px; line-height: 1.4; color: #CFC8B8">Abrimos a investigação. Veja o que encontramos.</p>'
    f'<div style="position: absolute; left: 88px; right: 88px; bottom: 96px; display: flex; justify-content: space-between; align-items: center"><span style="font-family: {MONO}; font-size: 22px; letter-spacing: 3px; color: #8C8578">INVESTIGAÇÃO EM ANDAMENTO</span>'
    f'<span style="display: flex; align-items: center; gap: 14px; border: 1px solid #F4C04F; border-radius: 999px; padding: 16px 28px; font-size: 22px; font-weight: 700; letter-spacing: 3px; color: #F4C04F">ABRA O ARQUIVO {arrow}</span></div>',
    DARK))
# 2 Evidências
ev = [("01","Software rodando em produção."),("02","Estratégia de marca — não só post."),("03","Funil montado do lead ao contrato.")]
evh = "".join(f'<div style="display: flex; align-items: center; gap: 36px"><div style="flex: none; width: 120px; height: 120px; background: {G}; clip-path: polygon(50% 0, 100% 100%, 0 100%); display: flex; align-items: flex-end; justify-content: center; padding-bottom: 16px; box-sizing: border-box"><span style="font-family: {MONO}; font-weight: 700; font-size: 30px; color: #14120D">{n}</span></div><span style="font-size: 50px; font-weight: 800; letter-spacing: -1.5px; line-height: 1.1; color: #14120D">{t}</span></div>' for n,t in ev)
slides.append(frame(
    head(False, "02") +
    f'<p style="position: absolute; left: 88px; top: 240px; margin: 0; font-family: {MONO}; font-size: 26px; letter-spacing: 5px; color: #8F6214">EVIDÊNCIAS ENCONTRADAS NO LOCAL</p>'
    f'<div style="position: absolute; left: 88px; right: 88px; top: 340px; display: flex; flex-direction: column; gap: 60px">{evh}</div>'
    f'<p style="position: absolute; left: 88px; right: 88px; bottom: 120px; margin: 0; font-family: {SERIF}; font-style: italic; font-size: 64px; line-height: 1.12; color: #14120D">Isso não é trabalho <span style="color: #8F6214">de uma agência.</span></p>',
    PAPER))
# 3 A pista
slides.append(frame(
    head(True, "03") +
    f'<p style="position: absolute; left: 88px; top: 300px; margin: 0; font-family: {MONO}; font-size: 26px; letter-spacing: 5px; color: #F4C04F">A PISTA</p>'
    f'<p style="position: absolute; left: 88px; top: 380px; width: 900px; margin: 0; font-size: 104px; font-weight: 800; letter-spacing: -3.5px; line-height: 1.02; color: #FAF7F0">Não era uma pessoa.</p>'
    f'<p style="position: absolute; left: 88px; top: 640px; width: 920px; margin: 0; font-family: {SERIF}; font-style: italic; font-weight: 600; font-size: 116px; line-height: 1; {GT}; padding-right: 20px">Era uma operação inteira.</p>'
    f'<p style="position: absolute; left: 88px; right: 88px; bottom: 120px; margin: 0; font-size: 36px; line-height: 1.4; color: #CFC8B8">Quatro nomes no topo do arquivo.</p>',
    DARK))
# 4-7 Fichas
for i,(k,area,nome,func,ass) in enumerate(SUSP):
    dark = (i % 2 == 0)
    ink = "#FAF7F0" if dark else "#14120D"; acc = "#F4C04F" if dark else "#8F6214"
    slides.append(frame(
        head(dark, f"0{4+i}") + mugboard(dark) +
        f'<div style="position: absolute; left: 0; right: 0; top: 240px; display: flex; justify-content: center">{photo(440, k)}</div>'
        f'<div style="position: absolute; left: 50%; transform: translateX(-50%); top: 740px; background: #0C0B09; border: 2px solid #F4C04F; border-radius: 8px; padding: 16px 40px; font-family: {MONO}; font-weight: 700; font-size: 34px; letter-spacing: 6px; color: #F4C04F; white-space: nowrap">SUSPEITO 0{i+1} · {area}</div>'
        f'<p style="position: absolute; left: 0; right: 0; top: 838px; margin: 0; text-align: center; font-family: {MONO}; font-size: 24px; letter-spacing: 5px; color: {acc}">{nome}</p>'
        f'<div style="position: absolute; left: 88px; right: 88px; top: 920px; display: flex; flex-direction: column; gap: 26px">'
        f'<div><p style="margin: 0; font-family: {MONO}; font-size: 22px; letter-spacing: 4px; color: {acc}">FUNÇÃO NO CASO</p><p style="margin: 6px 0 0; font-size: 46px; font-weight: 800; letter-spacing: -1px; line-height: 1.15; color: {ink}">{func}</p></div>'
        f'<div><p style="margin: 0; font-family: {MONO}; font-size: 22px; letter-spacing: 4px; color: {acc}">ASSINATURA</p><p style="margin: 6px 0 0; font-family: {SERIF}; font-style: italic; font-size: 54px; font-weight: 600; line-height: 1.1; color: {ink}">{ass}</p></div></div>',
        DARK if dark else PAPER))
# 8 Time oculto
team = ["MOISÉS","VINÍCIUS","DANIEL"]
def tcard(name, inner):
    return (f'<div style="width: 196px; background: #FAF7F0; padding: 12px 12px 10px; box-shadow: 0 18px 40px rgba(0,0,0,.45)">'
            f'<div style="background: #2A251C; height: 230px; display: flex; justify-content: center; align-items: flex-end; overflow: hidden">{inner}</div>'
            f'<p style="margin: 10px 0 0; text-align: center; font-family: {MONO}; font-weight: 700; font-size: 20px; letter-spacing: 3px; color: #14120D">{name}</p></div>')
def hidden(w):
    h = int(w*1.2)
    return (f'<div style="position: relative; width: {w}px; height: {h}px"><svg width="{w}" height="{h}" viewBox="0 0 200 240" aria-hidden="true" style="position: absolute; left: 0; top: 0"><circle cx="100" cy="86" r="48" fill="#4A4236"/><path d="M14 240 C14 176 56 144 100 144 C144 144 186 176 186 240 Z" fill="#4A4236"/></svg>'
            f'<span style="position: absolute; left: 0; right: 0; top: {int(h*0.2)}px; text-align: center; font-family: {SERIF}; font-weight: 600; font-size: {int(w*0.42)}px; line-height: 1; color: #F4C04F">?</span></div>')
cards8 = "".join(tcard(n, hidden(172)) for n in team)
cards8 += tcard("PARCEIROS", f'<div style="height: 230px; display: flex; align-items: center; justify-content: center"><span style="font-size: 120px; font-weight: 300; {GT}">+</span></div>')
slides.append(frame(
    head(True, "08") +
    f'<p style="position: absolute; left: 88px; top: 230px; margin: 0; font-family: {MONO}; font-size: 26px; letter-spacing: 5px; color: #F4C04F">NOVAS PISTAS</p>'
    f'<p style="position: absolute; left: 88px; right: 88px; top: 300px; margin: 0; font-size: 86px; font-weight: 800; letter-spacing: -3px; line-height: 1.02; color: #FAF7F0">Eles não agiam sozinhos.</p>'
    f'<div style="position: absolute; left: 88px; right: 88px; top: 580px; display: flex; justify-content: space-between">{cards8}</div>' +
    stamp("IDENTIDADE PROTEGIDA", "#F4C04F", rot=-4, size=24, x=560, y=490) +
    f'<p style="position: absolute; left: 88px; right: 88px; top: 950px; margin: 0; font-family: {SERIF}; font-style: italic; font-weight: 600; font-size: 72px; line-height: 1.08; {GT}; padding-right: 20px">Por trás deles, um time inteiro.</p>'
    f'<p style="position: absolute; left: 88px; right: 88px; bottom: 110px; margin: 0; font-family: {MONO}; font-size: 24px; letter-spacing: 3px; color: #CFC8B8">IDENTIDADES REVELADAS NOS PRÓXIMOS ARQUIVOS.</p>',
    DARK))
# 9 Revelação
cards = [(150, 300, "GESTÃO"), (700, 300, "OPERAÇÃO"), (150, 690, "BRANDING"), (700, 690, "RELACIONAMENTO")]
cx, cy = 540, 560
strings = "".join(f'<line x1="{x+115}" y1="{y+125}" x2="{cx}" y2="{cy}" stroke="#F4C04F" stroke-width="3"/>' for x,y,_ in cards)
board = f'<svg width="1080" height="1350" viewBox="0 0 1080 1350" aria-hidden="true" style="position: absolute; left: 0; top: 0">{strings}</svg>'
cardh = "".join(f'<div style="position: absolute; left: {x}px; top: {y}px; width: 230px; background: #FAF7F0; padding: 14px 14px 12px; box-shadow: 0 18px 40px rgba(0,0,0,.45); transform: rotate({(-3,2,3,-2)[k]}deg)"><div style="display: flex; justify-content: center">{photo(202, KEYS[k], False)}</div><p style="margin: 10px 0 0; text-align: center; font-family: {MONO}; font-weight: 700; font-size: {20 if len(t)<10 else 16}px; letter-spacing: {3 if len(t)<10 else 1}px; color: #14120D">{t}</p><div style="position: absolute; left: 50%; top: -10px; width: 22px; height: 22px; margin-left: -11px; border-radius: 50%; background: {G}"></div></div>' for k,(x,y,t) in enumerate(cards))
center = f'<div style="position: absolute; left: {cx-90}px; top: {cy-90}px; width: 180px; height: 180px; border-radius: 50%; background: #0C0B09; border: 3px solid #F4C04F; display: flex; align-items: center; justify-content: center"><img src="{{LOGO_GOLD}}" alt="" style="width: 120px; height: 120px"></div>'
slides.append(frame(
    head(True, "09") + board + cardh + center +
    f'<p style="position: absolute; left: 88px; right: 88px; top: 1030px; margin: 0; font-size: 62px; font-weight: 800; letter-spacing: -2px; line-height: 1.05; color: #FAF7F0">Cada um com sua expertise.</p>'
    f'<p style="position: absolute; left: 88px; right: 88px; top: 1110px; margin: 0; font-family: {SERIF}; font-style: italic; font-weight: 600; font-size: 70px; line-height: 1.1; {GT}; padding-right: 20px">Juntos, uma solução completa.</p>',
    DARK))
# 10 Caso resolvido
slides.append(frame(
    f'<div style="position: absolute; left: 88px; right: 88px; top: 80px; display: flex; justify-content: space-between; align-items: center"><span style="font-family: {MONO}; font-size: 22px; letter-spacing: 3px; color: #14120D">ARQUIVO Nº 07 · 10/10</span></div>' +
    stamp("CASO RESOLVIDO", "#14120D", rot=-5, size=34, x=88, y=190) +
    f'<p style="position: absolute; left: 88px; right: 88px; top: 330px; margin: 0; font-family: {MONO}; font-size: 26px; letter-spacing: 5px; color: #14120D">VEREDITO</p>'
    f'<p style="position: absolute; left: 88px; right: 88px; top: 380px; margin: 0; font-size: 74px; font-weight: 800; letter-spacing: -2.5px; line-height: 1.04; color: #14120D">Não somos uma agência tradicional.</p>'
    f'<p style="position: absolute; left: 88px; right: 88px; top: 580px; margin: 0; font-size: 38px; line-height: 1.35; font-weight: 600; color: #14120D">Somos a VSeven: uma empresa que une <b>Marketing, Branding, Tecnologia e Vendas</b> em soluções para grandes empresas.</p>'
    f'<div style="position: absolute; left: 88px; top: 820px; display: flex; align-items: center; gap: 18px; background: #14120D; border-radius: 999px; padding: 26px 44px"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#F4C04F" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg><span style="font-size: 32px; font-weight: 800; letter-spacing: 1px; color: #F4C04F">Qual frente sua empresa precisa agora?</span></div>'
    f'<p style="position: absolute; left: 88px; right: 88px; top: 960px; margin: 0; font-size: 32px; line-height: 1.4; font-weight: 600; color: #14120D">Comente ou chame a VSeven no direct.</p>'
    f'<div style="position: absolute; left: 88px; right: 88px; bottom: 90px; display: flex; justify-content: space-between; align-items: center"><div style="display: flex; align-items: center; gap: 22px"><img src="{{LOGO_INK}}" alt="" style="width: 110px; height: 110px"><div><p style="margin: 0; font-size: 40px; font-weight: 800; color: #14120D">VSeven</p><p style="margin: 2px 0 0; font-size: 21px; font-weight: 700; letter-spacing: 1px; color: #14120D">Marketing · Branding · Tecnologia · Vendas</p></div></div><span style="font-size: 24px; font-weight: 700; color: #14120D">grupovseven.com</span></div>',
    f"background: {G}"))

json.dump(slides, open('/home/claude/caso07/v2/html.json','w'), ensure_ascii=False)
out = [s.replace('{LOGO_GOLD}', ASSETS['logo_gold']).replace('{LOGO_INK}', ASSETS['logo_ink']) for s in slides]
for p in render_slides(out, sys.argv[1], 'caso-07'): print(p)
