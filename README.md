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

### GitHub Trending Repositories (Last Updated: 2026-08-25 00:44:37 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [MengTo/threeui](https://github.com/MengTo/threeui) | 3,452 | HTML | Open-source ThreeUI Community catalog with live interactive components and compl... |
| [b-nnett/grok-bot-0.18-reconstructed](https://github.com/b-nnett/grok-bot-0.18-reconstructed) | 1,726 | TypeScript | Unofficial source-oriented reconstruction and extension of Grok Bot 0.18.0 for m... |
| [duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server) | 1,224 | Zig | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg tha... |
| [tobi/walgit](https://github.com/tobi/walgit) | 1,050 | Rust | No description |
| [cclank/lanshu-create-ai-presenter-video](https://github.com/cclank/lanshu-create-ai-presenter-video) | 837 | Python | Provider-neutral Codex Skill for producing verified AI presenter videos from a s... |

### Hacker News Top Stories (Last Updated: 2026-08-25 00:44:37 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [iCloud+ Hide My Email addresses will remain on icloud.com](https://developer.apple.com/news/?id=1ptvdtcm) | 180 | [36 comments](https://news.ycombinator.com/item?id=49426564) |
| [Xiaomi: New CPU matches Apple cores single threaded, much faster multithreaded](https://twitter.com/lemire/status/2091894299289874926) | 713 | [476 comments](https://news.ycombinator.com/item?id=49420873) |
| [Moon (2024)](https://ciechanow.ski/moon/) | 82 | [13 comments](https://news.ycombinator.com/item?id=49426466) |
| [MS Paint and Photos inivisibly watermark even locally generated output with GUID](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) | 540 | [218 comments](https://news.ycombinator.com/item?id=49421158) |
| [The entire city of San Francisco as a video game](https://sf.thijs.gg/) | 323 | [113 comments](https://news.ycombinator.com/item?id=49422784) |
| [One corner of China’s internet is insisting that the Tang Dynasty never existed](https://www.cnn.com/2026/08/19/style/china-tang-dynasty-never-existed-hoax-intl-hnk) | 115 | [88 comments](https://news.ycombinator.com/item?id=49425819) |
| [How Europe is killing makers and micro-entrepreneurs](https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs) | 1035 | [649 comments](https://news.ycombinator.com/item?id=49419237) |
| [Bookshelf – Self-hosted eBook library that runs on object storage](https://github.com/murerkinn/bookshelf) | 20 | [3 comments](https://news.ycombinator.com/item?id=49427001) |
| [Where did all the public bathrooms go?](https://daily.jstor.org/where-did-all-the-public-bathrooms-go/) | 137 | [283 comments](https://news.ycombinator.com/item?id=49422800) |
| [Jabber/XMPP: 25 Years of Digital Independence](https://gultsch.de/posts/25-years-of-digital-independence/) | 162 | [63 comments](https://news.ycombinator.com/item?id=49421536) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 25.0°C (77.0°F) |
| Average Humidity | 66% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-25 00:44:37 UTC*
