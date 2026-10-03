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

### GitHub Trending Repositories (Last Updated: 2026-10-03 03:04:14 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT) | 4,989 | TypeScript | 一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。 |
| [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) | 3,004 | Swift | A tiny friend that lives in your notch (macOS) or at the top of your screen (Win... |
| [feder-cr/dots](https://github.com/feder-cr/dots) | 2,509 | Python | Open-source dots for the web: an AI agent with its own browser, one that does no... |
| [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) | 2,173 | Python | Point Claude at any game. Skills, tools and the fal MCP that let Claude Code mod... |
| [CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots) | 1,536 | TypeScript | Your always-on AI coworkers that move between text, calls, and Slack. |

### Hacker News Top Stories (Last Updated: 2026-10-03 03:04:14 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [The Forgetful CPU (Linux on M4)](https://yuka.dev/blog-2026-10-02-linux-m4.html) | 130 | [56 comments](https://news.ycombinator.com/item?id=49933869) |
| [Court agrees with EFF: Utah's VPN law demands a technical impossibility](https://www.eff.org/deeplinks/2026/10/court-agrees-eff-utahs-vpn-law-demands-technical-impossibility) | 533 | [233 comments](https://news.ycombinator.com/item?id=49927754) |
| [Newgrounds.com – A community of games, music, and art](https://www.newgrounds.com/) | 30 | [0 comments](https://news.ycombinator.com/item?id=49940394) |
| [Mike Tomlin spent 12 years building a Minecraft city](https://www.nytimes.com/athletic/7648198/2026/10/01/mike-tomlin-minecraft-nfl-coach/) | 320 | [86 comments](https://news.ycombinator.com/item?id=49925184) |
| [A 12-year sequence of telescope images of a star and four planets orbiting](https://bsky.app/profile/theplanetaryguy.com/post/3mwucf5ert22f) | 212 | [50 comments](https://news.ycombinator.com/item?id=49932147) |
| [Apple Pass Designer](https://developer.apple.com/pass-designer/) | 337 | [223 comments](https://news.ycombinator.com/item?id=49937276) |
| [Things that apparently cause cancer](https://www.breakthroughjournal.org/p/things-that-apparently-cause-cancer) | 94 | [37 comments](https://news.ycombinator.com/item?id=49940219) |
| [With most information hidden, the game Stratego had stumped AI until now](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) | 189 | [91 comments](https://news.ycombinator.com/item?id=49933740) |
| [NTSB Preliminary Report: Prime Air 767 Runway Overrun [pdf]](https://www.ntsb.gov/investigations/Documents/DCA26MA352%20Prelim.pdf) | 17 | [9 comments](https://news.ycombinator.com/item?id=49940467) |
| [Loss of cell identity drives human aging: Two new papers](https://erictopol.substack.com/p/loss-of-cell-identity-drives-human) | 188 | [49 comments](https://news.ycombinator.com/item?id=49926411) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 18.0°C (64.0°F) |
| Average Humidity | 84% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-03 03:04:14 UTC*
