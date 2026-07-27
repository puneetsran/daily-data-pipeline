# 📊 Daily Data Pipeline Showcase

[![Data Pipeline](https://github.com/puneetsran/daily-data-pipeline/actions/workflows/daily-pipeline.yml/badge.svg)](https://github.com/puneetsran/daily-data-pipeline/actions/workflows/daily-pipeline.yml)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Views](https://komarev.com/ghpvc/?username=puneetsran-daily-data-pipeline&label=views&color=blueviolet&style=flat-square)

An automated data engineering project that demonstrates ETL pipeline skills using GitHub Actions. This pipeline runs daily to collect, process, and visualize data automatically.

## 🎯 Project Overview

This project showcases:
- **Automated ETL Pipeline**: Scheduled data collection and processing
- **CI/CD with GitHub Actions**: Fully automated workflow
- **Data Engineering Best Practices**: Clean code, error handling, logging
- **Real-time Data Processing**: Daily updates without manual intervention
- **Data Visualization**: Auto-generated insights and charts

## 📈 Current Data Insights

### GitHub Trending Repositories (Last Updated: 2026-07-27 02:05:25 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | 1,363 | Python | No description |
| [Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs) | 1,101 | TypeScript | Dotted thought-orb loading indicators for AI & agent UIs — six tuned states, two... |
| [mikiarlo3/ai-copywriter](https://github.com/mikiarlo3/ai-copywriter) | 857 | Python | An AI copywriter that uses real copywriting skills + real marketing knowledge wi... |
| [mshumer/Claude-of-Duty](https://github.com/mshumer/Claude-of-Duty) | 676 | JavaScript | A Call of Duty-quality FPS in Three.js, built from a single prompt. |
| [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | 654 | JavaScript | Agent skill: convert Chinese story copy or ordered images into a hand-drawn diar... |

### Hacker News Top Stories (Last Updated: 2026-07-27 02:05:25 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [PGSimCity - How PostgreSQL Works](https://nikolays.github.io/PGSimCity/) | 92 | [15 comments](https://news.ycombinator.com/item?id=49063754) |
| [Decker, a platform that builds on the legacy of Hypercard and classic macOS](https://beyondloom.com/decker/) | 225 | [55 comments](https://news.ycombinator.com/item?id=49060856) |
| [Show HN: Physically accurate black hole you can put in your room](https://blackhole.plav.in) | 26 | [4 comments](https://news.ycombinator.com/item?id=49021270) |
| [We have proof automation now](https://www.imperialviolet.org/2026/07/26/zstd-lean.html) | 78 | [10 comments](https://news.ycombinator.com/item?id=49062291) |
| [French firefighters face 'pyrocumulonimbus' for first time](https://www.france24.com/en/live-news/20260726-french-firefighters-face-pyrocumulonimbus-for-first-time) | 186 | [96 comments](https://news.ycombinator.com/item?id=49060495) |
| [I Championed Prediction Markets. Look What They've Become](https://newsletter.platypuseconomics.com/p/i-championed-prediction-markets-look) | 20 | [36 comments](https://news.ycombinator.com/item?id=49063789) |
| [Teaching Kids Forth](https://gracefulliberty.com/articles/teaching-kids-forth/) | 52 | [13 comments](https://news.ycombinator.com/item?id=49062700) |
| [US citizen charged after GrapheneOS phone wipes during airport search](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html) | 170 | [97 comments](https://news.ycombinator.com/item?id=49063022) |
| [Introduction to Data-Oriented Design [pdf]](https://www.gamedevs.org/uploads/introduction-to-data-oriented-design.pdf) | 110 | [35 comments](https://news.ycombinator.com/item?id=49060724) |
| [Design is compromise](https://stephango.com/design-is-compromise) | 196 | [74 comments](https://news.ycombinator.com/item?id=49059367) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 17.0°C (62.0°F) |
| Average Humidity | 93% |
| Data Points | 1 |

## 🛠️ Tech Stack

- **Language**: Python 3.9+
- **Libraries**: pandas, requests, matplotlib, seaborn
- **Automation**: GitHub Actions
- **Data Storage**: CSV/JSON in repository
- **Scheduling**: Cron (daily at 00:00 UTC)

## 🚀 Pipeline Architecture

```
┌─────────────────┐
│  GitHub Actions │
│   (Scheduler)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Data Collection│
│   (API Calls)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Data Processing │
│ (pandas/Python) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Data Storage   │
│   (CSV/JSON)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ README Update   │
│ (Auto-generated)│
└─────────────────┘
```

## 📁 Project Structure

```
daily-data-pipeline/
├── .github/
│   └── workflows/
│       └── daily-pipeline.yml    # GitHub Actions workflow
├── data/
│   ├── raw/                      # Raw data from APIs
│   ├── processed/                # Cleaned and processed data
│   └── archive/                  # Historical data
├── scripts/
│   ├── collect_data.py           # Data collection script
│   ├── process_data.py           # Data processing script
│   └── update_readme.py          # README auto-update script
├── visualizations/               # Generated charts and graphs
├── requirements.txt              # Python dependencies
├── .gitignore
└── README.md
```

## 🔄 Automation Details

The pipeline runs automatically:
- **Schedule**: Daily at 00:00 UTC
- **Trigger**: Can also be manually triggered
- **Duration**: ~2-3 minutes per run
- **Cost**: $0 (GitHub Actions free tier)

## 📊 Data Sources

1. **GitHub API**: Genuinely trending repos — new repositories (created in the last 7 days) sorted by stars gained
2. **Hacker News API**: Top stories updated daily (no API key required)
3. **wttr.in**: Weather data for Vancouver (no API key required)
4. **CoinGecko API**: Cryptocurrency prices and 24h change (no API key required)

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Building production-ready data pipelines
- ✅ Implementing CI/CD workflows
- ✅ Working with REST APIs
- ✅ Data cleaning and transformation
- ✅ Automated reporting and visualization
- ✅ Git workflow and version control
- ✅ Error handling and logging

## 🚦 Getting Started

### Prerequisites
```bash
python 3.9+
pip
git
```

### Local Setup
```bash
# Clone the repository
git clone https://github.com/puneetsran/daily-data-pipeline.git
cd daily-data-pipeline

# Install dependencies
pip install -r requirements.txt

# Run the pipeline manually
python scripts/collect_data.py
python scripts/process_data.py
python scripts/update_readme.py
```

## 📝 License

MIT License - feel free to use this project as a template for your own data pipelines!

## 👤 Author

**Puneet Sran**
- Portfolio: [puneetsran.github.io/portfolio-website](https://puneetsran.github.io/portfolio-website/)
- GitHub: [@puneetsran](https://github.com/puneetsran)
- LinkedIn: [puneetsran](https://www.linkedin.com/in/puneetsran/)

---

*This README is automatically updated by the data pipeline. Last update: 2026-07-27 02:05:25 UTC*
