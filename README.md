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

### GitHub Trending Repositories (Last Updated: 2026-07-30 01:42:08 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | 5,846 | N/A | Open Frontier Intelligence |
| [mshumer/Claude-of-Duty](https://github.com/mshumer/Claude-of-Duty) | 2,251 | JavaScript | A Call of Duty-quality FPS in Three.js, built from a single prompt. |
| [digimata/quill](https://github.com/digimata/quill) | 1,528 | Swift | Ultra-minimalist macOS recording + transcription. |
| [mikiarlo3/ai-copywriter](https://github.com/mikiarlo3/ai-copywriter) | 1,046 | Python | An AI copywriter that uses real copywriting skills + real marketing knowledge wi... |
| [fuadmefleh/Shared-Claude-Chats](https://github.com/fuadmefleh/Shared-Claude-Chats) | 933 | Python | An archive of public Claude and Grok conversations, exported from their share li... |

### Hacker News Top Stories (Last Updated: 2026-07-30 01:42:08 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [AI's top startups are barely publishing their research](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research) | 198 | [112 comments](https://news.ycombinator.com/item?id=49103285) |
| [The coolest use for the Vision Pro](https://christianselig.com/2026/07/vision-pro-house/) | 385 | [183 comments](https://news.ycombinator.com/item?id=49102774) |
| [Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac](https://github.com/drumih/turbo-fieldfare) | 651 | [226 comments](https://news.ycombinator.com/item?id=49098510) |
| [Superlogical](https://www.superlogical.com/) | 524 | [322 comments](https://news.ycombinator.com/item?id=49098965) |
| [LLM Honeypot](https://llm2human.pages.dev/) | 48 | [17 comments](https://news.ycombinator.com/item?id=49104117) |
| [Keychron announces first open-source firmware for gaming mice](https://www.digitalfoundry.net/news/2026/07/keychron-announces-first-open-source-firmware-for-gaming-mice) | 292 | [109 comments](https://news.ycombinator.com/item?id=49099715) |
| [The Cold Email](https://zachholman.com/posts/cold-email) | 87 | [38 comments](https://news.ycombinator.com/item?id=49103089) |
| [Anatomy of a Frontier Lab Agent Intrusion: A Timeline of the July 2026 Incident](https://huggingface.co/blog/agent-intrusion-technical-timeline) | 292 | [171 comments](https://news.ycombinator.com/item?id=49089500) |
| [The Productivity Mirage](https://frantic.im/mirage/) | 39 | [11 comments](https://news.ycombinator.com/item?id=49104335) |
| [Flume Water Monitor 915 MHz Security Is Pretty Good](https://waveformsecurity.com/blog/flume/) | 4 | [0 comments](https://news.ycombinator.com/item?id=49105136) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 24.0°C (74.0°F) |
| Average Humidity | 51% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-30 01:42:08 UTC*
