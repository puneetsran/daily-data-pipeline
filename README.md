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

### GitHub Trending Repositories (Last Updated: 2026-10-14 02:51:31 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | 8,374 | JavaScript | An agent skill for creating detailed, interactive isometric illustrations of rea... |
| [mhtsec/ARTEX](https://github.com/mhtsec/ARTEX) | 3,906 | Go | AI 自主渗透测试系统 | 百度“agent+”攻防挑战赛冠军项目 |
| [t4t5/omdrop-owl](https://github.com/t4t5/omdrop-owl) | 2,595 | Shell | airdrop for non-apple devices |
| [ARahim3/DigUp](https://github.com/ARahim3/DigUp) | 2,539 | Swift | Search your Mac by what's in your files: photos, PDFs, recordings, videos and co... |
| [storytold/craft-launcher](https://github.com/storytold/craft-launcher) | 2,342 | Rust | The Craft App Launcher |

### Hacker News Top Stories (Last Updated: 2026-10-14 02:51:31 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Gemini 4 Argon](https://deepmind.google/models/gemini/) | 1052 | [783 comments](https://news.ycombinator.com/item?id=50073879) |
| [Show HN: Guitoro, a virtual guitar you strum with your keyboard](https://guitoro.com/) | 308 | [92 comments](https://news.ycombinator.com/item?id=50077020) |
| [Ledger confirms spy chip implant behind wallet crypto thefts](https://www.bleepingcomputer.com/news/security/ledger-confirms-hardware-wallet-spy-implant-behind-crypto-thefts/) | 476 | [354 comments](https://news.ycombinator.com/item?id=50054092) |
| [Redesigning source control at Anthropic](https://www.anthropic.com/engineering/redesigning-source-control) | 575 | [545 comments](https://news.ycombinator.com/item?id=50073633) |
| [Show HN: Pulse Local, a Mac budgeting app whose AI models run on your machine](https://pulseos.finance) | 68 | [32 comments](https://news.ycombinator.com/item?id=50080275) |
| [Apple HomeView](https://www.apple.com/apple-homeview/) | 681 | [795 comments](https://news.ycombinator.com/item?id=50071017) |
| [900-Page Pre-Pantone Guide to Color from 1692 (With Complete High-Res Scan)](https://www.openculture.com/2026/10/a-900-page-pre-pantone-guide-to-color-from-1692.html) | 62 | [4 comments](https://news.ycombinator.com/item?id=50053487) |
| [High-speed video reveals how honey bee stingers pump venom](https://arstechnica.com/science/2026/10/honey-bee-stingers-are-double-piston-venom-pumps/) | 20 | [0 comments](https://news.ycombinator.com/item?id=50081133) |
| [Thunderbird for iOS](https://blog.thunderbird.net/2026/10/thunderbird-for-ios-a-first-look-at-the-native-iphone-email-app-in-development/) | 357 | [160 comments](https://news.ycombinator.com/item?id=50072913) |
| [Firefox Enterprise](https://www.firefox.com/en-US/enterprise/) | 665 | [269 comments](https://news.ycombinator.com/item?id=50070302) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 12.0°C (53.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-14 02:51:31 UTC*
