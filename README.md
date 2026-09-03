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

### GitHub Trending Repositories (Last Updated: 2026-09-03 02:14:14 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt) | 2,285 | TypeScript | ChatGPT thinks. Codex works. Use ChatGPT as the planning brain while keeping the... |
| [Nanako0129/sepia](https://github.com/Nanako0129/sepia) | 1,599 | Python | De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CL... |
| [MetaMask-AI/metamask-desktop](https://github.com/MetaMask-AI/metamask-desktop) | 1,230 | CSS | 🌐 🔌 The MetaMask desktop app enables browsing Ethereum blockchain enabled websit... |
| [cbrock84/headcount](https://github.com/cbrock84/headcount) | 1,118 | Markdown | An agent organization for Claude Code, structured as a company — 15+ departments... |
| [GangTailorUpgrade/undress-service](https://github.com/GangTailorUpgrade/undress-service) | 934 | Python | Dress AI Sponsor |

### Hacker News Top Stories (Last Updated: 2026-09-03 02:14:14 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Muse Spark 1.3](https://developer.meta.com/ai/models/muse-spark/) | 405 | [269 comments](https://news.ycombinator.com/item?id=49541256) |
| [Gemini 3.8 Flash and 3.8 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) | 839 | [488 comments](https://news.ycombinator.com/item?id=49537553) |
| [Google avoids a breakup of its ad tech business](https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html) | 273 | [187 comments](https://news.ycombinator.com/item?id=49537131) |
| [Holden's Lightning Flight](https://en.wikipedia.org/wiki/Holden%27s_Lightning_flight) | 65 | [9 comments](https://news.ycombinator.com/item?id=49508405) |
| [Launch HN: RonanRX (YC S26) – Personalized Peptides and GLP-1s](https://ronanrx.com/) | 27 | [32 comments](https://news.ycombinator.com/item?id=49543530) |
| [Fable 5.1 World Modeling](https://github.com/PhiloLabs/fable51-worlds) | 147 | [53 comments](https://news.ycombinator.com/item?id=49541458) |
| [Reverse Engineering Unknown File Formats with ImHex](https://werwolv.net/posts/file_format_reverse_engineering/) | 109 | [20 comments](https://news.ycombinator.com/item?id=49508608) |
| [Three sites made 215,128 “best software” pages for AI. Perplexity cites them](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) | 316 | [144 comments](https://news.ycombinator.com/item?id=49536375) |
| [Can I opt out of my input or output data being used for training?](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) | 377 | [165 comments](https://news.ycombinator.com/item?id=49535284) |
| [The shrinking landscape of linguistic diversity in the age of LLMs](https://www.nature.com/articles/s41562-026-02550-0) | 36 | [10 comments](https://news.ycombinator.com/item?id=49497996) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 15.0°C (60.0°F) |
| Average Humidity | 78% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-03 02:14:14 UTC*
