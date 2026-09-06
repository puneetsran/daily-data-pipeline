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

### GitHub Trending Repositories (Last Updated: 2026-09-06 02:06:09 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [lnkiai/m3e-canvas](https://github.com/lnkiai/m3e-canvas) | 3,733 | TypeScript | Sketch Material 3 Expressive screens in the browser and turn them into vibe-codi... |
| [anthropics/commerce-agents](https://github.com/anthropics/commerce-agents) | 2,055 | Python | Reference blueprint for building shopping and merchant agents with Claude. Examp... |
| [shadcn-ui/cn](https://github.com/shadcn-ui/cn) | 1,172 | TypeScript | cn is a new engine for Tailwind class merging and conflict resolution. It replac... |
| [GangTailorUpgrade/undress-service](https://github.com/GangTailorUpgrade/undress-service) | 1,091 | Python | Dress AI Sponsor |
| [2akouwu/reverify](https://github.com/2akouwu/reverify) | 923 | Python | Stop your AI from making things up — it proposes, deterministic tools decide, ev... |

### Hacker News Top Stories (Last Updated: 2026-09-06 02:06:09 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Cloud in a Bottle: making self-hosting accessible to everyone](https://cloudinabottle.org/blog/launch-post) | 108 | [38 comments](https://news.ycombinator.com/item?id=49582000) |
| [The revolt of the reader](https://bcantrill.dtrace.org/2026/09/05/the-revolt-of-the-reader/) | 114 | [33 comments](https://news.ycombinator.com/item?id=49580939) |
| [Private German rocket makes history, reaches orbit from European soil](https://www.space.com/space-exploration/launches-spacecraft/isar-aerospace-second-launch-norway-andoya-spaceport-spectrum-rocket) | 375 | [197 comments](https://news.ycombinator.com/item?id=49580369) |
| [Learn Programming with OCaml](https://usr.lmf.cnrs.fr/lpo/) | 181 | [74 comments](https://news.ycombinator.com/item?id=49578280) |
| [The "$60 Gaming PC" – AMD BC-250 (2025)](https://devquasar.com/hardware/the-60-gaming-pc-amd-bc-250/) | 280 | [85 comments](https://news.ycombinator.com/item?id=49576386) |
| [Finite time blowup for an averaged three-dimensional Navier-Stokes equation (201...](https://terrytao.wordpress.com/2014/02/04/finite-time-blowup-for-an-averaged-three-dimensional-navier-stokes-equation/) | 59 | [23 comments](https://news.ycombinator.com/item?id=49580329) |
| [Discovery of a new OpenAI agent message board](https://collusion.wiki/) | 2115 | [1518 comments](https://news.ycombinator.com/item?id=49563355) |
| [How Swiss tables work in Go built-in map](https://victoriametrics.com/blog/go-swiss-table-map/index.html) | 46 | [3 comments](https://news.ycombinator.com/item?id=49548852) |
| [Visualizing Rust's Vtables: How dyn Trait Works In Memory](https://sofiabelen.github.io/projects/visualizing-rusts-vtables-how-dyn-trait-works-in-memory/) | 134 | [19 comments](https://news.ycombinator.com/item?id=49576343) |
| [Actively exploited sandbox RCE in all Chromium versions](https://nvd.nist.gov/vuln/detail/cve-2026-85046) | 746 | [442 comments](https://news.ycombinator.com/item?id=49570669) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 20.0°C (68.0°F) |
| Average Humidity | 56% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-06 02:06:09 UTC*
