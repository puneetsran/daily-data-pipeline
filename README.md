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

### GitHub Trending Repositories (Last Updated: 2026-10-15 02:30:40 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [storytold/craft-launcher](https://github.com/storytold/craft-launcher) | 2,668 | Rust | The Craft App Launcher |
| [liseami/CCBaga](https://github.com/liseami/CCBaga) | 2,260 | Rust | No description |
| [jhaizhou-ops/d2r-mobile](https://github.com/jhaizhou-ops/d2r-mobile) | 2,227 | C | Open-source iOS / macOS compatibility layer for Diablo II: Resurrected with the ... |
| [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) | 2,113 | C | Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, ... |
| [Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill) | 1,283 | Python | Qwen-Image 2.1 NSFW/姿势出图 skill：作者级提示词配方 + NSFW LoRA + 136 姿势 VNCCS 人偶控制；适用 Claud... |

### Hacker News Top Stories (Last Updated: 2026-10-15 02:30:40 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Things to know when you get cancer](https://jjmaxwell4.com/writing/things-to-know-when-you-get-cancer/) | 844 | [211 comments](https://news.ycombinator.com/item?id=50093568) |
| [OpenCode 2.0](https://anoma.ly/notes/opencode-2-0/) | 338 | [138 comments](https://news.ycombinator.com/item?id=50094994) |
| [Tiny Little Office](https://tinylittleoffice.com/) | 161 | [24 comments](https://news.ycombinator.com/item?id=50096142) |
| [LFM2.5-24B-A2B: Built for fast on-device agents](https://www.liquid.ai/blog/lfm2-5-24b-a2b) | 85 | [19 comments](https://news.ycombinator.com/item?id=50097369) |
| [We’re releasing Jev 1.14.0 along with experimental features for dreamers](https://typesafe.ai/blog/jev-1-14) | 202 | [62 comments](https://news.ycombinator.com/item?id=50095353) |
| [Do dentists know what they're doing?](https://mapwriting.substack.com/p/dentists) | 451 | [335 comments](https://news.ycombinator.com/item?id=50050553) |
| [The Double Headed Stack Allocator](https://blog.demofox.org/2026/10/03/the-double-headed-stack-allocator/) | 6 | [0 comments](https://news.ycombinator.com/item?id=50098274) |
| [Americans' social activity has steeply declined in the past 30 years](https://www.dataforprogress.org/blog/2026/9/29/americans-social-activity-has-steeply-declined-in-the-past-30-years) | 247 | [269 comments](https://news.ycombinator.com/item?id=50089921) |
| [Better HTTP/1 connection reuse in Go 1.27](https://go.dev/blog/http-connection-reuse) | 206 | [30 comments](https://news.ycombinator.com/item?id=50090369) |
| [your C is not standard C](https://sebsite.pw/w/20261012-notstdc.html) | 30 | [8 comments](https://news.ycombinator.com/item?id=50071546) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 13.0°C (55.0°F) |
| Average Humidity | 82% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-15 02:30:40 UTC*
