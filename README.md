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

### GitHub Trending Repositories (Last Updated: 2026-09-07 02:03:22 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [lnkiai/m3e-canvas](https://github.com/lnkiai/m3e-canvas) | 4,303 | TypeScript | Sketch Material 3 Expressive screens in the browser and turn them into vibe-codi... |
| [anthropics/commerce-agents](https://github.com/anthropics/commerce-agents) | 2,226 | Python | Reference blueprint for building shopping and merchant agents with Claude. Examp... |
| [ashemag/human-atlas](https://github.com/ashemag/human-atlas) | 1,376 | TypeScript | Open-source 3D anatomy explorer: 2,234 selectable BodyParts3D meshes, system lay... |
| [Rion-Wu-tech/wechat-intelligence-hub](https://github.com/Rion-Wu-tech/wechat-intelligence-hub) | 1,128 | Python | Local-first WeChat intelligence system with a read-only CLI, Codex skills, searc... |
| [pierrenade/short-video-generator-AI](https://github.com/pierrenade/short-video-generator-AI) | 909 | Python | Free open-source project designed for turning youtube-viedos into viral short vi... |

### Hacker News Top Stories (Last Updated: 2026-09-07 02:03:22 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Making a Python interpreter in 1024 bytes](https://austinhenley.com/blog/python1024.html) | 91 | [33 comments](https://news.ycombinator.com/item?id=49591876) |
| [GrapheneOS Overhauled Default Apps and Secure Clipboard](https://grapheneos.social/@GrapheneOS/117225539756835649) | 199 | [123 comments](https://news.ycombinator.com/item?id=49590512) |
| [It took a year to ship WebAssembly in Anubis](https://anubis.techaro.lol/blog/2026/anubis-wasm/) | 144 | [87 comments](https://news.ycombinator.com/item?id=49590611) |
| [Ponytail: Lazy Senior Engineer Skill](https://ponytail.dev/) | 6 | [2 comments](https://news.ycombinator.com/item?id=49592706) |
| [Your intellectual fly is open when you use an LLM to author a post (2025)](https://bcantrill.dtrace.org/2025/12/05/your-intellectual-fly-is-open/) | 529 | [342 comments](https://news.ycombinator.com/item?id=49585644) |
| [Show HN: Mador – Make any DOM reactive with a tiny 80-line Proxy state tuple](https://github.com/marsbos/mador) | 68 | [22 comments](https://news.ycombinator.com/item?id=49590738) |
| [Nitter and XCancel resume service after legal advice](https://github.com/zedeus/nitter/commit/1428b4c2b4246f92a7e5b2673438e5fb39fcc4a3) | 477 | [248 comments](https://news.ycombinator.com/item?id=49588988) |
| [Is mathematics about to enter the conservatory?](https://mbmccoy.dev/posts/mathematical-conservatory/) | 21 | [31 comments](https://news.ycombinator.com/item?id=49591793) |
| [Harnessing the Universal Geometry of Embeddings](https://arxiv.org/abs/2505.12540) | 45 | [11 comments](https://news.ycombinator.com/item?id=49590595) |
| [Babylonian Lamb Stew with Beets (1750–1730 BCE)](https://babylonian-collection.yale.edu/about/babylonian-cooking) | 100 | [54 comments](https://news.ycombinator.com/item?id=49554622) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 20.0°C (67.0°F) |
| Average Humidity | 59% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-07 02:03:22 UTC*
