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

### GitHub Trending Repositories (Last Updated: 2026-08-26 00:45:52 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [MengTo/threeui](https://github.com/MengTo/threeui) | 3,915 | HTML | Open-source ThreeUI Community catalog with live interactive components and compl... |
| [b-nnett/grok-bot-0.18-reconstructed](https://github.com/b-nnett/grok-bot-0.18-reconstructed) | 2,546 | TypeScript | Unofficial source-oriented reconstruction and extension of Grok Bot 0.18.0 for m... |
| [tobi/walgit](https://github.com/tobi/walgit) | 1,548 | Rust | No description |
| [duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server) | 1,381 | Zig | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg tha... |
| [cclank/lanshu-create-ai-presenter-video](https://github.com/cclank/lanshu-create-ai-presenter-video) | 913 | Python | Provider-neutral Codex Skill for producing verified AI presenter videos from a s... |

### Hacker News Top Stories (Last Updated: 2026-08-26 00:45:52 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [FDA authorizes first wearable device that monitors ketone and blood sugar levels](https://www.fda.gov/news-events/press-announcements/fda-authorizes-first-wearable-device-continuously-monitors-both-ketone-levels-and-blood-sugar) | 231 | [136 comments](https://news.ycombinator.com/item?id=49439017) |
| [Apple introduces M6 and M5 Ultra](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) | 932 | [887 comments](https://news.ycombinator.com/item?id=49433292) |
| [Python's pre-declared constants are kinda weird](https://sebsite.pw/w/20260801-pythonconstants.html) | 126 | [78 comments](https://news.ycombinator.com/item?id=49441033) |
| [OpenAI Jalapeño: Better than Nvidia Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) | 302 | [205 comments](https://news.ycombinator.com/item?id=49434378) |
| [New Mac Studio with M5 Max and M5 Ultra](https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/) | 695 | [440 comments](https://news.ycombinator.com/item?id=49433316) |
| [Maiao: Gerrit-style code review workflow for GitHub, GitLab, Gitea, others](https://github.com/runetes/maiao) | 20 | [1 comments](https://news.ycombinator.com/item?id=49441666) |
| [Black hole singularity is a surface not a point](https://arxiv.org/abs/2608.21590) | 178 | [123 comments](https://news.ycombinator.com/item?id=49437210) |
| [When str.lower() is a security vulnerability in Python – Seth Larson](https://sethmlarson.dev/when-str-lower-is-a-security-vulnerability) | 47 | [24 comments](https://news.ycombinator.com/item?id=49440410) |
| [Show HN: TeXbrain, a LaTeX editor that runs pdfTeX in the browser via WASM](https://github.com/swimmingbrain/texbrain) | 37 | [7 comments](https://news.ycombinator.com/item?id=49441375) |
| [C2PA Cameras Do Not Survive Contact with Reality](https://www.da.vidbuchanan.co.uk/blog/android-c2pa.html) | 69 | [28 comments](https://news.ycombinator.com/item?id=49439499) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 31.0°C (87.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-26 00:45:52 UTC*
