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

### GitHub Trending Repositories (Last Updated: 2026-10-04 03:32:44 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT) | 5,465 | TypeScript | 一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。 |
| [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) | 2,666 | Python | Point Claude at any game. Skills, tools and the fal MCP that let Claude Code mod... |
| [CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots) | 2,602 | TypeScript | Your always-on AI coworkers that move between text, calls, and Slack. |
| [feder-cr/dots](https://github.com/feder-cr/dots) | 2,575 | Python | Open-source dots for the web: an AI agent with its own browser, one that does no... |
| [wy51ai/floorplan-3d](https://github.com/wy51ai/floorplan-3d) | 1,363 | HTML | No description |

### Hacker News Top Stories (Last Updated: 2026-10-04 03:32:44 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [We're going to need default hard budget caps on pretty much everything](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/) | 253 | [136 comments](https://news.ycombinator.com/item?id=49949235) |
| [Bob Cringely Has Died](https://news.ycombinator.com/item?id=49949438) | 189 | [29 comments](https://news.ycombinator.com/item?id=49949438) |
| [Treachery in the Rodin Museum 3D scan verdict](https://cosmowenman.substack.com/p/rodin-museum-3d-scan-verdict) | 107 | [55 comments](https://news.ycombinator.com/item?id=49946355) |
| [Hole Punch: Sling your spaceship around gravitational fields](https://notoriousbfg.com/hole-punch/) | 249 | [62 comments](https://news.ycombinator.com/item?id=49946393) |
| [The work by Valve's Timur Kristóf on improving old AMD GPUs on Linux](https://www.phoronix.com/news/XDC-2026-Valve-Timur-AMDGPU) | 171 | [21 comments](https://news.ycombinator.com/item?id=49946895) |
| [Inside Anthropic's Quest to Instill Morality into Its A.I. Models](https://www.nytimes.com/2026/09/29/us/anthropic-claude-morals-ai.html) | 6 | [2 comments](https://news.ycombinator.com/item?id=49950052) |
| [Reasons I didn't become an EMT, ranked](https://ben.stolovitz.com/posts/reasons-not-emt-ranked/) | 114 | [56 comments](https://news.ycombinator.com/item?id=49947631) |
| [Celebrating the 100th birthday of the kidney donated to him as a teenager](https://www.whec.com/top-news/webster-man-celebrating-the-100th-birthday-of-the-kidney-his-mom-donated-to-him-as-a-teenager/) | 157 | [41 comments](https://news.ycombinator.com/item?id=49923873) |
| [So You Think You Could Be an Electrician?](https://asteriskmag.com/issues/15/so-you-think-you-could-be-an-electrician) | 38 | [17 comments](https://news.ycombinator.com/item?id=49910462) |
| [Kolibri: A Sovereign Open-Weight Model](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/) | 537 | [307 comments](https://news.ycombinator.com/item?id=49942706) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 15.0°C (60.0°F) |
| Average Humidity | 82% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-04 03:32:44 UTC*
