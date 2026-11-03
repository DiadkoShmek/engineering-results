#!/usr/bin/env python3
"""Offline data, generated-source, local-link, evidence and privacy invariants."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import sys
from datetime import date

# The normal documented CLI must not manufacture bytecode artifacts.
sys.dont_write_bytecode = True

from public_files import public_files
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]


def validate(records):
    assert len({r['id'] for r in records}) == len(records), 'duplicate record id'
    for r in records:
        allowed = {
            'upstream_contribution': {'merged', 'incorporated_in_maintainer_fix', 'superseded_by_open_maintainer_fix'},
            'external_audit': {'credited_in_release'},
            'competition': {'snapshot', 'preliminary', 'final'},
        }
        assert r['category'] in allowed, ('unknown category', r['id'])
        assert r['status'] in allowed[r['category']], ('unknown or incompatible status', r['id'])
        date.fromisoformat(r['as_of'])
        assert urlparse(r['source_url']).scheme == 'https', r['id']
        if r['status'] == 'merged':
            assert r.get('contribution_merged') is True and r.get('merge_commit_sha'), r['id']
        if r['status'] == 'incorporated_in_maintainer_fix':
            assert r.get('contribution_merged') is False, r['id']
            assert r.get('upstream_fixes') and all(f.get('merged') is True and f.get('merge_commit_sha') for f in r['upstream_fixes']), r['id']
        if r['status'] == 'superseded_by_open_maintainer_fix':
            assert r.get('contribution_merged') is False, 'pending replacement counted as direct merge'
            assert r.get('upstream_fixes') and all(f.get('merged') is False and f.get('state') == 'OPEN' for f in r['upstream_fixes']), 'pending replacement claims a merge'
        evidence = r.get('evidence')
        if evidence:
            data = (ROOT/evidence['path']).read_bytes()
            assert hashlib.sha256(data).hexdigest() == evidence['sha256'], evidence['path']


def run():
    from build import counts
    ledger = json.loads((ROOT/'results.json').read_text())
    narrative = json.loads((ROOT/'book/narrative.json').read_text())
    records = ledger['records']; validate(records)
    covered = [rid for c in narrative['chapters'] for rid in c['record_ids']]
    assert sorted(covered) == sorted(r['id'] for r in records), 'chapter coverage or double count'
    assert all(c['uk'] and c['en'] for c in narrative['chapters'])
    # Keep this schema control independent of whether any real replacement
    # is still open: a journal with no pending outcomes is valid.
    pending = {
        'id': 'pending-merge-validation-control',
        'category': 'upstream_contribution',
        'status': 'superseded_by_open_maintainer_fix',
        'as_of': records[0]['as_of'],
        'source_url': records[0]['source_url'],
        'contribution_merged': False,
        'upstream_fixes': [{'state': 'OPEN', 'merged': False}],
    }
    validate(records + [pending])
    corrupt = copy.deepcopy(records + [pending])
    corrupt[-1]['upstream_fixes'][0]['merged'] = True
    try:
        validate(corrupt)
    except AssertionError:
        pass
    else:
        raise AssertionError('negative control accepted a pending merge')
    competition = [r for r in records if r['category'] == 'competition']
    assert counts(records)['arenas'] == len({r['competition'] for r in competition})
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    ledger_sha = sha(ROOT/'results.json'); narrative_sha = sha(ROOT/'book/narrative.json')
    generated = ['README.md','README.en.md','RESULTS.md','RESULTS.en.md','book/uk/BOOK.md','book/en/BOOK.md']
    for name in generated:
        text=(ROOT/name).read_text()
        assert 'ledger-sha256:'+ledger_sha in text and 'narrative-sha256:'+narrative_sha in text, 'stale '+name
    files = list(public_files(ROOT))
    links=0
    for path in (p for p in files if p.suffix == '.md'):
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',path.read_text()):
            if urlparse(target).scheme in ('http','https','mailto'):continue
            name=unquote(target.split('#')[0])
            if not name:continue
            destination=(path.parent/name).resolve()
            assert ROOT in destination.parents, ('link escapes repository', target)
            assert destination.is_file(), (path.relative_to(ROOT),target)
            if '#' in target and destination.suffix=='.md':
                content=destination.read_text();fragment=unquote(target.split('#',1)[1])
                anchors=set(re.findall(r'id="([^"]+)"',content))
                for heading in re.findall(r'^#+ (.+)$',content,re.M):
                    slug=re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-')
                    anchors.add(slug)
                assert fragment in anchors,(path.relative_to(ROOT),target,'missing anchor')
            links+=1
    forbidden = ['/'+ 'home/', '/'+ 'Users/', 'local'+'host', '127.'+'0.0.1', '\u0410\u0440\u0442\u0443\u0440', 'Ar'+'tur']
    for path in files:
        try:
            text=path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        assert not any(x in text for x in forbidden), 'privacy '+str(path.relative_to(ROOT))
        assert not re.search(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}',text), 'email '+str(path.relative_to(ROOT))
        assert not re.search(r'\+380\d{9}',text), 'phone '+str(path.relative_to(ROOT))
    books=list((ROOT/'book/pdf').glob('*.pdf'));assert len(books)==2
    for path in books:
        assert path.read_bytes().startswith(b'%PDF-') and ledger_sha.encode() in path.read_bytes(), 'PDF ledger identity '+path.name
    assert not (ROOT/'house').exists() and not (ROOT/'engineering-results-qa').exists(), 'private/unwanted tree'
    return {'status':'PASS','records':len(records),'chapters':len(narrative['chapters']),'counts':counts(records),'local_links_checked':links,'negative_pending_merge_control':'rejected','ledger_sha256':ledger_sha,'files_sha256':{str(p.relative_to(ROOT)):sha(p) for p in files}}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--manifest',type=Path);args=parser.parse_args()
    result=run()
    if args.manifest:
        assert ROOT not in args.manifest.resolve().parents, 'keep QA manifest outside public repo'
        args.manifest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='files_sha256'},indent=2))
