import sys, importlib.util, reel
p = sys.argv[1]
spec_mod = importlib.util.spec_from_file_location("m", p); m = importlib.util.module_from_spec(spec_mod); spec_mod.loader.exec_module(m)
import re
for i,s in enumerate(m.SPEC["scenes"]):
    words=len(re.sub(r"[*\"]","",s["text"]+" "+s.get("sub","")).split())
    need=max(2.5,0.4*words)
    print(f"scene {i+1}: {words} words, {s['dur']}s, need {need:.1f}s ->", "OK" if s["dur"]>=need-0.05 else "FAIL")
tot=sum(s["dur"] for s in m.SPEC["scenes"])
print(f"total {tot:.1f}s ->", "OK" if tot<=12.0 else "FAIL (Reels must be <= 12 s)")
mp4, total, mi = reel.render(m.SPEC, "out")
starts=[0]
for s in m.SPEC["scenes"]: starts.append(starts[-1]+s["dur"])
times=[min(starts[i]+0.6, starts[i+1]-0.3) if i==0 else starts[i]+s["dur"]*0.85 for i,s in enumerate(m.SPEC["scenes"])]
times[0]=0.1
print(mp4, total, mi)
print(reel.stills(mp4, times, f"out/{m.SPEC['id']}_sheet.jpg"))
