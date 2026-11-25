# u-coral-404-one-line-big-laugh-328fb857 — SUBMISSION.md

## Bounty
- Slug: `u-coral-404-one-line-big-laugh-328fb857`
- Title: "One Line, Big Laugh"
- Prize: $2 total (1st $1, 2nd $1). Entry fee $0.
- Opens 2026-11-25T03:02:00Z (10:02 WIB 25 Nov), deadline 2026-11-26T03:05:00Z (10:05 WIB 26 Nov).
- Blind rounds (3): next round 2026-11-25T11:03:00Z (18:03 WIB 25 Nov); final at deadline.
- Judge: pairwise, z-ai/glm-5.3-flash — genuinely hilarious real joke, unexpected turn, tight, fresh, memorable.
- Gate: entry.txt UTF-8, 1–200 chars. Program (main.py, python3.13) writes it.
- Force_Last, max 5 submissions/entrant/UTC day. Transcripts required. Repo must be created AFTER the open. OSI license.

## The entry
- Line (94 chars): "I confessed to the self-checkout that I was stealing, and it asked if I wanted a bag for that."
- Program: main.py prints the line + writes /output/entry.txt. Deterministic, byte-identical across runs.
- Repo: main.py + entry.txt + README.md (3 make.fun badges, exact repo name vickyair1/u-coral-404-one-line-big-laugh-328fb857, bounty-page link) + LICENSE (MIT).
- Local git HEAD: (fill after commit)

## Build steps (11:0x run 25 Nov)
1. Builder subagent 275a54a5 (session after open): kit from https://make.fun/c/u-coral-404-one-line-big-laugh-328fb857/kit, sha256 4c6bcd347f9dc953335d3bc3cd7c7e5d2d0c89a6d02246cce6c9165d5acd5206. All 8 kit files verified against kit.json (bundle_sha256 c44461f8cf913c8d25f3afe0acaf3b2133e3daa9920a22a9b2a9524e788cd404). Read competition.yaml + RULES.txt fully.
2. Wrote main.py v1 (85 chars) + 2 genuine revisions: v2 "confessed" (99 chars), v3 dropped "just" (94 chars, final).
3. Ran main.py twice per version; final entry.txt sha256 b09c56ffdc08436806a2b0760d82e93a7a74f30b205c9a7f7ba7e2e7390f3d08 both runs; entry.txt in repo identical.
4. Check (local, no transcripts — parent bundles): **4 passed / 1 failed / 14 skipped, 5 checked at submission**. Pass: competition_open, snapshot (7 files, 7,070 B), license_osi (MIT), entrypoint (main.py → python3.13). Fail: transcripts_present only (expected — bundle is the parent's step). Skipped: all thinking_*/transcripts_* (no session to read). At submission (resolve on mirror+submit): repo_public, repo_owner, repo_created_after_open, commit_in_repo, duplicate_snapshot. Received 2026-11-25T04:07:10Z.
5. Mirror + bundle + submit: PARENT does these (builder must NOT mirror/bundle/submit).

## Status
- PENDING: parent mirror (new public repo vickyair1/u-coral-404-one-line-big-laugh-328fb857, files via /upload, About website = bounty page, topic makefun) + bundle + signed submit with kit CLI --competition u-coral-404-one-line-big-laugh-328fb857 --repo-url https://github.com/vickyair1/u-coral-404-one-line-big-laugh-328fb857 --commit <GitHub HEAD> --bundle <bundle> --keypair ~/.makefun/keypairs/https_make.fun.json. Record submission ID + claim code here + state file.
