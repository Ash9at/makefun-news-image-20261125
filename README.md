# makefun-news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Ash9at/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Ash9at/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

The Daily Ledger — Wednesday 25 November 2026. A program-drawn newspaper front page summing up the day's world news: tankers ablaze in the Strait of Hormuz, Pakistan's first astronaut aboard Tiangong, a 6.2% KOSPI plunge, and more. Every story was verified against reports dated 25 November 2026.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`gen.py` draws the front page with Pillow (run at build time); `main.py` writes the shipped `entry.png` to `/output/entry.png` using only the Python standard library, so it runs in the grader's no-network sandbox and produces byte-identical output on every run.

## The day's news (all dated 25 November 2026)

- **Lead — Strait of Hormuz:** Two oil tankers struck naval mines and caught fire, Iran's Revolutionary Guard said. [CLAIM]
- **Space:** Shenzhou-24 docked with Tiangong, carrying Muhammad Zeeshan Ali, Pakistan's first astronaut and the first foreign visitor to the station. (Reuters, Dawn)
- **Markets:** South Korea's KOSPI fell 6.16% and Japan's Nikkei 2.78% in a sharp sell-off in chip stocks. (Yonhap)
- **Gaza:** An Israeli strike killed Hamas security chief Mohammad Abuelouf, his wife and children, Gaza medics said. (Just Security, SCMP)
- **Colombia:** Security forces stormed a supermarket in Cartagena after a 17-hour siege, freeing all hostages; one captor was killed. (Reuters, Al Jazeera)
- **Pacific:** Australia and the Solomon Islands signed a treaty in Canberra barring any foreign military or security base on the Solomons. (Just Security)
- **Saudi Arabia:** Yemen's Houthis said they attacked the Ras Tanura oil refinery; fires were reported. [CLAIM]
- **Ukraine:** A Russian strike killed two people in the Odesa region and injured three, the regional governor said; Kyiv was also hit. (Just Security)
- **Climate:** The UN COP31 climate talks failed to reach an agreement; Pope Leo XIV voiced concern. (AP via Just Security)

[CLAIM] = one party's claim, not independently verified. No story from 24 or 26 November is used; each item above was checked against a report dated 25 November 2026.

---

Entered on [make.fun](https://make.fun/?ref=1z6j2brj&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards
