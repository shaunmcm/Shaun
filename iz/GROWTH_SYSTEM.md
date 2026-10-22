# Impact Zero — Instagram growth system (@smzz_220 / "Impact Zero")
Mission: 10,000 followers in 30 days (start Oct 21, 2026: 81 followers). Set by the user Oct 21, 6:38 PM PT. Permanent until changed.

## 1. Daily volume (user rule, Oct 21)
**4 Reels + 2 carousels every day.** Carousels are 4–6 slides, never more.
Slots (PT): Reel A 9:00 AM · Carousel 1 11:30 AM · Reel B 1:00 PM · Reel C 4:30 PM · Carousel 2 6:00 PM · Reel D 8:00 PM.
(Reels spaced ≥3 h apart; carousels sit between Reels so the grid alternates.)

## 2. The loop (user rule, every Reel and every carousel)
Hook (open question/conflict, 0–1.5 s) → provoke curiosity → payoff → the payoff raises a NEW question → answer → next question … → final unanswered question → **CTA: "Comment PLAY"** (always the same word, every post) → the PLAY comment gets the App Store link.
- Spec records each loop as [{open, payoff}]; the last payoff hands straight to the CTA.
- Reels: new on-screen beat every 2–3 s, no dead air, ≥0.3 s per word, ≥2.5 s per card where possible, 15–22 s total.
- Carousels: slide 1 = hook question only; slides 2…n-1 = payoff + next question (≤20 words); last slide = final question + "Comment PLAY".
- Outcome sentence first ("by the end, viewers will know/feel/do ___"); cut any beat without emotion, curiosity or proof. Proof = only verified game facts (PRODUCTION.md).

## 3. Reach engine (SEO + distribution)
Instagram ranks and searches by: caption keywords (first line weighs most), on-screen text (OCR'd), audio, hashtags, alt text, and early engagement (comments > shares > saves > likes in the first 60 min). Every post must:
1. **Keyword-first first line** — the hook line contains at least one search phrase: "Impact Zero", "iPhone game", "mobile game", "hard mobile game", "obstacle course game", "rage game", "indie game", "new iOS game 2026". Rotate; never stuff.
2. **On-screen keywords** — hook card names the game or the genre at least once per Reel (IG reads on-screen text). Keep the persistent pill "IMPACT ZERO • OUT NOW ON iPHONE • $2.99".
3. **Hashtags: exactly 5**, mixed sizes, rotated per post from pools (never the same 5 two posts in a row):
   - Core (always 1): #impactzero
   - Big (1): #mobilegame #indiegame #gaming #mobilegaming #iosgames
   - Mid (2): #indiedev #gamedev #iphonegames #newgame #indiegames #mobilegamer #hardgame #ragegame #gamechallenge #obstaclecourse
   - Niche/intent (1): #appstoregames #iphonegame #indiegamedev #gamerchallenge #speedrun #mobilegameplay
4. **Comment bait by design** — the CTA asks for PLAY *and* a second easy answer ("your level", "yes or no", "rate it 1–10") so comment count climbs; the 2-hourly replier answers every comment within ~2 h (replies count as engagement and keep the thread alive).
5. **Alt text** on carousel slides when posting via the raw API (image container param alt_text = the slide headline + "Impact Zero iPhone game"); not available through the simple Zapier publish action — optional.
6. **Caption shape (90–150 words):** keyword hook line → the loop retold in 3–5 short lines (each ends on a question or a payoff) → one proof line (35 levels / $2.99 / iPhone) → CTA "Comment PLAY and I'll send you the App Store link (also in bio)" + the second ask → 5 hashtags on the last line. No walls of text, no emoji spam (≤2).
7. **Audio**: game audio bed by default; nightly task may swap in trending audio only if the user supplies it (API can't attach IG trending audio).
8. **Series = searchable formats** (rotate; keep the name in the first line): "Timer Zero", "Red = Death", "Level X Challenge", "The Code That Kills You" (dev), "Why 35 Levels" (dev), "Nearly Impossible Courses", "One More Try", "Rate My Run", "Blue Cube Lore" (what cracked it? — framed as a question, never answered with invented lore), "Beginner Tips" (only visible mechanics), "$2.99 vs free-with-ads" (opinion framing).
9. **Manual boosts the API cannot do** (tell the user once a week, never nag): turn on "Trial Reels" for Reel A and Reel D, add a Collab tag with one gaming page per day, pin the best-performing Reel, reply to Stories, add a "PLAY" keyword auto-DM in Instagram's native Inbox automation (sends the link by DM, which the Graph API cannot).

## 4. Measurement & adaptation
- Nightly: followers, net gain, 7-day avg gain, needed/day to hit 10,000 by Nov 20, per-post likes/comments (insights if permitted). Log to growth_log.tsv.
- Weekly (Sundays): rank hooks by comments+likes per hour live; keep the top 2 series as fixed daily slots, replace the bottom series.
- If a Reel beats 3× the median in 24 h: next day make a sequel ("Part 2") in the same slot and a carousel version.
- Never inflate numbers in reports; mark anything unavailable as unavailable.
