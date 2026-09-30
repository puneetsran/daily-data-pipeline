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

### GitHub Trending Repositories (Last Updated: 2026-09-30 03:10:45 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT) | 3,367 | TypeScript | 一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。 |
| [mexicat/pdoom-video](https://github.com/mexicat/pdoom-video) | 1,991 | TypeScript | Code-rendered music video for "I'm Upping My P(doom)" |
| [tobi/disktree](https://github.com/tobi/disktree) | 1,919 | Rust | A treemap for finding and removing what fills your disk, for Omarchy. Rust + GPU... |
| [Niko1221/Strata](https://github.com/Niko1221/Strata) | 1,848 | C++ | Qwen3.8-Flash-Next (125B MoE) on a 8GB+ NVIDIA GPU: one-click install for Window... |
| [dzhng/jevgrep](https://github.com/dzhng/jevgrep) | 1,789 | TypeScript | Find code by asking what it does. A CLI for coding agents that uses Jev to disco... |

### Hacker News Top Stories (Last Updated: 2026-09-30 03:10:45 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Livenerf: Has Opus 5.5 been nerfed yet?](https://github.com/ninjahawk/livenerf) | 305 | [133 comments](https://news.ycombinator.com/item?id=49901736) |
| [U.S. postal inspectors shut down website selling counterfeit postage labels](https://postalemployeenetwork.com/news/2026/09/26/u-s-postal-inspectors-shut-down-website-selling-millions-of-counterfeit-postage-labels/) | 182 | [107 comments](https://news.ycombinator.com/item?id=49899090) |
| [America.gov](https://america.gov/) | 398 | [322 comments](https://news.ycombinator.com/item?id=49893509) |
| [Show HN: Real-time Solar System with 526k asteroids and all tracked satellites](https://space.bl2.net/) | 132 | [32 comments](https://news.ycombinator.com/item?id=49898778) |
| [GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price](https://openai.com/index/introducing-gpt-6-1-sol/) | 816 | [748 comments](https://news.ycombinator.com/item?id=49896586) |
| [How Delhi cut electricity loss from 50 to 5 percent](https://spectrum.ieee.org/delhi-electricity-loss) | 449 | [264 comments](https://news.ycombinator.com/item?id=49892245) |
| [PS5 Relapse Exploit](https://github.com/ntfargo/Relapse-Exploit) | 243 | [132 comments](https://news.ycombinator.com/item?id=49895304) |
| [Language models for text classification: From bag-of-words to Jev](https://magazine.sebastianraschka.com/p/classifier-history-and-jev) | 42 | [1 comments](https://news.ycombinator.com/item?id=49891203) |
| [Needed 1+1, built a functional programming language](https://hereticpleb.vercel.app/blog/needed-one-plus-one/) | 40 | [9 comments](https://news.ycombinator.com/item?id=49895864) |
| [Backblaze drive stats for Q2 2026](https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2026/) | 98 | [17 comments](https://news.ycombinator.com/item?id=49893002) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 13.0°C (56.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-30 03:10:45 UTC*
