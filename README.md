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

### GitHub Trending Repositories (Last Updated: 2026-09-08 02:14:56 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [lnkiai/m3e-canvas](https://github.com/lnkiai/m3e-canvas) | 4,696 | TypeScript | Sketch Material 3 Expressive screens in the browser and turn them into vibe-codi... |
| [ashemag/human-atlas](https://github.com/ashemag/human-atlas) | 2,041 | TypeScript | Open-source 3D anatomy explorer: 2,234 selectable BodyParts3D meshes, system lay... |
| [Rion-Wu-tech/wechat-intelligence-hub](https://github.com/Rion-Wu-tech/wechat-intelligence-hub) | 1,825 | Python | Local-first WeChat intelligence system with a read-only CLI, Codex skills, searc... |
| [pierrenade/short-video-generator-AI](https://github.com/pierrenade/short-video-generator-AI) | 1,178 | Python | Free open-source project designed for turning youtube-viedos into viral short vi... |
| [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) | 940 | Lean | No description |

### Hacker News Top Stories (Last Updated: 2026-09-08 02:14:56 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [I've factored the RSA keys of a Certificate Authority from the 90s](https://mcpherrin.ca/2026/09/07/rsa.html) | 76 | [12 comments](https://news.ycombinator.com/item?id=49604637) |
| [Jellyfin 12.0](https://jellyfin.org/posts/jellyfin-release-12.0/) | 34 | [5 comments](https://news.ycombinator.com/item?id=49604861) |
| [TALA Is Open-Source](https://d2lang.com/blog/tala-is-open-source/) | 91 | [8 comments](https://news.ycombinator.com/item?id=49604150) |
| [Watch Los Angeles get built, one building at a time (1880–2026)](https://lax-skyline.parcelscope.net/) | 223 | [107 comments](https://news.ycombinator.com/item?id=49601655) |
| [Show HN: Stuxnet – A reconstructed source code of the infamous cyber-weapon](https://github.com/Sadpainy/Stuxnet) | 101 | [31 comments](https://news.ycombinator.com/item?id=49603546) |
| [Leaving VMware just got harder after Broadcom pulled VDDK downloads](https://www.virtualizationhowto.com/2026/09/leaving-vmware-just-got-harder-after-broadcom-pulled-vddk-downloads/) | 97 | [47 comments](https://news.ycombinator.com/item?id=49602699) |
| [Trusting-Trust Attack against an Entire Linux Distribution](https://arxiv.org/abs/2607.24888) | 157 | [35 comments](https://news.ycombinator.com/item?id=49575515) |
| [WeatherNext 3](https://deepmind.google/science/weathernext/) | 236 | [57 comments](https://news.ycombinator.com/item?id=49552299) |
| [Disconnect your LG television from the internet, now](https://appleinsider.com/articles/26/09/07/disconnect-your-lg-television-from-the-internet-now) | 51 | [25 comments](https://news.ycombinator.com/item?id=49604537) |
| [Scientists observe Einstein's gravity in the quantum world](https://www.ox.ac.uk/news/2026-08-28-scientists-observe-einsteins-gravity-in-the-quantum-world) | 148 | [37 comments](https://news.ycombinator.com/item?id=49569838) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 22.0°C (72.0°F) |
| Average Humidity | 63% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-08 02:14:56 UTC*
