# makefun-news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/yudhisutawan/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/yudhisutawan/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

The World, Today — a one-page newspaper front page summing up the world's news of Monday 23 November 2026 in 48 stories: COP31 collapses with no deal at all, tankers burn in the Strait of Hormuz, NATO meets as Russian missiles land in Poland, sea drones sink a Russian warship off Libya — plus 44 more stories across world, business, tech, science, sport and culture.

The picture is pre-rendered and stored in this repository as `entry.png`. `main.py` only copies it to the output path, using nothing but the Python standard library: no network, no clock, no randomness, so a second run writes byte-identical output. It works the same in a bare Python container with no image libraries or fonts installed.

## How to run it

```sh
python3 main.py   # writes /output/entry.png
```

Running it drops the picture at `/output/entry.png` — or at `$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set. The file is a 1024x1024 PNG of 164,491 bytes, far below the 1 MiB cap.

## How it was built

Three front-page candidates were drawn from the same verified set of 23 November 2026 stories (COP31, Hormuz, Poland/NATO, Benghazi, Dymer, Asian markets, BepiColombo, MotoGP, the Wellington Test and more) and judged head-to-head on the competition's own criteria — naming the day, selection and breadth, readability, faithfulness, craft. The winner is this one: the proven "The World Today" template (2 leads + 1 banner + 15 tiles + 30 briefs = 48 stories), leading with the day's biggest story, the COP31 collapse, with every headline and body checked to fit without clipping.

---

<sub>Entered on [make.fun](https://make.fun/?ref=2fnbbcz4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
