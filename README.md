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

### GitHub Trending Repositories (Last Updated: 2026-07-18 01:43:59 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [xai-org/grok-build](https://github.com/xai-org/grok-build) | 16,548 | Rust | SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensib... |
| [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | 8,708 | JavaScript | Codex Dream Skin |
| [pixel-point/aval](https://github.com/pixel-point/aval) | 1,164 | TypeScript | A new open-source format for interactive video on the web, with a built-in state... |
| [littledivy/mimic](https://github.com/littledivy/mimic) | 1,149 | Python | Intercept any app, then call it from Python like a library |
| [CluvexStudio/Aether](https://github.com/CluvexStudio/Aether) | 1,144 | Rust | No description |

### Hacker News Top Stories (Last Updated: 2026-07-18 01:43:59 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Kaiser nurses say AI, workplace surveillance are making their jobs, care worse](https://localnewsmatters.org/2026/07/15/kaiser-nurses-say-ai-workplace-surveillance-are-making-their-jobs-and-patient-care-worse/) | 266 | [161 comments](https://news.ycombinator.com/item?id=48952880) |
| [AWS: Inaccurate Estimated Billing Data – $1.7 billion](https://news.ycombinator.com/item?id=48945241) | 1048 | [639 comments](https://news.ycombinator.com/item?id=48945241) |
| [Thanks HN for 15 years of support and helping me find my life's work](https://news.ycombinator.com/item?id=48949551) | 322 | [29 comments](https://news.ycombinator.com/item?id=48949551) |
| [The Zilog Z80 has turned 50](https://goliath32.com/blog/z80.html) | 164 | [48 comments](https://news.ycombinator.com/item?id=48951461) |
| [The Isomorphic Labs Drug Design Engine unlocks a new frontier beyond AlphaFold](https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier) | 32 | [2 comments](https://news.ycombinator.com/item?id=48953406) |
| [First atmosphere found on Earth-like planet in habitable zone of distant star](https://www.bbc.com/news/articles/cy4kdd1e0ejo) | 366 | [231 comments](https://news.ycombinator.com/item?id=48947560) |
| [Vāgdhenu: A Sanskrit Chanting TTS System](https://prathosh.in/vagdhenu/) | 45 | [3 comments](https://news.ycombinator.com/item?id=48896149) |
| [I Started a "Dirt Notebook"](https://pinewind.bearblog.dev/i-started-a-dirt-notebook/) | 4 | [0 comments](https://news.ycombinator.com/item?id=48954149) |
| [Learning a few things about running SQLite](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/) | 164 | [39 comments](https://news.ycombinator.com/item?id=48950122) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 23.0°C (73.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-18 01:43:59 UTC*
