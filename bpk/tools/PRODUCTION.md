# BrokeProofKids — Production System (read before every run)

The user's full brief is MASTER_PROMPT.txt in this folder. It is the top-level operating system. This file is the house method that implements it. Newest USER UPDATE blocks (add them at the top) win.

## ⭐ PERMANENT USER RULE (Oct 20, 5:06 PM) — OUTCOME + CURIOSITY LOOPS (applies to EVERY Reel and carousel; top priority)
Keep niche, style, visuals, pacing, CTAs, hashtags and post counts the same. On top of that:
1. OUTCOME FIRST: before writing, write one sentence in the production record: "By the end of this post, viewers will know / feel / be able to ___." Cut anything that doesn't serve it.
2. HOOK: emotionally strong AND built around an open question (e.g. "...so what should you say instead?").
3. LOOPS all the way through: open a question → pay it off → open the next question. Each scene/slide = payoff of the last question + the next open question (often in the sub line). The LAST payoff delivers the outcome, then the ending.
4. NEW EVERY 2–4 s: each beat adds a number, an example, a screenshot-style visual (receipt, app screen, price tag, chat bubble) or a short story beat. Animate props so something changes within each scene.
5. EMOTION + CURIOSITY + PROOF: every post has all three; proof = real or clearly-labeled example numbers only (no invented stats). Cut any beat that gives none of them.
6. READABILITY: scene duration ≥ 0.4 s × words on screen (text + sub), minimum 2.5 s per screen, simple words. If it runs long, CUT beats/words — never speed up. render_reel.py prints a timing check; fix any FAIL.
7. BOOK CTA: the product is named the **Money Smart Kids Coloring Book**. Every Reel/carousel/caption ends with "Get the Money Smart Kids Coloring Book — link in bio" (+ the follow line). The whole post should build toward it: the final loop's payoff should make practicing at home the natural next step (e.g. "want them practicing this on paper?") → CTA. Still don't describe specific pages/contents unless the user supplies them.

## USER UPDATE Oct 20 (3:24 PM) — HOOK + CTA STYLE (overrides older hook guidance)
User wants opening hooks that hit like: "Your kid doesn't become broke later, they become broke now" / "Your kid can build rich habits right now on their own". Every hook must be EMOTIONALLY STRONG + CURIOSITY-DRIVEN, framed around the child's future money life being shaped TODAY (broke-later vs habits-now, identity, stakes), and must still name the specific problem the post solves.
- Hook formulas: "Broke adults start as kids who never learned ___." · "Your kid isn't going broke at 25. It's starting right now, with ___." · "The habit that keeps kids broke later shows up at age __: ___." · "Rich habits don't start with a paycheck. They start with ___." · "Your kid can start building rich habits today, with ___."
- Honesty guardrails still apply: no promises that a kid will "be rich", no invented stats; "rich habits" / "broke habits" language is fine.
- Every post ends with BOTH CTAs: the book ("Get the Money Smart Kids Coloring Book, link in bio") AND follow ("Follow @kids_and_money_554 for a new money lesson every day"). Reels: last scene shows both. Carousels: last slide shows both. Captions: book CTA paragraph + follow line.

## Account + publishing (verified Oct 20, 2026)
- Instagram: @kids_and_money_554 ("Kids & Money"), instagramPageId **17841440839365671**. Post ONLY here. Never post to Odds Visualized (17841423585967011), Money Mapped (17841413335234840), Unspoken at Work (17841420504964559) or any other account.
- Publish via Zapier InstagramBusinessCLIAPI: Reels = `publish_video` (tool instagram_for_business_publish_video); carousels = `publish_media_v2` (tool instagram_for_business_publish_photo_s); Stories = Make API Mutating Request: POST https://graph.facebook.com/v19.0/17841440839365671/media with querystring media_type=STORIES & image_url=<raw url>, then POST .../media_publish with creation_id.
- Media hosting: public repo clone /home/claude/shaun (GitHub shaunmcm/Shaun, branch master), folder bpk/ (r/ reels, c/ carousels, s/ stories). Raw URL base: https://raw.githubusercontent.com/shaunmcm/Shaun/master/bpk/  (if the user creates shaunmcm/brokeproofkids-media, switch to it and update this line). Re-clone with add_repo if the folder is missing. Commit as Claude <noreply@anthropic.com>.
- "Still processing" rule: wait 75 s, GET .../17841440839365671/media?fields=id,permalink,timestamp,caption&limit=3 via Make API GET Request; retry only if the post is not there. Never post twice.
- The separate 30-day OpusClip clip run (Day N clips, 10:00 AM PT, ends Nov 15) also posts to this account. Leave it alone; don't duplicate its topics.

