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

### GitHub Trending Repositories (Last Updated: 2026-07-31 01:59:28 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | 7,542 | N/A | Open Frontier Intelligence |
| [mshumer/Claude-of-Duty](https://github.com/mshumer/Claude-of-Duty) | 2,406 | JavaScript | A Call of Duty-quality FPS in Three.js, built from a single prompt. |
| [VictorTaelin/OptMem](https://github.com/VictorTaelin/OptMem) | 934 | Python | Permanent memory for AI agents. A 426-token prompt, a script, plug and play. |
| [xikhar/persona](https://github.com/xikhar/persona) | 676 | JavaScript | Bringing real-time voice to life. |
| [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | 564 | JavaScript | Makes your AI agent think like the laziest senior dev in the room. The best code... |

### Hacker News Top Stories (Last Updated: 2026-07-31 01:59:28 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [The AI Aesthetic](https://blog.jim-nielsen.com/2026/ai-aesthetic/) | 111 | [58 comments](https://news.ycombinator.com/item?id=49117099) |
| [Read this before you buy that TV streaming stick](https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/) | 572 | [337 comments](https://news.ycombinator.com/item?id=49112744) |
| [I flagged two research papers for fake authors and both were accepted as orals](https://geospatialml.com/posts/reviewing-ai-slop/) | 87 | [34 comments](https://news.ycombinator.com/item?id=49116721) |
| [Agent Skill to Force Docs in ASD-STE100 Simplified Technical English](https://github.com/AminBlg/SimpleEnglish) | 203 | [73 comments](https://news.ycombinator.com/item?id=49114639) |
| [Stacked PRs are now live on GitHub](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/) | 469 | [164 comments](https://news.ycombinator.com/item?id=49112232) |
| [Gemini Robotics 2 brings whole body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) | 478 | [394 comments](https://news.ycombinator.com/item?id=49111237) |
| [Destroying a Community with a Gigantic "Clogged Vacuum Cleaner"](https://gizmodo.com/this-viral-data-center-sounds-like-satans-buzzsaw-2000791122) | 58 | [33 comments](https://news.ycombinator.com/item?id=49068760) |
| [The American Grilled Cheese Sandwich Essay (2024)](https://buttondown.com/theswordandthesandwich/archive/the-best-american-grilled-cheese-sandwich-essay/) | 15 | [3 comments](https://news.ycombinator.com/item?id=49073017) |
| [Rune 1.1: adds Python, an Emacs editor, a symbol index and is now free](https://rune.build/blog/rune-1-1-release) | 48 | [13 comments](https://news.ycombinator.com/item?id=49116272) |
| [CodePen 2.0](https://chriscoyier.net/2026/07/30/codepen-2-0/) | 132 | [38 comments](https://news.ycombinator.com/item?id=49113338) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 26.0°C (78.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-31 01:59:28 UTC*
