#!/usr/bin/env python3
"""Build both languages from one outcome ledger and a separate narrative source."""
from __future__ import annotations
import hashlib
import json
import os
import re
from pathlib import Path
from datetime import datetime
from xml.sax.saxutils import escape
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = 'https://github.com/DiadkoShmek/engineering-results/blob/main/'
LABELS = {
    'merged': ('Власний PR merged', 'Direct PR merged'),
    'incorporated_in_maintainer_fix': ('Внесок у merged fix мейнтейнера', 'Incorporated into a merged maintainer fix'),
    'superseded_by_open_maintainer_fix': ('Superseded; заміна OPEN', 'Superseded; replacement OPEN'),
    'credited_in_release': ('Аудит відзначено в релізі', 'Audit credited in release'),
    'snapshot': ('Датований зріз арени', 'Dated arena snapshot'),
    'preliminary': ('Історичний попередній результат', 'Historical preliminary result'),
    'final': ('Призер сезону; точне місце не встановлено', 'Season prize winner; exact rank not established'),
}


def load():
    return json.loads((ROOT / 'results.json').read_text()), json.loads((ROOT / 'book/narrative.json').read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pr_summary(lang):
    snapshot = json.loads((ROOT/'pr-status.json').read_text())
    c = snapshot['counts']
    when = datetime.fromisoformat(snapshot['observed_at'].replace('Z','+00:00')).strftime('%Y-%m-%d %H:%M UTC')
    if lang == 'uk':
        return (f"Публічні PR у чужих репозиторіях: {c['total']} подано; {c['merged']} злитих, "
                f"{c['open']} відкритих, {c['closed_unmerged']} закритих без merge. "
                f"Зріз GitHub: {when}. Власна та приватна активність виключені.")
    return (f"Public PRs in other owners' repositories: {c['total']} submitted; {c['merged']} merged, "
            f"{c['open']} open, {c['closed_unmerged']} closed without merge. "
            f"GitHub snapshot: {when}. Own-repository and private activity is excluded.")


def pr_markdowns():
    snapshot = json.loads((ROOT/'pr-status.json').read_text())
    credited = counts(load()[0]['records'])['incorporated']
    stamp = '<!-- generated; pr-status-sha256:'+digest(ROOT/'pr-status.json')+' -->'
    for lang in ('uk', 'en'):
        uk = lang == 'uk'; suffix = '' if uk else '.en'
        lines = ['# '+('Стан зовнішніх PR' if uk else 'External PR status'), stamp,
                 pr_summary(lang),
                 (f'Закритий без merge PR не обов’язково відхилений: {credited} пропозиції відзначено у злитих рішеннях мейнтейнерів. Схвалення не є merge. Повнота цього зрізу стосується переліку PR, а не всіх CI чи рев’ю.' if uk else
                  f'Closed without merge does not necessarily mean rejected: {credited} proposals are credited in merged maintainer solutions. Approval is not a merge. Snapshot completeness covers the PR inventory, not every CI run or review.'),
                 '[Українська](PR_STATUS.md) · [English](PR_STATUS.en.md) · [JSON](pr-status.json) · [Results](RESULTS'+suffix+'.md)',
                 '## '+('Окремі сигнали рев’ю' if uk else 'Selected review signals')]
        for item in snapshot.get('review_signals', []):
            lines.append(f"- [{item['label']}]({item['url']}): {item[lang]}. {item['checked_at']}")
        for state, a, b in [('MERGED','Злиті PR','Merged PRs'),('OPEN','Відкриті PR','Open PRs'),('CLOSED','Закриті без merge','Closed without merge')]:
            rows = [x for x in snapshot['pull_requests'] if x['state'] == state]
            lines += ['## '+(a if uk else b)+f' ({len(rows)})',
                      '| '+('Проєкт / PR | Зміна | Дата merge або оновлення UTC' if uk else 'Repository / PR | Change | Merge or update date UTC')+' |', '|---|---|---|']
            for x in sorted(rows, key=lambda x: x['merged_at'] or x['updated_at'], reverse=True):
                label=x['repository']+' #'+str(x['number'])
                title=escape(x['title']).replace('[','&#91;').replace(']','&#93;').replace('`','&#96;').replace('|','\\|')
                lines.append(f"| [{label}]({x['url']}) | {title} | {x['merged_at'] or x['updated_at']} |")
        for item in snapshot.get('featured_submissions', []):
            target=item['report_path']+('' if uk else '#english-summary')
            lines.append(f"[{'Поданий інженерний кейс: Triton' if uk else 'Submitted engineering case: Triton'}]({target})")
        (ROOT/f'PR_STATUS{suffix}.md').write_text('\n\n'.join(lines).replace('|\n\n|','|\n|')+'\n')


def counts(records):
    return {
        'direct': sum(r['status'] == 'merged' and r.get('contribution_merged') is True for r in records),
        'incorporated': sum(r['status'] == 'incorporated_in_maintainer_fix' for r in records),
        'pending': sum(r['status'] == 'superseded_by_open_maintainer_fix' for r in records),
        'audits': sum(r['category'] == 'external_audit' for r in records),
        'competition_records': sum(r['category'] == 'competition' for r in records),
        'arenas': len({r['competition'] for r in records if r['category'] == 'competition'}),
    }


def summary(records, lang):
    c = counts(records)
    if lang == 'uk':
        parts = [f"Власні злиті PR: {c['direct']}", f"внески у злиті рішення мейнтейнерів: {c['incorporated']}"]
        if c['pending']:
            parts.append(f"відкриті мейнтейнерські заміни: {c['pending']}")
        parts.append(f"технічні аудити: {c['audits']}")
        return ('; '.join(parts) + '. ' +
                f"Змагання: часових записів {c['competition_records']}, подій {c['arenas']}; Zoria враховано один раз.")
    parts = [f"{c['direct']} directly merged PRs", f"{c['incorporated']} contributions incorporated into merged maintainer fixes"]
    if c['pending']:
        parts.append(f"{c['pending']} replacement still OPEN")
    parts.append(f"{c['audits']} audit")
    return ('; '.join(parts) + '. ' +
            f"{c['competition_records']} observations across {c['arenas']} arenas/events, with Zoria counted once.")


def source_links(r, lang):
    uk = lang == 'uk'
    pairs = [('Першоджерело' if uk else 'Primary source', r['source_url'])]
    pairs += [('Наша пропозиція' if uk else 'Our proposal', r.get('contribution_url')),
              ('Відзначення внеску' if uk else 'Acknowledgement', r.get('acknowledgement_url')),
              ('Профіль арени' if uk else 'Arena profile', r.get('profile_url'))]
    pairs += [('Реалізація мейнтейнера' if uk else 'Maintainer implementation', f['url']) for f in r.get('upstream_fixes', [])]
    seen = set(); out = []
    for label, url in pairs:
        if url and url not in seen:
            seen.add(url); out.append((label, url))
    return out


def boundary(r, chapter, lang):
    return chapter['uk']['boundaries'][r['id']] if lang == 'uk' else r['boundary']


def record_text(r, lang):
    date = r['as_of'] + (' ('+r['display_timezone']+')' if r.get('display_timezone') else '')
    text = f"{date} · {LABELS[r['status']][lang == 'en']}"
    if r.get('observed_at') or r.get('checked_at'):
        text += ' · UTC '+r.get('observed_at',r.get('checked_at'))
    if r['category'] == 'competition' and 'rank' in r:
        scope = r['rank_scope']
        if lang == 'uk' and scope == 'overall preliminary score of second-stage participants':
            scope = 'загальний попередній підсумок учасників другого етапу'
        text += f" · {r['rank']}/{r['participants']} ({scope})"
    if r.get('merged_at'):
        text += ' · ' + r['merged_at']
    return text


def markdowns(ledger, narrative):
    records = ledger['records']; by_id = {r['id']: r for r in records}
    stamp = f"<!-- generated; ledger-sha256:{digest(ROOT/'results.json')}; narrative-sha256:{digest(ROOT/'book/narrative.json')}; pr-status-sha256:{digest(ROOT/'pr-status.json')} -->\n"
    for lang in ('uk', 'en'):
        suffix = '' if lang == 'uk' else '.en'
        title = 'Зовнішні результати' if lang == 'uk' else 'External results'
        date = max(r['as_of'] for r in records)
        lines = [f'# {title}', stamp, f'**{date} UTC**', summary(records, lang), pr_summary(lang),
                 f"[{'Повний стан PR' if lang=='uk' else 'Complete PR status'}](PR_STATUS{suffix}.md)",
                 '[Українська](RESULTS.md) · [English](RESULTS.en.md) · [JSON](results.json)',
                 ('| Дата запису / основа | Кейс | Зовнішній стан | Джерело |' if lang=='uk' else '| Record date / source basis | Case | Outcome | Source |'), '|---|---|---|---|']
        for chapter in narrative['chapters']:
            for rid in chapter['record_ids']:
                r = by_id[rid]; target = chapter['report'] or ('RESULTS'+suffix+'.md#zoria-2026--підсумок-ua-skills')
                if lang == 'en' and chapter['report']: target += '#english-summary'
                lines.append(f"| {r['as_of']} | [{chapter['title']}]({target}) | {LABELS[r['status']][lang == 'en']} | [{'Джерело' if lang=='uk' else 'Public source'}]({r['source_url']}) |")
        lines += ['\n<a id="codingame--mad-pod-racing"></a>', '## CodinGame - Mad Pod Racing',
                  '![Dated public evidence](evidence/codingame-2026-10-21.jpg)',
                  '\n<a id="zoria-2026--підсумок-ua-skills"></a>', '## Zoria 2026 / UA SKILLS']
        for r in records:
            if r['category'] == 'competition':
                lines += [record_text(r, lang), f"[Source]({r['source_url']})", boundary(r,next(c for c in narrative['chapters'] if r['id'] in c['record_ids']),lang)]
        lines += ['\n[Engineering cases](ENGINEERING.md) · [Case reports](reports/README.md)']
        index_text='\n\n'.join(lines)+'\n'
        index_text=re.sub(r'(?m)(^\|[^\n]*\|)\n\n(?=\|)',r'\1\n',index_text)
        (ROOT / f'RESULTS{suffix}.md').write_text(index_text)
        intro = ("Я досліджую дефект, визначаю контракт і перевіряю наслідок. AI-інструменти допомагають із пошуком, реалізацією та перевіркою; я задаю напрям, відповідаю за інженерне рішення й погоджую зовнішні дії. Ця книга не вимірює відсоток автономності чи перевагу однієї моделі." if lang == 'uk' else
                 "I investigate failures, define contracts and verify consequences. AI tools assist research, implementation and checking; I set direction, take responsibility for engineering decisions and authorize external actions. This book does not measure autonomy percentages or rank AI models.")
        text = [f'# {title}', stamp, f'DiadkoShmek · {date} UTC', '## '+('Роль і доказ' if lang=='uk' else 'Role and evidence'), intro, summary(records,lang), pr_summary(lang),
                f"[{'Повний стан PR' if lang=='uk' else 'Complete PR status'}](../../PR_STATUS{suffix}.md)",
                ('Усі статуси й дати нижче походять із results.json. Локальний PASS, зовнішній credit і merge - різні твердження. Попередній та фінальний записи Zoria належать одній події.' if lang=='uk' else
                 'Every status and date below comes from results.json. A local PASS, external credit and a merge are different claims. The preliminary and final Zoria records belong to one event.'),
                '## '+('Зміст' if lang=='uk' else 'Contents')]
        text += [f"{i}. [{c['title']}](#case-{c['key']})" for i,c in enumerate(narrative['chapters'],1)]
        headings = [('problem','Проблема','Problem'),('decision','Моє рішення та зовнішній вибір','My decision and the external choice'),('proof','Перевірка й обмеження','Validation and limits'),('lesson','Що переношу далі','What I carry forward')]
        for i,c in enumerate(narrative['chapters'],1):
            text += [f'<a id="case-{c["key"]}"></a>',f'## {i:02d}. {c["title"]}']
            for rid in c['record_ids']:
                r=by_id[rid];text += ['**'+record_text(r,lang)+'**', boundary(r,next(c for c in narrative['chapters'] if r['id'] in c['record_ids']),lang)]
            for key,uk,en in headings: text += ['### '+(uk if lang=='uk' else en),c[lang][key]]
            for rid in c['record_ids']:
                text += [f"- [{label}]({u})" for label,u in source_links(by_id[rid],lang)]
            if c['report']:text += [f"[Повний кейс / Full report](../../{c['report']})"]
        text += ['## '+('Як продовжувати книгу' if lang=='uk' else 'How this book grows'),
                 ('Для нового результату я зберігаю дату спостереження UTC, свою роль, первинне джерело й точний зовнішній статус. Старе відтворення лишається датованим; повторну перевірку не видаю за повний аудит. Додаю запис до results.json, розбір до book/narrative.json і запускаю збірку та офлайн-перевірку.' if lang=='uk' else
                  'For each new result I retain the UTC observation date, my role, primary source and exact external disposition. Old reproductions remain dated; a follow-up is not a complete reaudit. I append results.json, add narrative to book/narrative.json and run the build and offline check.')]
        (ROOT/f'book/{lang}/BOOK.md').write_text('\n\n'.join(text)+'\n')
        readme = [f'# {title}',stamp, ('Інженерні результати, які можна перевірити за зовнішнім джерелом. Окрема книга про код, дослідження, аудит і арени - без підміни одного виду результату іншим.' if lang=='uk' else
                     'Engineering outcomes tied to external evidence. A separate casebook for code, investigation, audits and arenas, keeping each kind of result distinct.'),summary(records,lang),pr_summary(lang),
                  f"[{'Усі PR і поточні статуси' if lang=='uk' else 'All PRs and current dispositions'}](PR_STATUS{suffix}.md)",
                  f"**{date} UTC** · [Українська](README.md) · [English](README.en.md)",
                  '## '+('Книга' if lang=='uk' else 'The book'),
                  '[Українська PDF](book/pdf/external-results-uk.pdf) · [English PDF](book/pdf/external-results-en.pdf)',
                  '[Українська Markdown](book/uk/BOOK.md) · [English Markdown](book/en/BOOK.md)',
                  (('[Журнал результатів](RESULTS.md) · [Детальні двомовні кейси](reports/README.md) · [Інженерні кейси](ENGINEERING.md)') if lang=='uk' else '[Results](RESULTS.en.md) · [Detailed bilingual cases](reports/README.md) · [Engineering](ENGINEERING.md)'),
                  '## '+('Що означають статуси' if lang=='uk' else 'What the statuses mean'),
                  ('Merged означає злиття власного PR. Incorporated означає внесок у прийняте рішення мейнтейнера, не merge власного patch. Відкриті мейнтейнерські заміни обліковуються як незавершені. Аудит і змагання обліковуються окремо; три competition records описують дві події.' if lang=='uk' else
                   'Merged means our PR was merged. Incorporated means a contribution to an accepted maintainer solution, not a merge of our patch. Open maintainer replacements are recorded as pending. Audits and competitions are separate; three competition records describe two events.'),
                  '## '+('Як додати результат' if lang=='uk' else 'How to append a result'),
                  ('1. Додайте датований запис і первинне публічне джерело до [results.json](results.json).\n2. Додайте двомовний кейс у reports/ та розділ у [book/narrative.json](book/narrative.json).\n3. Запустіть `python tools/build.py` (потрібні requirements.txt і шрифти DejaVu).\n4. Запустіть `python tools/check.py` офлайн; перед публікацією огляньте нові сторінки PDF.' if lang=='uk' else '1. Add a dated record and primary public source to [results.json](results.json).\n2. Add a bilingual case in reports/ and a chapter in [book/narrative.json](book/narrative.json).\n3. Run `python tools/build.py` (requires requirements.txt and DejaVu fonts).\n4. Run `python tools/check.py` offline; inspect newly rendered PDF pages before publishing.'),
                  ('[Схема журналу та правила доповнення](SCHEMA.md)' if lang=='uk' else '[Ledger schema and append contract](SCHEMA.md)'), '## '+('Джерела та відтворюваність' if lang=='uk' else 'Sources and reproducibility'),
                  ('`results.json` містить підтверджені результати, `book/narrative.json` - авторський текст, `pr-status.json` - датований перелік усіх зовнішніх PR. Згенеровані індекси й книги прив’язані до трьох джерел. Детальні звіти зберігають часові межі; оригінальний PDF аудиту M7 додано без переписування.' if lang=='uk' else '`results.json` owns confirmed outcomes, `book/narrative.json` authored narrative, and `pr-status.json` the dated inventory of all external PRs. Generated indices and books bind all three sources. Detailed reports retain dated scope; the original M7 audit PDF is attached unchanged.'),
                  ('Перевірка працює офлайн й не засвідчує upstream CI, поточний рейтинг чи кожне твердження історичного аудиту. AI-допомогу розкрито; приватні робочі журнали, модельні виклики й особиста біографія не публікуються.' if lang=='uk' else 'The check is offline and does not certify upstream CI, current live rankings or every claim in an attached historical audit. AI assistance is disclosed; no private work logs, model calls or personal biography are published.')]
        (ROOT/f'README{suffix}.md').write_text('\n\n'.join(readme)+'\n')


def pdfs(ledger,narrative):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import A5
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, KeepTogether, Flowable
    from reportlab.platypus.tableofcontents import TableOfContents
    from reportlab.pdfgen import canvas
    from functools import partial
    fonts=Path(os.environ.get('DEJAVU_DIR','/usr/share/fonts/truetype/dejavu'))
    for name,file in [('Serif','DejaVuSerif.ttf'),('SerifBold','DejaVuSerif-Bold.ttf'),('Sans','DejaVuSans.ttf'),('SansBold','DejaVuSans-Bold.ttf')]:pdfmetrics.registerFont(TTFont(name,str(fonts/file)))
    ink=colors.HexColor('#1F2B31');teal=colors.HexColor('#126A6C');copper=colors.HexColor('#A26745');muted=colors.HexColor('#59666D')
    w,h=A5; margin=17*mm; width=w-2*margin
    st={
        'body':ParagraphStyle('Body',fontName='Serif',fontSize=9.5,leading=14.2,textColor=ink,spaceAfter=9),
        'small':ParagraphStyle('Small',fontName='Sans',fontSize=7.5,leading=11,textColor=muted,spaceAfter=7),
        'chapter':ParagraphStyle('Chapter',fontName='SerifBold',fontSize=18,leading=23,textColor=ink,spaceAfter=17,keepWithNext=True),
        'head':ParagraphStyle('Section',fontName='SansBold',fontSize=10,leading=14,textColor=teal,spaceBefore=10,spaceAfter=7,keepWithNext=True),
        'cover':ParagraphStyle('Cover',fontName='SerifBold',fontSize=30,leading=36,textColor=ink,spaceAfter=22),
        'label':ParagraphStyle('Label',fontName='SansBold',fontSize=9,leading=13,textColor=copper,spaceAfter=13),
    }
    class Provenance(Flowable):
        def __init__(self,lang):super().__init__();self.width=width;self.height=54*mm;self.lang=lang
        def draw(self):
            c=self.canv; labels=(['Проблема','Відтворення','Перевірка','Зовнішній стан'] if self.lang=='uk' else ['Failure','Reproduction','Review','External state'])
            for i,label in enumerate(labels):
                y=self.height-16*mm-i*10*mm;c.setStrokeColor(teal);c.setFillColor(colors.HexColor('#F1F6F5'));c.roundRect(0,y,width,8*mm,2*mm,fill=1,stroke=0)
                c.setFillColor(teal);c.setFont('Sans',8);c.drawString(4*mm,y+2.7*mm,f'{i+1:02d}  '+label)
                if i<3:c.setStrokeColor(copper);c.line(width/2,y,width/2,y-2*mm)
    records = ledger['records']
    date = max(max(r['as_of'] for r in records), json.loads((ROOT/'pr-status.json').read_text())['observed_at'][:10])
    ledger_hash = digest(ROOT/'results.json')
    class Book(BaseDocTemplate):
        def afterFlowable(self,f):
            if isinstance(f,Paragraph) and getattr(f,'toc_key',None):
                self.canv.bookmarkPage(f.toc_key);self.canv.addOutlineEntry(f.getPlainText(),f.toc_key,0)
                self.notify('TOCEntry',(0,f.getPlainText(),self.page,f.toc_key))
    for lang in ('uk','en'):
        uk=lang=='uk';title='Зовнішні результати' if uk else 'External results'
        def page(c,d):
            c.setTitle(title);c.setAuthor('DiadkoShmek');c.setSubject('Ledger SHA256: '+ledger_hash+'; Narrative SHA256: '+digest(ROOT/'book/narrative.json')+'; PR snapshot SHA256: '+digest(ROOT/'pr-status.json'))
            c.setFillColor(muted);c.setFont('Sans',7)
            if d.page>1:
                c.drawString(margin,h-12*mm,title);c.setStrokeColor(colors.HexColor('#D5DEDE'));c.line(margin,h-14*mm,w-margin,h-14*mm)
            c.drawString(margin,10*mm,'DiadkoShmek  /  '+date+' UTC');c.drawRightString(w-margin,10*mm,str(d.page))
        doc=Book(str(ROOT/f'book/pdf/external-results-{lang}.pdf'),pagesize=A5,leftMargin=margin,rightMargin=margin,topMargin=21*mm,bottomMargin=20*mm)
        doc.invariant = 1
        doc.addPageTemplates(PageTemplate(id='book',frames=[Frame(margin,20*mm,width,h-41*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=page))
        story=[]
        P=lambda text,style='body':Paragraph(escape(text),st[style])
        story += [Spacer(1,24*mm),P('ІНЖЕНЕРНА КНИГА' if uk else 'ENGINEERING CASEBOOK','label'),P(title,'cover'),P('Код. Дослідження. Зовнішній наслідок.' if uk else 'Code. Investigation. External consequence.','head'),P('DiadkoShmek','body'),Spacer(1,12*mm),P(summary(records,lang)),P('Датований запис із публічними першоджерелами.' if uk else 'A dated record with public primary sources.','small'),PageBreak()]
        story += [P('Зміст' if uk else 'Contents','chapter')]
        toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC',fontName='Sans',fontSize=9,leading=14,textColor=ink,leftIndent=0,firstLineIndent=0,spaceBefore=0)];toc.dotsMinLevel=0;story += [toc,PageBreak()]
        intro=P('Роль, метод і одиниця доказу' if uk else 'Role, method and units of evidence','chapter');intro.toc_key='method';story.append(intro)
        md=(ROOT/f'book/{lang}/BOOK.md').read_text();role=md.split('## '+('Роль і доказ' if uk else 'Role and evidence'))[1].split('## ')[0].strip().split('\n\n')[0]
        story += [P(role),P(summary(records,lang)),Provenance(lang),P('Локальний тест перевіряє механізм. Upstream merge або credit підтверджує зовнішній наслідок. Жоден із них сам собою не доводить повний CI, adoption чи оплату.' if uk else 'A local test verifies a mechanism. An upstream merge or credit records an external outcome. Neither alone establishes complete CI, adoption or payment.'),P('Дати мають UTC-прив’язку. Для історичних зрізів збережені початкові часові поля; дата перевірки оголошення може відрізнятися від дати публікації.' if uk else 'Dates are stated against UTC. Original timestamp fields remain for historical snapshots; the date an announcement was checked may differ from publication.'),PageBreak()]
        portfolio=P('Поточний портфель PR' if uk else 'Current PR portfolio','chapter');portfolio.toc_key='portfolio'
        story += [portfolio,P(pr_summary(lang)),P('Цей зріз відділяє завершені результати від відкритої роботи. Відзначені внески в реалізації мейнтейнерів обліковуються окремо від власних merge; закриті без merge PR не прирівнюються до відмов.' if uk else 'This snapshot separates completed outcomes from open work. Credited contributions to maintainer implementations remain separate from direct merges; closed-without-merge PRs are not all rejections.')]
        snapshot=json.loads((ROOT/'pr-status.json').read_text())
        for item in snapshot.get('review_signals',[]):story += [P(item['label'],'head'),P(item[lang],'small')]
        story += [Paragraph(f'<link href="{PUBLIC}PR_STATUS{("" if uk else ".en")}.md" color="#126A6C"><u>{"Повний датований перелік PR" if uk else "Complete dated PR inventory"}</u></link>',st['small']),P('Зріз не прогнозує merge і не засвідчує всі перевірки CI. Triton #12611 поданий; до злитих результатів він не входить.' if uk else 'This snapshot does not predict merges or certify every CI check. Triton #12611 is submitted and is not counted as a merged result.'),PageBreak()]
        by_id={r['id']:r for r in records}
        labels=[('problem','Проблема','Problem'),('decision','Рішення та роль','Decision and role'),('proof','Перевірка','Validation'),('lesson','Що переношу далі','What I carry forward')]
        for i,ch in enumerate(narrative['chapters'],1):
            heading=P(f'{i:02d}  '+ch['title'],'chapter');heading.toc_key='case-'+ch['key'];story.append(heading)
            for rid in ch['record_ids']:story.append(P(record_text(by_id[rid],lang),'label'))
            for key,a,b in labels[:3]:story += [P(a if uk else b,'head'),P(ch[lang][key])]
            tail = [P('Що переношу далі' if uk else 'What I carry forward','head'),P(ch[lang]['lesson'])]
            tail.append(P('Межа зовнішнього результату' if uk else 'External outcome boundary','head'))
            for rid in ch['record_ids']:tail.append(P(boundary(by_id[rid],ch,lang),'small'))
            tail.append(P('Джерела' if uk else 'Sources','head'))
            links=list(dict.fromkeys(pair for rid in ch['record_ids'] for pair in source_links(by_id[rid],lang)))
            if ch['report']:links.append(('Докладний кейс' if uk else 'Detailed case', PUBLIC+ch['report']))
            for j,(label,u) in enumerate(links,1):
                tail.append(Paragraph(f'<link href="{escape(quote(u, safe=':/?=&%#'))}" color="#126A6C"><u>{j}. {escape(label)}</u></link>',st['small']))
            story += [KeepTogether(tail), PageBreak()]
        close=P('Як зростає журнал' if uk else 'A growing record','chapter');close.toc_key='growing';story += [close]
        end=md.split('## '+('Як продовжувати книгу' if uk else 'How this book grows'))[-1].strip();story += [P(end),P('Джерела збірки' if uk else 'Build sources','head'),P('results.json: '+ledger_hash,'small'),P('book/narrative.json: '+digest(ROOT/'book/narrative.json'),'small'),P('pr-status.json: '+digest(ROOT/'pr-status.json'),'small'),P('Детальні двомовні звіти та незмінений історичний аудит M7 доступні в репозиторії.' if uk else 'Detailed bilingual reports and the unchanged historical M7 audit are available in the repository.'),Paragraph(f'<link href="{PUBLIC}README.md" color="#126A6C"><u>github.com/DiadkoShmek/engineering-results</u></link>',st['small'])]
        doc.multiBuild(story,canvasmaker=partial(canvas.Canvas,invariant=1))


if __name__=='__main__':
    ledger,narrative=load();pr_markdowns();markdowns(ledger,narrative);pdfs(ledger,narrative)
    print(json.dumps({'records':len(ledger['records']),'chapters':len(narrative['chapters']),'counts':counts(ledger['records']),'created_pdfs':2}))
