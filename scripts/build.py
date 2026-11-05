"""Build the browser and email editions using the approved editorial newsletter template.

Run from any directory: python3 scripts/build.py. No third-party dependency.
"""
from pathlib import Path
from html import escape, unescape
from html.parser import HTMLParser
from urllib.parse import urlencode
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = 'https://raphaeldumaslevillain-commits.github.io/NEWSLETTER-ANEKDOTE/'
OFFERS = json.loads((ROOT / 'offers.json').read_text())
BASE = (ROOT / 'templates/newsletter-base.html').read_text().strip()


def contact(offer):
    return 'https://www.anekdote.fr/contact/?' + urlencode({
        'utm_source': 'newsletter', 'utm_medium': 'email',
        'utm_campaign': 'offres-du-moment-demo', 'utm_content': offer['id'],
    })


def card(offer):
    url = escape(contact(offer), quote=True)
    text = {k: escape(v) for k, v in offer.items()}
    return f'''<table role="presentation" class="offer-card" width="268" cellpadding="0" cellspacing="0" style="width:268px;border-collapse:collapse;table-layout:fixed;background-color:#ffffff">
<tbody><tr><td style="padding:0;font-size:0;line-height:0"><a href="{url}" target="_blank" style="color:#171717;text-decoration:none"><img src="assets/offers/offre-{text['id']}.jpg?v=couleur-20261102" width="268" height="168" alt="{text['alt']}" class="offer-image" style="display:block;border:0;width:268px;height:168px;max-width:100%;object-fit:cover"></a></td></tr>
<tr><td class="offer-copy" style="padding:22px 22px 0"><p style="margin:0 0 10px;font-size:9px;line-height:15px;letter-spacing:1.3px;color:#686868">{text['category']}</p><h3 style="margin:0 0 9px;font-size:22px;line-height:28px;letter-spacing:-0.6px;font-weight:400;font-family:Georgia,'Times New Roman',serif">{text['name']}</h3><p class="offer-headline" style="margin:0;font-size:15px;line-height:22px;min-height:44px;font-weight:600;letter-spacing:-0.3px">{text['headline']}</p></td></tr>
<tr><td class="offer-description" height="147" valign="top" style="height:147px;padding:12px 22px 0;vertical-align:top"><p style="margin:0;font-size:13px;line-height:21px;color:#555555">{text['description']}</p></td></tr>
<tr><td class="offer-copy" style="padding:15px 22px 14px"><p style="margin:0;font-size:10px;line-height:16px;letter-spacing:0.2px;color:#686868">{text['format']}</p></td></tr>
<tr><td class="offer-button-pad" style="padding:0 22px 24px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;width:100%"><tbody><tr><td align="center" bgcolor="#171717" height="48" style="height:48px;background-color:#171717"><a class="offer-cta" href="{url}" target="_blank" style="display:block;padding:15px 8px;color:#ffffff;background-color:#171717;text-decoration:none;text-align:center;font-size:11px;line-height:18px;font-weight:500">{text['cta']} <span aria-hidden="true">↗</span></a></td></tr></tbody></table></td></tr></tbody></table>'''


def offers_section():
    rows = []
    for i in range(0, len(OFFERS), 2):
        rows.append('<tr>' + ''.join(
            f'<td class="offer-column" width="268" valign="top" style="width:268px;vertical-align:top;padding:0 0 24px">{card(OFFERS[j])}</td>'
            + ('<td class="offer-gap" width="24" style="width:24px;font-size:0;line-height:0">&nbsp;</td>' if j == i else '')
            for j in range(i, i + 2)
        ) + '</tr>')
    return '''<!-- OFFERS:BEGIN -->
<tr><td id="offres-du-moment" class="offers-section email-pad" bgcolor="#f2f1ee" style="padding:40px 40px 20px;background-color:#f2f1ee;border-bottom:1px solid #d8d8d8;scroll-margin-top:20px">
<p style="margin:0 0 14px;font-size:10px;line-height:17px;letter-spacing:1.8px;color:#555555">LES OFFRES DU MOMENT</p>
<h2 class="offers-title" style="margin:0 0 14px;font-family:Georgia,'Times New Roman',serif;font-size:38px;line-height:42px;font-weight:400;letter-spacing:-1px">Votre marque.<br>Au bon endroit.</h2>
<p style="margin:0 0 28px;font-size:14px;line-height:23px;color:#4a4a4a">Quatre temps forts pour créer la rencontre.<br>Choisissez le vôtre, on imagine la suite ensemble.</p>
<table role="presentation" class="offer-grid" width="560" cellpadding="0" cellspacing="0" style="width:560px;border-collapse:collapse;table-layout:fixed"><tbody>''' + ''.join(rows) + '''</tbody></table>
<p style="margin:0 0 10px;font-size:12px;line-height:20px;color:#555555">Une autre idée en tête ? <a href="https://www.anekdote.fr/contact/?utm_source=newsletter&amp;utm_medium=email&amp;utm_campaign=offres-du-moment-demo&amp;utm_content=sur-mesure" target="_blank" style="color:#171717;text-decoration:underline">Parlons de votre projet ↗</a></p>
</td></tr>
<!-- OFFERS:END -->'''


