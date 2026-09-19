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

### GitHub Trending Repositories (Last Updated: 2026-09-19 02:24:23 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 5,685 | Python | i. am. speed. |
| [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 3,320 | TypeScript | Claude Code plugin that replaces the compaction summary with Jev decisions: ever... |
| [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) | 1,613 | Python | Semantic ifs from open models, on a 3090 at home. Independent; not affiliated wi... |
| [mcncarl/jianying-headless](https://github.com/mcncarl/jianying-headless) | 1,069 | Python | Private source preview: native Jianying drafts, isolated editing/export, and sta... |
| [vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike) | 897 | Python | No description |

### Hacker News Top Stories (Last Updated: 2026-09-19 02:24:23 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Android 17 is the first since 3.x to add new APIs without releasing to the AOSP](https://grapheneos.social/@GrapheneOS/117282080803799576) | 561 | [267 comments](https://news.ycombinator.com/item?id=49758736) |
| [Cloudflare Quick Tunnels](https://try.cloudflare.com/) | 592 | [251 comments](https://news.ycombinator.com/item?id=49754785) |
| [Saving another 100TB of RAM](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/) | 239 | [45 comments](https://news.ycombinator.com/item?id=49758580) |
| [The Farnese letter](https://simonklee.dk/farnese-letter) | 30 | [5 comments](https://news.ycombinator.com/item?id=49744036) |
| [How to Write with an LLM](https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/) | 400 | [274 comments](https://news.ycombinator.com/item?id=49747070) |
| [Xcode 27.1 Beta Release Notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) | 116 | [68 comments](https://news.ycombinator.com/item?id=49758419) |
| [Show HN: LiveWorld – Every 24/7 YouTube live camera on one globe](https://liveworld.info/) | 13 | [7 comments](https://news.ycombinator.com/item?id=49762099) |
| [Photon-Emission-Guided Laser Fault Injection Enables RP2350 Secure Debug](https://donjon.ledger.com/blog/rp2350-secure-debug-laser-fault-injection/) | 160 | [54 comments](https://news.ycombinator.com/item?id=49757050) |
| [Show HN: Cactus Needle 3: 8-29MB automation models can match DeepSeek V4 Flash](https://cactuscompute.com/needle) | 166 | [78 comments](https://news.ycombinator.com/item?id=49748553) |
| [The first new cat species discovered in 100 years](https://www.nationalgeographic.com/animals/article/meet-the-first-new-cat-species-discovered-in-100-years) | 179 | [62 comments](https://news.ycombinator.com/item?id=49744704) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 15.0°C (58.0°F) |
| Average Humidity | 84% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-19 02:24:23 UTC*
