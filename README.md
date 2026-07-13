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

### GitHub Trending Repositories (Last Updated: 2026-07-13 01:57:00 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 2,715 | JavaScript | No description |
| [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | 932 | Python | Infinite Worlds with Versatile Interactions |
| [x4gKing/3x-ui-Upgrade](https://github.com/x4gKing/3x-ui-Upgrade) | 890 | HTML | No description |
| [Robbyant/lingbot-video](https://github.com/Robbyant/lingbot-video) | 712 | Python | Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence |
| [mereyabdenbekuly-ctrl/clodex-ide](https://github.com/mereyabdenbekuly-ctrl/clodex-ide) | 640 | TypeScript | Local-first, zero-trust agentic IDE for verifiable autonomous software developme... |

### Hacker News Top Stories (Last Updated: 2026-07-13 01:57:00 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Since Chromium 148, Math.tanh is now fingerprintable to link underlying OS](https://scrapfly.dev/posts/browser-math-os-fingerprint/) | 305 | [152 comments](https://news.ycombinator.com/item?id=48884853) |
| [Cyberpunk Comics, Manga and Graphic Novels](https://shellzine.net/cyberpunk-comics/) | 74 | [15 comments](https://news.ycombinator.com/item?id=48885643) |
| [Tiny Emulators](https://floooh.github.io/tiny8bit-preview/index.html) | 145 | [7 comments](https://news.ycombinator.com/item?id=48884395) |
| [Designing and assembling my first PCB](https://vilkeliskis.com/b/2026/0711.html) | 46 | [4 comments](https://news.ycombinator.com/item?id=48885728) |
| [So you want to learn physics (second edition, 2021)](https://www.susanrigetti.com/physics) | 97 | [9 comments](https://news.ycombinator.com/item?id=48827126) |
| [A Peek Inside Jim Henson's Creature Shop, Where Whimsical Puppets Are Designed](https://www.smithsonianmag.com/travel/a-peek-inside-jim-hensons-creature-shop-where-sesame-street-characters-and-other-whimsical-puppets-are-designed-180989051/) | 17 | [0 comments](https://news.ycombinator.com/item?id=48818314) |
| [Ask HN: What Are You Working On? (July 2026)](https://news.ycombinator.com/item?id=48884984) | 76 | [191 comments](https://news.ycombinator.com/item?id=48884984) |
| [Why Vanilla JavaScript](https://guseyn.com/html/posts/why-vanilla-js.html) | 39 | [17 comments](https://news.ycombinator.com/item?id=48885705) |
| [Ask HN: Add flag for AI-generated articles](https://news.ycombinator.com/item?id=48886741) | 26 | [7 comments](https://news.ycombinator.com/item?id=48886741) |
| [Old and new apps, via modern coding agents](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/) | 413 | [120 comments](https://news.ycombinator.com/item?id=48880170) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 20.0°C (68.0°F) |
| Average Humidity | 47% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-13 01:57:00 UTC*
