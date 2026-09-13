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

### GitHub Trending Repositories (Last Updated: 2026-09-13 02:17:16 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86) | 2,197 | N/A | Here is a dlssg for RTX30 Series GPU  |
| [openai/NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler) | 1,829 | Lean | Lean certificates accompanying Navier-Stokes and Euler results |
| [EverettFish/holo-card-studio](https://github.com/EverettFish/holo-card-studio) | 1,470 | Python | Turn the user's description or uploaded reference into a finished, editable Blen... |
| [Edge0-AI/Edge0](https://github.com/Edge0-AI/Edge0) | 1,451 | Python | No description |
| [Vincentwei1021/anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | 1,077 | TypeScript | Topic in, narrated explainer video out. A Claude Code / Codex skill that turns a... |

### Hacker News Top Stories (Last Updated: 2026-09-13 02:17:16 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Make your first edit to OpenStreetMap](https://high5apps.github.io/josm-plugin-website-wizard/) | 338 | [78 comments](https://news.ycombinator.com/item?id=49674050) |
| [Real-SWE: Benchmarking AI models on private, real-world, enterprise codebases](https://withspecific.com/benchmarks/real-swe) | 125 | [64 comments](https://news.ycombinator.com/item?id=49676820) |
| [Align AI and Mathematics–To Something Else](https://liorpachter.wordpress.com/2026/09/12/align-ai-and-mathematics-to-something-else/) | 13 | [1 comments](https://news.ycombinator.com/item?id=49678783) |
| [Nvidia is the central bank of AI](https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai) | 403 | [272 comments](https://news.ycombinator.com/item?id=49673098) |
| [Apple iPod Engraver (2019)](https://dunstanorchard.com/apple-ipod-engraver/) | 129 | [27 comments](https://news.ycombinator.com/item?id=49619848) |
| [Everyone should slow down AI development except for me](https://xeiaso.net/notes/2026/everyone-slowdown-but-me/) | 131 | [40 comments](https://news.ycombinator.com/item?id=49678683) |
| [Recurrent Looped Transformer](https://yifanzhang-pro.github.io/recurrent-looped-tranformer/) | 12 | [3 comments](https://news.ycombinator.com/item?id=49678548) |
| [Why are AI agents lying, cheating and coordinating?](https://yoshuabengio.org/en/publication/why-are-ai-agents-lying-cheating-and-coordinating) | 6 | [1 comments](https://news.ycombinator.com/item?id=49678969) |
| [Getting 50 GB/S Back from the Apple Neural Engine](https://eiln.github.io/posts/ane-dma.html) | 81 | [15 comments](https://news.ycombinator.com/item?id=49636479) |
| [Stabilizing Rust's Never Type](https://lwn.net/SubscriberLink/1091015/d9e48318ed242b41/) | 141 | [34 comments](https://news.ycombinator.com/item?id=49625056) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 21.0°C (69.0°F) |
| Average Humidity | 41% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-13 02:17:16 UTC*
