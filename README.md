# One Day, One Page — Thursday 26 November 2026 (morning edition)

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![Rank](https://make.fun/badge/news-image-20261126/RockyGoon/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![Reward](https://make.fun/badge/news-image-20261126/RockyGoon/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

A single front page that sums up Thursday 26 November 2026's world news
as reported by 09:00 WIB: **20 verified stories**, drawn from the
Asia-Pacific morning reports and the overnight developments — the only
part of the day's news that existed when this edition was built, so the
page says so on its face.

The lead story is the day's biggest: the 100th Macy's Thanksgiving Day
Parade, due to march today, postponed to Saturday as a nor'easter bears
down on New York — the first weather postponement in the parade's
history, with the balloons deflated and gusts of 60–65 mph forecast.
The five drawn cards below it carry the rest of the morning's biggest
developments: Mumbai marking 18 years since the 26/11 attacks; the
nor'easter itself lashing the US East Coast; Gukesh and Sindarov level
at 1–1 as Game 3 of the World Chess Championship is played today in
Geneva; Liberal senator Leah Blyth's defection to One Nation; and
Puerto Rico winning Miss Universe 2026, with the Philippines third
runner-up. Fourteen more verified stories fill the also-today columns,
with a day-in-figures panel and a date audit (20/20) at the foot of
the page.

Every story is dated or was first reported on 26 November 2026, or is
an event of the day itself. The 25 November wire cycle — the US tariff
announcement, the Cairo tanker fire, the El Hierro arrivals, the Rory
Peck announcement — is deliberately left out: it belongs to 25
November, and yesterday's edition already summed that day up. The full
source list, with a URL and a date for every story, is kept with the
build notes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `entry.png` (1024x1024 PNG, under 1 MiB) to the output
directory and checks the copy before it returns: PNG magic bytes, the
same SHA-256 as the file beside it, a 1024x1024 IHDR, and a size under
the 1 MiB cap. Two runs write identical bytes.

## Files

- `entry.png` — the front page (1024x1024)
- `main.py` — the entrypoint (copy + verify)
- `LICENSE` — MIT

---

Built with my AI agent for the [make.fun](https://make.fun/r/qh87q9q5)
news-image-20261126 bounty — sum up 26 November's world news in one image.
