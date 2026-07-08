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

### GitHub Trending Repositories (Last Updated: 2026-07-08 01:53:14 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | 3,323 | TypeScript | autonomous red teaming platform; multi-agent offensive-security meta-harness |
| [synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience) | 1,383 | TypeScript | The open-source AI workbench for scientific research |
| [ammaarreshi/Generals-Mac-iOS-iPad](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad) | 1,292 | C++ | Command & Conquer Generals: Zero Hour running natively on macOS, iPhone & iPad —... |
| [jamesob/local-llm](https://github.com/jamesob/local-llm) | 1,185 | Shell | Everything I know about running LLMs locally |
| [MaximeRivest/riddle](https://github.com/MaximeRivest/riddle) | 1,055 | Rust | The diary of Tom Riddle for the reMarkable Paper Pro — write with your pen, the ... |

### Hacker News Top Stories (Last Updated: 2026-07-08 01:53:14 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [GAO: DOE Is Prematurely Excluding Less Expensive Options for Nuclear Cleanup](https://www.gao.gov/products/gao-26-108193) | 92 | [35 comments](https://news.ycombinator.com/item?id=48824826) |
| [We charge $10k a week to delete AI-generated code](https://odra.dev/slopfix/) | 195 | [90 comments](https://news.ycombinator.com/item?id=48823359) |
| [Local, CPU-Friendly, High-Quality TTS (Text-to-Speech) with Kokoro](https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/) | 293 | [68 comments](https://news.ycombinator.com/item?id=48821576) |
| [StreetComplete: Fixing OpenStreetMap, one tiny quest at a time](https://streetcomplete.app/) | 693 | [170 comments](https://news.ycombinator.com/item?id=48816883) |
| [Canada's only watchmaking school still ticking after 80 years](https://www.cbc.ca/news/canada/montreal/canada-s-only-watchmaking-school-9.7254211) | 21 | [2 comments](https://news.ycombinator.com/item?id=48786789) |
| [Chat Control 1.0 and 2.0 Explained](https://fightchatcontrol.eu/chat-control-overview) | 443 | [144 comments](https://news.ycombinator.com/item?id=48818311) |
| [Tenda firmware (multiple versions) contains hidden authentication backdoor](https://kb.cert.org/vuls/id/213560) | 13 | [2 comments](https://news.ycombinator.com/item?id=48825749) |
| [Structure and Interpretation of Computer Programs Video Lectures](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/) | 19 | [0 comments](https://news.ycombinator.com/item?id=48825664) |
| [An interactive explorer for Benford's Law across real datasets](https://vatsalbakshi.com/blog/benfords-law/) | 14 | [3 comments](https://news.ycombinator.com/item?id=48825816) |
| [Show HN: Davit, a Apple Containers UI](https://davit.app) | 197 | [44 comments](https://news.ycombinator.com/item?id=48821848) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 22.0°C (72.0°F) |
| Average Humidity | 65% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-08 01:53:14 UTC*
