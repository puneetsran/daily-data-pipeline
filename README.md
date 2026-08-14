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

### GitHub Trending Repositories (Last Updated: 2026-08-14 01:11:34 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 47,152 | TypeScript | DeepSeek Harness: Everything is a Plugin. |
| [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | 5,437 | Python | Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrit... |
| [antirez/h3.c](https://github.com/antirez/h3.c) | 1,778 | C | MiniMax H3 inference engine for Mac computers |
| [SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI) | 1,683 | TypeScript | No description |
| [Leutenegger/book-to-skill](https://github.com/Leutenegger/book-to-skill) | 1,027 | Python | Turn any technical book PDF into a Claude Code skill — ready to study, reference... |

### Hacker News Top Stories (Last Updated: 2026-08-14 01:11:34 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) | 600 | [335 comments](https://news.ycombinator.com/item?id=49289112) |
| [Bluesky Protocol Services](https://atproto.com/blog/introducing-bluesky-protocol-services) | 44 | [5 comments](https://news.ycombinator.com/item?id=49293324) |
| [Accelerating GPT-5.6 Sol Ultrafast](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) | 408 | [172 comments](https://news.ycombinator.com/item?id=49289844) |
| [NP-Overrated](https://gruhn.me/blog/2026-08-13/) | 142 | [87 comments](https://news.ycombinator.com/item?id=49291268) |
| [How AI text watermarking works](https://declaude.org/watermarking/) | 51 | [32 comments](https://news.ycombinator.com/item?id=49292932) |
| [Understanding is the new bottleneck](https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck) | 192 | [100 comments](https://news.ycombinator.com/item?id=49290299) |
| [Donkey.bas is 45 Years Old – 131 line of Glory](https://donkeybas.com/) | 184 | [79 comments](https://news.ycombinator.com/item?id=49289465) |
| [DeepSeek Harness developer preview](https://deepseek.com/harness/en/) | 551 | [241 comments](https://news.ycombinator.com/item?id=49285244) |
| [Mistral OCR 4.1](https://docs.mistral.ai/models/ocr-4-1) | 248 | [97 comments](https://news.ycombinator.com/item?id=49288889) |
| [Choose Boring Technology (2015)](https://mcfunley.com/choose-boring-technology) | 243 | [125 comments](https://news.ycombinator.com/item?id=49289512) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 28.0°C (82.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-14 01:11:34 UTC*
