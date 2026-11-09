# Templates de posts do Instagram: @juliopalhoto (pessoal) e VSeven.
# Cada função recebe A (urls dos assets) e devolve o HTML de um slide 1080x1350.
W, H = 1080, 1350
INK = '#14120D'; SOFT = '#4A4438'; MUTE = '#6E675A'; BLACK = '#0C0B09'
OFF = '#F5F0E6'; PAPER = '#FBF8F2'; GOLDTXT = '#8F6214'; GOLD5 = '#F4C04F'
WHITE = '#FFFFFF'; SOFT_W = '#444444'; MUTE_W = '#6B6B6B'; LINE_W = '#E6E6E6'
G = 'linear-gradient(135deg, #E9A23B 0%, #FFD45E 45%, #FFEB8A 65%, #F2AE3F 100%)'
GD = 'linear-gradient(120deg, #7A5210 0%, #B98424 55%, #8F6214 100%)'
SANS = "'Manrope', Arial, sans-serif"; SERIF = "'Cormorant Garamond', Georgia, serif"; HAND = "'Caveat', 'Brush Script MT', cursive"
DARKBG = f'background: {BLACK}; background-image: radial-gradient(circle at 85% 12%, #4A3511 0%, #1C150B 30%, #0C0B09 62%)'

def gt(grad):  # texto com gradiente
    return f'background: {grad}; -webkit-background-clip: text; background-clip: text; color: transparent'

def frame(inner, bg, extra=''):
    return f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; {bg}; font-family: {SANS}; font-variant-numeric: lining-nums; {extra}">{inner}</div>'

def label(text, color, bar=G, x=80, y=80):
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; display: flex; align-items: center; gap: 16px">'
            f'<div style="width: 56px; height: 4px; border-radius: 2px; background: {bar}"></div>'
            f'<p style="margin: 0; font-size: 22px; font-weight: 700; letter-spacing: 6px; text-transform: uppercase; color: {color}">{text}</p></div>')

def handle_personal(A, dark=False, x=80, bottom=80):
    c = '#FAF7F0' if dark else INK; m = '#A9A193' if dark else MUTE_W
    return (f'<div style="position: absolute; left: {x}px; bottom: {bottom}px; display: flex; align-items: center; gap: 18px">'
            f'<img src="{A["avatar"]}" alt="Julio Palhoto" style="width: 84px; height: 84px; border-radius: 50%; object-fit: cover; border: 3px solid #E9B44C">'
            f'<div style="display: flex; flex-direction: column; gap: 2px"><p style="margin: 0; font-size: 28px; font-weight: 800; color: {c}">Julio Palhoto</p>'
            f'<p style="margin: 0; font-size: 22px; font-weight: 500; color: {m}">@juliopalhoto</p></div></div>')

def vs_footer(A, dark=True, x=80, bottom=72):
    c = '#FAF7F0' if dark else INK; logo = A['logo_gold'] if dark else A['logo_ink']
    return (f'<div style="position: absolute; left: {x}px; right: {x}px; bottom: {bottom}px; display: flex; align-items: center; justify-content: space-between">'
            f'<div style="display: flex; align-items: center; gap: 14px"><img src="{logo}" alt="VSeven" style="width: 64px; height: 64px; object-fit: contain">'
            f'<p style="margin: 0; font-size: 30px; font-weight: 800; letter-spacing: -0.5px; color: {c}">VSeven</p></div>'
            f'<p style="margin: 0; font-size: 22px; font-weight: 600; letter-spacing: 1px; color: {"#A9A193" if dark else MUTE}">grupovseven.com</p></div>')

def hl(text):  # marca-texto dourado sobre papel
    return f'<span style="background: linear-gradient(180deg, rgba(255,212,94,0) 58%, #FFD45E 58%, #FFD45E 92%, rgba(255,212,94,0) 92%)">{text}</span>'

