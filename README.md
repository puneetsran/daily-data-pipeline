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

### GitHub Trending Repositories (Last Updated: 2026-07-10 02:05:23 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [x4gKing/X4G](https://github.com/x4gKing/X4G) | 3,407 | Python | No description |
| [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | 1,570 | JavaScript | Chrome extension that filters pseudo-brand junk out of Amazon. Buy from real, es... |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 1,441 | JavaScript | No description |
| [ammaarreshi/Generals-Mac-iOS-iPad](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad) | 1,393 | C++ | Command & Conquer Generals: Zero Hour running natively on macOS, iPhone & iPad —... |
| [MaximeRivest/riddle](https://github.com/MaximeRivest/riddle) | 1,285 | Rust | The diary of Tom Riddle for the reMarkable Paper Pro — write with your pen, the ... |

### Hacker News Top Stories (Last Updated: 2026-07-10 02:05:23 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Show HN: Getting GLM 5.2 running on my slow computer](https://github.com/JustVugg/colibri) | 390 | [101 comments](https://news.ycombinator.com/item?id=48842459) |
| [EU Parliament greenlights Chat Control 1.0](https://www.patrick-breyer.de/en/eu-parliament-greenlights-chat-control-1-0-breyer-our-children-lose-out/) | 1002 | [480 comments](https://news.ycombinator.com/item?id=48843923) |
| [GPT-5.6](https://openai.com/index/gpt-5-6/) | 1073 | [782 comments](https://news.ycombinator.com/item?id=48849066) |
| [Show HN: 18 Words](https://18words.com/) | 833 | [284 comments](https://news.ycombinator.com/item?id=48845049) |
| [Star Just Ate a Planet, and It's Not Done Yet](https://www.nytimes.com/2026/07/09/science/space/planetary-engulfment-hungry-star.html) | 8 | [3 comments](https://news.ycombinator.com/item?id=48854638) |
| [Train sim created by just one person is being called the best ever made](https://kotaku.com/a-train-sim-created-by-just-one-person-is-being-called-the-best-ever-made-2000699429) | 293 | [114 comments](https://news.ycombinator.com/item?id=48792383) |
| [Focus](https://boz.com/articles/focus) | 13 | [1 comments](https://news.ycombinator.com/item?id=48854363) |
| [Interview with Mitchell Hashimoto about Ghostty and Zig](https://alexalejandre.com/programming/interview-with-mitchell-hashimoto/) | 126 | [49 comments](https://news.ycombinator.com/item?id=48849292) |
| [My Story of 3D Realms / Apogee Part I (2020)](https://joesiegler.blog/2020/11/my-story-of-apogee-3dr/) | 32 | [0 comments](https://news.ycombinator.com/item?id=48757291) |
| [Hy3](https://hy.tencent.com/research/hy3) | 389 | [86 comments](https://news.ycombinator.com/item?id=48847552) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 22.0°C (72.0°F) |
| Average Humidity | 46% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-10 02:05:23 UTC*
