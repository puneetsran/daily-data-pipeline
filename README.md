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

### GitHub Trending Repositories (Last Updated: 2026-07-19 01:52:09 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [xai-org/grok-build](https://github.com/xai-org/grok-build) | 18,885 | Rust | SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensib... |
| [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | 9,761 | JavaScript | Codex Dream Skin |
| [CluvexStudio/Aether](https://github.com/CluvexStudio/Aether) | 1,256 | Rust | No description |
| [pixel-point/aval](https://github.com/pixel-point/aval) | 1,211 | TypeScript | A new open-source format for interactive video on the web, with a built-in state... |
| [littledivy/mimic](https://github.com/littledivy/mimic) | 1,176 | Python | Intercept any app, then call it from Python like a library |

### Hacker News Top Stories (Last Updated: 2026-07-19 01:52:09 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Transcribe.cpp](https://workshop.cjpais.com/projects/transcribe-cpp) | 40 | [5 comments](https://news.ycombinator.com/item?id=48963879) |
| [Speech Recognition and TTS in less than 500kb](https://github.com/moonshine-ai/moonshine/tree/main/micro) | 274 | [32 comments](https://news.ycombinator.com/item?id=48911793) |
| [Better and Cheaper Than IPTV](https://github.com/stupside/castor) | 16 | [4 comments](https://news.ycombinator.com/item?id=48964015) |
| [Classic Amiga titles, free to download](https://amigafreeware.downer.tech/) | 49 | [7 comments](https://news.ycombinator.com/item?id=48962838) |
| [If You Build It, They Will Come](https://www.benlandautaylor.com/p/if-you-build-it-they-will-come) | 269 | [99 comments](https://news.ycombinator.com/item?id=48959090) |
| [GPT-5.6 used a prompt to close a 30-year gap in convex optimization](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) | 500 | [324 comments](https://news.ycombinator.com/item?id=48957779) |
| [Mayor Mamdani Says Landlords Can't Use AI Images to Advertise](https://petapixel.com/2026/07/16/mayor-mamdani-says-landlords-cant-secretly-use-ai-images-to-advertise-properties/) | 201 | [100 comments](https://news.ycombinator.com/item?id=48962983) |
| [Hardcore IndieWeb: Run your own website 100% independently for only $0.01/day](https://www.neatnik.net/hardcore-indieweb) | 79 | [59 comments](https://news.ycombinator.com/item?id=48962758) |
| [Real-Time LuaTeX: Recompiling Large Documents in 1ms [pdf]](https://www.tug.org/tug2026/preprints/lode-realtime.pdf) | 31 | [4 comments](https://news.ycombinator.com/item?id=48962944) |
| [Judge a book by its first pages](https://uncovered.ink) | 42 | [31 comments](https://news.ycombinator.com/item?id=48962893) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 23.0°C (73.0°F) |
| Average Humidity | 69% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-19 01:52:09 UTC*
