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

### GitHub Trending Repositories (Last Updated: 2026-08-12 01:10:54 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness) | 1,502 | Python | let your agent control your phone |
| [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | 1,483 | Python | Create smooth, responsive interactive web animations. |
| [SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI) | 1,427 | TypeScript | No description |
| [antirez/h3.c](https://github.com/antirez/h3.c) | 1,245 | C | MiniMax H3 inference engine for Mac computers |
| [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | 904 | JavaScript | AI 短剧制作的 skill 集合：拆角色、出设定图、排大纲 | Agent skills for AI short-drama production — ch... |

### Hacker News Top Stories (Last Updated: 2026-08-12 01:10:54 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [CFTC declares market emergency, orders Kalshi to continue to operate in New York](https://www.cftc.gov/PressRoom/PressReleases/9281-26) | 75 | [27 comments](https://news.ycombinator.com/item?id=49266277) |
| [WorldClaw Agentic 3D open-world generation at scale](https://tencent-hunyuan.github.io/Hunyuan3D-WorldClaw/) | 106 | [38 comments](https://news.ycombinator.com/item?id=49265051) |
| [Compression is prediction](https://ngrok.com/blog/compression-is-prediction) | 236 | [101 comments](https://news.ycombinator.com/item?id=49263497) |
| [Nvidia Nemotron 3.5 Lightning and NeMo Switchyard](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/) | 173 | [89 comments](https://news.ycombinator.com/item?id=49263340) |
| [Mojo 1.0](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here) | 279 | [127 comments](https://news.ycombinator.com/item?id=49261128) |
| [Stealing Reasoning Traces from Proprietary LLM APIs](https://stolen-thoughts.com/) | 485 | [202 comments](https://news.ycombinator.com/item?id=49257876) |
| [OpenAI’s head of ethics leaves less than a year after joining](https://www.ft.com/content/e49dfb75-f841-4466-a577-f7aaff8779a0) | 270 | [341 comments](https://news.ycombinator.com/item?id=49257160) |
| [Making holograms with a pen plotter](https://blog.jordan.matelsky.com/Penplotter-holography/) | 110 | [11 comments](https://news.ycombinator.com/item?id=49262811) |
| [Show HN: iPhone app takes simultaneous images from 2 lenses, fuses into 1 photo](https://photosynthesis.camera) | 198 | [201 comments](https://news.ycombinator.com/item?id=49226623) |
| [US hires over 2k video gamers as air traffic controllers](https://www.cbsnews.com/news/video-gamer-air-traffic-controllers-faa-recruitment-sean-duffy/) | 57 | [39 comments](https://news.ycombinator.com/item?id=49265879) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 21.0°C (69.0°F) |
| Average Humidity | 64% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-12 01:10:54 UTC*
