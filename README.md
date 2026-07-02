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

### GitHub Trending Repositories (Last Updated: 2026-07-02 02:30:46 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | 5,756 | Python | DeepSpec: a full-stack codebase for training and evaluating speculative decoding... |
| [Krishnagangwal/CS-Fundamentals](https://github.com/Krishnagangwal/CS-Fundamentals) | 1,332 | N/A | Curated CS fundamentals for placement prep: DSA,Computer Networks, DBMS & SQL, O... |
| [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | 1,018 | Python | No description |
| [Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills) | 752 | N/A | A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): re... |
| [TianhangZhuzth/Fundamental-Ava](https://github.com/TianhangZhuzth/Fundamental-Ava) | 721 | Python | Build digital human beings — autonomous, collaborative, and socially intelligent... |

### Hacker News Top Stories (Last Updated: 2026-07-02 02:30:46 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [ZCode – Harness for GLM-5.2](https://zcode.z.ai/en) | 219 | [217 comments](https://news.ycombinator.com/item?id=48753715) |
| [Show HN: Searchable directory of 22k+ products from worker-owned co-ops](https://www.workerowned.info/) | 238 | [38 comments](https://news.ycombinator.com/item?id=48752905) |
| [Building an Open-Source Robot Vacuum – Meet Oomwoo](https://makerspet.com/blog/building-an-open-source-robot-vacuum-meet-oomwoo/) | 39 | [2 comments](https://news.ycombinator.com/item?id=48755005) |
| [For first time, a cell built from scratch grows and divides](https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/) | 743 | [255 comments](https://news.ycombinator.com/item?id=48747304) |
| [Global review confirms mRNA vaccines are safe, effective and full of promise ](https://news.ubc.ca/2026/06/mrna-vaccines-are-safe-effective-and-full-of-promise/) | 111 | [64 comments](https://news.ycombinator.com/item?id=48754963) |
| [What to learn to be a graphics programmer](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/) | 247 | [130 comments](https://news.ycombinator.com/item?id=48750710) |
| [The <Usermedia> HTML Element](https://developer.chrome.com/blog/usermedia-html-element) | 35 | [15 comments](https://news.ycombinator.com/item?id=48754700) |
| [Physical disc production ending in Jan 2028 for new games on PlayStation](https://blog.playstation.com/2026/07/01/physical-disc-production-ending-in-january-2028-for-new-games-releasing-on-playstation-consoles/) | 611 | [633 comments](https://news.ycombinator.com/item?id=48745456) |
| [The Underhanded C Contest](https://underhanded-c.org/) | 38 | [5 comments](https://news.ycombinator.com/item?id=48754080) |
| [Opening up 'Zero-Knowledge Proof' technology to promote privacy in age assurance](https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/) | 60 | [38 comments](https://news.ycombinator.com/item?id=48753979) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 19.0°C (66.0°F) |
| Average Humidity | 60% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-02 02:30:46 UTC*
