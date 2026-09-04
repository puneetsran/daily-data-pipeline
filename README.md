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

### GitHub Trending Repositories (Last Updated: 2026-09-04 02:10:09 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [anthropics/commerce-agents](https://github.com/anthropics/commerce-agents) | 1,591 | Python | Reference blueprint for building shopping and merchant agents with Claude. Examp... |
| [rakanki911/DLSS5-Swapper](https://github.com/rakanki911/DLSS5-Swapper) | 1,107 | JavaScript | DLSS 5 Swapper is a powerful, easy-to-use tool for installing, managing, and res... |
| [GangTailorUpgrade/undress-service](https://github.com/GangTailorUpgrade/undress-service) | 1,018 | Python | Dress AI Sponsor |
| [shadcn-ui/cn](https://github.com/shadcn-ui/cn) | 967 | TypeScript | cn is a new engine for Tailwind class merging and conflict resolution. It replac... |
| [2akouwu/reverify](https://github.com/2akouwu/reverify) | 790 | Python | Anti-hallucination for AI agents that read binaries. The model proposes, determi... |

### Hacker News Top Stories (Last Updated: 2026-09-04 02:10:09 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [GPT-6 Astra](https://openai.com/index/gpt-6-astra/) | 1345 | [1075 comments](https://news.ycombinator.com/item?id=49554643) |
| [.name Termination](https://neil.fraser.name/news/2026/09/03/) | 1383 | [380 comments](https://news.ycombinator.com/item?id=49550772) |
| [Qwen 3.8 27B available on Cerebras at 1500 tokens/s](https://inference-docs.cerebras.ai/models/overview) | 457 | [134 comments](https://news.ycombinator.com/item?id=49554520) |
| [New type of dice guarantees no tie when deciding who goes first](https://www.cbc.ca/lite/story/9.7328614) | 37 | [21 comments](https://news.ycombinator.com/item?id=49530807) |
| [The largest electric aircraft just flew [video]](https://www.youtube.com/watch?v=nM86DBOqgPM) | 207 | [135 comments](https://news.ycombinator.com/item?id=49526453) |
| [Artificial beaver dams saw juvenile coho salmon survival rates go from 8% to 60%](https://www.discoverwildlife.com/animal-facts/artificial-beaver-dams-california) | 164 | [55 comments](https://news.ycombinator.com/item?id=49552572) |
| [Porting my 1993 Amiga game to Godot, with an LLM reading the 68000 assembly](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/) | 205 | [62 comments](https://news.ycombinator.com/item?id=49550375) |
| [Which tools do Claude, Codex and Cursor choose? We measured 17k runs to find out](https://armature.tech/blog/which-tools-coding-agents-install) | 105 | [33 comments](https://news.ycombinator.com/item?id=49557206) |
| [K2 Horizon: A connected fleet of six open models](https://ifm.ai/blog/k2/) | 259 | [84 comments](https://news.ycombinator.com/item?id=49551760) |
| [GPS glitched across the US by as much as 33 feet](https://www.sciencealert.com/gps-glitched-across-the-us-by-as-much-as-33-feet-scientists-have-never-seen-this-before) | 120 | [67 comments](https://news.ycombinator.com/item?id=49544618) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 19.0°C (66.0°F) |
| Average Humidity | 61% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-04 02:10:09 UTC*