# ---------------- PESSOAL ----------------
def p1_frase(A):
    inner = (f'<div style="position: absolute; left: 40px; top: 40px; right: 40px; bottom: 40px; border: 1px solid #D9C49A"></div>'
             + label('Reflexão', GOLDTXT, x=80, y=96) +
             f'<p style="position: absolute; left: 72px; top: 150px; margin: 0; font-family: {SERIF}; font-size: 340px; font-weight: 600; line-height: 1; {gt(GD)}">&#8220;</p>'
             f'<p style="position: absolute; left: 80px; top: 430px; width: 920px; margin: 0; font-family: {SERIF}; font-style: italic; font-size: 86px; font-weight: 500; line-height: 1.08; color: {INK}">Marca forte não é a que aparece mais. É a que é <span style="color: {GOLDTXT}">lembrada</span> quando importa.</p>'
             + handle_personal(A, bottom=96))
    return frame(inner, f'background: {WHITE}')

def p2_foto(A):
    inner = (f'<div style="position: absolute; left: 420px; top: 520px; width: 900px; height: 900px; border-radius: 50%; background: {BLACK}; background-image: radial-gradient(circle at 40% 35%, #3E2D0F 0%, #0C0B09 65%)"></div>'
             f'<div style="position: absolute; left: 380px; top: 480px; width: 980px; height: 980px; border-radius: 50%; border: 3px solid #D9A84C"></div>'
             f'<img src="{A["julio_cut"]}" alt="Julio Palhoto" style="position: absolute; left: 400px; top: 470px; width: 880px; height: 880px; object-fit: contain; object-position: bottom">'
             + label('Marketing sem romantismo', GOLDTXT, y=96) +
             f'<p style="position: absolute; left: 80px; top: 170px; width: 900px; margin: 0; font-size: 92px; font-weight: 800; letter-spacing: -3px; line-height: 1.02; color: {INK}">Ninguém compra o que {hl("não entende.")}</p>'
             f'<p style="position: absolute; left: 80px; top: 600px; width: 380px; margin: 0; font-size: 30px; line-height: 1.4; color: {SOFT_W}">Clareza vende mais do que criatividade sem direção.</p>'
             f'<p style="position: absolute; left: 80px; bottom: 96px; margin: 0; font-size: 24px; font-weight: 700; color: {MUTE_W}">@juliopalhoto</p>')
    return frame(inner, f'background: {WHITE}')

def p3_carrossel(A):
    s1 = frame(label('Carrossel', GOLDTXT, y=96) +
               f'<p style="position: absolute; right: 40px; top: 60px; margin: 0; font-family: {SERIF}; font-size: 560px; font-weight: 600; line-height: 1; {gt(GD)}">5</p>'
               f'<p style="position: absolute; left: 80px; top: 640px; width: 900px; margin: 0; font-size: 84px; font-weight: 800; letter-spacing: -2.5px; line-height: 1.04; color: {INK}">erros que fazem sua marca parecer <span style="font-family: {SERIF}; font-style: italic; font-weight: 600; color: {GOLDTXT}">pequena</span></p>'
               f'<div style="position: absolute; left: 80px; right: 80px; bottom: 96px; display: flex; justify-content: space-between; align-items: center"><p style="margin: 0; font-size: 24px; font-weight: 700; color: {MUTE_W}">@juliopalhoto</p><p style="margin: 0; font-size: 24px; font-weight: 700; letter-spacing: 4px; color: {INK}">ARRASTE &#8594;</p></div>',
               f'background: {WHITE}')
    dots = ''.join(f'<div style="width: {36 if i==1 else 12}px; height: 12px; border-radius: 6px; background: {INK if i==1 else "#DADADA"}"></div>' for i in range(5))
    s2 = frame(f'<p style="position: absolute; left: 70px; top: 90px; margin: 0; font-family: {SERIF}; font-size: 200px; font-weight: 600; line-height: 1; {gt(GD)}">01</p>'
               f'<div style="position: absolute; left: 80px; top: 330px; width: 120px; height: 4px; background: {G}"></div>'
               f'<p style="position: absolute; left: 80px; top: 380px; width: 920px; margin: 0; font-size: 80px; font-weight: 800; letter-spacing: -2.5px; line-height: 1.05; color: {INK}">Falar de tudo para todo mundo</p>'
               f'<p style="position: absolute; left: 80px; top: 680px; width: 900px; margin: 0; font-size: 44px; line-height: 1.5; color: {SOFT_W}">Quando a mensagem tenta agradar a todos, ela não convence ninguém. Escolha para quem você fala e diga isso com clareza.</p>'
               f'<div style="position: absolute; left: 80px; bottom: 110px; display: flex; gap: 10px">{dots}</div>'
               f'<p style="position: absolute; right: 80px; bottom: 96px; margin: 0; font-size: 24px; font-weight: 700; color: {MUTE_W}">@juliopalhoto</p>',
               f'background: {WHITE}')
    s3 = frame(f'<div style="position: absolute; left: 540px; top: 675px; width: 1000px; height: 1000px; margin: -500px 0 0 -500px; border-radius: 50%; border: 2px solid rgba(244,192,79,0.35)"></div>'
               + label('Para guardar', GOLD5, y=96) +
               f'<p style="position: absolute; left: 80px; top: 360px; width: 920px; margin: 0; font-size: 86px; font-weight: 800; letter-spacing: -2.5px; line-height: 1.05; color: #FAF7F0">Salve este post e mande para quem <span style="{gt(G)}">precisa ouvir isso.</span></p>'
               + handle_personal(A, dark=True, bottom=96),
               DARKBG)
    return [s1, s2, s3]

