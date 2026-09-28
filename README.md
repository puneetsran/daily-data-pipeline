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

### GitHub Trending Repositories (Last Updated: 2026-09-28 02:45:39 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [Contrastive-LM/CLM](https://github.com/Contrastive-LM/CLM) | 1,942 | Python | No description |
| [tobi/disktree](https://github.com/tobi/disktree) | 1,635 | Rust | A treemap for finding and removing what fills your disk, for Omarchy. Rust + GPU... |
| [yetone/magpie](https://github.com/yetone/magpie) | 1,279 | Go | Every agent's model. One place. Codex on DeepSeek, Claude Code on Kimi, from the... |
| [JohnHeibel/PDoomVideo](https://github.com/JohnHeibel/PDoomVideo) | 1,268 | JavaScript | Source code for the Claude Opus 5.5 music video for I'm Upping My P(doom) |
| [mexicat/pdoom-video](https://github.com/mexicat/pdoom-video) | 1,202 | TypeScript | Code-rendered music video for "I'm Upping My P(doom)" |

### Hacker News Top Stories (Last Updated: 2026-09-28 02:45:39 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Self-parking car using genetic algorithm (2021)](https://trekhleb.dev/blog/2021/self-parking-car-evolution/) | 32 | [4 comments](https://news.ycombinator.com/item?id=49872472) |
| [Ember-1](https://fireworks.ai/blog/ember-1) | 368 | [186 comments](https://news.ycombinator.com/item?id=49868830) |
| [When did Google get so weird?](https://sancho.bearblog.dev/google-weird/) | 852 | [457 comments](https://news.ycombinator.com/item?id=49870367) |
| [Owed a billion dollars in Nvidia stock](https://colo.to/nvidia-stock-narrative.html) | 10 | [1 comments](https://news.ycombinator.com/item?id=49872723) |
| [Research finds 485 chemicals in US pesticide products linked to breast cancer](https://www.theguardian.com/us-news/2026/sep/26/breast-cancer-us-pesticide-products) | 42 | [10 comments](https://news.ycombinator.com/item?id=49872497) |
| [Alan Kay's answer to “Did the ENIAC have a BIOS”?](https://www.quora.com/Did-the-ENIAC-have-a-BIOS/answer/Alan-Kay-11) | 79 | [30 comments](https://news.ycombinator.com/item?id=49870070) |
| [There is more to code review than (automatable) detection](https://www.adaptivecapacitylabs.com/2026/08/24/there-is-more-to-code-review-than-automatable-detection/) | 73 | [37 comments](https://news.ycombinator.com/item?id=49857281) |
| [The state of SIMD in Rust in 2026](https://shnatsel.github.io/state-of-simd-rust-2026/) | 102 | [21 comments](https://news.ycombinator.com/item?id=49844629) |
| [Guitar amp and effects pedal built on the Waveshare ESP32-S3-Touch-AMOLED-2.06](https://github.com/dashersw/coyopedal) | 26 | [4 comments](https://news.ycombinator.com/item?id=49852600) |
| [Lunar Terminator Paradox](https://notes.secretsauce.net/notes/2026/09/27_lunar-terminator-paradox.html) | 49 | [32 comments](https://news.ycombinator.com/item?id=49870837) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 14.0°C (57.0°F) |
| Average Humidity | 61% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-28 02:45:39 UTC*
