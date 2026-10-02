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

### GitHub Trending Repositories (Last Updated: 2026-10-02 03:18:12 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT) | 4,703 | TypeScript | 一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。 |
| [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) | 2,513 | Swift | A tiny friend that lives in your notch (macOS) or at the top of your screen (Win... |
| [feder-cr/dots](https://github.com/feder-cr/dots) | 2,391 | Python | Open-source dots for the web: an AI agent with its own browser, one that does no... |
| [dzhng/jevgrep](https://github.com/dzhng/jevgrep) | 2,003 | TypeScript | Find code by asking what it does. A CLI for coding agents that uses Jev to disco... |
| [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) | 1,606 | Python | Point Claude at any game. Skills, tools and the fal MCP that let Claude Code mod... |

### Hacker News Top Stories (Last Updated: 2026-10-02 03:18:12 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Pi 1.0](https://earendil.com/posts/pi-1-0/) | 837 | [288 comments](https://news.ycombinator.com/item?id=49926069) |
| [Several vulnerabilities have been discovered in the Linux kernel](https://lwn.net/Articles/1097401/) | 143 | [79 comments](https://news.ycombinator.com/item?id=49928121) |
| [Clef: Open-weight decision models, and new RL fine-tuning platform](https://blog.cloudflare.com/clef-decision-models/) | 450 | [165 comments](https://news.ycombinator.com/item?id=49923692) |
| [SvelteKit 3](https://svelte.dev/blog/sveltekit-3-is-here) | 143 | [56 comments](https://news.ycombinator.com/item?id=49926536) |
| [Ask HN: Who is hiring? (October 2026)](https://news.ycombinator.com/item?id=49922569) | 164 | [170 comments](https://news.ycombinator.com/item?id=49922569) |
| [Pi Durable](https://earendil.com/posts/pi-durable/) | 260 | [29 comments](https://news.ycombinator.com/item?id=49925969) |
| [Using Opus 5.5 to discover a new eyewitness record of the dodo](https://resobscura.substack.com/p/using-opus-55-to-discover-a-new-eyewitness) | 89 | [16 comments](https://news.ycombinator.com/item?id=49926917) |
| [StreetComplete on iOS is now in public beta](https://github.com/streetcomplete/StreetComplete/issues/5421) | 531 | [135 comments](https://news.ycombinator.com/item?id=49920160) |
| [CSS Bed: Classless CSS themes to use as starting points in web development](https://www.cssbed.com) | 67 | [15 comments](https://news.ycombinator.com/item?id=49927212) |
| [Git 3.0's upcoming SHA-256 default will be a costly mistake](https://blog.gitbutler.com/git-3-sha-256) | 246 | [251 comments](https://news.ycombinator.com/item?id=49924179) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 14.0°C (57.0°F) |
| Average Humidity | 86% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-02 03:18:12 UTC*
