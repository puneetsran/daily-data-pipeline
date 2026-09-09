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

### GitHub Trending Repositories (Last Updated: 2026-09-09 02:18:33 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [ashemag/human-atlas](https://github.com/ashemag/human-atlas) | 2,473 | TypeScript | Open-source 3D anatomy explorer: 2,234 selectable BodyParts3D meshes, system lay... |
| [Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo) | 2,169 | TypeScript | Open-source AI brand visibility and competitor reports |
| [Rion-Wu-tech/wechat-intelligence-hub](https://github.com/Rion-Wu-tech/wechat-intelligence-hub) | 1,946 | Python | Local-first WeChat intelligence system with a read-only CLI, Codex skills, searc... |
| [EverettFish/holo-card-studio](https://github.com/EverettFish/holo-card-studio) | 1,134 | Python | Turn the user's description or uploaded reference into a finished, editable Blen... |
| [vinzdg/codenotch](https://github.com/vinzdg/codenotch) | 1,113 | Swift | A macOS app that pins usage limits from Claude Code, Cursor, Codex, and Antigrav... |

### Hacker News Top Stories (Last Updated: 2026-09-09 02:18:33 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Harvard study predicts most suicide attempts a week in advance](https://current.fas.harvard.edu/stories/harvard-study-predicts-most-suicide-attempts-week-advance) | 17 | [1 comments](https://news.ycombinator.com/item?id=49619906) |
| [Muse – Meta’s personal AI agent](https://ai.meta.com/muse/) | 329 | [325 comments](https://news.ycombinator.com/item?id=49615537) |
| [Large language models develop novel social biases through adaptive exploration](https://openreview.net/challenge?redirect=%2Fforum%3Fid%3Dpc7fqaOcAH) | 98 | [49 comments](https://news.ycombinator.com/item?id=49617581) |
| [How to build a printer](https://nishantjosh.dev/blogs/how-to-build-a-fking-printer/) | 150 | [37 comments](https://news.ycombinator.com/item?id=49617255) |
| [Navier-Stokes – Tristan Buckmaster [pdf]](https://cims.nyu.edu/~tristanb/statement.pdf) | 1287 | [554 comments](https://news.ycombinator.com/item?id=49605915) |
| [AlphaGenome Atlas: a high-resolution map of human DNA](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/) | 498 | [115 comments](https://news.ycombinator.com/item?id=49611251) |
| [DaVinci Resolve 21.1](https://www.blackmagicdesign.com/media/release/20260908-03) | 357 | [157 comments](https://news.ycombinator.com/item?id=49610181) |
| [On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/) | 1135 | [978 comments](https://news.ycombinator.com/item?id=49613262) |
| [Benchmarking Qwen3.8 27B quantizations: 4-bit holds up, 1-bit collapses](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) | 218 | [109 comments](https://news.ycombinator.com/item?id=49611128) |
| [Tao: Open math problems being non-renewably mined by AI](https://mathstodon.xyz/@tao/117237320796901560) | 157 | [105 comments](https://news.ycombinator.com/item?id=49616968) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 21.0°C (70.0°F) |
| Average Humidity | 74% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-09 02:18:33 UTC*
