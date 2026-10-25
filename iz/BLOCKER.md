# ACTIVE BLOCKER (set 2026-10-25 03:00 UTC = Sat Oct 24 8:00 PM PT)
Zapier returned "Task limits for this account have been reached." on a Make API GET Request.
All Zapier calls (posting, comment checks, analytics) will fail until the user raises the limit
(turn on pay-per-task or upgrade in Zapier -> Settings -> Billing & Usage) or the monthly reset (likely Nov 17, the plan's billing date).
User has been told once. Scheduled tasks hitting the same error: do NOT message the user again;
log the post as "blocked-zapier-task-limit" in content_log.tsv, keep the chains alive, and try the
blocked posts again on the next run. When a Zapier call succeeds again, delete this file, post the
blocked items (oldest first, skipping any whose caption already exists), and tell the user in one line that posting resumed.
Blocked queue: R016_tag (day04.json)
