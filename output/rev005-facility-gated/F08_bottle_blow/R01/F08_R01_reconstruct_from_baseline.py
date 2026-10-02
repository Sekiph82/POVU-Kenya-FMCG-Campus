from pathlib import Path
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus')
BASE=ROOT/'output/rev005-facility-gated/F08_bottle_blow'
WORK=BASE/'R01/F08_bottle_blow'
for name in ('F08_LEGACY_BOTTLE_BLOW_INVENTORY.json','F08_PROTECTION_BEFORE.json'):
 assert (WORK/name).exists(), 'R01_MISSING_LOCKED_INPUT '+name
for name in ('F08_build_scene.py','F08_visual_refine.py'):
 source=(BASE/name).read_text(encoding='utf-8')
 old="E=ROOT/'output/rev005-facility-gated/F08_bottle_blow'"
 new="E=ROOT/'output/rev005-facility-gated/F08_bottle_blow/R01/F08_bottle_blow'"
 assert old in source, 'R01_HELPER_PATH_BINDING_NOT_FOUND '+name
 source=source.replace(old,new,1)
 print('R01_EXEC_PUBLISHED_HELPER',name,'SHA256_SOURCE_FROM_GIT_WORKTREE')
 exec(compile(source,str(BASE/name),'exec'),globals())
print('R01_DETERMINISTIC_RECONSTRUCTION_COMPLETE',str(WORK/'F08_STAGED.blend'))
