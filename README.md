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

### GitHub Trending Repositories (Last Updated: 2026-08-01 02:00:37 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | 7,724 | N/A | Open Frontier Intelligence |
| [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | 2,064 | TypeScript | No description |
| [yc-software/qm](https://github.com/yc-software/qm) | 2,015 | TypeScript | Multiplayer agent harness for work |
| [xikhar/persona](https://github.com/xikhar/persona) | 716 | JavaScript | Bringing real-time voice to life. |
| [QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent) | 612 | JavaScript | A realtime voice runtime that keeps Agents talking, working, and present.  Real-... |

### Hacker News Top Stories (Last Updated: 2026-08-01 02:00:37 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Tailscale didn't stop the Hugging Face intrusion](https://tailscale.com/blog/hugging-face-intrusion) | 463 | [173 comments](https://news.ycombinator.com/item?id=49127306) |
| [Elevators](https://john.fun/elevators) | 884 | [221 comments](https://news.ycombinator.com/item?id=49124218) |
| [qm – Multiplayer agent harness for work](https://github.com/yc-software/qm) | 465 | [99 comments](https://news.ycombinator.com/item?id=49126604) |
| [Twenty-five years ago it was cryptography, today it's model weights](https://weeraman.com/because-we-can/) | 164 | [63 comments](https://news.ycombinator.com/item?id=49083599) |
| [The Absurdity of Albert Camus](https://www.historytoday.com/archive/portrait-author-historian/absurdity-albert-camus) | 50 | [32 comments](https://news.ycombinator.com/item?id=49117089) |
| [June in Servo: real world compat, media queries, SharedWorker, and more](https://servo.org/blog/2026/07/31/june-in-servo/) | 104 | [32 comments](https://news.ycombinator.com/item?id=49126765) |
| [Progressive Web Components](https://arielsalminen.com/2026/progressive-web-components/) | 88 | [13 comments](https://news.ycombinator.com/item?id=49121196) |
| [Big Food vs. the People](https://www.lighthousereports.com/investigation/big-food-vs-the-people/) | 192 | [131 comments](https://news.ycombinator.com/item?id=49124858) |
| [Getting 25 Gbps Thunderbolt Ethernet on My Mac Studio](https://www.jeffgeerling.com/blog/2026/getting-25g-ethernet-mac-thunderbolt/) | 142 | [84 comments](https://news.ycombinator.com/item?id=49125034) |
| [Demystifying DRAM Read Disturbance: RowHammer and RowPress Phenomena](https://arxiv.org/abs/2607.28233) | 31 | [17 comments](https://news.ycombinator.com/item?id=49128323) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 28.0°C (82.0°F) |
| Average Humidity | 36% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-01 02:00:37 UTC*
