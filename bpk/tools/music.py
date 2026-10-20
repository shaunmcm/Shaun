"""Original, procedurally generated background music (no samples, no copyrighted material).
Styles: piano, pluck (gentle acoustic), lofi, playful. Every call with a new seed gives a different track."""
import numpy as np, wave, random

SR = 44100
KEYS = {"C": 60, "D": 62, "Eb": 63, "F": 65, "G": 67, "A": 57, "Bb": 58}
PROGS = [[0, 7, 9, 5], [0, 5, 9, 7], [9, 5, 0, 7], [0, 9, 5, 7], [5, 7, 0, 9], [0, 4, 9, 5]]
MAJ = {0: [0, 4, 7], 2: [2, 5, 9], 4: [4, 7, 11], 5: [5, 9, 12], 7: [7, 11, 14], 9: [9, 12, 16]}


def hz(m): return 440 * 2 ** ((m - 69) / 12)


def env(n, a=0.005, r=1.2):
    t = np.arange(n) / SR
    e = np.minimum(1, t / a) * np.exp(-t / r)
    return e


def piano(f, dur, vel=.5):
    n = int(dur * SR); t = np.arange(n) / SR
    s = sum(np.sin(2 * np.pi * f * k * t) / k ** 1.6 for k in range(1, 6))
    return vel * s * env(n, .004, .9)


def pluck(f, dur, vel=.5):
    n = int(dur * SR); p = max(2, int(SR / f))
    buf = np.random.uniform(-1, 1, p); out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % p]
        buf[i % p] = .5 * (buf[i % p] + buf[(i + 1) % p]) * .996
    return vel * out * env(n, .002, 1.4)


def pad(f, dur, vel=.12):
    n = int(dur * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) + .5 * np.sin(2 * np.pi * f * 2.003 * t) + .3 * np.sin(2 * np.pi * f * .998 * t)
    e = np.minimum(1, t / .6) * np.minimum(1, (dur - t) / .6).clip(0)
    return vel * s * e


def bass(f, dur, vel=.3):
    n = int(dur * SR); t = np.arange(n) / SR
    return vel * np.sin(2 * np.pi * f * t) * env(n, .01, .7)


def lowpass(x, a=.15):
    y = np.zeros_like(x); acc = 0
    for i in range(len(x)):
        acc += a * (x[i] - acc); y[i] = acc
    return y


def make(path, dur, style=None, seed=None):
    rng = random.Random(seed); np.random.seed(seed if seed is not None else None)
    style = style or rng.choice(["piano", "pluck", "lofi", "playful"])
    key = KEYS[rng.choice(list(KEYS))]
    bpm = {"piano": rng.randint(72, 84), "pluck": rng.randint(88, 100), "lofi": rng.randint(70, 80), "playful": rng.randint(104, 116)}[style]
    prog = rng.choice(PROGS)
    beat = 60 / bpm; bar = 4 * beat
    total = int((dur + 2) * SR)
    mix = np.zeros(total)
    inst = {"piano": piano, "pluck": pluck, "lofi": piano, "playful": pluck}[style]
    patterns = [[0, 1, 2, 1, 0, 2, 1, 2], [0, 2, 1, 2, 0, 2, 1, 0], [0, 1, 2, 0, 1, 2, 1, 2]]
    pat = rng.choice(patterns)
    mel_scale = [0, 2, 4, 7, 9, 12, 14, 16]
    nb = int(dur / bar) + 2
    for b in range(nb):
        root = prog[b % 4]; ch = MAJ[root]
        st = int(b * bar * SR)
        # pad
        for m in ch:
            p = pad(hz(key + m - 12), bar + .4, .05 if style != "lofi" else .07)
            mix[st:st + len(p)] += p[:max(0, total - st)]
        # bass
        bl = bass(hz(key + root - 24), bar * .9, .22)
        mix[st:st + len(bl)] += bl[:max(0, total - st)]
        if style in ("pluck", "playful"):
            bl2 = bass(hz(key + root - 24), beat * 1.5, .16)
            s2 = st + int(2 * beat * SR); mix[s2:s2 + len(bl2)] += bl2[:max(0, total - s2)]
        # arpeggio (8th notes)
        for i in range(8):
            if style == "piano" and i % 2: continue
            m = ch[pat[i]] + (12 if i >= 4 and style == "playful" else 0)
            nt = inst(hz(key + m), beat * 1.6, .16 if style != "lofi" else .12)
            s = st + int(i * beat / 2 * SR)
            mix[s:s + len(nt)] += nt[:max(0, total - s)]
        # sparse melody every other bar
        if b % 2 == 1 and b < nb - 1:
            for j in range(rng.choice([2, 3])):
                m = rng.choice(mel_scale) + 12
                nt = inst(hz(key + m), beat * 2, .13)
                s = st + int(rng.choice([0, 1, 2, 3]) * beat * SR)
                mix[s:s + len(nt)] += nt[:max(0, total - s)]
    if style == "playful" or style == "pluck":
        # soft shaker on off-beats
        for k in range(int(dur / beat * 2)):
            if k % 2 == 1:
                n = int(.05 * SR); s = int(k * beat / 2 * SR)
                if s + n < total:
                    mix[s:s + n] += np.random.uniform(-1, 1, n) * np.exp(-np.arange(n) / (SR * .01)) * .03
    if style == "lofi":
        mix = lowpass(mix, .2)
        mix += np.random.uniform(-1, 1, total) * .004  # vinyl hiss
    mix = mix[:int(dur * SR)]
    # fades
    fi, fo = int(.4 * SR), int(1.6 * SR)
    mix[:fi] *= np.linspace(0, 1, fi); mix[-fo:] *= np.linspace(1, 0, fo)
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * .55
    st = np.stack([mix, mix], 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype(np.int16).tobytes())
    return {"style": style, "bpm": bpm, "key": key}


if __name__ == "__main__":
    import sys
    print(make(sys.argv[1], float(sys.argv[2]), sys.argv[3] if len(sys.argv) > 3 else None, int(sys.argv[4]) if len(sys.argv) > 4 else None))
