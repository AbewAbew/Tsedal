"""Verify the running landing routes, translations, assets and LMS links."""
import requests
from bs4 import BeautifulSoup
s=requests.Session(); s.headers['Host']='tsedal.localhost:18780'
base='http://127.0.0.1:18780'
r=s.get(base+'/',allow_redirects=False,timeout=30)
assert r.status_code in (301,302) and r.headers['Location']=='/en', (r.status_code,r.headers.get('Location'))
for language in ['en','am']:
    r=s.get(base+'/'+language,timeout=30)
    assert r.status_code==200, (language,r.status_code,r.text[-1000:])
    soup=BeautifulSoup(r.text,'html.parser')
    assert soup.html['lang']==language
    assert len(soup.select('html'))==1 and r.text.lstrip().lower().startswith('<!doctype html>')
    assert len(soup.select('h1'))==1
    assert ('Accessible digital education' in soup.h1.get_text()) == (language=='en')
    assert soup.select_one(f'[data-language="{language}"]')['aria-current']=='page'
    assert all(a['href']=='/lms/courses' for a in soup.select('.lms-link-btn'))
    assert not soup.select('#configModal,#googleModal')
    assert 'http://tsedal.localhost:18780/lms' not in r.text
    assert soup.select_one('link[rel=canonical]')['href']=='http://tsedal.localhost:18780/'+language
    for attr in ['src','href']:
        for tag in soup.select('['+attr+']'):
            value=tag[attr]
            if value.startswith('/assets/'):
                asset=s.get(base+value,timeout=30)
                assert asset.status_code==200,(value,asset.status_code)
    print(language+': route, translation, metadata, CTA links and assets OK')
for path in ['/lms/courses','/login?redirect-to=/lms/courses','/tsedal-help']:
    r=s.get(base+path,timeout=30); assert r.status_code==200,(path,r.status_code)
print('Homepage redirects to /en; LMS, sign-in and Help remain available.')
