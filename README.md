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

### GitHub Trending Repositories (Last Updated: 2026-08-30 02:39:54 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [HEJustinSun/my-girlfriend-jingtian-latex](https://github.com/HEJustinSun/my-girlfriend-jingtian-latex) | 3,948 | TeX | No description |
| [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | 3,203 | Python | Autonomous research system for measurable, computer-executable research. |
| [wide-trace/open-higgsfield](https://github.com/wide-trace/open-higgsfield) | 1,071 | TypeScript | A studio for image and video generation — one prompt bar, each model’s own setti... |
| [bryllim/workout-guide](https://github.com/bryllim/workout-guide) | 1,004 | Astro | 302 open exercise illustrations and a framework-neutral npm package by Bryl Lim |
| [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt) | 966 | TypeScript | ChatGPT thinks. Codex works. Use ChatGPT as the planning brain while keeping the... |

### Hacker News Top Stories (Last Updated: 2026-08-30 02:39:54 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Bug Blindness](https://danluu.com/bug-blind/) | 65 | [26 comments](https://news.ycombinator.com/item?id=49494520) |
| [FreeCORE TrueNAS Core – Continued](https://freecore.org/) | 28 | [14 comments](https://news.ycombinator.com/item?id=49494856) |
| [Hy4 preview](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/) | 206 | [131 comments](https://news.ycombinator.com/item?id=49492632) |
| [RISC-V is now officially supported by CPython](https://blog.python.org/2026/08/riscv-now-officially-supported/) | 28 | [2 comments](https://news.ycombinator.com/item?id=49425252) |
| [Tether: iMessage, SMS, etc. on Linux](https://zackbartel.com/blog/2026/08/tether/) | 372 | [155 comments](https://news.ycombinator.com/item?id=49415386) |
| [Nancy Grace Roman Space Telescope](https://science.nasa.gov/mission/roman-space-telescope/) | 135 | [66 comments](https://news.ycombinator.com/item?id=49490870) |
| [Lawmakers added $1 to car insurance policies. That money paid for Flock cameras](https://www.texastribune.org/2026/08/28/texas-flock-cameras-auto-insurance-fee-mvcpa-grants/) | 129 | [43 comments](https://news.ycombinator.com/item?id=49494182) |
| [Calibrate Before You Accelerate: Bias Toward Action in a New Role](https://tucker.wales/writing/bias-towards-action/) | 118 | [49 comments](https://news.ycombinator.com/item?id=49491714) |
| [Show HN: I missed the moving blocks, so I built a real Linux disk defragmenter](https://github.com/gbin/defragger) | 7 | [1 comments](https://news.ycombinator.com/item?id=49438865) |
| [Domain-Driven Agents](https://coldtake.dev/blog/domain-driven-agents) | 59 | [6 comments](https://news.ycombinator.com/item?id=49492584) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 21.0°C (70.0°F) |
| Average Humidity | 68% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-30 02:39:54 UTC*
