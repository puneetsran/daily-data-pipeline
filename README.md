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

### GitHub Trending Repositories (Last Updated: 2026-08-23 00:47:54 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill) | 3,779 | N/A | A compact Agent Skill for highly simplified, rounded, subtly neo-skeuomorphic IP... |
| [yetone/cumora](https://github.com/yetone/cumora) | 2,901 | TypeScript | Where agent teams gather. Cross-platform team chat where AI agents are first-cla... |
| [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | 2,327 | TypeScript | Open-source AI coworkers that each get a computer of their own: a browser, files... |
| [MengTo/threeui](https://github.com/MengTo/threeui) | 1,886 | HTML | Open-source ThreeUI Community catalog with live interactive components and compl... |
| [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | 1,243 | Python | Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent ne... |

### Hacker News Top Stories (Last Updated: 2026-08-23 00:47:54 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Scrap](https://twitter.com/moxie/status/2091218652133732491) | 292 | [147 comments](https://news.ycombinator.com/item?id=49402189) |
| [NanoGPT Speedrun Frontier](https://www.primeintellect.ai/research/nanogpt-speedrun) | 39 | [8 comments](https://news.ycombinator.com/item?id=49404380) |
| [Why your local LLM feels dumber than it is](https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917) | 164 | [49 comments](https://news.ycombinator.com/item?id=49402232) |
| [ElevenLabs, TwelveLabs, ThirteenLabs](https://quantumi.sh/public/labs.html) | 292 | [99 comments](https://news.ycombinator.com/item?id=49400408) |
| [Hister – A private, full content search index that you control](https://hister.org/) | 221 | [65 comments](https://news.ycombinator.com/item?id=49351802) |
| [NetBSD and my life (2005)](https://mail-index.netbsd.org/netbsd-advocacy/2005/09/10/0000.html) | 89 | [22 comments](https://news.ycombinator.com/item?id=49402781) |
| [RF Cafe](https://www.rfcafe.com/) | 143 | [23 comments](https://news.ycombinator.com/item?id=49355659) |
| [typ.ing](https://typ.ing/) | 166 | [54 comments](https://news.ycombinator.com/item?id=49346854) |
| [How a Texas student blew the whistle on a rogue AI hacking attempt](https://www.reuters.com/world/how-texas-student-blew-whistle-rogue-ai-hacking-attempt-2026-08-20/) | 99 | [37 comments](https://news.ycombinator.com/item?id=49387959) |
| [A Friendly Introduction to Racket](https://geometridae.bearblog.dev/a-friendly-introduction-to-racket/) | 184 | [92 comments](https://news.ycombinator.com/item?id=49399898) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 22.0°C (72.0°F) |
| Average Humidity | 64% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-23 00:47:54 UTC*
