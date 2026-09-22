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

### GitHub Trending Repositories (Last Updated: 2026-09-22 02:34:31 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 16,029 | Python | Fastest and cheapest web agent |
| [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 10,920 | Python | No description |
| [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 6,006 | TypeScript | Claude Code plugin that replaces the compaction summary with Jev decisions: ever... |
| [zai-org/ZCode](https://github.com/zai-org/ZCode) | 5,760 | TypeScript | Z.ai's coding agent harness. Powerful, intelligent, extensible. |
| [robbietilton/Compositor](https://github.com/robbietilton/Compositor) | 4,436 | Swift | The Photoshop alternative for Mac |

### Hacker News Top Stories (Last Updated: 2026-09-22 02:34:31 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Xiaomi MiMo v2.6](https://mimo.xiaomi.com/mimo-v2-6) | 578 | [293 comments](https://news.ycombinator.com/item?id=49792730) |
| [Spymarks, Not Watermarks](https://brand.io/article/spymarks/) | 138 | [34 comments](https://news.ycombinator.com/item?id=49794615) |
| [Claude Status – Elevated errors for multiple models](https://status.claude.com/incidents/7g1qpkyz5gxh) | 64 | [44 comments](https://news.ycombinator.com/item?id=49795579) |
| [I don't want to read what you didn't write](https://blog.colinbreck.com/i-dont-want-to-read-what-you-didnt-write/) | 303 | [111 comments](https://news.ycombinator.com/item?id=49794330) |
| [Transformers Explained Visually](https://poloclub.github.io/transformer-explainer/) | 222 | [38 comments](https://news.ycombinator.com/item?id=49792342) |
| [What Sun got wrong](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) | 512 | [302 comments](https://news.ycombinator.com/item?id=49787436) |
| [Attention is all you have](https://alicegg.tech/2026/09/21/attention) | 598 | [180 comments](https://news.ycombinator.com/item?id=49787726) |
| [NASA’s Mars Sample Return mission is dead](https://www.science.org/content/article/nasa-s-mars-sample-return-mission-dead) | 319 | [253 comments](https://news.ycombinator.com/item?id=49791939) |
| [AI coding has made CI a bottleneck, so we reworked ours to keep up](https://linear.app/now/ci-bottleneck-reworked) | 148 | [152 comments](https://news.ycombinator.com/item?id=49792067) |
| [Looking forward to Git 2.56 – and 3.0](https://lwn.net/SubscriberLink/1094575/2385e98583715c2b/) | 38 | [7 comments](https://news.ycombinator.com/item?id=49794736) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 15.0°C (59.0°F) |
| Average Humidity | 79% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-22 02:34:31 UTC*
