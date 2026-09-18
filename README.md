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

### GitHub Trending Repositories (Last Updated: 2026-09-18 02:24:26 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 2,377 | Python | No description |
| [Chuloo/mural](https://github.com/Chuloo/mural) | 1,322 | Kotlin | The language app you eventually delete. A native iPhone companion for learning t... |
| [yifanzhang-pro/recurrent-looped-tranformer](https://github.com/yifanzhang-pro/recurrent-looped-tranformer) | 873 | HTML | Official Project Page for Recurrent Looped Transformer (RLT) |
| [TheoLeeCJ/openjev](https://github.com/TheoLeeCJ/openjev) | 854 | Python | Can we run something like Jev on a 3090 at home? |
| [zjwzcx/Awesome-Astra-Embodied-AI](https://github.com/zjwzcx/Awesome-Astra-Embodied-AI) | 825 | N/A | GPT-6 Astra for embodied AI and robotics. |

### Hacker News Top Stories (Last Updated: 2026-09-18 02:24:26 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Astra for Law](https://openai.com/index/astra-for-law/) | 330 | [362 comments](https://news.ycombinator.com/item?id=49745940) |
| [Bonsai 2 27B: Near-Lossless Compression in a 9x Smaller Footprint](https://prismml.com/news/bonsai-2-27b) | 247 | [75 comments](https://news.ycombinator.com/item?id=49746618) |
| [Bend – A language that blocks AI mistakes via proof, on CPU and GPU](https://bend-lang.com/) | 302 | [155 comments](https://news.ycombinator.com/item?id=49746163) |
| [Goose: 1.16x faster than C++ and 1.12x than safe Rust, while memory safe](https://github.com/aardappel/goose/tree/master) | 31 | [27 comments](https://news.ycombinator.com/item?id=49748954) |
| [Hister: A private search engine for the pages you visit and the files you keep](https://github.com/asciimoo/hister) | 478 | [137 comments](https://news.ycombinator.com/item?id=49743097) |
| [Wax motor](https://en.wikipedia.org/wiki/Wax_motor) | 252 | [50 comments](https://news.ycombinator.com/item?id=49726007) |
| [Fujitsu launches made-in-Japan next-generation CPU FUJITSU-MONAKA](https://global.fujitsu/en-global/pr/news/2026/09/14-02) | 520 | [198 comments](https://news.ycombinator.com/item?id=49715813) |
| [Alibaba releases Qwen 3.8 Omni Flash](https://qwen.ai/blog?id=qwen3.8-omni-flash) | 34 | [5 comments](https://news.ycombinator.com/item?id=49747925) |
| [Telstra outage: The night a network decided the year was 2006](https://www.netnod.se/blog/telstra-outage-night-network-decided-year-was-2006) | 12 | [3 comments](https://news.ycombinator.com/item?id=49748957) |
| [Flet 1.0 – Build cross-platform apps in Python](https://flet.dev/) | 64 | [34 comments](https://news.ycombinator.com/item?id=49746290) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 16.0°C (62.0°F) |
| Average Humidity | 73% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-18 02:24:26 UTC*