TEASER = '''<!-- OFFERS-TEASER:BEGIN --><tr><td class="email-pad" bgcolor="#171717" style="padding:14px 40px;background-color:#171717"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse"><tbody><tr><td style="font-size:10px;line-height:18px;letter-spacing:1.1px;color:#ffffff">EN CE MOMENT</td></tr></tbody></table></td></tr><!-- OFFERS-TEASER:END -->'''


def add_mobile_classes(match):
    tag = match.group(0)
    classes = []
    if tag.startswith('<table') and 'width="640"' in tag:
        classes.append('email-wrap')
    if tag.startswith('<img') and 'width:640px' in tag:
        classes.append('email-image')
    if tag.startswith('<td') and re.search(r'padding:[^";]*\b40px', tag):
        classes.append('email-pad')
    if tag.startswith('<table') and re.search(r'width:(560|268|232)px', tag):
        classes.append('email-fluid')
    if classes:
        existing = re.search(r'class="([^"]*)"', tag)
        if existing:
            tag = tag[:existing.end(1)] + ' ' + ' '.join(classes) + tag[existing.end(1):]
        else:
            tag = tag[:-1] + ' class="' + ' '.join(classes) + '">'
    return tag


body = re.sub(r'<[a-zA-Z][^>]*>', add_mobile_classes, BASE)
photo_marker = '<tr><td bgcolor="#4a4a4a"'
assert body.count(photo_marker) == 1
body = body.replace(photo_marker, TEASER + photo_marker, 1)
section_marker = '<tr><td bgcolor="#ffffff" style="padding:44px 40px 46px;'
# A mobile class may have been appended, but attribute order is unchanged.
assert body.count(section_marker) == 1
body = body.replace(section_marker, offers_section() + section_marker, 1)
body = body.replace('<a style="color:rgb(102,102,102);text-decoration-line:underline">Voir cet email', '<a href="' + PUBLIC + '" style="color:rgb(102,102,102);text-decoration-line:underline">Voir cet email', 1)

MOBILE = '''
a:focus-visible { outline: 2px solid #777; outline-offset: 4px; }
@media only screen and (max-width: 640px) {
  .email-wrap { width:100% !important; max-width:640px !important; }
  .email-image { width:100% !important; height:auto !important; }
  .email-pad { padding-left:24px !important; padding-right:24px !important; }
  .email-fluid, .offer-grid { width:100% !important; max-width:100% !important; }
  .offer-column { display:block !important; width:100% !important; padding-bottom:20px !important; }
  .offer-gap { display:none !important; }
  .offer-card { width:100% !important; }
  .offer-image { width:100% !important; height:auto !important; }
  .offer-description { height:auto !important; padding-top:12px !important; padding-bottom:4px !important; }
  .offer-headline { min-height:0 !important; }
  .offer-cta { font-size:13px !important; }
  .offer-description p { font-size:16px !important; line-height:25px !important; }
  .offers-title { font-size:34px !important; line-height:39px !important; }
}
'''

rules = {}


def extract_style(match):
    tag = match.group(0)
    attr = re.search(r'\sstyle="([^"]*)"', tag)
    if not attr:
        return tag
    style = unescape(attr.group(1))
    rules.setdefault(style, 'nl-' + str(len(rules) + 1).zfill(3))
    cls = rules[style]
    tag = tag[:attr.start()] + tag[attr.end():]
    existing = re.search(r'class="([^"]*)"', tag)
    if existing:
        return tag[:existing.end(1)] + ' ' + cls + tag[existing.end(1):]
    return tag[:-1] + ' class="' + cls + '">'


