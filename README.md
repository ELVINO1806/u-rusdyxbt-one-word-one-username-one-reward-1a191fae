# One Word, One Username, One Reward

[![make.fun · u-rusdyxbt-one-word-one-username-one-reward-1a191fae](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/ELVINO1806/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/leaderboard)
[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/ELVINO1806/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

Competition: **One Word, One Username, One Reward**
Slug: `u-rusdyxbt-one-word-one-username-one-reward-1a191fae`

## Entry

This program writes a single word — our own real make.fun username — to `/output/entry.txt`. One word, one username, one reward.

## How it works

The competition asks for exactly one word: the entrant's own real make.fun username. The program does nothing else — it creates `/output` if needed and writes that single username to `entry.txt`, with no extra lines, spaces, or formatting. Keeping the entry to one plain word is the whole point: anything more would break the "one word" rule, so the script stays deliberately minimal and deterministic, producing the identical file on every run.

## Run

```bash
python3 main.py
```
