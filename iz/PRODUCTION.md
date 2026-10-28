# Impact Zero — Instagram production system (@Smzz_220)

> **CHECK FIRST:** if /home/claude/iz/BLOCKER.md exists, follow it (Zapier task limit; queue blocked posts; do not re-alert). When it clears, re-slot the queue into the next day's regular slots instead of posting everything at once (never dump more than 1 post immediately).

Owner: Shaun (shaunmunoz145@gmail.com). Set up Oct 21, 2026. Permanent, hands-off: never ask permission to post, change or schedule.

## The game (only claim what is verified)
- **NO TIMER (user, Oct 21 7:34 PM): the game has no timer. Never mention a timer, countdown, clock, "finish in time" or "before time runs out" in any post, caption, reply or report.** The penalty is one-touch death on red; the in-game line "Can you win before it takes you out?" refers to the course taking you out, not a clock.
- Impact Zero — "Outer Space Adventure". Blue cracked cube protagonist, RED blocks/lasers = death, green platforms/goals. One touch of red ends the run; you restart the course.
- 35 unique, challenging levels. "Nearly impossible obstacle courses." "Frustratingly satisfying."
- OUT NOW on iPhone, **$2.99**. App Store: https://apps.apple.com/us/app/impact-zero-space-trials/id6808934326
- NEVER show or say: August 27 / 9-9-26 release dates, "wish list" / Steam wishlist, "Steam in November", $6.99, the "Will feature online co-op" segment (gp_v5 19.5–23.5 s). Never invent mechanics, stats, player counts, review quotes or dev-process facts beyond the list above.

## USER UPDATE Oct 21, 6:38 PM PT (newest rules win)
- **4 Reels + 2 carousels per day**; carousels **4–6 slides max**. Slots and the full reach/SEO strategy are in GROWTH_SYSTEM.md (goal: 10,000 followers in one month).
- Every Reel AND carousel: curiosity loop — hook → provoke curiosity → payoff → payoff opens the next question → answer → … → final question → CTA "Comment PLAY" (same word every time).
- Strategy must maximise reach: SEO captions (keyword-first first line), on-screen keywords, 5 rotated hashtags, comment-bait CTA, fast replies. See GROWTH_SYSTEM.md section 3.

- NOTE for the nightly run: if the scheduled message still says "3 Reels + 1 carousel" / old slots, IGNORE that and follow this block + GROWTH_SYSTEM.md (4 Reels + 2 carousels, new slots). When re-scheduling tomorrow's run, write the new prompt in full (6 posts, slots, SEO rules).

## User's master prompt (verbatim rules)
Role: elite indie game marketing director / viral strategist. Daily output: originally 3 Reels + 1 Carousel — now **4 Reels + 2 Carousels** (Oct 21 update).
Every post is a continuous curiosity loop:
1. PRIMARY HOOK (0–1.5 s): intriguing, urgent question or conflict.
2. QUICK RESOLUTION (2–4 s): briefly answer/show the result so nobody scrolls.
3. NEXT LOOP (4–7 s): a new problem/secret/question spawned by that answer.
4. FINAL BRIDGE (7 s+): chain micro-questions to the climax.
5. CTA: high-impact direct command linking the final unanswered question to the action — "Comment PLAY ..." → the PLAY comment leads to the App Store link.
Reel 1 = Hook / Gameplay Action. Reel 2 = Behind-the-Scenes / Dev Journey / Easter Egg. Reel 3 = Community / Challenge / Meta. Carousel = Story, Lore, Tips or Feature Breakdown: slide 1 hook headline, slide 2 answer + secondary hook, slides 3–9 answer→question loop (≤25 words/slide), slide 10 final unanswered question → CTA.
Per Reel the plan records: hook text, loop 1 answer + loop 2 question, visual/clip notes, voiceover script, exact CTA + caption with targeted hashtags.
Style: passionate transparent indie dev talking to gamers; never generic AI slop; quick cuts, dynamic text positioning, zero dead air.
Standing rule from the user's other pages (Oct 20): write the one-sentence outcome first, emotional curiosity hook, loops all the way through, something new every 2–4 s, emotion + curiosity + proof, readable (≥0.3 s per word, ≥2.5 s per card where possible).

- Never describe what a specific numbered level contains (e.g. "level 5 is mostly red") — the footage is not labelled by level. Level numbers only as challenges ("can you clear level 5?").

