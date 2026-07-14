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

### GitHub Trending Repositories (Last Updated: 2026-07-14 01:43:55 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 2,923 | JavaScript | No description |
| [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | 1,033 | Python | Infinite Worlds with Versatile Interactions |
| [x4gKing/3x-ui-Upgrade](https://github.com/x4gKing/3x-ui-Upgrade) | 959 | HTML | No description |
| [vinhhien112/Three.js-Object-Sculptor-Codex-Plugin](https://github.com/vinhhien112/Three.js-Object-Sculptor-Codex-Plugin) | 859 | Python | Codex plugin that turns attached object images into code-only, animation-ready p... |
| [Robbyant/lingbot-video](https://github.com/Robbyant/lingbot-video) | 758 | Python | Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence |

### Hacker News Top Stories (Last Updated: 2026-07-14 01:43:55 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [The Git history command deserves more attention](https://lalitm.com/post/git-history/) | 21 | [3 comments](https://news.ycombinator.com/item?id=48901010) |
| [Building and shipping Mac and iOS apps without opening Xcode](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/) | 309 | [134 comments](https://news.ycombinator.com/item?id=48896665) |
| [Apple's new SpeechAnalyzer API, benchmarked against Whisper and its predecessor](https://get-inscribe.com/blog/apple-speech-api-benchmark.html) | 449 | [180 comments](https://news.ycombinator.com/item?id=48894752) |
| [An Englishwoman who sketched India before photography took hold](https://www.bbc.com/news/articles/cm2drrv6q54o) | 47 | [7 comments](https://news.ycombinator.com/item?id=48900191) |
| [MorphoHDL: A minimalistic language for growing circuits](https://paradigms-of-intelligence.github.io/morpho/) | 8 | [0 comments](https://news.ycombinator.com/item?id=48901126) |
| [Success may not matter if you aren't doing what you love](https://12gramsofcarbon.com/p/founders-guide-success-may-not-matter) | 9 | [0 comments](https://news.ycombinator.com/item?id=48900790) |
| [ESBMC-Arduino: Closing the Deployment Gap for Formal Verification](https://arxiv.org/abs/2607.08550) | 4 | [0 comments](https://news.ycombinator.com/item?id=48901020) |
| [The infinite scroll may become endangered if controversial Calif. law passes](https://www.sfgate.com/politics/article/meta-social-media-teenagers-22337724.php) | 75 | [129 comments](https://news.ycombinator.com/item?id=48897104) |
| [The art and engineering of Sega CD Silpheed](https://fabiensanglard.net/silpheed/index.html) | 222 | [46 comments](https://news.ycombinator.com/item?id=48893639) |
| [Show HN: YouTube Guitar Tab Parser](https://github.com/marcelpanse/youtube-guitar-tab-parser) | 70 | [47 comments](https://news.ycombinator.com/item?id=48898154) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 24.0°C (75.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-14 01:43:55 UTC*
