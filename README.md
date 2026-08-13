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

### GitHub Trending Repositories (Last Updated: 2026-08-13 01:12:41 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | 2,387 | Python | Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrit... |
| [ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness) | 1,639 | Python | let your agent control your phone |
| [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | 1,614 | Python | Create smooth, responsive interactive web animations. |
| [antirez/h3.c](https://github.com/antirez/h3.c) | 1,597 | C | MiniMax H3 inference engine for Mac computers |
| [SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI) | 1,520 | TypeScript | No description |

### Hacker News Top Stories (Last Updated: 2026-08-13 01:12:41 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [DeepSeek V4 Pro 0813](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) | 724 | [274 comments](https://news.ycombinator.com/item?id=49274600) |
| [Delta](https://zed.dev/blog/introducing-delta) | 378 | [124 comments](https://news.ycombinator.com/item?id=49276574) |
| [Tailscale Traces Database Corruption to 16y/o SQLite WAL-Reset Bug](https://tailscale.com/blog/sqlite-wal-reset-bug) | 784 | [141 comments](https://news.ycombinator.com/item?id=49272832) |
| [Happy 45th Birthday to the IBM PC and Model F/XT](https://sharktastica.co.uk/articles/pc-fxt-45) | 20 | [1 comments](https://news.ycombinator.com/item?id=49280103) |
| [Qwen3.8-2.4T](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) | 485 | [104 comments](https://news.ycombinator.com/item?id=49273478) |
| [What's New in Flutter 3.47](https://flutter.dev/blog/whats-new-in-flutter-3-47) | 27 | [16 comments](https://news.ycombinator.com/item?id=49280061) |
| [Principia Mathematica is modern and insightful](https://okmij.org/ftp/Computation/Impressions/PrincipiaMathematica.html) | 27 | [5 comments](https://news.ycombinator.com/item?id=49279928) |
| [Show HN: Ballet – Workflow automation that writes integrations against any API](https://www.ballet.dev/) | 12 | [1 comments](https://news.ycombinator.com/item?id=49280184) |
| [Why Target Common Lisp for Code Generation?](http://funcall.blogspot.com/2026/08/why-vibe-code-in-lisp.html) | 25 | [22 comments](https://news.ycombinator.com/item?id=49269429) |
| [2026 Eclipse Webcams](https://jonty.github.io/2026_eclipse_webcams/) | 457 | [124 comments](https://news.ycombinator.com/item?id=49270953) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 25.0°C (77.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-13 01:12:41 UTC*
