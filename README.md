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

### GitHub Trending Repositories (Last Updated: 2026-09-16 02:32:55 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [Chuloo/mural](https://github.com/Chuloo/mural) | 1,054 | Kotlin | The language app you eventually delete. A native iPhone companion for learning t... |
| [sumimakito/Mac-Duo](https://github.com/sumimakito/Mac-Duo) | 914 | Swift | Wish you could bring the iPhone Duo effect to your MacBook? |
| [yifanzhang-pro/recurrent-looped-tranformer](https://github.com/yifanzhang-pro/recurrent-looped-tranformer) | 830 | HTML | Official Project Page for Recurrent Looped Transformer (RLT) |
| [kruzovic7/ai-data-extractor](https://github.com/kruzovic7/ai-data-extractor) | 822 | Python | Free open-source extractor for AI coding assistant chat histories. Supports Clau... |
| [ai-sucks-butt/ai-sucks-butt](https://github.com/ai-sucks-butt/ai-sucks-butt) | 812 | N/A | If you think AI sucks, star the repo. |

### Hacker News Top Stories (Last Updated: 2026-09-16 02:32:55 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | 825 | [273 comments](https://news.ycombinator.com/item?id=49717558) |
| [Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations](https://github.com/arnegiacomo/fugleramme) | 1348 | [183 comments](https://news.ycombinator.com/item?id=49711544) |
| [An Update on Wayback Machine Access](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) | 403 | [218 comments](https://news.ycombinator.com/item?id=49716176) |
| [Gemini 3.8 Live and 3.8 Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) | 320 | [195 comments](https://news.ycombinator.com/item?id=49715947) |
| [German Rheinmetall open-sources its Battlesuite connected weapon system protcol](https://rheinmetall.github.io/onboardapi-documentation/9.10.0/index.html) | 135 | [41 comments](https://news.ycombinator.com/item?id=49718928) |
| [Cloudflare: Stay discoverable in search while disallowing AI training](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/) | 4 | [0 comments](https://news.ycombinator.com/item?id=49721435) |
| [We got admin access to Baseten's production GitHub in 25 minutes](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) | 227 | [121 comments](https://news.ycombinator.com/item?id=49716476) |
| [Recreating Voodoo Graphics and a Late-1990s Gaming PC on an FPGA](https://nand2mario.github.io/posts/2026/zsst-voodoo/) | 42 | [9 comments](https://news.ycombinator.com/item?id=49719938) |
| [Sierra digital cameras on the Apple II](https://www.colino.net/wordpress/archives/2026/09/11/sierra-digital-cameras-on-the-apple-ii/) | 23 | [2 comments](https://news.ycombinator.com/item?id=49680916) |
| [Building a Linux GPU Driver for the M4 Mac Mini in One Month](https://codyho.dev/blog/gpu-driver/) | 173 | [113 comments](https://news.ycombinator.com/item?id=49717638) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 15.0°C (60.0°F) |
| Average Humidity | 80% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-16 02:32:55 UTC*