def p4_dossie(A):
    tape = lambda l, t, r: f'<div style="position: absolute; left: {l}px; top: {t}px; width: 170px; height: 52px; background: rgba(233,216,170,0.75); transform: rotate({r}deg); box-shadow: 0 2px 6px rgba(0,0,0,0.08)"></div>'
    inner = (
        # folha do dossiê
        f'<div style="position: absolute; left: 70px; top: 120px; width: 940px; height: 1110px; background: {WHITE}; border: 1px solid #E2E2E2; transform: rotate(-1.5deg); box-shadow: 0 30px 60px rgba(0,0,0,0.14)">'
        f'<div style="position: absolute; left: 60px; top: 60px; right: 60px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid {INK}; padding-bottom: 18px">'
        f'<p style="margin: 0; font-family: \'Courier New\', monospace; font-size: 28px; font-weight: 700; letter-spacing: 3px; color: {INK}">DOSSIÊ · CASO Nº 07</p>'
        f'<p style="margin: 0; font-family: \'Courier New\', monospace; font-size: 24px; color: {MUTE_W}">CONFIDENCIAL</p></div>'
        f'<p style="position: absolute; left: 60px; top: 170px; width: 820px; margin: 0; font-size: 76px; font-weight: 800; letter-spacing: -2.5px; line-height: 1.04; color: {INK}">O caso do perfil bonito que <span style="position: relative">{hl("não vendia.")}</span></p>'
        # cartões de evidência
        f'<div style="position: absolute; left: 60px; top: 560px; width: 380px; height: 300px; background: #FFFFFF; border: 1px solid #E6E6E6; box-shadow: 0 10px 24px rgba(0,0,0,0.12); transform: rotate(-3deg); padding: 28px; box-sizing: border-box">'
        f'<p style="margin: 0; font-family: \'Courier New\', monospace; font-size: 22px; font-weight: 700; color: {MUTE_W}">PROVA A</p>'
        f'<p style="margin: 18px 0 0; font-family: {HAND}; font-size: 64px; font-weight: 700; line-height: 1; color: {INK}">feed lindo</p>'
        f'<p style="margin: 10px 0 0; font-family: {HAND}; font-size: 44px; line-height: 1.1; color: {SOFT_W}">muitas curtidas</p></div>'
        f'<div style="position: absolute; left: 480px; top: 600px; width: 380px; height: 300px; background: #FFFFFF; border: 1px solid #E6E6E6; box-shadow: 0 10px 24px rgba(0,0,0,0.12); transform: rotate(2.5deg); padding: 28px; box-sizing: border-box">'
        f'<p style="margin: 0; font-family: \'Courier New\', monospace; font-size: 22px; font-weight: 700; color: {MUTE_W}">PROVA B</p>'
        f'<p style="margin: 18px 0 0; font-family: {HAND}; font-size: 64px; font-weight: 700; line-height: 1; color: {INK}">zero vendas</p>'
        f'<p style="margin: 10px 0 0; font-family: {HAND}; font-size: 44px; line-height: 1.1; color: {SOFT_W}">nenhum pedido</p></div>'
        # fio dourado entre as provas
        f'<svg width="940" height="1110" style="position: absolute; left: 0; top: 0" aria-hidden="true"><path d="M250 575 C 400 520, 560 540, 670 615" fill="none" stroke="#B98424" stroke-width="4"></path>'
        f'<circle cx="250" cy="575" r="12" fill="#B98424"></circle><circle cx="670" cy="615" r="12" fill="#B98424"></circle></svg>'
        f'<p style="position: absolute; left: 60px; top: 930px; width: 480px; margin: 0; font-family: {HAND}; font-size: 54px; line-height: 1.1; color: {GOLDTXT}">pista: ninguém sabia o que ela vendia...</p>'
        f'</div>'
        + tape(110, 95, -8) + tape(820, 1180, -6) +
        # carimbo
        f'<div style="position: absolute; left: 640px; top: 1075px; padding: 14px 30px; border: 6px solid {INK}; border-radius: 10px; transform: rotate(-12deg); opacity: 0.85">'
        f'<p style="margin: 0; font-family: \'Courier New\', monospace; font-size: 44px; font-weight: 700; letter-spacing: 6px; color: {INK}">ANALISADO</p></div>'
        f'<p style="position: absolute; left: 80px; bottom: 40px; margin: 0; font-size: 22px; font-weight: 700; color: {MUTE_W}">@juliopalhoto · arraste para a investigação &#8594;</p>')
    return frame(inner, f'background: {WHITE}')

