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

### GitHub Trending Repositories (Last Updated: 2026-08-11 01:03:29 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | 2,275 | Python | 让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。 |
| [Binaryify/open-kimi-ppt-skill](https://github.com/Binaryify/open-kimi-ppt-skill) | 1,607 | N/A | 非官方 Kimi Slides Skill：让 AI Agent 生成可编辑 PPTD + PPTX，并附带本地浏览器编辑器 Unofficial Kimi S... |
| [ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness) | 1,316 | Python | let your agent control your phone |
| [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | 1,199 | Python | Create smooth, responsive interactive web animations. |
| [MengTo/kage](https://github.com/MengTo/kage) | 774 | HTML | An interactive five-chapter night walk through a Kyoto mountain temple, rendered... |

### Hacker News Top Stories (Last Updated: 2026-08-11 01:03:29 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [The UK's War on Anonymity Has Come to America](https://www.effort.news/uk-lobby) | 93 | [22 comments](https://news.ycombinator.com/item?id=49251411) |
| [Show HN: Needle2: 14MB agentic LLM for phones, wearables, smart home and robots](https://cactuscompute.com/needle) | 154 | [70 comments](https://news.ycombinator.com/item?id=49246804) |
| [Muse Glimmer: 30B-parameter model optimized for always-on local agent workflows](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) | 1024 | [570 comments](https://news.ycombinator.com/item?id=49241679) |
| [Show HN: Scroll through all 43252003274489856000 Rubik's Cube states](https://everycube.alen.is/) | 31 | [4 comments](https://news.ycombinator.com/item?id=49251179) |
| [The "mechanical miracle" that ruined Mark Twain's life](https://resobscura.substack.com/p/the-mechanical-miracle-that-ruined) | 23 | [4 comments](https://news.ycombinator.com/item?id=49184220) |
| [Mark Zuckerberg attacks 'closed' AI rivals as Meta returns to open models](https://www.ft.com/content/4e3957f8-ea7c-4c46-a3de-cdce8e526878) | 353 | [373 comments](https://news.ycombinator.com/item?id=49243880) |
| [Publishing Schematics Before “Open Source” Was a Word](https://fabscene.medium.com/publishing-schematics-before-open-source-was-a-word-55-years-of-akizuki-denshi-japans-be7ca9629704) | 60 | [15 comments](https://news.ycombinator.com/item?id=49212449) |
| [Rust SIMD on the GPU](https://www.vectorware.com/blog/simd-on-gpu/) | 119 | [59 comments](https://news.ycombinator.com/item?id=49247477) |
| [Sonic Pi v5](https://www.patreon.com/samaaron/posts/sonic-pi-v5-166001392) | 303 | [78 comments](https://news.ycombinator.com/item?id=49208296) |
| [Confessions of a Long-Distance Sailor](https://arachnoid.com/lutusp/sailbook.html) | 56 | [10 comments](https://news.ycombinator.com/item?id=49249555) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 24.0°C (76.0°F) |
| Average Humidity | 57% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-11 01:03:29 UTC*
