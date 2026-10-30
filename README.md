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

### GitHub Trending Repositories (Last Updated: 2026-10-30 03:42:33 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [unclebob/ub-mode](https://github.com/unclebob/ub-mode) | 4,813 | N/A | No description |
| [rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner) | 4,789 | Python | 关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。 |
| [interplains/Zero-Breach-Toolkit](https://github.com/interplains/Zero-Breach-Toolkit) | 3,644 | Python | Free, open-source, offline checks for traces of known mercenary spyware. Works o... |
| [anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh) | 3,306 | HTML | 中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊 |
| [designfuchen/word-atlas](https://github.com/designfuchen/word-atlas) | 3,264 | TypeScript | 词光 · Word Atlas — Illustrated IELTS vocabulary with 7,298 words, UK/US audio and... |

### Hacker News Top Stories (Last Updated: 2026-10-30 03:42:33 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Binance-hacker-1029 – $5.6B stolen from Binance](https://arkm.com/explorer/entity/21a94755-f604-45e5-9501-6542e23005e8) | 877 | [512 comments](https://news.ycombinator.com/item?id=50296470) |
| [We're releasing the weights of Mistral Large 4](https://mistral.ai/news/mistral-large-4-oss/) | 1254 | [350 comments](https://news.ycombinator.com/item?id=50289418) |
| [Cuis: The Modern Smalltalk-80](https://cuis.st/) | 16 | [1 comments](https://news.ycombinator.com/item?id=50255343) |
| [We ran AI agent swarms in Minecraft and Mindustry](https://labs.ycombinator.com/projects/games/index.html) | 211 | [68 comments](https://news.ycombinator.com/item?id=50296486) |
| [Astroterm: A Planetarium for Your Terminal](https://github.com/da-luce/astroterm) | 19 | [1 comments](https://news.ycombinator.com/item?id=50270651) |
| [I'm so bad at billiards that I ended up in the hyperbolic plane [video]](https://www.youtube.com/watch?v=kL9BTbIGxLg) | 18 | [2 comments](https://news.ycombinator.com/item?id=50273104) |
| [A tiny world model running games on a Raspberry Pi Pico 2 W](https://github.com/SheepSeb/tinyworldformer) | 161 | [8 comments](https://news.ycombinator.com/item?id=50295450) |
| [CVE-2026-98432: Linux TCP Use-After-Free Risk and Patch Validation](https://www.penligent.ai/hackinglabs/cve-2026-98432/) | 7 | [1 comments](https://news.ycombinator.com/item?id=50299182) |
| [Pico CSS is no longer maintained](https://github.com/picocss/pico/discussions/754) | 51 | [18 comments](https://news.ycombinator.com/item?id=50298964) |
| [H.264 Is Magic (2016)](https://sidbala.com/h-264-is-magic/) | 356 | [130 comments](https://news.ycombinator.com/item?id=50291054) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 8.0°C (47.0°F) |
| Average Humidity | 77% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-30 03:42:33 UTC*
