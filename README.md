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

### GitHub Trending Repositories (Last Updated: 2026-09-27 02:43:38 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | 6,679 | Kotlin | 装在手机上的对话副驾：在 QQ / X / 飞书里读懂对方、给出候选回复、一键填入输入框，发不发由你。非侵入，只读屏幕，不 hook 不改包。 |
| [unreallabsai/unreal-agent](https://github.com/unreallabsai/unreal-agent) | 1,969 | Go | Async-first agent harness |
| [Contrastive-LM/CLM](https://github.com/Contrastive-LM/CLM) | 1,609 | Python | No description |
| [tobi/disktree](https://github.com/tobi/disktree) | 1,311 | Rust | A treemap for finding and removing what fills your disk, for Omarchy. Rust + GPU... |
| [JohnHeibel/PDoomVideo](https://github.com/JohnHeibel/PDoomVideo) | 1,056 | JavaScript | Source code for the Claude Opus 5.5 music video for I'm Upping My P(doom) |

### Hacker News Top Stories (Last Updated: 2026-09-27 02:43:38 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Does Georgism work? Five years later](https://www.astralcodexten.com/p/does-georgism-work-five-years-later) | 157 | [88 comments](https://news.ycombinator.com/item?id=49844657) |
| [PipePipe: NewPipe hard fork implementing SponsorBlock](https://github.com/InfinityLoop1308/PipePipe) | 327 | [185 comments](https://news.ycombinator.com/item?id=49842764) |
| [DeepSeek Elastic Compute (DSec)](https://arxiv.org/abs/2609.22978) | 166 | [52 comments](https://news.ycombinator.com/item?id=49859112) |
| [Go Concurrency Distilled](https://antonz.org/go-concurrency-distilled/) | 48 | [9 comments](https://news.ycombinator.com/item?id=49856988) |
| [Show HN: Reladraw – A diagram language where you decide where to place things](https://github.com/reladraw/reladraw) | 200 | [57 comments](https://news.ycombinator.com/item?id=49858513) |
| [Turning GLM-5.3-Flash into a Jev-like decision model](https://www.privatemode.ai/blog/system-one-from-glm-flash) | 35 | [18 comments](https://news.ycombinator.com/item?id=49857656) |
| [Evolving programming languages in the AI era](https://dashbit.co/blog/evolving-ai-era) | 38 | [24 comments](https://news.ycombinator.com/item?id=49839567) |
| [A searchable library of forgotten public-domain film clips from 1915 onward](https://www.movingimagearchive.com/) | 118 | [25 comments](https://news.ycombinator.com/item?id=49832768) |
| [Drawgent: Coding agent on a live Excalidraw canvas](https://tangled.org/yanndegat.tngl.sh/drawgent) | 112 | [32 comments](https://news.ycombinator.com/item?id=49857729) |
| [Fifteen years later, the Apple Cards origin story](https://lexontech.org/fifteen-years-later-the-apple-cards-origin-story) | 348 | [90 comments](https://news.ycombinator.com/item?id=49854693) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 13.0°C (55.0°F) |
| Average Humidity | 68% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-27 02:43:38 UTC*
