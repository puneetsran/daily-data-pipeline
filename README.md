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

### GitHub Trending Repositories (Last Updated: 2026-07-16 01:50:18 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [xai-org/grok-build](https://github.com/xai-org/grok-build) | 3,504 | Rust | SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensib... |
| [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | 1,349 | Python | A Codex CLI jailbreak prompt and test pack for gpt-5.6-sol. 针对 gpt-5.6 系列的 Codex... |
| [littledivy/mimic](https://github.com/littledivy/mimic) | 1,024 | Python | Intercept any app, then call it from Python like a library |
| [mereyabdenbekuly-ctrl/clodex-ide](https://github.com/mereyabdenbekuly-ctrl/clodex-ide) | 810 | TypeScript | Local-first, zero-trust agentic IDE for verifiable autonomous software developme... |
| [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) | 807 | Python | A practical, open-source guide to mastering WorkBuddy through real-world workflo... |

### Hacker News Top Stories (Last Updated: 2026-07-16 01:50:18 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Inkling: Our Open-Weights Model](https://thinkingmachines.ai/news/introducing-inkling/) | 681 | [176 comments](https://news.ycombinator.com/item?id=48924912) |
| [SQLite should have (Rust-style) editions](https://mort.coffee/home/sqlite-editions/) | 115 | [44 comments](https://news.ycombinator.com/item?id=48928135) |
| [Grok Build is open source](https://github.com/xai-org/grok-build) | 257 | [302 comments](https://news.ycombinator.com/item?id=48926590) |
| [Governments, companies, nonprofits should invest in free, open source AI [pdf]](https://www.siegelendowment.org/wp-content/uploads/2026/07/fortune-david-siegel-open-source-ai.pdf) | 87 | [32 comments](https://news.ycombinator.com/item?id=48927095) |
| [Metal-Organic Frameworks, Chemistry's New Miracle Materials (2018)](https://chemistry.berkeley.edu/news/meet-metal-organic-frameworks-chemistry%E2%80%99s-new-miracle-materials) | 36 | [10 comments](https://news.ycombinator.com/item?id=48928313) |
| [Stripe and Advent have made a joint offer to acquire PayPal – sources](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) | 341 | [208 comments](https://news.ycombinator.com/item?id=48915953) |
| [LLM Networking with MikroTik](https://blog.greg.technology/2026/07/14/llm-networking-with-mikrotik.html) | 46 | [10 comments](https://news.ycombinator.com/item?id=48927915) |
| [Nul Characters in Strings in SQLite](https://sqlite.org/nulinstr.html) | 28 | [2 comments](https://news.ycombinator.com/item?id=48928343) |
| [G# – A modern .NET language with Go, Kotlin, and Swift ergonomics](https://davidobando.github.io/gsharp/) | 8 | [0 comments](https://news.ycombinator.com/item?id=48871721) |
| [Running Gemma 4 26B at 5 tokens/sec on a 13-year-old Xeon with no GPU](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/) | 230 | [151 comments](https://news.ycombinator.com/item?id=48922434) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 28.0°C (82.0°F) |
| Average Humidity | 46% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-16 01:50:18 UTC*
