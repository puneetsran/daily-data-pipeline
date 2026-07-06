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

### GitHub Trending Repositories (Last Updated: 2026-07-06 02:24:20 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | 1,736 | TypeScript | autonomous red teaming platform; multi-agent offensive-security meta-harness |
| [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | 1,329 | JavaScript | Standalone iOS app to spoof GPS location without jailbreak. Includes Shadowrocke... |
| [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | 991 | Python | Let Claude (or any LLM) actually watch a video — scene-aware, deduplicated frame... |
| [jamesob/local-llm](https://github.com/jamesob/local-llm) | 927 | Shell | Everything I know about running LLMs locally |
| [ammaarreshi/Generals-Mac-iOS-iPad](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad) | 811 | C++ | Command & Conquer Generals: Zero Hour running natively on macOS, iPhone & iPad —... |

### Hacker News Top Stories (Last Updated: 2026-07-06 02:24:20 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [GPT-5.6 Sol Ultra will be in Codex](https://twitter.com/thsottiaux/status/2073933490513752151) | 51 | [14 comments](https://news.ycombinator.com/item?id=48799614) |
| [OpenPrinter](https://www.opentools.studio/) | 460 | [116 comments](https://news.ycombinator.com/item?id=48797916) |
| [Al Vigier: Canada's AI strategy shouldn't include secret Palantir bills](https://www.readtheline.ca/p/al-vigier-canadas-ai-strategy-shouldnt) | 82 | [27 comments](https://news.ycombinator.com/item?id=48799256) |
| [Has_not_been_viewed_much](https://iamwillwang.com/notes/has-not-been-viewed-much/) | 88 | [22 comments](https://news.ycombinator.com/item?id=48799155) |
| [Organic Maps](https://organicmaps.app/) | 820 | [226 comments](https://news.ycombinator.com/item?id=48794446) |
| [Show HN: Homegames. An open-source game platform I've been making for 8 years](https://homegames.io) | 96 | [30 comments](https://news.ycombinator.com/item?id=48798153) |
| [Does Code Cleanliness Affect Coding Agents?](https://arxiv.org/abs/2605.20049) | 33 | [11 comments](https://news.ycombinator.com/item?id=48798815) |
| [Completing a computer science degree on Coursera](https://notesbylex.com/completing-a-computer-science-degree-on-coursera) | 107 | [76 comments](https://news.ycombinator.com/item?id=48798061) |
| [The Private Capture of Public Genius](https://www.wysr.xyz/p/the-private-capture-of-public-genius) | 26 | [2 comments](https://news.ycombinator.com/item?id=48799178) |
| [It's not about physical vs. digital games, it's about ownership](https://popcar.bearblog.dev/its-about-ownership/) | 328 | [238 comments](https://news.ycombinator.com/item?id=48794750) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 20.0°C (68.0°F) |
| Average Humidity | 73% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-06 02:24:20 UTC*
