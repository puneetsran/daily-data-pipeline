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

### GitHub Trending Repositories (Last Updated: 2026-07-11 01:51:50 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 2,143 | JavaScript | No description |
| [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | 1,706 | JavaScript | Chrome extension that filters pseudo-brand junk out of Amazon. Buy from real, es... |
| [MaximeRivest/riddle](https://github.com/MaximeRivest/riddle) | 1,341 | Rust | The diary of Tom Riddle for the reMarkable Paper Pro — write with your pen, the ... |
| [514-labs/dnsglobe](https://github.com/514-labs/dnsglobe) | 795 | Rust | Global DNS propagation checker TUI — watch a DNS record propagate across 34 publ... |
| [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | 701 | Python | Infinite Worlds with Versatile Interactions |

### Hacker News Top Stories (Last Updated: 2026-07-11 01:51:50 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Einstein's relativity rules chemical bonds in heavy elements, new research shows](https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity) | 94 | [37 comments](https://news.ycombinator.com/item?id=48866134) |
| [Apple sues OpenAI, accuses ex-employees of stealing trade secrets](https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/) | 522 | [252 comments](https://news.ycombinator.com/item?id=48865019) |
| [QuadRF can spot drones and see WiFi through my wall](https://www.jeffgeerling.com/blog/2026/quadrf-can-spot-drones-and-see-wifi-through-my-wall/) | 451 | [172 comments](https://news.ycombinator.com/item?id=48861717) |
| [FreeCAD in the Browser](https://magik.net/freecad/) | 15 | [10 comments](https://news.ycombinator.com/item?id=48867264) |
| [GPT-5.6 Sol Ultra produces proof of the Cycle Double Cover Conjecture [pdf]](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf) | 348 | [280 comments](https://news.ycombinator.com/item?id=48863490) |
| [Meta pulls new AI image feature after days of backlash](https://www.bbc.com/news/articles/c2dy6e8klw0o) | 7 | [1 comments](https://news.ycombinator.com/item?id=48867233) |
| [An update on residential proxies and the scraper situation](https://lwn.net/SubscriberLink/1080822/990a8a5e2d379085/) | 83 | [68 comments](https://news.ycombinator.com/item?id=48864252) |
| [An iroh powered smart fan](https://www.iroh.computer/blog/an-iroh-powered-smart-fan) | 11 | [0 comments](https://news.ycombinator.com/item?id=48817539) |
| [The tech of 'Terminator 2' – an oral history (2017)](https://vfxblog.com/2017/08/23/the-tech-of-terminator-2-an-oral-history/) | 163 | [67 comments](https://news.ycombinator.com/item?id=48862365) |
| [Combustion engine web-based simulator](https://combustionlab.net) | 118 | [52 comments](https://news.ycombinator.com/item?id=48795900) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 22.0°C (72.0°F) |
| Average Humidity | 57% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-11 01:51:50 UTC*