def p5_diario(A):
    lines = 'background: #FFFFFF; background-image: repeating-linear-gradient(180deg, rgba(0,0,0,0) 0px, rgba(0,0,0,0) 63px, #ECECEC 63px, #ECECEC 65px)'
    inner = (f'<div style="position: absolute; left: 150px; top: 0; width: 3px; height: {H}px; background: {G}"></div>'
             f'<p style="position: absolute; left: 190px; top: 84px; margin: 0; font-size: 22px; font-weight: 700; letter-spacing: 6px; color: {GOLDTXT}">DIÁRIO DE CEO</p>'
             f'<p style="position: absolute; left: 186px; top: 118px; margin: 0; font-family: {HAND}; font-size: 120px; font-weight: 700; line-height: 1; color: {INK}">Dia 14</p>'
             # polaroid
             f'<div style="position: absolute; left: 700px; top: 80px; width: 300px; height: 360px; background: #FFFFFF; padding: 18px 18px 70px; box-sizing: border-box; transform: rotate(5deg); box-shadow: 0 16px 30px rgba(0,0,0,0.18)">'
             f'<img src="{A["avatar"]}" alt="Julio Palhoto" style="width: 264px; height: 272px; object-fit: cover; display: block">'
             f'<p style="margin: 10px 0 0; text-align: center; font-family: {HAND}; font-size: 34px; color: {SOFT_W}">bastidores</p></div>'
             f'<div style="position: absolute; left: 790px; top: 60px; width: 130px; height: 44px; background: rgba(233,216,170,0.8); transform: rotate(-4deg)"></div>'
             f'<p style="position: absolute; left: 190px; top: 520px; width: 800px; margin: 0; font-family: {HAND}; font-size: 72px; font-weight: 600; line-height: 1.33; color: {INK}">Hoje recusei um cliente. Não foi por dinheiro, foi por <span style="color: {GOLDTXT}">alinhamento</span>.</p>'
             f'<p style="position: absolute; left: 190px; top: 960px; width: 800px; margin: 0; font-family: {HAND}; font-size: 54px; line-height: 1.2; color: {SOFT_W}">Crescer também é saber dizer não.</p>'
             f'<p style="position: absolute; right: 80px; bottom: 90px; margin: 0; font-family: {HAND}; font-size: 64px; font-weight: 700; color: {INK}">— Julio</p>')
    return frame(inner, lines)