styled = re.sub(r'<[a-zA-Z][^>]*>', extract_style, body)


def document(markup, email=False):
    head = '<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>Anekdote — Les offres du moment</title>\n<meta name="description" content="Maquette de newsletter Anekdote : loges, Cannes, Les Ardentes et GP de Monaco. Offres et visuels fictifs.">\n'
    head += '<style>' + MOBILE + '</style>\n' if email else '<link rel="stylesheet" href="styles.css?v=expertises-20261105">\n'
    return head + '</head>\n<body style="margin:0;padding:0;background-color:#eeeeee;font-family:Arial,sans-serif">\n' + markup + '\n</body>\n</html>\n'


css = '/* Original newsletter declarations and new offer cards. Generated by scripts/build.py. */\nhtml { background:#eee; }\nbody { margin:0;padding:0;background:#eee;font-family:Arial,sans-serif; }\n'
css += '\n'.join('.' + cls + ' { ' + style + ' }' for style, cls in rules.items()) + '\n' + MOBILE
(ROOT / 'index.html').write_text(document(styled))
(ROOT / 'styles.css').write_text(css)
email_body = body.replace('src="assets/', 'src="' + PUBLIC + 'assets/')
email_body = email_body.replace('href="#offres-du-moment"', 'href="' + PUBLIC + '#offres-du-moment"')
(ROOT / 'newsletter.html').write_text(document(email_body, email=True))
(ROOT / '.nojekyll').write_text('')

# Confirm that inserting the offer module preserves the approved editorial template.
class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
    def handle_data(self, data):
        self.parts.append(data)


def text(markup):
    parser = Text()
    parser.feed(markup)
    return ''.join(parser.parts)


without_new = re.sub(r'<!-- OFFERS(?:-TEASER)?:BEGIN -->.*?<!-- OFFERS(?:-TEASER)?:END -->', '', body, flags=re.S)
assert text(without_new) == text(BASE), 'Approved editorial text changed'
assert len(re.findall(r'<img\b', body)) == 12
assert (ROOT / 'assets/images/peugeot-mondial-auto-2026.jpg').is_file()
assert len(re.findall(r'<table\b', body)) == len(re.findall(r'</table>', body))
assert all((ROOT / ('assets/offers/offre-' + o['id'] + '.jpg')).is_file() for o in OFFERS)
assert len({contact(o) for o in OFFERS}) == 4
assert body.index('GHD × Juliette Has a Gun') < body.index('Et pour<br>votre marque ?') < body.index('id="offres-du-moment"') < body.index('LA SUITE, AVEC VOUS')
assert body.index('Émotions à la française.</h2>') < body.index('Et pour<br>votre marque ?')
assert 'cinq projets qui nous tiennent à cœur' in body
assert body.count('class="expertise ') == 7 and 'Voici sept expertises' in body
assert body.index('Programme ambassadeurs</h3>') < body.index('mailto:Christelle.egron@dbmgroup.fr') < body.index('id="offres-du-moment"')
assert 'L’OFFRE LOGE' not in body and 'Pack exemple' not in body
assert body.count('Votre marque aux premières loges.') == 1
assert 'Nous serions ravis' in body and 'Nous serons ravis' not in body

report = {
    'version': 'retours-editoriaux-2026-11-05',
    'approved_editorial_text_preserved': True,
    'case_studies_count': 5,
    'expertises_count': 7,
    'reading_order': ['case-studies', 'expertises', 'booking', 'offers', 'conclusion'],
    'offer_images': 'full-color',
    'fixed_guest_counts': False,
    'offers': [o['id'] for o in OFFERS],
    'fictional_content_labeled': False,
    'width_px': 640,
    'desktop_card_width_px': 268,
    'image_render_size_px': [268, 168],
    'image_file_size_px': [536, 336],
    'button_min_height_px': 48,
    'mobile_single_column_breakpoint_px': 640,
    'images': 12,
    'cta_destinations': [contact(o) for o in OFFERS],
    'checks': 'Approved editorial text, reading order, five case studies, seven expertises, booking link, balanced tables, assets and distinct offer links verified during build.',
    'sha256': {f: hashlib.sha256((ROOT / f).read_bytes()).hexdigest() for f in ('index.html', 'styles.css', 'newsletter.html')},
}
(ROOT / 'verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'build': 'OK', 'offers': len(OFFERS), 'approved_editorial_text_preserved': True, 'styles': len(rules)}, ensure_ascii=False))
