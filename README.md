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

### GitHub Trending Repositories (Last Updated: 2026-07-29 01:49:18 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | 3,444 | N/A | Open Frontier Intelligence |
| [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | 2,065 | Python | No description |
| [mshumer/Claude-of-Duty](https://github.com/mshumer/Claude-of-Duty) | 1,755 | JavaScript | A Call of Duty-quality FPS in Three.js, built from a single prompt. |
| [kvcache-ai/AgentENV](https://github.com/kvcache-ai/AgentENV) | 1,442 | Rust | AgentENV (AENV) is a distributed platform for running agent environments at scal... |
| [mikiarlo3/ai-copywriter](https://github.com/mikiarlo3/ai-copywriter) | 991 | Python | An AI copywriter that uses real copywriting skills + real marketing knowledge wi... |

### Hacker News Top Stories (Last Updated: 2026-07-29 01:49:18 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Codex Security](https://github.com/openai/codex-security) | 340 | [101 comments](https://news.ycombinator.com/item?id=49089755) |
| [Half-Life ported to Mac OS 9](https://mac-classic.com/news/half-life-ported-to-mac-os-9/) | 144 | [61 comments](https://news.ycombinator.com/item?id=49089814) |
| [Show HN: I was tired of opening 2 tabs for every HN link, so I made a userscript](https://github.com/twalichiewicz/HNewhere) | 120 | [40 comments](https://news.ycombinator.com/item?id=49090607) |
| [Substack writers, you need a website](https://elizabethtai.com/2026/06/10/substack-writers-you-need-a-website/) | 415 | [213 comments](https://news.ycombinator.com/item?id=49086788) |
| [The Difference Between a Button and a Link](https://unplannedobsolescence.com/blog/buttons-vs-links/) | 28 | [11 comments](https://news.ycombinator.com/item?id=49091738) |
| [Teach yourself programming in ten years (1998)](https://www.norvig.com/21-days.html) | 38 | [4 comments](https://news.ycombinator.com/item?id=49055816) |
| [Hubble: Open-source notetaking app for you and your agents](https://www.hubble.md/) | 26 | [6 comments](https://news.ycombinator.com/item?id=49091730) |
| [Steel Bank Common Lisp version 2.6.7](https://sbcl.org/all-news.html?2.6.7) | 196 | [82 comments](https://news.ycombinator.com/item?id=49086971) |
| [Lightweight Spring Boot Monitoring Without Prometheus and Grafana](https://pvrlabs.xyz/articles/lightweight-spring-boot-monitoring.html) | 10 | [0 comments](https://news.ycombinator.com/item?id=49091895) |
| [Kimi K3 Architecture Overview and Notes](https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html) | 312 | [41 comments](https://news.ycombinator.com/item?id=49085698) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 23.0°C (73.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-29 01:49:18 UTC*
