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

### GitHub Trending Repositories (Last Updated: 2026-09-01 02:47:32 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | 5,457 | Python | Autonomous research system for measurable, computer-executable research. |
| [HEJustinSun/my-girlfriend-jingtian-latex](https://github.com/HEJustinSun/my-girlfriend-jingtian-latex) | 4,195 | TeX | No description |
| [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt) | 1,880 | TypeScript | ChatGPT thinks. Codex works. Use ChatGPT as the planning brain while keeping the... |
| [Nanako0129/sepia](https://github.com/Nanako0129/sepia) | 1,248 | N/A | De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CL... |
| [MetaMask-AI/metamask-desktop](https://github.com/MetaMask-AI/metamask-desktop) | 1,228 | CSS | 🌐 🔌 The MetaMask desktop app enables browsing Ethereum blockchain enabled websit... |

### Hacker News Top Stories (Last Updated: 2026-09-01 02:47:32 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Google Has Removed MV2 Extensions from the Chrome Web Store, Including UBO](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) | 582 | [439 comments](https://news.ycombinator.com/item?id=49514878) |
| [Ex-Crips leader found guilty in 1996 murder of rapper Tupac Shakur](https://www.bbc.com/news/articles/c24j5192j7jo) | 10 | [0 comments](https://news.ycombinator.com/item?id=49517377) |
| [Run macOS Software on Linux](https://www.darlinghq.org/) | 127 | [37 comments](https://news.ycombinator.com/item?id=49515830) |
| [I turned my security cameras into an automatic bird identification system](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/) | 371 | [97 comments](https://news.ycombinator.com/item?id=49511856) |
| ['Mad honey' that can stop your heart is being sold online](https://phys.org/news/2026-08-mad-honey-heart-sold-online.html) | 151 | [96 comments](https://news.ycombinator.com/item?id=49476239) |
| [Playa Phone](https://playaphone.com/) | 511 | [187 comments](https://news.ycombinator.com/item?id=49510514) |
| [A walkable ASCII cyberpunk city in one HTML file [video]](https://www.youtube.com/watch?v=3YtygAx_C6A) | 218 | [30 comments](https://news.ycombinator.com/item?id=49512975) |
| [Lion-man – the oldest confirmed statue ever discovered](https://en.wikipedia.org/wiki/Lion-man) | 64 | [26 comments](https://news.ycombinator.com/item?id=49494181) |
| [Terence Tao explains 6 essential mathematical concepts [video]](https://www.youtube.com/watch?v=OOMx2BHHWtE) | 230 | [27 comments](https://news.ycombinator.com/item?id=49503521) |
| [Develop Cross-Platform CLI and GUI Tools with Tcl/Tk](https://cgicoffee.com/blog/2026/04/tcl-tk-develop-cross-platform-cli-gui-tools-tutorial-guide) | 47 | [29 comments](https://news.ycombinator.com/item?id=49515662) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 21.0°C (69.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-01 02:47:32 UTC*
