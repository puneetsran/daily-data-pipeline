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

### GitHub Trending Repositories (Last Updated: 2026-09-11 02:13:07 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [ashemag/human-atlas](https://github.com/ashemag/human-atlas) | 3,099 | TypeScript | Open-source 3D anatomy explorer: 2,234 selectable BodyParts3D meshes, system lay... |
| [openai/NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler) | 1,720 | Lean | Lean certificates accompanying Navier-Stokes and Euler results |
| [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86) | 1,444 | N/A | Here is a dlssg for RTX30 Series GPU  |
| [vinzdg/codenotch](https://github.com/vinzdg/codenotch) | 1,389 | Swift | A macOS app that pins usage limits from Claude Code, Cursor, Codex, and Antigrav... |
| [EverettFish/holo-card-studio](https://github.com/EverettFish/holo-card-studio) | 1,338 | Python | Turn the user's description or uploaded reference into a finished, editable Blen... |

### Hacker News Top Stories (Last Updated: 2026-09-11 02:13:07 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [YuE2 · Frontier Music with Symbolic Planning](https://map-yue2.github.io/) | 41 | [33 comments](https://news.ycombinator.com/item?id=49652028) |
| [Shopify is moving from React Native back to Swift and Kotlin](https://shopify.engineering/back-to-native) | 798 | [538 comments](https://news.ycombinator.com/item?id=49643982) |
| [More questions about whether researchers can trust OpenAI with unpublished math](https://mathstodon.xyz/@andreasthom/117240535270608201) | 685 | [635 comments](https://news.ycombinator.com/item?id=49639408) |
| [Google will buy half the electricity of a nuclear power plant](https://www.bbc.com/news/articles/c8r6y4me2g6o) | 78 | [53 comments](https://news.ycombinator.com/item?id=49652105) |
| [OpenAI Agents API](https://developers.openai.com/api/docs/guides/agents-api/overview) | 139 | [89 comments](https://news.ycombinator.com/item?id=49649213) |
| [The Deathray: A simple way for an untrusted site to freeze a Mac](https://auberon.xyz/blog/posts/deathray/) | 89 | [55 comments](https://news.ycombinator.com/item?id=49649124) |
| [Don't let anyone take away your big box of cables](https://blog.jim-nielsen.com/2026/hands-off-my-cables/) | 335 | [258 comments](https://news.ycombinator.com/item?id=49645393) |
| [Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra](https://cognition.com/blog/swe-2) | 357 | [150 comments](https://news.ycombinator.com/item?id=49645443) |
| [Thelio Mira AI Linux Workstation: 192 GB GPU Memory](https://system76.com/workstations/thelio-mira-ai) | 33 | [24 comments](https://news.ycombinator.com/item?id=49651372) |
| [Technique for Manipulating Satellite Photos Now Reveals Ancient Images (2025)](https://spinoff.nasa.gov/Manipulating_Satellite_Photos_Now_Reveals_Ancient_Images) | 277 | [42 comments](https://news.ycombinator.com/item?id=49645437) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 18.0°C (64.0°F) |
| Average Humidity | 63% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-11 02:13:07 UTC*
