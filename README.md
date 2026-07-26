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

### GitHub Trending Repositories (Last Updated: 2026-07-26 01:57:35 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [andrewyng/openworker](https://github.com/andrewyng/openworker) | 5,039 | Python | No description |
| [Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs) | 1,007 | TypeScript | Dotted thought-orb loading indicators for AI & agent UIs — six tuned states, two... |
| [Blaizzy/nativ](https://github.com/Blaizzy/nativ) | 885 | Swift | Local AI, native to your Mac. Chat, serve, monitor, and connect MLX models from ... |
| [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | 876 | Python | 一个先接住情绪、再分析关系并给出可执行策略的 Codex 恋爱军师，内置心理、法律、社会、人文、哲学、婚姻家庭与性学知识库，支持多元关系。 |
| [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | 817 | Python | No description |

### Hacker News Top Stories (Last Updated: 2026-07-26 01:57:35 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Systems and Delays](https://martin.janiczek.cz/2026/07/24/systems-and-delays.html) | 13 | [1 comments](https://news.ycombinator.com/item?id=49053382) |
| [Stolen Buttons](https://anatolyzenkov.com/stolen-buttons) | 573 | [133 comments](https://news.ycombinator.com/item?id=48976262) |
| [DeepSeek pause fundraise after comments on compute gap to US leaked (transcript)...](https://github.com/demo-zexuan/liang-wenfeng-investor-meeting-2026-7-22/blob/master/%E6%A2%81%E6%96%87%E9%94%8B%E6%8A%95%E8%B5%84%E8%80%85%E4%BA%A4%E6%B5%81%E4%BC%9A-%E6%96%87%E5%AD%97%E7%A8%BF_1_18_translate_20260723201651.pdf) | 74 | [41 comments](https://news.ycombinator.com/item?id=49052912) |
| [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) | 164 | [107 comments](https://news.ycombinator.com/item?id=49051361) |
| [Clinical Failure Rates over the Decades: Yikes](https://www.science.org/content/blog-post/clinical-failure-rates-over-decades-yikes) | 42 | [24 comments](https://news.ycombinator.com/item?id=49052628) |
| [GM Backs Sodium Ion Batteries for U.S. Grid Storage](https://spectrum.ieee.org/sodium-ion-battery-peak-energy) | 125 | [40 comments](https://news.ycombinator.com/item?id=49051947) |
| [Cloudflare's new AI traffic options for customers](https://blog.cloudflare.com/content-independence-day-ai-options/) | 29 | [11 comments](https://news.ycombinator.com/item?id=49052564) |
| [SIMD for Collision](https://box2d.org/posts/2026/07/simd-for-collision/) | 53 | [15 comments](https://news.ycombinator.com/item?id=49013464) |
| [Turn And Face The Strange](https://fly.io/blog/kurt-scott-money-sprites/) | 141 | [110 comments](https://news.ycombinator.com/item?id=49051369) |
| [LLM Usage in Debian: Three Proposals](https://www.debian.org/vote/2026/vote_002) | 69 | [63 comments](https://news.ycombinator.com/item?id=49050859) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 19.0°C (67.0°F) |
| Average Humidity | 71% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-26 01:57:35 UTC*
