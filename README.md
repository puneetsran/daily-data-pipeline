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

### GitHub Trending Repositories (Last Updated: 2026-10-25 02:27:55 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [openai/math](https://github.com/openai/math) | 14,133 | Lean | No description |
| [storytold/wordcraft](https://github.com/storytold/wordcraft) | 6,308 | Rust | An open-source, clean-room reimplementation of Microsoft Word in pure Rust |
| [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | 3,660 | JavaScript | An agent skill for creating detailed, interactive isometric illustrations of rea... |
| [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 3,415 | JavaScript | 艺术动画skill：35种艺术风格、9种解说语法，用代码让画动起来。 |
| [mhtsec/ARTEX](https://github.com/mhtsec/ARTEX) | 3,255 | Go | AI 自主渗透测试系统 | 百度“agent+”攻防挑战赛冠军项目 |

### Hacker News Top Stories (Last Updated: 2026-10-25 02:27:55 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Listen and read USA nuclear forces Emergency Action Messages, heard on 11175 kHz](https://missileer.watch) | 124 | [80 comments](https://news.ycombinator.com/item?id=50224422) |
| [The Goose Programming Language](https://aardappel.github.io/goose/) | 251 | [171 comments](https://news.ycombinator.com/item?id=50224100) |
| [America has lost 200k of jobs in media, film and the arts. How much is AI?](https://www.apricitas.io/p/ai-and-the-fall-of-the-creative-class) | 185 | [154 comments](https://news.ycombinator.com/item?id=50226419) |
| [We should be more ambitious with the software we build](https://danluu.com/ambitious/) | 192 | [154 comments](https://news.ycombinator.com/item?id=50225695) |
| [Why Gopher in 2026?](https://gopher.muffinlabs.com/sdf.org/users/nervtoji/phlog/001.txt) | 30 | [8 comments](https://news.ycombinator.com/item?id=50226577) |
| [Small Programs and Languages](https://ratfactor.com/cards/pl-small) | 46 | [2 comments](https://news.ycombinator.com/item?id=50225674) |
| [FindMyWeb: Apple Find My, reverse enginiered](https://codeberg.org/Misom/FindMyWeb) | 21 | [5 comments](https://news.ycombinator.com/item?id=50226646) |
| [SpeedCrunch 1.1](https://www.speedcrunch.org/) | 80 | [10 comments](https://news.ycombinator.com/item?id=50224210) |
| [Reactive Optimizers: rewrite the optimizer's source code during training](https://xingjianbai.com/reactive-optimizers/) | 10 | [1 comments](https://news.ycombinator.com/item?id=50188440) |
| [I Built a Stereo Vision Board for Hardware Hackers](https://rootkitlabs.com/2026/10/06/i-built-a-stereo-vision-board-for-hardware-hackers/) | 37 | [0 comments](https://news.ycombinator.com/item?id=50172432) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 8.0°C (47.0°F) |
| Average Humidity | 83% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-25 02:27:55 UTC*
