# Pass 2 brief — fold newly arrived transcripts into an existing note

Your note already exists at `notes/wss-<cluster-key>.md` and was written from an incomplete transcript set.
The backfill has since recovered most of the channel. New files for your cluster are listed in
`_clusters_pass2.json` (this folder) under your key. Read the original `_BRIEF.md` for format and rules;
they still apply in full (own words, quotes under 15 words and few, no transcript passages, no emoji,
only link to files that exist).

## Do, in this order
1. Read your note in full, especially its **Gaps** section and any places marked as reconstructed,
   pieced together from fragments, textbook, or "not from the channel".
2. Read every new transcript for your cluster. Also check whether titles in your Gaps list now have a
   file anywhere in `videos/` or `shorts/` (grep by video ID); read those too even if routed to another cluster.
3. **Upgrade, don't append.** For each concept the new material teaches:
   - If the concept already has a section: revise it in place with the channel's actual explanation,
     numbers and examples; replace reconstructions; keep corrections that still hold; add new ones.
   - If it is a new concept worth teaching: add a full section in the same 9-part format, placed in
     foundational → advanced order, and add it to the concept map.
   - Update **How the concepts connect** and add retrieval questions for new concepts.
4. Update the header blockquote source counts, and rewrite **Gaps** to list only what is still missing.
5. Keep the `> **Part of [[wall-street-skinny-insights]]**` line at the top intact.

## Do not
- Edit any file other than your own note.
- Pad. If a new transcript adds nothing beyond what the note says, skip it and count it as "read, no change".

Return a 5-line summary: transcripts read, sections revised, sections added, reconstructions replaced, remaining gaps.
