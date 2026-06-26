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

### GitHub Trending Repositories (Last Updated: 2026-06-26 14:38:12 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | 2,102 | HTML | Codex 橙皮书：从安装到实战案例的全链路 Codex 使用指南（非官方开源，含可下载 PDF） |
| [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | 1,055 | Python | 可溯源的郑希(易方达基金经理)投研 Agent Skill——基于他全部公开观点原文 + 有原话佐证的投资方法 + 全市场基金真实数据，能溯源问答、按他框架给基... |
| [kanavtwtgg/birds.cafe](https://github.com/kanavtwtgg/birds.cafe) | 783 | JavaScript | No description |
| [BohemiaInteractive/CWR](https://github.com/BohemiaInteractive/CWR) | 563 | C++ | Arma: Cold War Assault Remastered Source Code Repository. |
| [QwenLM/Qwen-AgentWorld](https://github.com/QwenLM/Qwen-AgentWorld) | 549 | Python | Qwen-AgentWorld: Language World Models for General Agents |

### Hacker News Top Stories (Last Updated: 2026-06-26 14:38:12 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Why have papers by one of history's most famous physicists been retracted?](https://www.science.org/content/article/why-have-papers-one-history-s-most-famous-physicists-been-retracted) | 36 | [10 comments](https://news.ycombinator.com/item?id=48686834) |
| [The AI backlash is only getting started](https://www.economist.com/leaders/2026/06/25/the-ai-backlash-is-only-getting-started) | 31 | [21 comments](https://news.ycombinator.com/item?id=48686219) |
| [Incident CVE-2026-LGTM](https://nesbitt.io/2026/06/26/incident-report-cve-2026-lgtm.html) | 84 | [23 comments](https://news.ycombinator.com/item?id=48686093) |
| [Om Malik has died](https://om.co/2026/06/24/1966-2026/) | 1094 | [129 comments](https://news.ycombinator.com/item?id=48678852) |
| [An entire Herculaneum scroll has been read for the first time](https://scrollprize.org/firstscroll) | 1469 | [311 comments](https://news.ycombinator.com/item?id=48675179) |
| [Bipartite Matching Is in NC](https://scottaaronson.blog/?p=9851) | 59 | [2 comments](https://news.ycombinator.com/item?id=48637433) |
| [Libre Barcode Project](https://graphicore.github.io/librebarcode/) | 222 | [36 comments](https://news.ycombinator.com/item?id=48681949) |
| [Ultrasound Imaging of the Brain](https://alephneuro.com/blog/ultrasound-brain) | 24 | [6 comments](https://news.ycombinator.com/item?id=48685558) |
| [What happened after 2k people tried to hack my AI assistant](https://www.fernandoi.cl/posts/hackmyclaw/) | 264 | [109 comments](https://news.ycombinator.com/item?id=48681687) |
| [Show HN: WebBase-III – dBASE III rebuilt in the browser with its own interpreter](https://github.com/DDecoene/WebBaseIII) | 30 | [8 comments](https://news.ycombinator.com/item?id=48656986) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 13.0°C (56.0°F) |
| Average Humidity | 100% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-06-26 14:38:12 UTC*
