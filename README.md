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

### GitHub Trending Repositories (Last Updated: 2026-08-18 00:42:55 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 150,029 | TypeScript | DeepSeek Harness: Everything is a Plugin. |
| [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | 11,659 | TypeScript | 为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。 |
| [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | 7,582 | Python | A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表 |
| [yjh051108/dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) | 5,368 | PowerShell | dsh-routing-suite — injector + router-standard kit: install the runtime injector... |
| [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | 4,106 | TypeScript | Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git g... |

### Hacker News Top Stories (Last Updated: 2026-08-18 00:42:55 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [How Bluesky draws its logo on screenshots](https://timmarinin.net/2026/bluesky-screenshots/) | 169 | [127 comments](https://news.ycombinator.com/item?id=49338459) |
| [Cursor Origin](https://cursor.com/docs/origin) | 40 | [16 comments](https://news.ycombinator.com/item?id=49339359) |
| [Quake Shareware, a CD-ROM just a little too full](https://fabiensanglard.net/quake_shareware_cd/index.html) | 110 | [50 comments](https://news.ycombinator.com/item?id=49338328) |
| [Fairphone 6 and PostmarketOS working main camera](https://catcrafts.net/posts/fairphone-6-postmarketos-working-main-camera) | 65 | [14 comments](https://news.ycombinator.com/item?id=49338285) |
| [GPU Offload in Rust: Portable, Safe, and Fast](https://arxiv.org/abs/2608.13759) | 151 | [33 comments](https://news.ycombinator.com/item?id=49334991) |
| [A Preview of DuckDB v2.0](https://duckdb.org/2026/08/17/duckdb-20-highlights) | 517 | [91 comments](https://news.ycombinator.com/item?id=49330781) |
| [Incident with Github.com](https://www.githubstatus.com/incidents/zkxwbgr0cnmx) | 520 | [903 comments](https://news.ycombinator.com/item?id=49330597) |
| [AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) | 307 | [123 comments](https://news.ycombinator.com/item?id=49331423) |
| [GPT-5.6 Sol Pricing Cut by 50%](https://openrouter.ai/openai/gpt-5.6-sol) | 56 | [10 comments](https://news.ycombinator.com/item?id=49337602) |
| [AI;DR (AI; Didn't Read)](https://www.rickmanelius.com/p/aidr-ai-didnt-read) | 558 | [343 comments](https://news.ycombinator.com/item?id=49336573) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 22.0°C (72.0°F) |
| Average Humidity | 74% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-18 00:42:55 UTC*
