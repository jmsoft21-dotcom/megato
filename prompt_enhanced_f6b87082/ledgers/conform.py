import re,glob,os
d=open('design.md',encoding='utf-8').read()
E='/home/user/megato/prompt_enhanced_f6b87082/'
roles={'5.1':'1','5.2':'5','5.3':'2','5.4':'3','5.5':'4'}
secs={}
for s in re.split(r'\n(?=### )',d):
    m=re.match(r'### (\d+\.\d+)',s)
    if m: secs[m.group(1)]=s
def fl(k): return re.findall(r'```text\n(.*?)\n```',secs[k],flags=re.S)
shared_role_line={'1':0,'5':0,'2':0,'3':0,'4':0}
print('== design fences (role-specific, sec 5.x) present verbatim ==')
for sec,r in roles.items():
    for cyc in ('c1','c2'):
        f=glob.glob(E+f'{cyc}_{r}_*.txt')[0]; t=open(f,encoding='utf-8').read()
        fs=fl(sec); miss=[x.split('\n',1)[0][:70] for x in fs if x not in t]
        # GM role lines (3.1) and personas (3.15)
        print(sec,cyc,f'fences {len(fs)-len(miss)}/{len(fs)}', 'MISSING:'+str(miss) if miss else '')
print('== section-3 fences per role present ==')
need={'1':[('3.1',0),('3.1',1),('3.2',0),('3.8',0),('3.9',1),('3.10',0),('3.11',1),('3.12',1),('3.14',0),('3.15',0),('3.16',0),('3.18',0),('3.19',0),('3.20',0),('3.17',1)],
      '5':[('3.1',0),('3.1',5),('3.2',0),('3.8',1),('3.9',2),('3.10',1),('3.11',2),('3.12',1),('3.14',0),('3.15',1),('3.16',0),('3.18',0),('3.19',0),('3.20',0),('3.17',2)],
      '2':[('3.1',0),('3.1',2),('3.2',0),('3.4',0),('3.5',0),('3.6',0),('3.7',0),('3.9',0),('3.11',0),('3.12',0),('3.13',0),('3.15',2)],
      '3':[('3.1',0),('3.1',3),('3.2',0),('3.4',0),('3.5',0),('3.6',0),('3.7',0),('3.9',0),('3.11',0),('3.12',0),('3.13',0),('3.15',3)],
      '4':[('3.1',0),('3.1',4),('3.2',0),('3.4',0),('3.5',0),('3.6',0),('3.7',1),('3.9',0),('3.11',0),('3.13',0),('3.15',4)]}
for r,lst in need.items():
    for cyc in ('c1','c2'):
        t=open(glob.glob(E+f'{cyc}_{r}_*.txt')[0],encoding='utf-8').read()
        miss=[f'{k}[{i}]' for k,i in lst if fl(k)[i] not in t]
        print('role',r,cyc,'missing:',miss)
print('== A14 legacy text ranking ==')
for f in sorted(glob.glob(E+'c*_*.txt')):
    n=os.path.basename(f)[:4]; L=open(f,encoding='utf-8').read().split('\n')
    fz=[i+1 for i,l in enumerate(L) if 'FALSIFIED when a gate misses' in l]
    bl=[i+1 for i,l in enumerate(L) if '<= +0.15%' in l and 'legacy' not in l.lower()]
    mx=[i+1 for i,l in enumerate(L) if 'maximum available' in l]
    p50=sum('50%' in l for l in L)
    print(n,'FALSIFIED@',fz,'| +0.15% w/o legacy@',bl,'| maximum available@',mx,'| 50% lines',p50)
print('== handoffs ==')
sc='candidate_id, OOS_rows, TRAIN_rows, n_selected, bad_count, good_count, bad_rate, good_loss, net30_mean_bps, net30_ci95_lower_bps, y2022_net30_bps, positive_years, thresholds_absolute'
for f in sorted(glob.glob(E+'c*_*.txt')):
    t=open(f,encoding='utf-8').read(); n=os.path.basename(f)[:4]
    print(n,'scorecard_keys',sc in t,'| bottleneck_verification',t.count('bottleneck_verification'),'| BETA_LANE_RESULT.json',t.count('BETA_LANE_RESULT.json'),'| overrides economics',('overrides the economics_verdict sentence of HTS_BACKTEST_ANALYZE' in t))
