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

### GitHub Trending Repositories (Last Updated: 2026-08-27 05:57:18 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [MengTo/threeui](https://github.com/MengTo/threeui) | 4,226 | HTML | Open-source ThreeUI Community catalog with live interactive components and compl... |
| [b-nnett/grok-bot-0.18-reconstructed](https://github.com/b-nnett/grok-bot-0.18-reconstructed) | 3,148 | TypeScript | Unofficial source-oriented reconstruction and extension of Grok Bot 0.18.0 for m... |
| [tobi/walgit](https://github.com/tobi/walgit) | 2,099 | Rust | No description |
| [duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server) | 1,479 | Zig | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg tha... |
| [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft) | 1,031 | JavaScript | Claude Code skill for premium scroll-driven websites. Scroll becomes the timelin... |

### Hacker News Top Stories (Last Updated: 2026-08-27 05:57:18 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Nvidia agrees to acquire Hugging Face for $13B](https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8) | 702 | [290 comments](https://news.ycombinator.com/item?id=49458161) |
| [CEO fired developers to make room for AI. Developers create open source AI CEO](https://github.com/SenteLabsAI/OpenExecutive) | 332 | [199 comments](https://news.ycombinator.com/item?id=49458418) |
| [Mechanical Turk shutting down September 30](https://www.mturk.com/) | 252 | [79 comments](https://news.ycombinator.com/item?id=49457545) |
| [GLM-5.3-Flash](https://z.ai/blog/glm-5.3-flash) | 958 | [482 comments](https://news.ycombinator.com/item?id=49449507) |
| [Kusama Yayoi Dies at 97](https://news.jp/i/1465528042000662661) | 109 | [9 comments](https://news.ycombinator.com/item?id=49458709) |
| [Asahi Linux Progress Report: Linux 7.2](https://asahilinux.org/2026/08/progress-report-7-2/) | 177 | [46 comments](https://news.ycombinator.com/item?id=49456851) |
| [Tailcat – Like netcat, but over Tailscale’s data plane](https://github.com/tailscale/tailcat) | 525 | [96 comments](https://news.ycombinator.com/item?id=49452990) |
| [Worst-case glacial lake flood scenarios in a transboundary Himalayan basin 2022](https://nhess.copernicus.org/articles/22/3765/2022/nhess-22-3765-2022.html) | 117 | [53 comments](https://news.ycombinator.com/item?id=49456929) |
| [Laion Big Video Dataset](https://projects.laion.ai/bvd/) | 37 | [6 comments](https://news.ycombinator.com/item?id=49458478) |
| [An ongoing 3D-printer AGPL violation](https://lwn.net/SubscriberLink/1089390/46116614cc74b814/) | 363 | [161 comments](https://news.ycombinator.com/item?id=49452980) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 17.0°C (63.0°F) |
| Average Humidity | 76% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-27 05:57:18 UTC*
