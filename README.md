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

### GitHub Trending Repositories (Last Updated: 2026-07-25 01:53:24 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [andrewyng/openworker](https://github.com/andrewyng/openworker) | 3,443 | Python | No description |
| [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 1,446 | TypeScript | AI video skill for Claude Code & Codex — cinematic product videos with Remotion:... |
| [Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs) | 933 | TypeScript | Dotted thought-orb loading indicators for AI & agent UIs — six tuned states, two... |
| [Blaizzy/nativ](https://github.com/Blaizzy/nativ) | 861 | Swift | Local AI, native to your Mac. Chat, serve, monitor, and connect MLX models from ... |
| [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | 803 | Python | 一个先接住情绪、再分析关系并给出可执行策略的 Codex 恋爱军师，内置心理、法律、社会、人文、哲学、婚姻家庭与性学知识库，支持多元关系。 |

### Hacker News Top Stories (Last Updated: 2026-07-25 01:53:24 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Claude Opus 5](https://www.anthropic.com/news/claude-opus-5) | 1311 | [708 comments](https://news.ycombinator.com/item?id=49038433) |
| [Postgres LISTEN/NOTIFY actually scales](https://www.dbos.dev/blog/postgres-listen-notify-scalability) | 202 | [37 comments](https://news.ycombinator.com/item?id=49040296) |
| [Opus 5 is currently #1 on Artificial Analysis Intelligence Leaderboard](https://artificialanalysis.ai/models) | 140 | [84 comments](https://news.ycombinator.com/item?id=49040741) |
| [My security camera shipped a GitHub admin token in its login page](https://hhh.hn/hanwha-github-token/) | 511 | [177 comments](https://news.ycombinator.com/item?id=49034292) |
| [Show HN: I simulated closing the Strait of Hormuz on real oil trade data](https://globaloilnetwork.staffinganalytics.io/) | 94 | [42 comments](https://news.ycombinator.com/item?id=49020545) |
| [Sperm Whales blow bubbles to achieve restful, vertical sleep](https://news.st-andrews.ac.uk/archive/sperm-whales-blow-bubbles-to-achieve-restful-vertical-sleep/) | 27 | [1 comments](https://news.ycombinator.com/item?id=49042751) |
| [India's first privately-developed rocket reaches orbit on debut launch](https://arstechnica.com/space/2026/07/indias-first-privately-developed-rocket-reaches-orbit-on-dramatic-debut-launch/) | 493 | [144 comments](https://news.ycombinator.com/item?id=48973835) |
| [Designing an Ethernet Switch ASIC](https://essenceia.github.io/projects/ethernet_switch_asic/) | 107 | [32 comments](https://news.ycombinator.com/item?id=48985182) |
| [If coding has been solved, why does software keep getting worse?](https://ptrchm.com/posts/nothing-works-and-everyone-is-euphoric/) | 528 | [412 comments](https://news.ycombinator.com/item?id=49033004) |
| [An old patent inspired the new "Y-zipper", a three-sided fastener](https://news.mit.edu/2026/three-sided-y-zipper-design-0504) | 130 | [30 comments](https://news.ycombinator.com/item?id=49008512) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 25.0°C (77.0°F) |
| Average Humidity | 65% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-25 01:53:24 UTC*