## Assets (repo shaunmcm/Shaun, folder iz/src; raw URLs https://raw.githubusercontent.com/shaunmcm/Shaun/master/iz/...)
- src/gp_v5.mp4 — 30.5 s clean gameplay band (1440x720, audio). In-game captions: "Nearly impossible obstacle courses…" (~1–4 s), "Can you win before it takes you out?" (~10–13 s). SKIP 19.5–23.5 s (co-op text). Best all-round source.
- src/gp_v1.mp4 — 14.4 s clean gameplay band (1080x542, audio): red walls → green ramp → red barrier → lasers → green particle finish.
- src/v2_main.mp4 — 13.7 s portrait edit: app-icon tap (0–1.5), "35 unique and challenging levels!" band (2.75–4.75), fullscreen gameplay with "Can you do it?" (~5–7). Top zone is free after 4.8 s; bottom zone free 0–4.8 s.
- src/v4_bts.mp4 — 12.4 s dev footage, no audio (1080x580): red-cube test level, Unity editor + code at 2.6–6.5 s.
- src/poster_299.jpg — updated key art: "OUT NOW ON iPHONE / $2.99" (old date + price removed). src/keyart_bg.jpg — clean key art, no text (backdrop).
- src/poster_orig.jpg — ORIGINAL with 9/9/26 + $6.99. Never publish.

## Pipeline
- Spec: posts/dayNN.json (reels.{id}.cards[{t,zone,style,text}], voiceover, caption; carousel.{id}.slides[{head,sub,visual}]).
- Render: `python3 tools/render.py posts/dayNN.json` → out/YYYYMMDD/R*.mp4 (1080x1920, 30 fps) and C*_N.jpg (1080x1350). Prints a s/word timing check — fix every "FAST".
- Reel look: dimmed key-art backdrop, gameplay band centred, Poppins Bold cards (top zone y≈400, bottom zone y≈1520), ALL-CAPS words coloured (RED/ZERO/ENDS red, others cyan), persistent pill "IMPACT ZERO • OUT NOW ON iPHONE • $2.99" (set "label_until" to hide it over an end card).
- New footage from the user: crop out any letterbox text with ffmpeg (detect the bright band rows), drop old end cards, save to src/ and describe it here.
- QA: look at frames at ~1, 5, 10, 15 s and the carousel contact sheet as a stranger would; nothing cut off, nothing overlapping baked text, no banned content.
- Publish media: copy to /home/claude/shaun/iz/{r,c}/, commit as Claude <noreply@anthropic.com>, push to master.

## Posting (Zapier → Instagram for Business)
- Account: Instagram **Smzz_220** = instagramPageId **17841442662401596** (verified Oct 21: username smzz_220, display name "Impact Zero"; the Zapier enum label is "Impact Zero", NOT "Smzz"). Website field already = App Store link. NEVER post to Unspoken At Work (17841420504964559), Money Mapped (17841413335234840), Odds Visualized (17841423585967011), Broke Proof Kids (17841440839365671) or Warriors for Christ (17841403533778015).
- If 17841442662401596 is missing from the enum, the connection dropped: SendUserMessage once (Instagram Smzz_220 must be a Professional/Business account linked to a Facebook Page, then reconnect Zapier "Instagram for Business" so Smzz_220 appears), reschedule the post for the same slot next day, and do not post anywhere else.
- Reels: instagram_for_business_publish_video (video = raw URL, caption, instagramPageId). Carousel: instagram_for_business_publish_photo_s (publish_media_v2) with slide URLs in order. "Still processing" → wait 75 s, GET https://graph.facebook.com/v19.0/<pageId>/media?fields=id,permalink,timestamp,caption&limit=5 via Make API GET Request and retry only if not there. Never post twice.
- Slots (PT) from Oct 22: Reel A 9:00 AM · Carousel 1 11:30 AM · Reel B 1:00 PM · Reel C 4:30 PM · Carousel 2 6:00 PM · Reel D 8:00 PM. Log to posted.log and content_log.tsv.

## "Comment PLAY" system
- Before replying, fetch replies too (comments{...,replies{...}}): if smzz_220 (the owner) already replied to a comment, do NOT add a second reply - log it as owner-replied-manually. (Oct 26: Shaun answered khuzaima_accel_brands himself; Claude's reply doubled it.)
- Owner-stated fact (Oct 26, his own reply): the lasers were the more difficult part. Usable as "the dev says lasers were the hardest part".
- Every 2 h (8 AM–10:30 PM PT) a task reads comments on the last 10 Smzz_220 posts (GET /<pageId>/media?fields=id,permalink,comments{id,text,username,timestamp}). For any comment containing "play" (case-insensitive) not yet in comments_log.tsv and not by Smzz_220: reply via Make API Mutating Request POST /<comment-id>/replies?message=<reply>. Reply text: "Here you go 🎮 https://apps.apple.com/us/app/impact-zero-space-trials/id6808934326 — comment the level that stops you!". Also send that link by DM only if a DM action is available; otherwise the reply is enough. Reply kindly to other comments (level numbers, feedback) in the dev's voice; never argue.

## Content series to rotate (no repeats within 7 days)
Red = Death, Level X Challenge ("comment your level"), The Code That Kills You (dev), Why 35 Levels (dev), Nearly Impossible Courses, One More Try psychology, Blue Cube lore (what cracked it?), Tips: how to survive level N (only from footage), Reaction/duet bait ("rate my run"), Price/launch meta ($2.99 vs free-with-ads — opinion framing only, no false claims).
