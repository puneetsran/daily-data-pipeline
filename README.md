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

### GitHub Trending Repositories (Last Updated: 2026-09-12 02:19:26 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86) | 1,789 | N/A | Here is a dlssg for RTX30 Series GPU  |
| [openai/NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler) | 1,778 | Lean | Lean certificates accompanying Navier-Stokes and Euler results |
| [EverettFish/holo-card-studio](https://github.com/EverettFish/holo-card-studio) | 1,447 | Python | Turn the user's description or uploaded reference into a finished, editable Blen... |
| [Edge0-AI/Edge0](https://github.com/Edge0-AI/Edge0) | 1,354 | Python | No description |
| [Vincentwei1021/anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | 945 | TypeScript | Topic in, narrated explainer video out. A Claude Code / Codex skill that turns a... |

### Hacker News Top Stories (Last Updated: 2026-09-12 02:19:26 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [A misalignment of AI in mathematics](https://mathandai.org/) | 661 | [695 comments](https://news.ycombinator.com/item?id=49662371) |
| [I spent $220 on Google app ads and 60% of the installs were robots](https://dayzlegame.com/blog/google-ads-bot-farm/) | 311 | [173 comments](https://news.ycombinator.com/item?id=49662990) |
| [A Design Space Exploration of Async/Await](https://cel.cs.brown.edu/blog/design-space-async-await/) | 152 | [31 comments](https://news.ycombinator.com/item?id=49626718) |
| [OpenAI agents carried out an undisclosed attack on RubyGems](https://www.rubyhack.ai/) | 355 | [213 comments](https://news.ycombinator.com/item?id=49666735) |
| [GrapheneOS' rewritten Messages app is released](https://github.com/GrapheneOS/Messaging/releases/tag/13) | 202 | [128 comments](https://news.ycombinator.com/item?id=49663373) |
| [AI researchers debate how close we are to recursive self-improvement](https://www.dwarkesh.com/p/john-beren-charlie) | 36 | [21 comments](https://news.ycombinator.com/item?id=49665711) |
| [Project Blinkenlights](https://blinkenlights.de/en/) | 51 | [23 comments](https://news.ycombinator.com/item?id=49666146) |
| [Litelm: LiteLLM Without the Bloat](https://github.com/kennethwolters/litelm) | 97 | [38 comments](https://news.ycombinator.com/item?id=49662767) |
| [Show HN: ResolveHQ – A Helpdesk Built on Cloudflare Workers, D1, R2 and Queues](https://github.com/mirza-rizvi/ResolveHQ) | 29 | [11 comments](https://news.ycombinator.com/item?id=49665864) |
| [Λ Snap – An inviting programming language for kids and adults for CS study](https://snap.berkeley.edu/) | 115 | [61 comments](https://news.ycombinator.com/item?id=49662214) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 17.0°C (63.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-12 02:19:26 UTC*
