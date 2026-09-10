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

### GitHub Trending Repositories (Last Updated: 2026-09-10 02:17:12 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [ashemag/human-atlas](https://github.com/ashemag/human-atlas) | 2,853 | TypeScript | Open-source 3D anatomy explorer: 2,234 selectable BodyParts3D meshes, system lay... |
| [Rion-Wu-tech/wechat-intelligence-hub](https://github.com/Rion-Wu-tech/wechat-intelligence-hub) | 2,025 | Python | Local-first WeChat intelligence system with a read-only CLI, Codex skills, searc... |
| [openai/NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler) | 1,567 | Lean | Lean certificates accompanying Navier-Stokes and Euler results |
| [vinzdg/codenotch](https://github.com/vinzdg/codenotch) | 1,288 | Swift | A macOS app that pins usage limits from Claude Code, Cursor, Codex, and Antigrav... |
| [EverettFish/holo-card-studio](https://github.com/EverettFish/holo-card-studio) | 1,243 | Python | Turn the user's description or uploaded reference into a finished, editable Blen... |

### Hacker News Top Stories (Last Updated: 2026-09-10 02:17:12 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [iPhone Duo](https://www.apple.com/iphone-duo/) | 911 | [1710 comments](https://news.ycombinator.com/item?id=49630931) |
| [Shopify acquires Tailwind](https://tailwindcss.com/blog/tailwind-is-joining-shopify) | 898 | [356 comments](https://news.ycombinator.com/item?id=49626190) |
| [What do Visa and Mastercard do? An intro to card networks](https://tautology.town/2026/06/01/card-networks.html) | 386 | [227 comments](https://news.ycombinator.com/item?id=49614280) |
| [AirPods 5](https://www.apple.com/newsroom/2026/09/apple-introduces-airpods-5-with-best-in-class-open-ear-active-noise-cancellation/) | 380 | [309 comments](https://news.ycombinator.com/item?id=49630253) |
| [Show HN: Compute polynomials twice as fast](https://thomasahle.com/fast-polynomials/) | 14 | [0 comments](https://news.ycombinator.com/item?id=49623398) |
| [Growing proof that autonomous cars save lives](https://spectrum.ieee.org/are-self-driving-cars-safe) | 219 | [423 comments](https://news.ycombinator.com/item?id=49629886) |
| [No Man's Sky Cosmos](https://www.nomanssky.com/cosmos-update/) | 306 | [327 comments](https://news.ycombinator.com/item?id=49628493) |
| [iPhone 18 Pro and iPhone 18 Pro Max](https://www.apple.com/newsroom/2026/09/apple-debuts-iphone-18-pro-and-iphone-18-pro-max/) | 284 | [297 comments](https://news.ycombinator.com/item?id=49630151) |
| [GPT-6 Astra, looped transformers, and hidden reasoning](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) | 354 | [124 comments](https://news.ycombinator.com/item?id=49627370) |
| [Factoring RSA 260](https://cognition.com/blog/factoring-rsa-260) | 36 | [5 comments](https://news.ycombinator.com/item?id=49633534) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 16.0°C (61.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-10 02:17:12 UTC*
