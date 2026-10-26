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

### GitHub Trending Repositories (Last Updated: 2026-10-26 02:27:29 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [pengchujin/aerial-tv](https://github.com/pengchujin/aerial-tv) | 5,106 | Kotlin | 给国产电视的一块干净桌面：参照 tvOS 设计的开源 Android TV 桌面，没有广告，开机自动接管。A tvOS-style launcher for X... |
| [JustAResearcher/gpu-unlock-ada](https://github.com/JustAResearcher/gpu-unlock-ada) | 2,731 | C | GPU tensor unlock source for RTX 4090 and experimental RTX 4070 Ti SUPER; firmwa... |
| [xevrion/hatchzip](https://github.com/xevrion/hatchzip) | 1,947 | Rust | HatchZip is a free, open-source archive extractor for Windows, macOS and Linux t... |
| [wesbos/3d-model-anything](https://github.com/wesbos/3d-model-anything) | 1,938 | Swift | Capture iPhone LiDAR and photos, reconstruct editable Three.js rooms, and explor... |
| [ikow/php2shell-poc](https://github.com/ikow/php2shell-poc) | 1,792 | Python | CVE-2026-109618/109619 — 5 RCE chains + detection rules (Suricata, Sigma, ModSec... |

### Hacker News Top Stories (Last Updated: 2026-10-26 02:27:29 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Dolly Parton's Imagination Library](https://imaginationlibrary.com/) | 400 | [69 comments](https://news.ycombinator.com/item?id=50234474) |
| [F-Zero X on Nintendo 3DS](https://hypnotize.works/gdx-3ds/postmortem/index.html) | 48 | [31 comments](https://news.ycombinator.com/item?id=50237078) |
| [Overgrown, when plants invade your abandoned tabs](https://charliegerard.dev/blog/overgrown-extension/) | 148 | [40 comments](https://news.ycombinator.com/item?id=50197108) |
| [Attention Is Not What You Need (2025)](https://arxiv.org/abs/2512.19428) | 30 | [11 comments](https://news.ycombinator.com/item?id=50237224) |
| [Why I Am a Programmer](https://www.alfie.wtf/programming/why-i-am-a-programmer.html) | 143 | [53 comments](https://news.ycombinator.com/item?id=50235017) |
| [What goes into making an animated film?](https://www.disneyanimation.com/process/) | 98 | [39 comments](https://news.ycombinator.com/item?id=50235738) |
| [The State of Context Engineering](https://www.dbreunig.com/2026/10/24/the-state-of-context-engineering.html) | 87 | [25 comments](https://news.ycombinator.com/item?id=50235780) |
| [A 10-year-old CNN outperforms frontier LLMs for skin cancer diagnosis](https://lynchlab.net/llm-skin-cancer) | 451 | [214 comments](https://news.ycombinator.com/item?id=50233779) |
| [OpenAI and Anthropic cut their LLM prices by up to 80% within a few months. Why?](https://minimaxir.com/2026/10/cheap-llms/) | 161 | [192 comments](https://news.ycombinator.com/item?id=50236102) |
| [Where the Romans Fought (interactive map)](https://iosiflazaridis.github.io/battles-of-the-romans/) | 53 | [21 comments](https://news.ycombinator.com/item?id=50234879) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 9.0°C (48.0°F) |
| Average Humidity | 88% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-26 02:27:29 UTC*
