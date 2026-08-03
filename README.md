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

### GitHub Trending Repositories (Last Updated: 2026-08-03 01:59:10 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [yc-software/qm](https://github.com/yc-software/qm) | 7,331 | TypeScript | Multiplayer agent harness for work |
| [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | 3,703 | TypeScript | No description |
| [trycompai/crm](https://github.com/trycompai/crm) | 1,857 | TypeScript | An open-source, agentic-first CRM. |
| [xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer](https://github.com/xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer) | 1,598 | N/A | FDE（前沿部署工程师）从零入门指南（基于范冰《增长黑客》原书框架） |
| [WilonityDev/WilonityLoader](https://github.com/WilonityDev/WilonityLoader) | 1,215 | N/A | Wilonity Loader – cheat lib w/ spoofer, driver bypass, undetected injector for 2... |

### Hacker News Top Stories (Last Updated: 2026-08-03 01:59:10 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Why Book Corners won't sync contributions back to OpenStreetMap](https://www.andreagrandi.it/posts/why-book-corners-wont-sync-contributions-back-to-openstreetmap/) | 37 | [13 comments](https://news.ycombinator.com/item?id=49149746) |
| [CP/M-386 – CP/M for 386 protected mode, derived from CP/M‑68K](https://github.com/johnsonjh/cpm386) | 17 | [4 comments](https://news.ycombinator.com/item?id=49149898) |
| [Karpathy’s Pelican](https://twitter.com/karpathy/status/2083749667410727319) | 440 | [340 comments](https://news.ycombinator.com/item?id=49140998) |
| [Autoregressive Language Model on the 6502 Processor](https://mattbeton.com/blog/bitnet-6502.html) | 57 | [6 comments](https://news.ycombinator.com/item?id=49122655) |
| [Show HN: Isopolis – isometric pixel map of SF](https://sf.isopolis.city/) | 20 | [3 comments](https://news.ycombinator.com/item?id=49149966) |
| [Show HN: Kakehashi – Experimental userspace to run macOS binaries on Linux ARM](https://github.com/wie-project/kakehashi) | 183 | [38 comments](https://news.ycombinator.com/item?id=49145937) |
| [Note-Taking and Personal Knowledge Management](https://unattributed.cc/note-taking-and-personal-knowledge-management) | 131 | [38 comments](https://news.ycombinator.com/item?id=49084324) |
| [Developers are attached to tools because tools encode trust](https://stackoverflow.blog/2026/07/29/developers-are-attached-to-tools-because-tools-encode-trust/) | 150 | [77 comments](https://news.ycombinator.com/item?id=49097961) |
| [Read the Novels and Forget Everything Else](https://hedgehogreview.com/web-features/thr/posts/read-the-novels-and-forget-everything-else) | 55 | [25 comments](https://news.ycombinator.com/item?id=49129676) |
| [RFC 9851: TLS 1.2 is in Feature Freeze](https://www.rfc-editor.org/rfc/rfc9851.html) | 8 | [1 comments](https://news.ycombinator.com/item?id=49150181) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 20.0°C (69.0°F) |
| Average Humidity | 55% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-03 01:59:10 UTC*
