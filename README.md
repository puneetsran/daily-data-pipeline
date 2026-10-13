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

### GitHub Trending Repositories (Last Updated: 2026-10-13 04:43:09 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [storytold/wordcraft](https://github.com/storytold/wordcraft) | 9,484 | Rust | An open-source, clean-room reimplementation of Microsoft Word in pure Rust |
| [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | 6,610 | JavaScript | An agent skill for creating detailed, interactive isometric illustrations of rea... |
| [storytold/gridcraft](https://github.com/storytold/gridcraft) | 3,935 | Rust | GridCraft: an open-source, clean-room spreadsheet (Microsoft Excel-style) in pur... |
| [mhtsec/ARTEX](https://github.com/mhtsec/ARTEX) | 3,657 | Go | AI 自主渗透测试系统 | 百度“agent+”攻防挑战赛冠军项目 |
| [storytold/cadcraft](https://github.com/storytold/cadcraft) | 3,582 | Rust | CADCraft: computer-aided design and drafting — an open-source, clean-room AutoCA... |

### Hacker News Top Stories (Last Updated: 2026-10-13 04:43:09 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [The baffling intelligence of a single cell (2024)](https://jsomers.net/e-coli-chemotaxis/) | 148 | [14 comments](https://news.ycombinator.com/item?id=50041866) |
| [GLM-Legal](https://z.ai/blog/glm-legal) | 483 | [279 comments](https://news.ycombinator.com/item?id=50058507) |
| [AI Models Can Provably Hide Arbitrary Capabilities](https://arxiv.org/abs/2610.13928) | 42 | [22 comments](https://news.ycombinator.com/item?id=50065692) |
| [Intel D270 GPU AI Accelerator–Up to 480 GB LPDDR5X](https://www.intel.com/content/www/us/en/products/details/discrete-gpus/data-center-gpu/d-series.html) | 125 | [47 comments](https://news.ycombinator.com/item?id=50063365) |
| [A Modern Web App in C](https://prophitt.me/writing/a-modern-web-app-in-c) | 456 | [181 comments](https://news.ycombinator.com/item?id=50058528) |
| [Who is vfmaddrnd231pd?](https://purplesyringa.moe/blog/who-is-vfmaddrnd231pd/) | 148 | [15 comments](https://news.ycombinator.com/item?id=50063138) |
| [Hackers activate automatic defrosting in supermarket fridges across Europe](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) | 515 | [708 comments](https://news.ycombinator.com/item?id=50055304) |
| [A look at OpenAI’s math that’s claimed computes faster Fourier transforms](https://www.argmin.net/p/faster-fourier-transforms) | 54 | [35 comments](https://news.ycombinator.com/item?id=50065932) |
| [Making big downloads resumable in Firefox](https://lunarwatcher.codeberg.page/til/firefox/resumable-big-downloads.html) | 134 | [43 comments](https://news.ycombinator.com/item?id=50061791) |
| [Janas: Run LLMs larger than RAM by streaming experts from SSD](https://github.com/prabanta-dev/janas) | 69 | [26 comments](https://news.ycombinator.com/item?id=50063717) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 11.0°C (51.0°F) |
| Average Humidity | 57% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-13 04:43:09 UTC*