def p6_numero(A):
    inner = (label('Dado', GOLDTXT, y=96) +
             f'<p style="position: absolute; left: 60px; top: 170px; margin: 0; font-family: {SERIF}; font-size: 400px; font-weight: 600; line-height: 1; letter-spacing: -10px; {gt(GD)}">XX%</p>'
             f'<div style="position: absolute; left: 80px; top: 640px; width: 160px; height: 4px; background: {G}"></div>'
             f'<p style="position: absolute; left: 80px; top: 690px; width: 900px; margin: 0; font-size: 64px; font-weight: 800; letter-spacing: -2px; line-height: 1.1; color: {INK}">dos clientes pesquisam sua marca antes de falar com você.</p>'
             f'<p style="position: absolute; left: 80px; top: 1000px; width: 900px; margin: 0; font-size: 34px; line-height: 1.45; color: {SOFT_W}">O que eles encontram hoje vende por você?</p>'
             f'<p style="position: absolute; right: 80px; bottom: 110px; margin: 0; font-size: 20px; color: {MUTE_W}">Fonte: [inserir fonte do dado]</p>'
             + handle_personal(A, bottom=86))
    return frame(inner, f'background: {WHITE}')

# ---------------- VSEVEN ----------------
def rings(cx, cy, color='#F4C04F', base=1.0):
    return ''.join(f'<div style="position: absolute; left: {cx-r}px; top: {cy-r}px; width: {2*r}px; height: {2*r}px; border-radius: 50%; border: 2px solid {color}; opacity: {o*base}"></div>' for r, o in [(260, 0.45), (360, 0.25), (470, 0.12)])

def v1_preto(A):
    inner = (rings(900, 1150) +
             f'<img src="{A["logo_gold"]}" alt="VSeven" style="position: absolute; left: 80px; top: 80px; width: 96px; height: 96px; object-fit: contain">'
             f'<p style="position: absolute; left: 80px; top: 360px; width: 920px; margin: 0; font-size: 104px; font-weight: 800; letter-spacing: -3.5px; line-height: 1.0; color: #FAF7F0">Marketing sem estratégia é só <span style="{gt(G)}">barulho.</span></p>'
             f'<p style="position: absolute; left: 80px; top: 820px; width: 700px; margin: 0; font-size: 34px; line-height: 1.45; color: #CFC8B8">Planejamento, execução e análise em um só lugar.</p>'
             + vs_footer(A, dark=True))
    return frame(inner, DARKBG)

def v2_ouro(A):
    inner = (f'<img src="{A["logo_ink"]}" alt="" style="position: absolute; left: 560px; top: 520px; width: 760px; height: 760px; object-fit: contain; opacity: 0.12">'
             f'<img src="{A["logo_ink"]}" alt="VSeven" style="position: absolute; left: 80px; top: 80px; width: 96px; height: 96px; object-fit: contain">'
             f'<p style="position: absolute; left: 80px; top: 380px; width: 920px; margin: 0; font-size: 120px; font-weight: 800; letter-spacing: -4px; line-height: 0.98; color: {INK}">Sua marca merece ser lembrada.</p>'
             f'<p style="position: absolute; left: 80px; bottom: 90px; margin: 0; padding: 18px 36px; border-radius: 999px; background: {BLACK}; font-size: 28px; font-weight: 700; color: {GOLD5}">grupovseven.com</p>')
    return frame(inner, f'background: {G}')

