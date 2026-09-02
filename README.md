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

### GitHub Trending Repositories (Last Updated: 2026-09-02 02:08:07 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | 6,208 | Python | Autonomous research system for measurable, computer-executable research. |
| [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt) | 2,145 | TypeScript | ChatGPT thinks. Codex works. Use ChatGPT as the planning brain while keeping the... |
| [crmne/fastpotify](https://github.com/crmne/fastpotify) | 1,554 | Rust | Spotify, native and fast. One lightweight Rust app for your whole library, local... |
| [Nanako0129/sepia](https://github.com/Nanako0129/sepia) | 1,358 | Python | De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CL... |
| [MetaMask-AI/metamask-desktop](https://github.com/MetaMask-AI/metamask-desktop) | 1,229 | CSS | 🌐 🔌 The MetaMask desktop app enables browsing Ethereum blockchain enabled websit... |

### Hacker News Top Stories (Last Updated: 2026-09-02 02:08:07 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Hang on to Your Firefox](https://www.newsonaut.com/articles/hang-on-to-your-firefox) | 554 | [299 comments](https://news.ycombinator.com/item?id=49527748) |
| [Claude Fable 5.1 and Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) | 948 | [892 comments](https://news.ycombinator.com/item?id=49525378) |
| [How accurate have Ed Zitron's AI skeptic predictions been?](https://danluu.com/zitron/) | 433 | [510 comments](https://news.ycombinator.com/item?id=49526069) |
| [The efficient frontier of LLM inference](https://www.baseten.co/blog/the-efficient-frontier-of-llm-inference/) | 42 | [7 comments](https://news.ycombinator.com/item?id=49529898) |
| [Show HN: Weedout – Safari extension that hides YouTube AI-labeled videos](https://masteranza.github.io/weedout/) | 59 | [20 comments](https://news.ycombinator.com/item?id=49528895) |
| [My local model setup on an M4 Pro Mac Mini](https://lws.io/blog/my-local-model-setup/) | 68 | [29 comments](https://news.ycombinator.com/item?id=49529132) |
| [Claude Fable 5.1 made me a nice animated pelican](https://simonwillison.net/2026/Sep/1/claude-fable-5-1/) | 34 | [8 comments](https://news.ycombinator.com/item?id=49530472) |
| [Introducing Ad Blocker for Firefox on iOS](https://blog.mozilla.org/en/firefox/ad-blocker-on-ios/) | 312 | [108 comments](https://news.ycombinator.com/item?id=49521973) |
| [Sonic Pi](https://sonic-pi.net/) | 35 | [4 comments](https://news.ycombinator.com/item?id=49482099) |
| [Building an interactive instrument for a one-of-a-kind festival](https://benholmen.com/blog/halfmoon-chimes/) | 14 | [1 comments](https://news.ycombinator.com/item?id=49479909) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 20.0°C (68.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-02 02:08:07 UTC*
