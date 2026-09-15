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

### GitHub Trending Repositories (Last Updated: 2026-09-15 02:38:24 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [sumimakito/Mac-Duo](https://github.com/sumimakito/Mac-Duo) | 874 | Swift | Wish you could bring the iPhone Duo effect to your MacBook? |
| [Chuloo/mural](https://github.com/Chuloo/mural) | 823 | Kotlin | The language app you eventually delete. A native iPhone companion for learning t... |
| [kruzovic7/ai-data-extractor](https://github.com/kruzovic7/ai-data-extractor) | 812 | Python | Free open-source extractor for AI coding assistant chat histories. Supports Clau... |
| [yifanzhang-pro/recurrent-looped-tranformer](https://github.com/yifanzhang-pro/recurrent-looped-tranformer) | 753 | HTML | Official Project Page for Recurrent Looped Transformer (RLT) |
| [angusdevgo/IDM_Pro_Tool](https://github.com/angusdevgo/IDM_Pro_Tool) | 697 | C# | IDM激活与状态维护工具 |

### Hacker News Top Stories (Last Updated: 2026-09-15 02:38:24 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [iOS 27, iPadOS 27, and macOS 27](https://www.apple.com/newsroom/2026/09/major-updates-for-apples-software-platforms-are-now-available/) | 406 | [463 comments](https://news.ycombinator.com/item?id=49701004) |
| [Pion, an agent designed to run any company autonomously](https://andonlabs.com/blog/why-we-built-pion) | 302 | [330 comments](https://news.ycombinator.com/item?id=49700477) |
| [Charts built for Chat](https://dbtcharts.com/blog/charts-built-for-chat/) | 111 | [37 comments](https://news.ycombinator.com/item?id=49704246) |
| [Show HN: Sunk Cost – How long until a local LLM rig pays for itself?](https://sunkcost.ai/) | 8 | [4 comments](https://news.ycombinator.com/item?id=49706656) |
| [Show HN: Macros with a Behringer FCB1010 MIDI Pedalboard in macOS](https://github.com/JamesRyanATX/fcbnerd) | 39 | [4 comments](https://news.ycombinator.com/item?id=49705442) |
| [4,400-Year-Old Tomb of Egyptian Judge Found at Saqqara with Colors on Walls](https://arkeonews.net/4400-year-old-tomb-of-an-egyptian-judge-found-at-saqqara-with-colors-still-on-the-walls/) | 26 | [4 comments](https://news.ycombinator.com/item?id=49675817) |
| [Compressing a Flag to 11 Bits](https://read.vantezzen.io/miniflags) | 77 | [37 comments](https://news.ycombinator.com/item?id=49673689) |
| [Dropping eBPF CPU Cost by About 90% with Memoization (Not AI Gen)](https://nathannaveen.dev/posts/dropping-ebpf-cpu-cost-by-90/) | 39 | [12 comments](https://news.ycombinator.com/item?id=49697477) |
| [Distributed Systems Classics (2017)](https://nvartolomei.com/dist-sys-classics/) | 242 | [54 comments](https://news.ycombinator.com/item?id=49699158) |
| [XCancel service is suspended until further notice](https://xcancel.com/#) | 476 | [781 comments](https://news.ycombinator.com/item?id=49694296) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 15.0°C (60.0°F) |
| Average Humidity | 80% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-15 02:38:24 UTC*
