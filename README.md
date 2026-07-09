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

### GitHub Trending Repositories (Last Updated: 2026-07-09 02:06:17 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [x4gKing/X4G](https://github.com/x4gKing/X4G) | 2,480 | Python | No description |
| [synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience) | 1,766 | TypeScript | The open-source AI workbench for scientific research |
| [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | 1,414 | JavaScript | Chrome extension that filters pseudo-brand junk out of Amazon. Buy from real, es... |
| [ammaarreshi/Generals-Mac-iOS-iPad](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad) | 1,363 | C++ | Command & Conquer Generals: Zero Hour running natively on macOS, iPhone & iPad —... |
| [jamesob/local-llm](https://github.com/jamesob/local-llm) | 1,276 | Shell | Everything I know about running LLMs locally |

### Hacker News Top Stories (Last Updated: 2026-07-09 02:06:17 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [John Deere owners will get the right to repair equipment under FTC settlement](https://apnews.com/article/john-deere-right-to-repair-agriculture-equipment-cb7514ffedb95c130a976af661f2bc02) | 308 | [63 comments](https://news.ycombinator.com/item?id=48838876) |
| [A software engineering interview question I like: computing the median](https://krisshamloo.com/blog/007) | 34 | [22 comments](https://news.ycombinator.com/item?id=48839434) |
| [Separating signal from noise in coding evaluations](https://openai.com/index/separating-signal-from-noise-coding-evaluations/) | 161 | [61 comments](https://news.ycombinator.com/item?id=48837396) |
| [Chatto is now open source](https://www.hmans.dev/blog/chatto-is-open-source) | 743 | [196 comments](https://news.ycombinator.com/item?id=48833116) |
| [I Think I Have LLM Burnout](https://www.alecscollon.com/blog/llm-burnout/) | 9 | [1 comments](https://news.ycombinator.com/item?id=48839984) |
| [Remote Attestation](https://www.liamcvw.com/p/remote-attestation) | 23 | [11 comments](https://news.ycombinator.com/item?id=48839397) |
| [Mistral's Robostral Navigate: a state of the art robotics navigation model](https://mistral.ai/news/robostral-navigate/) | 417 | [96 comments](https://news.ycombinator.com/item?id=48832212) |
| [Unicode's transliteration rules are Turing-complete](https://seriot.ch/computation/uts35/) | 39 | [8 comments](https://news.ycombinator.com/item?id=48829797) |
| [Show HN: Microsoft releases Flint, a visualization language for AI agents](https://microsoft.github.io/flint-chart/#/) | 207 | [76 comments](https://news.ycombinator.com/item?id=48834924) |
| [Patching MechCommander's "left arm bug" for fun and profit](https://mhloppy.com/2026/05/mechcommander-weapons-left-arm-bug-fix/) | 10 | [1 comments](https://news.ycombinator.com/item?id=48795591) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 20.0°C (68.0°F) |
| Average Humidity | 51% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-09 02:06:17 UTC*
