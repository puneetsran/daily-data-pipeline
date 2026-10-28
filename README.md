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

### GitHub Trending Repositories (Last Updated: 2026-10-28 03:13:51 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [JustAResearcher/gpu-unlock-ada](https://github.com/JustAResearcher/gpu-unlock-ada) | 4,304 | C | GPU tensor unlock source for RTX 4090 and experimental RTX 4070 Ti SUPER; firmwa... |
| [rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner) | 3,493 | Python | 关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。 |
| [designfuchen/word-atlas](https://github.com/designfuchen/word-atlas) | 2,653 | TypeScript | 词光 · Word Atlas — Illustrated IELTS vocabulary with 7,298 words, UK/US audio and... |
| [unclebob/ub-mode](https://github.com/unclebob/ub-mode) | 2,496 | N/A | No description |
| [t3dotgg/tstack](https://github.com/t3dotgg/tstack) | 2,029 | Python | The agent skills I use every day. Works with Claude Code and Codex. |

### Hacker News Top Stories (Last Updated: 2026-10-28 03:13:51 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Git for US Legislation](https://lexifina.com/blog/git-for-the-us-code) | 36 | [19 comments](https://news.ycombinator.com/item?id=50268380) |
| [Genie 4](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) | 770 | [466 comments](https://news.ycombinator.com/item?id=50261319) |
| [Ink droplets in motion snag top prize in Nikon Small World contest](https://arstechnica.com/science/2026/10/meet-the-2026-winner-of-nikons-small-world-photomicrography-contest/) | 97 | [14 comments](https://news.ycombinator.com/item?id=50234796) |
| [Ghostty 1.4](https://ghostty.org/docs/install/release-notes/1-4-0) | 818 | [246 comments](https://news.ycombinator.com/item?id=50261998) |
| [Early progress on accelerating drug development with Claude](https://www.anthropic.com/research/early-progress-drug-development) | 154 | [134 comments](https://news.ycombinator.com/item?id=50265609) |
| [Tailscale SSH: Investigation and remediation update](https://tailscale.com/ssh-investigation-update) | 214 | [114 comments](https://news.ycombinator.com/item?id=50264857) |
| [Survival LLM: AI assistant and emergency library that runs on your own computer](https://www.brangus.io/survival-llm) | 213 | [109 comments](https://news.ycombinator.com/item?id=50264853) |
| [Tabletop Whale is an original science illustration blog](https://tabletopwhale.com) | 19 | [2 comments](https://news.ycombinator.com/item?id=50217978) |
| [Raspberry Pi Zero 3W and Pi 4 Model A spotted in device trees](https://bret.dk/raspberry-pi-zero-3-w-pi-4-model-a/) | 112 | [43 comments](https://news.ycombinator.com/item?id=50265594) |
| [81 Jokes for the ZX81](https://spelk.press/gb/products/81-jokes-for-the-zx81) | 46 | [2 comments](https://news.ycombinator.com/item?id=50242688) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 8.0°C (47.0°F) |
| Average Humidity | 90% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-28 03:13:51 UTC*
