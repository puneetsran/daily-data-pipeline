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

### GitHub Trending Repositories (Last Updated: 2026-07-05 02:12:30 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | 1,287 | JavaScript | Standalone iOS app to spoof GPS location without jailbreak. Includes Shadowrocke... |
| [jamesob/local-llm](https://github.com/jamesob/local-llm) | 759 | Shell | Everything I know about running LLMs locally |
| [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | 750 | Python | Let Claude (or any LLM) actually watch a video — scene-aware, deduplicated frame... |
| [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | 651 | N/A | 小隐寺投资百科官方公开索引：美股、期权与加密货币知识框架 |
| [jmerelnyc/Talos](https://github.com/jmerelnyc/Talos) | 589 | Python | GPU worker client for the Talos network. Pairs with your Talos account, serves o... |

### Hacker News Top Stories (Last Updated: 2026-07-05 02:12:30 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Scientists reverse brain aging, with a nasal spray](https://stories.tamu.edu/news/2026/04/14/scientists-reverse-brain-aging-with-a-nasal-spray/) | 136 | [49 comments](https://news.ycombinator.com/item?id=48790066) |
| [Command and Conquer Generals natively ported to macOS, iPhone, iPad using Fable](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main) | 361 | [142 comments](https://news.ycombinator.com/item?id=48788283) |
| [GPT-5.5 Codex reasoning-token clustering may be leading to degraded performance](https://github.com/openai/codex/issues/30364) | 150 | [45 comments](https://news.ycombinator.com/item?id=48789428) |
| [Google Books (or similar) all book scans – $200k bounty (2025)](https://software.annas-archive.gl/AnnaArchivist/annas-archive/-/work_items/234) | 344 | [180 comments](https://news.ycombinator.com/item?id=48786838) |
| [Jellyfish can heal wounds in minutes. Scientists want their secrets](https://www.mbl.edu/news/jellyfish-can-heal-wounds-minutes-scientists-want-their-secrets) | 38 | [7 comments](https://news.ycombinator.com/item?id=48789712) |
| [Leaking YouTube creators' private videos](https://javoriuski.com/post/youtube) | 488 | [273 comments](https://news.ycombinator.com/item?id=48786781) |
| [Better Models: Worse Tools](https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/) | 94 | [32 comments](https://news.ycombinator.com/item?id=48788599) |
| [Explanation of everything you can see in htop/top on Linux (2019)](https://peteris.rocks/blog/htop/) | 397 | [52 comments](https://news.ycombinator.com/item?id=48784777) |
| [Potential session/cache leakage between workspace instances or consumer accounts](https://github.com/anthropics/claude-code/issues/74066) | 275 | [128 comments](https://news.ycombinator.com/item?id=48785485) |
| [Zig: All Package Management Functionality Moved from Compiler to Build System](https://ziglang.org/devlog/2026/#2026-06-30) | 140 | [27 comments](https://news.ycombinator.com/item?id=48786638) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 20.0°C (69.0°F) |
| Average Humidity | 60% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-05 02:12:30 UTC*
