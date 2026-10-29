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

### GitHub Trending Repositories (Last Updated: 2026-10-29 03:39:31 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [JustAResearcher/gpu-unlock-ada](https://github.com/JustAResearcher/gpu-unlock-ada) | 4,433 | C | GPU tensor unlock source for RTX 4090 and experimental RTX 4070 Ti SUPER; firmwa... |
| [rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner) | 4,388 | Python | 关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。 |
| [unclebob/ub-mode](https://github.com/unclebob/ub-mode) | 3,899 | N/A | No description |
| [designfuchen/word-atlas](https://github.com/designfuchen/word-atlas) | 3,086 | TypeScript | 词光 · Word Atlas — Illustrated IELTS vocabulary with 7,298 words, UK/US audio and... |
| [interplains/Zero-Breach-Toolkit](https://github.com/interplains/Zero-Breach-Toolkit) | 2,862 | Python | Free, open-source, offline checks for traces of known mercenary spyware. Works o... |

### Hacker News Top Stories (Last Updated: 2026-10-29 03:39:31 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Qwenputer: A functioning, deterministic RISC-V CPU inside Qwen3.5](https://divagr.com/blog/qwenputer) | 175 | [37 comments](https://news.ycombinator.com/item?id=50282838) |
| [Why is this fingerprinting script creating bioweapons?](https://nullpt.rs/fingerprinting-bioweapons) | 928 | [195 comments](https://news.ycombinator.com/item?id=50276998) |
| [GitLab Security Incident: Attempted Exploitation of CVE-2026-97229](https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html) | 109 | [43 comments](https://news.ycombinator.com/item?id=50282544) |
| [A Health Update](https://furbo.org/2026/10/28/a-health-update/) | 140 | [17 comments](https://news.ycombinator.com/item?id=50280974) |
| [CNC Stone Carving](https://carmelitegothic.com/cnc-stone-carving/) | 425 | [122 comments](https://news.ycombinator.com/item?id=50274409) |
| [Human-enhanced tsunami hazard in large lakes](https://www.nature.com/articles/s41467-026-78272-8) | 11 | [0 comments](https://news.ycombinator.com/item?id=50242873) |
| [Richest 0.1% (8M) produce more carbon pollution than 3.5B](https://www.oxfam.org/en/press-releases/ultra-rich-01-produce-more-carbon-pollution-nearly-half-humanity-while-cashing) | 21 | [0 comments](https://news.ycombinator.com/item?id=50284089) |
| [Gemini 4 Carbon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) | 836 | [698 comments](https://news.ycombinator.com/item?id=50276792) |
| [StackOverflow now gets fewer than 1000 questions a month](https://data.stackexchange.com/stackoverflow/query/1926661#graph?t=1) | 164 | [170 comments](https://news.ycombinator.com/item?id=50282454) |
| [Formlabs Studio 1 $699 Resin Printer](https://formlabs.com/products/form-studio-1-basic-founders-edition/) | 141 | [91 comments](https://news.ycombinator.com/item?id=50281044) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 8.0°C (46.0°F) |
| Average Humidity | 84% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-29 03:39:31 UTC*
