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

### GitHub Trending Repositories (Last Updated: 2026-09-21 02:31:53 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 12,223 | Python | i. am. speed. |
| [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 5,277 | TypeScript | Claude Code plugin that replaces the compaction summary with Jev decisions: ever... |
| [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 4,562 | Python | No description |
| [robbietilton/Compositor](https://github.com/robbietilton/Compositor) | 3,736 | Swift | The Photoshop alternative for Mac |
| [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) | 2,482 | Python | Semantic ifs from open models, on a 3090 at home. Independent; not affiliated wi... |

### Hacker News Top Stories (Last Updated: 2026-09-21 02:31:53 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Google's Open Agentic Orchestrator](https://agentexecutor.io) | 232 | [97 comments](https://news.ycombinator.com/item?id=49780797) |
| [Samsung is expected to more than double output of its HBM4 and HBM4E DRAM](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say) | 359 | [232 comments](https://news.ycombinator.com/item?id=49778029) |
| [What happened to the Snowden archive](https://libroot.org/posts/what-happened-to-the-snowden-archive) | 186 | [91 comments](https://news.ycombinator.com/item?id=49780820) |
| [ChatGPT now knows what you do on other websites via ad collector](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/) | 615 | [327 comments](https://news.ycombinator.com/item?id=49776729) |
| [Can I Let My AI Agent Run on Shabbat?](https://www.chabad.org/library/article_cdo/aid/7288064/jewish/Can-I-Let-My-AI-Agent-Run-on-Shabbat.htm) | 11 | [1 comments](https://news.ycombinator.com/item?id=49782242) |
| [Qwen Image 2.1](https://qwen.ai/blog?id=qwen-image-2.1) | 514 | [156 comments](https://news.ycombinator.com/item?id=49775499) |
| [Amiga Unix, Again](https://amigaux.org/) | 21 | [7 comments](https://news.ycombinator.com/item?id=49781436) |
| [The Effect of CRTs on Pixel Art (2024)](https://datagubbe.se/crt/) | 99 | [24 comments](https://news.ycombinator.com/item?id=49768336) |
| [Pirate Face Rescues LLM Models from Deletion](https://pirateface.co/) | 457 | [134 comments](https://news.ycombinator.com/item?id=49776699) |
| [Bill to Ban Private Equity from Owning Medical Practices](https://truthout.org/articles/warren-introduces-bill-to-ban-private-equity-from-owning-medical-practices/) | 291 | [189 comments](https://news.ycombinator.com/item?id=49780630) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 15.0°C (59.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-21 02:31:53 UTC*
