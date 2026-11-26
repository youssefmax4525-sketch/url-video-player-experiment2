from pathlib import Path
import re,json,difflib,zipfile,hashlib
w=Path('/tmp/player');root=w/'decoded';before=w/'before';changes=[]
# Modify only app-owned request instructions, keeping construction and startup order.
for rel, pairs in {
 'smali/info/t4w/vp/view/VideoPlayer.smali': [('p0, p1, v0, v1','v1','v2')],
 'smali/sPos9472.smali': [('v1, v0, v3, v4','v4','v0'),('v1, v0, v2, v3','v3','v0')]
}.items():
 p=root/rel;s=p.read_text();orig=s
 for regs,callback,temp in pairs:
  needle=f'    invoke-static {{{regs}}}, LRTuÒD5;->e8$mp_s$(Landroid/content/Context;Ljava/lang/String;LtmpOffset3178;LIemp;)V'
  assert s.count(needle)==1
  replacement=f'    const/4 {temp}, 0x0\n\n    invoke-virtual {{{callback}, {temp}}}, LlenIth;->$ÒcdS(LD6$Ff_rK$;)V'
  s=s.replace(needle,replacement)
 b=before/rel;b.parent.mkdir(parents=True,exist_ok=True);b.write_text(orig);p.write_text(s)
 changes.append(rel)
with (w/'changes.patch').open('w') as f:
 for rel in changes:f.writelines(difflib.unified_diff((before/rel).read_text().splitlines(True),(root/rel).read_text().splitlines(True),fromfile='original/'+rel,tofile='experiment/'+rel))
(w/'changed.json').write_text(json.dumps(changes))
print('Patched three request instructions across two files; manifest/resources untouched.')
