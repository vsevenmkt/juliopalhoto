"""Renderiza slides HTML (1080x1350) em JPG com as fontes e assets locais.

Uso em outro script:
    import sys; sys.path.insert(0, '<repo>/_sistema')
    from render import render_slides, ASSETS
    from templates import *          # helpers e paleta (WHITE, INK, GOLDTXT, G, GD, frame, label, ...)
    render_slides([html1, html2], '/caminho/saida', 'nome-base')
Requer: pip install playwright pillow  +  Chrome em /usr/bin/google-chrome (ou chromium do playwright).
"""
import os, shutil
from PIL import Image
BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = {k: f'file://{BASE}/assets/{v}' for k, v in {
    'avatar': 'julio-avatar.jpg', 'julio_cut': 'julio-cut.png',
    'logo_gold': 'logo-gold.png', 'logo_ink': 'logo-ink.png',
    'vsdok_icone': 'vsdok-icone.png', 'vsdok_banner': 'vsdok-banner.png'}.items()}
FAM = [('manrope', 'Manrope', 'normal', [300, 400, 500, 600, 700, 800]),
       ('cormorant-garamond', 'Cormorant Garamond', 'normal', [500, 600]),
       ('cormorant-garamond', 'Cormorant Garamond', 'italic', [500, 600]),
       ('caveat', 'Caveat', 'normal', [400, 600, 700])]
FACES = ''.join(f"@font-face{{font-family:'{n}';font-style:{st};font-weight:{w};src:url(file://{BASE}/fonts/{f}-latin-{w}-{st}.woff2)}}"
                for f, n, st, ws in FAM for w in ws)

def render_slides(slides, out_dir, name, quality=93):
    from playwright.sync_api import sync_playwright
    os.makedirs(out_dir, exist_ok=True)
    exe = shutil.which('google-chrome') or None
    paths = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': 1350})
        tmp = os.path.join(out_dir, '_tmp.html')
        for i, h in enumerate(slides):
            open(tmp, 'w').write(f"<!doctype html><html><head><meta charset='utf-8'><style>{FACES}body{{margin:0}}</style></head><body>{h}</body></html>")
            pg.goto('file://' + tmp); pg.wait_for_timeout(500)
            png = os.path.join(out_dir, '_s.png'); pg.screenshot(path=png)
            out = os.path.join(out_dir, f'{name}-{i+1:02d}.jpg')
            Image.open(png).convert('RGB').save(out, quality=quality, optimize=True); paths.append(out)
        b.close()
    for f in ('_tmp.html', '_s.png'):
        try: os.remove(os.path.join(out_dir, f))
        except OSError: pass
    return paths
