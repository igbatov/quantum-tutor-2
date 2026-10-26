import re,sys,base64,os
src=sys.argv[1]; dst=sys.argv[2]; base=os.path.dirname(src)
html=open(src).read()
def rep(m):
    p=os.path.join(base,m.group(2))
    if not os.path.exists(p): return m.group(0)
    data=base64.b64encode(open(p,'rb').read()).decode()
    ext=p.rsplit('.',1)[-1].lower(); mime='image/gif' if ext=='gif' else 'image/png'
    return f'{m.group(1)}data:{mime};base64,{data}{m.group(3)}'
html=re.sub(r'(<img[^>]*src=")([^"]+)(")',rep,html)
open(dst,'w').write(html)
