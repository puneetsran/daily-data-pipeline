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

### GitHub Trending Repositories (Last Updated: 2026-08-29 04:55:09 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [HEJustinSun/my-girlfriend-jingtian-latex](https://github.com/HEJustinSun/my-girlfriend-jingtian-latex) | 3,752 | TeX | No description |
| [b-nnett/grok-bot-0.18-reconstructed](https://github.com/b-nnett/grok-bot-0.18-reconstructed) | 3,411 | TypeScript | Unofficial source-oriented reconstruction and extension of Grok Bot 0.18.0 for m... |
| [tobi/walgit](https://github.com/tobi/walgit) | 2,304 | Rust | No description |
| [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | 1,777 | Python | Autonomous research system for measurable, computer-executable research. |
| [bryllim/workout-guide](https://github.com/bryllim/workout-guide) | 983 | Astro | 302 open exercise illustrations and a framework-neutral npm package by Bryl Lim |

### Hacker News Top Stories (Last Updated: 2026-08-29 04:55:09 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Boot a Virtual iPhone via Apple's Virtualization.framework](https://github.com/Lakr233/vphone-cli) | 171 | [60 comments](https://news.ycombinator.com/item?id=49485267) |
| [GUIs should be fully keyboard-driven](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html) | 686 | [335 comments](https://news.ycombinator.com/item?id=49479837) |
| [TurboKV: Insanely fast Rust key-value store](https://github.com/kingroryg/turbokv) | 41 | [12 comments](https://news.ycombinator.com/item?id=49486334) |
| [9th Circuit sides with states in Kalshi gambling fight](https://azmirror.com/2026/08/28/9th-circuit-sides-with-states-in-kalshi-gambling-fight-potentially-reviving-arizonas-prosecution/) | 97 | [71 comments](https://news.ycombinator.com/item?id=49485452) |
| [Htmx 4.0](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released) | 575 | [142 comments](https://news.ycombinator.com/item?id=49478178) |
| [Our decision on Cursor following its acquisition by SpaceX](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) | 249 | [89 comments](https://news.ycombinator.com/item?id=49486172) |
| [Does the Sumerian King List Align with Paleoclimate Events?](https://www.vectorian.be/articles/2026-06-07/sumerian-king-list-paleoclimate-alignment-explorer/) | 73 | [24 comments](https://news.ycombinator.com/item?id=49485532) |
| [I accidentally turned LLM memory into program analysis](https://pwning.systems/posts/llm-memory-program-analysis/) | 72 | [13 comments](https://news.ycombinator.com/item?id=49485416) |
| [StemDeck, a free, open-source and local AI stem separator](https://github.com/stemdeckapp/stemdeck) | 49 | [12 comments](https://news.ycombinator.com/item?id=49486081) |
| [U.S. sanctions against the A/I Collective](https://www.inventati.org/) | 528 | [498 comments](https://news.ycombinator.com/item?id=49477854) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 16.0°C (61.0°F) |
| Average Humidity | 80% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-29 04:55:09 UTC*
