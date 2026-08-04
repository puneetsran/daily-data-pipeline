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

### GitHub Trending Repositories (Last Updated: 2026-08-04 01:45:32 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [yc-software/qm](https://github.com/yc-software/qm) | 9,767 | TypeScript | Multiplayer agent harness for work |
| [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | 4,260 | TypeScript | No description |
| [trycompai/crm](https://github.com/trycompai/crm) | 3,311 | TypeScript | An open-source, agentic-first CRM. |
| [xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer](https://github.com/xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer) | 2,095 | N/A | FDE（前沿部署工程师）从零入门指南（基于范冰《增长黑客》原书框架） |
| [microsoft/skill-recorder](https://github.com/microsoft/skill-recorder) | 1,428 | TypeScript | Desktop app that records your on-screen work session and uses the GitHub Copilot... |

### Hacker News Top Stories (Last Updated: 2026-08-04 01:45:32 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [LLMs reward expertise](https://www.seangoedecke.com/llms-reward-expertise/) | 437 | [191 comments](https://news.ycombinator.com/item?id=49161518) |
| [Amazonian civilization had estimated 3M people in 3% of forest area](https://www.science.org/content/article/odd-shapes-hidden-dense-amazon-rainforest-reveal-sprawling-ancient-civilization) | 20 | [7 comments](https://news.ycombinator.com/item?id=49099336) |
| [Ten advances in mathematics and theoretical computer science](https://openai.com/index/ten-advances-in-mathematics/) | 430 | [714 comments](https://news.ycombinator.com/item?id=49157930) |
| [Ask HN: Who is hiring? (August 2026)](https://news.ycombinator.com/item?id=49156683) | 103 | [102 comments](https://news.ycombinator.com/item?id=49156683) |
| [Devtools must be open source](https://blog.exe.dev/devtools-must-be-open-source) | 502 | [177 comments](https://news.ycombinator.com/item?id=49156111) |
| [Windows XP 2002 for the Itanium: Unbridled rage](https://virtuallyfun.com/2026/08/03/windows-xp-2002-for-the-itanium-unbridled-rage/) | 56 | [25 comments](https://news.ycombinator.com/item?id=49162086) |
| [Ask HN: Who wants to be hired? (August 2026)](https://news.ycombinator.com/item?id=49156682) | 53 | [178 comments](https://news.ycombinator.com/item?id=49156682) |
| [Smaller, faster, safer: running Kimi and GLM at scale](https://blog.cloudflare.com/smaller-faster-safer-models/) | 144 | [39 comments](https://news.ycombinator.com/item?id=49158581) |
| [MiniMax H3 Day-0 Support in ComfyUI: Open Weights, Native Audio, and 2K Video](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui) | 254 | [79 comments](https://news.ycombinator.com/item?id=49155629) |
| [Celebrating 45 Years of Kermit with the First New C-Kermit Release in 15 Years](https://changelog.complete.org/archives/44456-celebrating-45-years-of-kermit-with-the-first-new-c-kermit-release-in-15-years-and-working-with-a-decades-old-c-codebase) | 124 | [35 comments](https://news.ycombinator.com/item?id=49158474) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 24.0°C (74.0°F) |
| Average Humidity | 52% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-04 01:45:32 UTC*
