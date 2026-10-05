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

### GitHub Trending Repositories (Last Updated: 2026-10-05 03:13:20 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) | 3,252 | Python | Point Claude at any game. Skills, tools and the fal MCP that let Claude Code mod... |
| [CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots) | 3,238 | TypeScript | Your always-on AI coworkers that move between text, calls, and Slack. |
| [feder-cr/dots](https://github.com/feder-cr/dots) | 2,604 | Python | Open-source dots for the web: an AI agent with its own browser, one that does no... |
| [nanaism/yomiyasu](https://github.com/nanaism/yomiyasu) | 1,412 | Python | AI生成の日本語を自然な日本語へ推敲するAgent Skill / Agent Skill for Refining AI-Generated Japanese... |
| [wy51ai/floorplan-3d](https://github.com/wy51ai/floorplan-3d) | 1,394 | HTML | No description |

### Hacker News Top Stories (Last Updated: 2026-10-05 03:13:20 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Powerless F1 drivers frustrated by Bahrain F1 software glitch](https://www.motorsport.com/f1/news/horrible-totally-unacceptable-powerless-f1-drivers-frustrated-by-bahrain-f1-software-glitch/10861968/) | 75 | [30 comments](https://news.ycombinator.com/item?id=49959869) |
| [Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s](https://github.com/Niko1221/Strata) | 639 | [300 comments](https://news.ycombinator.com/item?id=49953495) |
| [In the wake of closure, a digital archive of animated materials appears online](https://filmstories.co.uk/news/tippett-studios-in-the-wake-of-its-closure-a-digital-archive-of-animated-materials-appears-online/) | 48 | [4 comments](https://news.ycombinator.com/item?id=49957812) |
| [Nearly 200 People Under Observation After Irkutsk Lab Worker Dies from Plague](https://www.themoscowtimes.com/2026/10/02/nearly-200-people-under-observation-after-irkutsk-lab-worker-dies-from-plague-a93857) | 31 | [5 comments](https://news.ycombinator.com/item?id=49960084) |
| [A tribute to one of the best games on the Atari 2600](https://plicerin.github.io/riverraid-rom-port/) | 8 | [2 comments](https://news.ycombinator.com/item?id=49959865) |
| [Infidel goes wild](https://blog.zarfhome.com/2026/10/infidel-goes-wild) | 86 | [13 comments](https://news.ycombinator.com/item?id=49943637) |
| [The Tao of Backup](http://www.taobackup.com/index.html) | 40 | [9 comments](https://news.ycombinator.com/item?id=49932236) |
| [A browser-native classic Visual Basic VB6 IDE](https://wieslawsoltes.github.io/VB6/) | 104 | [44 comments](https://news.ycombinator.com/item?id=49956681) |
| [Quantitative Finance with OCaml](https://qcaml.com/index.html) | 18 | [1 comments](https://news.ycombinator.com/item?id=49930690) |
| [Turn off Apple Intelligence on macOS 27 and get its disk space back](https://github.com/omlahore/RemoveMacAI) | 407 | [268 comments](https://news.ycombinator.com/item?id=49957116) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 14.0°C (58.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-05 03:13:20 UTC*
