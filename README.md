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

### GitHub Trending Repositories (Last Updated: 2026-07-15 01:40:20 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | 1,015 | Python | A Codex CLI jailbreak prompt and test pack for gpt-5.6-sol. 针对 gpt-5.6 系列的 Codex... |
| [vinhhien112/Three.js-Object-Sculptor-Codex-Plugin](https://github.com/vinhhien112/Three.js-Object-Sculptor-Codex-Plugin) | 966 | Python | Codex plugin that turns attached object images into code-only, animation-ready p... |
| [littledivy/mimic](https://github.com/littledivy/mimic) | 909 | Python | Intercept any app, then call it from Python like a library |
| [mereyabdenbekuly-ctrl/clodex-ide](https://github.com/mereyabdenbekuly-ctrl/clodex-ide) | 801 | TypeScript | Local-first, zero-trust agentic IDE for verifiable autonomous software developme... |
| [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) | 695 | Python | A practical, open-source guide to mastering WorkBuddy through real-world workflo... |

### Hacker News Top Stories (Last Updated: 2026-07-15 01:40:20 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Vancouver PD website features Quick Escape button that wipes itself from history](https://vpd.ca/) | 59 | [21 comments](https://news.ycombinator.com/item?id=48914644) |
| [TS-2026-009: Insecure argument handling in Tailscale SSH permitted root access](https://tailscale.com/security-bulletins) | 18 | [2 comments](https://news.ycombinator.com/item?id=48915004) |
| [Bonsai 27B: A 27B-Class model that runs on a phone](https://prismml.com/news/bonsai-27b) | 430 | [160 comments](https://news.ycombinator.com/item?id=48910545) |
| [Dependabot version updates introduce default package cooldown](https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/) | 95 | [59 comments](https://news.ycombinator.com/item?id=48913050) |
| [The Tower Keeps Rising](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/) | 336 | [164 comments](https://news.ycombinator.com/item?id=48909785) |
| [Financing the AI boom: from cash flows to debt [pdf]](https://www.bis.org/publ/bisbull120.pdf) | 85 | [32 comments](https://news.ycombinator.com/item?id=48913443) |
| [Cursor 0day: When Full Disclosure Becomes the Only Protection Left](https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left) | 248 | [107 comments](https://news.ycombinator.com/item?id=48910676) |
| [How I use HTMX with Go](https://www.alexedwards.net/blog/how-i-use-htmx-with-go) | 110 | [26 comments](https://news.ycombinator.com/item?id=48912175) |
| [C++20 Improved the For-Loop Syntax](https://lzon.ca/posts/tips/cpp-for-range-init/) | 23 | [17 comments](https://news.ycombinator.com/item?id=48873275) |
| [Your 'app' could have been a webpage (so I fixed it for you)](https://danq.me/2026/07/09/your-app-could-have-been-a-webpage/) | 716 | [438 comments](https://news.ycombinator.com/item?id=48869989) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 27.0°C (81.0°F) |
| Average Humidity | 39% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-15 01:40:20 UTC*
