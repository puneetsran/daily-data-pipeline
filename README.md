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

### GitHub Trending Repositories (Last Updated: 2026-08-08 00:58:49 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | 11,033 | Rust | Convert Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, and PDF to clean ... |
| [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | 1,982 | TypeScript | An interactive 3D human anatomy explorer built using threejs with GPT 5.6 Sol |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | 1,874 | Python | 让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。 |
| [Binaryify/open-kimi-ppt-skill](https://github.com/Binaryify/open-kimi-ppt-skill) | 1,588 | N/A | 非官方 Kimi Slides Skill：让 AI Agent 生成可编辑 PPTD + PPTX，并附带本地浏览器编辑器 Unofficial Kimi S... |
| [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | 1,492 | N/A | No description |

### Hacker News Top Stories (Last Updated: 2026-08-08 00:58:49 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [DeepSeek V4 Flash 0731](https://arcprize.org/results/deepseek-v4-flash-0731) | 442 | [256 comments](https://news.ycombinator.com/item?id=49214008) |
| [U.S. Department of Energy Launches the Genesis Open Models Initiative](https://genesisopenmodels.anl.gov/) | 53 | [17 comments](https://news.ycombinator.com/item?id=49216946) |
| [Assembly Hall of Shame](https://github.com/xoreaxeaxeax/asm-hall-of-shame) | 240 | [55 comments](https://news.ycombinator.com/item?id=49214098) |
| [Ancient Library – 1,060 Greek/Latin texts, click any word to parse it](https://ancientlibrary.net/) | 139 | [47 comments](https://news.ycombinator.com/item?id=49214770) |
| [Should AI labs be treated like the owners of dangerous animals?](https://www.economist.com/science-and-technology/2026/08/06/should-ai-labs-be-treated-like-the-owners-of-dangerous-animals) | 13 | [9 comments](https://news.ycombinator.com/item?id=49217629) |
| [What happens if an entire class of workers loses faith in their careers](https://www.noemamag.com/why-is-everyone-in-tech-so-sad/) | 393 | [526 comments](https://news.ycombinator.com/item?id=49209539) |
| [Managing AI Coding Costs at Scale](https://www.databricks.com/blog/managing-ai-coding-costs-scale) | 156 | [163 comments](https://news.ycombinator.com/item?id=49214468) |
| [Responding to the next frontier of critical cyber capabilities](https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/) | 151 | [167 comments](https://news.ycombinator.com/item?id=49213029) |
| [An all-sky map of half a million supermassive black holes](https://www.sdss.org/black-hole-mapper-release-20/) | 137 | [35 comments](https://news.ycombinator.com/item?id=49211921) |
| [Oracle bans AI-generated code from OpenJDK](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code) | 373 | [248 comments](https://news.ycombinator.com/item?id=49213754) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 27.0°C (80.0°F) |
| Average Humidity | 54% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-08 00:58:49 UTC*
