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

### GitHub Trending Repositories (Last Updated: 2026-09-29 03:27:11 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [Contrastive-LM/CLM](https://github.com/Contrastive-LM/CLM) | 2,306 | Python | No description |
| [tobi/disktree](https://github.com/tobi/disktree) | 1,832 | Rust | A treemap for finding and removing what fills your disk, for Omarchy. Rust + GPU... |
| [mexicat/pdoom-video](https://github.com/mexicat/pdoom-video) | 1,793 | TypeScript | Code-rendered music video for "I'm Upping My P(doom)" |
| [yetone/magpie](https://github.com/yetone/magpie) | 1,656 | Go | Every agent's model. One place. Codex on DeepSeek, Claude Code on Kimi, from the... |
| [dzhng/jevgrep](https://github.com/dzhng/jevgrep) | 1,473 | TypeScript | Find code by asking what it does. A CLI for coding agents that uses Jev to disco... |

### Hacker News Top Stories (Last Updated: 2026-09-29 03:27:11 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms](https://github.com/firelex/jeff) | 330 | [133 comments](https://news.ycombinator.com/item?id=49883844) |
| [U.S. Strategic Petroleum Reserve Falls to Lowest Level Since 1982](https://oilprice.com/Latest-Energy-News/World-News/US-Strategic-Petroleum-Reserve-Falls-to-Lowest-Level-Since-1982.html) | 50 | [8 comments](https://news.ycombinator.com/item?id=49887337) |
| [Pirating the Pirates](https://mubi.com/en/notebook/posts/pirating-the-pirates) | 443 | [235 comments](https://news.ycombinator.com/item?id=49880036) |
| [12,000-year-old Göbeklitepe burials explain scattered bones](https://archaeologymag.com/2026/09/gobeklitepe-burials-hundreds-of-scattered-bones/) | 92 | [23 comments](https://news.ycombinator.com/item?id=49855059) |
| [1996 chat room simulator connected to Win95 and System 7 web desktops](https://lolchat.rip/) | 39 | [23 comments](https://news.ycombinator.com/item?id=49886195) |
| [MicroLLM Lab – Try 7 tiny LLM's in the browser](https://stateofutopia.com/experiments/microllmlab/) | 154 | [66 comments](https://news.ycombinator.com/item?id=49882781) |
| [California farmers are struggling to sell grapes as demand for wine drops](https://www.kqed.org/news/12101534/california-farmers-are-struggling-to-sell-grapes-as-demand-for-wine-drops) | 86 | [219 comments](https://news.ycombinator.com/item?id=49883539) |
| [Scientists solve 1840s space weather mystery](https://arstechnica.com/science/2026/09/scientists-solve-1840s-space-weather-mystery/) | 72 | [39 comments](https://news.ycombinator.com/item?id=49883536) |
| [Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5) | 633 | [425 comments](https://news.ycombinator.com/item?id=49881850) |
| [ESP32S3 cluster running 1.58-bit (BitNet) Language model](https://github.com/Low-Zi-Hong/ESP32s3-LLM-Cluster) | 42 | [5 comments](https://news.ycombinator.com/item?id=49884625) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 13.0°C (55.0°F) |
| Average Humidity | 82% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-29 03:27:11 UTC*
