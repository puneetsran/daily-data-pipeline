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

### GitHub Trending Repositories (Last Updated: 2026-07-24 01:54:11 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [lopopolo/harness-engineering](https://github.com/lopopolo/harness-engineering) | 2,276 | Python | 🐎 Ryan Lopopolo’s anthology, field guide, and agent context bundle for harness e... |
| [andrewyng/openworker](https://github.com/andrewyng/openworker) | 1,328 | Python | No description |
| [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 947 | TypeScript | AI video skill for Claude Code & Codex — cinematic product videos with Remotion:... |
| [Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs) | 830 | TypeScript | Dotted thought-orb loading indicators for AI & agent UIs — six tuned states, two... |
| [Blaizzy/nativ](https://github.com/Blaizzy/nativ) | 818 | Swift | Local AI, native to your Mac. Chat, serve, monitor, and connect MLX models from ... |

### Hacker News Top Stories (Last Updated: 2026-07-24 01:54:11 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [98.css](https://jdan.github.io/98.css/#status-bar) | 214 | [42 comments](https://news.ycombinator.com/item?id=49028927) |
| [Writing by hand is good for your brain](https://nealstephenson.substack.com/p/writing-by-hand-is-good-for-your) | 978 | [481 comments](https://news.ycombinator.com/item?id=49022152) |
| [The Visual 6502](http://visual6502.org/JSSim/index.html) | 43 | [12 comments](https://news.ycombinator.com/item?id=49029538) |
| [Show HN: Echo – Fable-level results at 1/3 the cost using open-weight models](https://news.ycombinator.com/item?id=49026810) | 231 | [115 comments](https://news.ycombinator.com/item?id=49026810) |
| [The Beam Engine](https://glinscott.github.io/beam-engine/) | 162 | [55 comments](https://news.ycombinator.com/item?id=49007221) |
| [What happened to TheNumbers.com](https://stephenfollows.com/p/what-just-happened-to-thenumberscom-should-worry-us-all) | 292 | [126 comments](https://news.ycombinator.com/item?id=49024691) |
| [A taxonomy of omnicidal futures involving artificial intelligence (2025)](https://arxiv.org/abs/2507.09369) | 48 | [37 comments](https://news.ycombinator.com/item?id=49029133) |
| [Startup founders urge U.S. government not to shut off Chinese open weight AI](https://www.politico.com/news/2026/07/22/startup-founders-urge-trump-not-to-shut-off-chinese-open-weight-ai-01008992) | 723 | [651 comments](https://news.ycombinator.com/item?id=49023016) |
| [Building on ATProto](https://lukekanies.com/writing/building-on-atproto/) | 128 | [59 comments](https://news.ycombinator.com/item?id=49025984) |
| [Why Software Factories Fail (or: harness engineering is not enough)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md) | 174 | [145 comments](https://news.ycombinator.com/item?id=49023019) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 26.0°C (78.0°F) |
| Average Humidity | 53% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-24 01:54:11 UTC*
