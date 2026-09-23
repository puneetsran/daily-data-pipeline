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

### GitHub Trending Repositories (Last Updated: 2026-09-23 02:34:49 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 16,962 | Python | No description |
| [zai-org/ZCode](https://github.com/zai-org/ZCode) | 6,334 | TypeScript | Z.ai's coding agent harness. Powerful, intelligent, extensible. |
| [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 6,332 | TypeScript | Claude Code plugin that replaces the compaction summary with Jev decisions: ever... |
| [mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx) | 5,511 | Python | Native MLX runtime for Laya typed decision models — 7–14 ms short decisions on M... |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 4,405 | Python | tiny Jev-like family of decision models built on top of Qwen3.5 you can train an... |

### Hacker News Top Stories (Last Updated: 2026-09-23 02:34:49 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/) | 1215 | [619 comments](https://news.ycombinator.com/item?id=49805509) |
| [Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) | 1239 | [833 comments](https://news.ycombinator.com/item?id=49803892) |
| ['We hacked the FBI:' Hackers say they have data on all FBI employees](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) | 430 | [300 comments](https://news.ycombinator.com/item?id=49805278) |
| [OpenAI GPT–6 Astra breaks Enigma message that has resisted solution since 2005](https://www.cryptocellar.org/bgac/the-mvueh-break.html) | 572 | [362 comments](https://news.ycombinator.com/item?id=49801324) |
| [ReBarUEFI: Resizable BAR for almost any UEFI system](https://github.com/xCuri0/ReBarUEFI) | 81 | [23 comments](https://news.ycombinator.com/item?id=49781862) |
| [Microsoft killed FoxPro in 2007. Anyway, here's FoxPro revived](https://foxscript.org/) | 193 | [133 comments](https://news.ycombinator.com/item?id=49808023) |
| [What California is learning from solar panels built over irrigation canals](https://www.kqed.org/science/2002033/heres-what-california-is-learning-from-solar-panels-built-over-irrigation-canals) | 126 | [172 comments](https://news.ycombinator.com/item?id=49796379) |
| [SAML: A fractal of bad design](https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/) | 167 | [94 comments](https://news.ycombinator.com/item?id=49806335) |
| [Claude Opus 5.5 Intelligence, Performance and Price Analysis (Max)](https://artificialanalysis.ai/models/claude-opus-5-5) | 239 | [72 comments](https://news.ycombinator.com/item?id=49804316) |
| [WordPress: Unauthenticated path traversal leading to conditional RCE](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp) | 158 | [84 comments](https://news.ycombinator.com/item?id=49803959) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 16.0°C (61.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-23 02:34:49 UTC*