## Known limits (tell the user, don't fake)
- Bio link: the API cannot edit it. As of Oct 20 the bio link was the YouTube channel; user was asked to set https://a.co/d/01qxpxia. Check `website` field each night; if still not Amazon, mention it in the daily report.
- Story link stickers: NOT supported by the API. Stories post as plain frames; say "link in bio" on them.
- Comment-to-DM: no integration. Never write "Comment BOOK".
- Amazon listing could not be opened (robots block). Never describe specific pages, activities, ratings, prices or reviews of the book. Name: Money Smart Kids Coloring Book (user, Oct 20). Describe it only as a kids' money activity & coloring book until the user supplies contents.
- Insights: try GET /{media-id}/insights?metric=reach,saved,shares,total_interactions,ig_reels_avg_watch_time for Reels; if not permitted, use like_count/comments_count only and say so.

## Schedule
- USER UPDATE Oct 20 (3:32 PM): EVERY DAY = 2 Reels + 1 carousel. Slots: Reel A 12:00 PM PT, carousel 4:30 PM PT, Reel B 7:30 PM PT (both Reels use the day's theme from different angles/mechanisms). Plus 1-2 Story frames (~9:30 AM teaser, ~6:00 PM tip/question). The OpusClip clip run at 10 AM is separate and continues until Nov 15.
- Weekday themes: Mon Allowance Mistake · Tue Teaching Kids to Save · Wed Money Quotes With Practical Lessons · Thu Digital Spending & Gaming Currency · Fri Real-Life Money Decisions · Sat Parenting Money Myths · Sun Family Money Challenges.
- Rotate the 8 hook mechanisms; no mechanism twice in a row. Check topic_log.tsv: nothing substantially similar to the last 60 days (including the 30-day clip captions: allowance-gone-day-one, refilling allowance, 24-hour rule, Robux cost, 3 questions before buying, spend/keep envelopes, $1/day allowance, monthly digital-purchase total, saving-everything, goal-based saving, kids learn by watching you).

## Per-post method (MASTER_PROMPT sections 4–8, 13, 14)
1. Pick the problem (theme + PLAN.md / topic_log). 2. Write 5 hooks with different mechanisms; score each 1–10 on the 8 criteria; keep the best (rewrite if <8 avg). Record all in records/<id>.md (section-13 production record).
3. Reels: copy posts/R001_seeit.py as the template. 6 scenes, ~28–34 s: hook (instant, readable at frame 1, held ≥3.8 s, states the problem AND the promised payoff in the sub line) → tension → TRY THIS solution → concrete numbers demo (animated prop) → payoff that resolves the hook → CTA (rotate wording, "link in bio"). Text y 340–~800, props ~830–1500 (bottom of screen is covered by IG caption UI). Every scene has a prop that changes and illustrates the idea (props.py; add new props there when a topic needs them). No voiceover (no TTS tool) — must make sense muted.
4. Music: music.py, original procedural, new seed every post, rotate style (piano / pluck / lofi / playful) to match the emotional arc.
5. Carousels: copy posts/C001_freechoice.py. 7 slides, 1080x1350: problem hook (+ "Swipe") → why → mistake/contrast → solution → worked example with numbers → payoff → CTA. Complete solution in the slides.
6. Captions: 5 paragraphs (emotional hook / why it matters / the lesson / one actionable takeaway with age note / book CTA "through the link in our bio"), 3–5 hashtags, rotate SEO phrases. Never say URLs in captions are clickable. Store in posts/captions.json.
7. Render: `python3 render_reel.py posts/<id>.py` / `python3 render_carousel.py posts/<id>.py` (from /home/claude/bpk). Open the contact sheet and check like a stranger: readable, nothing overlapping/cut off, payoff resolves hook. Fix before shipping.
8. QA checklist (section 14) — all 15 must be yes.
9. Copy to /home/claude/shaun/bpk/{r,c,s}/, commit, push. Append to topic_log.tsv (date, id, type, theme, mechanism, problem, hook, status).
10. Schedule with send_later; each message self-contained (id, raw URL(s), caption key in /home/claude/bpk/posts/captions.json, action, page id 17841440839365671 ONLY, still-processing rule, append to posted.log, update topic_log status, SendUserMessage one line with permalink).

## Weekly review (Sundays)
Rank the week's posts by (saves+shares)/reach if insights work, else likes+comments per post. Which mechanisms/themes win? Where do viewers drop? Change ONE variable at a time. Write findings to LEARNINGS.md and adjust PLAN for next week. Real data only.