def v3_carrossel(A):
    s1 = frame(label('Soluções VSeven', GOLDTXT, y=96) +
               f'<p style="position: absolute; right: 50px; top: 120px; margin: 0; font-family: {SERIF}; font-size: 420px; font-weight: 600; line-height: 1; {gt(GD)}">3</p>'
               f'<p style="position: absolute; left: 80px; top: 600px; width: 920px; margin: 0; font-size: 88px; font-weight: 800; letter-spacing: -3px; line-height: 1.02; color: {INK}">passos para transformar seguidores em <span style="{gt(GD)}">clientes</span></p>'
               f'<div style="position: absolute; left: 80px; right: 80px; bottom: 80px; display: flex; justify-content: space-between; align-items: center"><img src="{A["logo_ink"]}" alt="VSeven" style="width: 64px; height: 64px; object-fit: contain"><p style="margin: 0; font-size: 24px; font-weight: 700; letter-spacing: 4px; color: {INK}">ARRASTE &#8594;</p></div>',
               f'background: {OFF}')
    items = [('Diagnóstico', 'Entender o negócio, o público e o que já funciona.'), ('Conteúdo com intenção', 'Cada post com um papel claro na jornada.'), ('Conversão medida', 'Do clique à conversa, com dados.')]
    rows = ''.join(f'<div style="display: flex; gap: 28px; align-items: flex-start; border-top: 1px solid #2B261C; padding: 50px 0"><p style="margin: 0; width: 130px; font-family: {SERIF}; font-size: 100px; font-weight: 600; line-height: 1; {gt(G)}">0{i+1}</p><div style="flex: 1; display: flex; flex-direction: column; gap: 8px"><p style="margin: 0; font-size: 54px; font-weight: 800; letter-spacing: -1px; color: #FAF7F0">{a}</p><p style="margin: 0; font-size: 36px; line-height: 1.4; color: #CFC8B8">{b}</p></div></div>' for i, (a, b) in enumerate(items))
    s2 = frame(label('O método', GOLD5, y=96) +
               f'<div style="position: absolute; left: 80px; right: 80px; top: 230px; display: flex; flex-direction: column">{rows}</div>'
               + vs_footer(A, dark=True), DARKBG)
    s3 = frame(f'<img src="{A["logo_ink"]}" alt="" style="position: absolute; left: 290px; top: 170px; width: 500px; height: 500px; object-fit: contain">'
               f'<p style="position: absolute; left: 80px; top: 760px; width: 920px; margin: 0; text-align: center; font-size: 84px; font-weight: 800; letter-spacing: -2.5px; line-height: 1.04; color: {INK}">Vamos aumentar suas vendas?</p>'
               f'<p style="position: absolute; left: 0; width: {W}px; top: 1010px; margin: 0; text-align: center; font-size: 34px; font-weight: 600; color: #2E2410">Fale com a VSeven</p>'
               f'<p style="position: absolute; left: 330px; width: 420px; bottom: 110px; margin: 0; padding: 18px 0; text-align: center; border-radius: 999px; background: {BLACK}; font-size: 28px; font-weight: 700; color: {GOLD5}">grupovseven.com</p>',
               f'background: {G}')
    return [s1, s2, s3]

def v4_investigacao(A):
    grid = f'background: {BLACK}; background-image: linear-gradient(rgba(244,192,79,0.06) 1px, rgba(0,0,0,0) 1px), linear-gradient(90deg, rgba(244,192,79,0.06) 1px, rgba(0,0,0,0) 1px), radial-gradient(circle at 70% 45%, #2A1F0C 0%, #0C0B09 60%); background-size: 54px 54px, 54px 54px, 100% 100%'
    card = lambda l, t, r, n, txt: (f'<div style="position: absolute; left: {l}px; top: {t}px; width: 400px; box-sizing: border-box; padding: 34px 32px; background: #17140F; border: 1px solid #5A4A24; transform: rotate({r}deg); box-shadow: 0 20px 40px rgba(0,0,0,0.5)">'
                                    f'<p style="margin: 0; font-family: \'Courier New\', monospace; font-size: 22px; font-weight: 700; letter-spacing: 3px; color: {GOLD5}">PISTA {n}</p>'
                                    f'<p style="margin: 14px 0 0; font-size: 36px; font-weight: 700; line-height: 1.2; color: #FAF7F0">{txt}</p></div>')
    inner = (label('Investigação de marketing', GOLD5, y=96) +
             f'<p style="position: absolute; left: 80px; top: 160px; width: 920px; margin: 0; font-size: 84px; font-weight: 800; letter-spacing: -2.5px; line-height: 1.02; color: #FAF7F0">Por que a campanha <span style="{gt(G)}">não converte?</span></p>'
             f'<svg width="{W}" height="{H}" style="position: absolute; left: 0; top: 0" aria-hidden="true">'
             f'<path d="M290 590 L 780 700 L 420 960" fill="none" stroke="#E9B44C" stroke-width="3"></path>'
             f'<circle cx="290" cy="590" r="14" fill="#F4C04F"></circle><circle cx="780" cy="700" r="14" fill="#F4C04F"></circle><circle cx="420" cy="960" r="14" fill="#F4C04F"></circle>'
             f'<circle cx="820" cy="1060" r="90" fill="none" stroke="#F4C04F" stroke-width="10"></circle><path d="M885 1125 L 980 1220" stroke="#F4C04F" stroke-width="18" stroke-linecap="round"></path></svg>'
             + card(90, 590, -3, '01', 'Público amplo demais') + card(580, 700, 2.5, '02', 'Página lenta no celular') + card(220, 960, -1.5, '03', 'Oferta confusa') +
             f'<div style="position: absolute; left: 640px; top: 470px; padding: 10px 24px; border: 5px solid {GOLD5}; border-radius: 8px; transform: rotate(-10deg)"><p style="margin: 0; font-family: \'Courier New\', monospace; font-size: 34px; font-weight: 700; letter-spacing: 5px; color: {GOLD5}">CASO ABERTO</p></div>'
             + vs_footer(A, dark=True, bottom=60))
    return frame(inner, grid)

