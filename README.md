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

### GitHub Trending Repositories (Last Updated: 2026-07-12 01:54:36 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 2,413 | JavaScript | No description |
| [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | 1,773 | JavaScript | Chrome extension that filters pseudo-brand junk out of Amazon. Buy from real, es... |
| [oso95/scroll-world](https://github.com/oso95/scroll-world) | 893 | JavaScript | A skill that turn any brand into a scrollable 3D world |
| [x4gKing/3x-ui-Upgrade](https://github.com/x4gKing/3x-ui-Upgrade) | 800 | HTML | No description |
| [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | 797 | Python | Infinite Worlds with Versatile Interactions |

### Hacker News Top Stories (Last Updated: 2026-07-12 01:54:36 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Mesh LLM: distributed AI computing on iroh](https://www.iroh.computer/blog/mesh-llm) | 89 | [22 comments](https://news.ycombinator.com/item?id=48876505) |
| [Show HN: Ant – A JavaScript runtime and ecosystem](https://antjs.org) | 178 | [77 comments](https://news.ycombinator.com/item?id=48875377) |
| [RISCBoy is an open-source portable games console, designed from scratch](https://github.com/Wren6991/RISCBoy) | 60 | [16 comments](https://news.ycombinator.com/item?id=48876245) |
| [A dock that wakes up reliably](https://fabiensanglard.net/tb4/index.html) | 15 | [12 comments](https://news.ycombinator.com/item?id=48877269) |
| [Long Covid May Physically Damage the Nerves That Control the Stomach](https://www.ijidonline.com/article/S1201-9712(26)00608-9/fulltext) | 27 | [3 comments](https://news.ycombinator.com/item?id=48877192) |
| [Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom) | 159 | [57 comments](https://news.ycombinator.com/item?id=48873836) |
| [A pure scheme web programming tool](https://goeteia.dev) | 5 | [1 comments](https://news.ycombinator.com/item?id=48877314) |
| [I Did Not Kill Stanley Lieber: How to Draw (With 9front)](https://triapul.cz/automa/i_did_not_kill_stanley_lieber) | 6 | [1 comments](https://news.ycombinator.com/item?id=48846177) |
| [A public ledger of cloud outages and the SLA credits they trigger](https://slacreditwatch.com) | 12 | [3 comments](https://news.ycombinator.com/item?id=48877009) |
| [Billions of Sketches Reveal Hidden Cultural Variation in Human Concepts](https://arxiv.org/abs/2607.07267) | 50 | [5 comments](https://news.ycombinator.com/item?id=48849744) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 20.0°C (67.0°F) |
| Average Humidity | 50% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-12 01:54:36 UTC*
