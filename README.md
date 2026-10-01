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

### GitHub Trending Repositories (Last Updated: 2026-10-01 03:17:42 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT) | 4,137 | TypeScript | 一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。 |
| [feder-cr/dots](https://github.com/feder-cr/dots) | 1,937 | Python | Open-source dots for the web: an AI agent with its own browser, one that does no... |
| [dzhng/jevgrep](https://github.com/dzhng/jevgrep) | 1,910 | TypeScript | Find code by asking what it does. A CLI for coding agents that uses Jev to disco... |
| [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) | 1,456 | Swift | A tiny friend that lives in your notch (macOS) or at the top of your screen (Win... |
| [firelex/jeff](https://github.com/firelex/jeff) | 1,200 | Python | Fine-tunes of Qwen3.5 and Gemma 4 for zero-shot classification |

### Hacker News Top Stories (Last Updated: 2026-10-01 03:17:42 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) | 1065 | [713 comments](https://news.ycombinator.com/item?id=49913571) |
| [California bans child marriage, a practice still legal in 32 US states](https://www.bbc.com/news/articles/c6rm9mnn0w3eo) | 29 | [15 comments](https://news.ycombinator.com/item?id=49917089) |
| [The top secret URSALA, RAQUEL, and FARRAH satellites (2025)](https://www.thespacereview.com/article/4951/1) | 147 | [61 comments](https://news.ycombinator.com/item?id=49915082) |
| [56k.rip – the 1996 dial-up internet experience](https://56k.rip/) | 88 | [52 comments](https://news.ycombinator.com/item?id=49915126) |
| [Surprisingly complex waves reveal the brain's inner workings](https://www.quantamagazine.org/surprisingly-complex-waves-reveal-the-brains-inner-workings-20260930/) | 134 | [42 comments](https://news.ycombinator.com/item?id=49912955) |
| [Why the Bronze Age Collapsed](https://www.worksinprogress.news/p/why-really-caused-the-bronze-age) | 106 | [62 comments](https://news.ycombinator.com/item?id=49890732) |
| [Show HN: Yantra – an LALR(1) parser generator for C++](https://github.com/TantrixAuto/yantra) | 4 | [0 comments](https://news.ycombinator.com/item?id=49916997) |
| [EDG C++ front-end goes public](https://edgcpp.org/#transition) | 164 | [78 comments](https://news.ycombinator.com/item?id=49913192) |
| [Launch HN: Magnitude (YC S25) – Self-optimizing inference engine for agents](https://github.com/magnitudedev/magnitude) | 131 | [60 comments](https://news.ycombinator.com/item?id=49911995) |
| [Singapore govt dating app uses Gale-Shapley stable marriage algorithm](https://twitter.com/tuakdotsol/status/2105105417760391258) | 248 | [186 comments](https://news.ycombinator.com/item?id=49906432) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 12.0°C (54.0°F) |
| Average Humidity | 74% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-01 03:17:42 UTC*