def v5_checklist(A):
    items = ['Posicionamento claro', 'Perfil que explica o que você faz', 'Conteúdo com frequência', 'Anúncios ligados a uma oferta', 'Atendimento rápido no WhatsApp']
    rows = ''.join(f'<div style="display: flex; align-items: center; gap: 26px; padding: 26px 0; border-top: {"none" if i==0 else "1px solid #2B261C"}"><div style="width: 52px; height: 52px; border-radius: 12px; background: {G}; display: flex; align-items: center; justify-content: center"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#14120D" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg></div><p style="margin: 0; font-size: 38px; font-weight: 700; color: #FAF7F0">{t}</p></div>' for i, t in enumerate(items))
    inner = (label('Checklist', GOLDTXT, y=96) +
             f'<p style="position: absolute; left: 80px; top: 160px; width: 920px; margin: 0; font-size: 76px; font-weight: 800; letter-spacing: -2.5px; line-height: 1.04; color: {INK}">Sua marca está pronta para <span style="{gt(GD)}">vender?</span></p>'
             f'<div style="position: absolute; left: 80px; right: 80px; top: 430px; padding: 26px 48px; border-radius: 28px; background: {BLACK}; box-shadow: 0 30px 60px rgba(60,40,10,0.2)">{rows}</div>'
             + vs_footer(A, dark=False))
    return frame(inner, f'background: {OFF}')

def v6_equipe(A):
    inner = (f'<img src="{A["team"]}" alt="Líderes da VSeven" style="position: absolute; left: -120px; top: 40px; width: 1320px; height: 1002px; object-fit: cover">'
             f'<div style="position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; background: linear-gradient(180deg, rgba(12,11,9,0.55) 0%, rgba(12,11,9,0) 18%, rgba(12,11,9,0) 52%, #0C0B09 74%)"></div>'
             + label('Bastidores', GOLD5, y=80) +
             f'<p style="position: absolute; left: 80px; top: 930px; width: 920px; margin: 0; font-size: 80px; font-weight: 800; letter-spacing: -2.5px; line-height: 1.02; color: #FAF7F0">Quem faz a VSeven <span style="{gt(G)}">acontecer.</span></p>'
             + vs_footer(A, dark=True, bottom=70))
    return frame(inner, f'background: {BLACK}')

PERSONAL = [('p1-frase', 'Frase / opinião', p1_frase), ('p2-foto', 'Foto + manchete', p2_foto), ('p3-carrossel', 'Carrossel editorial', p3_carrossel),
            ('p4-dossie', 'Investigativo · dossiê', p4_dossie), ('p5-diario', 'Diário de CEO', p5_diario), ('p6-numero', 'Dado / número', p6_numero)]
VSEVEN = [('v1-preto', 'Statement · preto', v1_preto), ('v2-ouro', 'Statement · ouro', v2_ouro), ('v3-carrossel', 'Carrossel · paleta alternada', v3_carrossel),
          ('v4-investigacao', 'Investigação de marketing', v4_investigacao), ('v5-checklist', 'Checklist', v5_checklist), ('v6-equipe', 'Bastidores · equipe', v6_equipe)]
