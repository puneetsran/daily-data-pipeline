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

### GitHub Trending Repositories (Last Updated: 2026-07-03 02:06:11 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [Krishnagangwal/CS-Fundamentals](https://github.com/Krishnagangwal/CS-Fundamentals) | 1,437 | N/A | Curated CS fundamentals for placement prep: DSA,Computer Networks, DBMS & SQL, O... |
| [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | 1,117 | JavaScript | Standalone iOS app to spoof GPS location without jailbreak. Includes Shadowrocke... |
| [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | 1,112 | Python | No description |
| [Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills) | 897 | N/A | A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): re... |
| [TianhangZhuzth/Fundamental-Ava](https://github.com/TianhangZhuzth/Fundamental-Ava) | 754 | Python | Build digital human beings — autonomous, collaborative, and socially intelligent... |

### Hacker News Top Stories (Last Updated: 2026-07-03 02:06:11 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Virginia bans sale of geolocation data](https://www.hunton.com/privacy-and-cybersecurity-law-blog/virginia-bans-sale-of-geolocation-data) | 492 | [89 comments](https://news.ycombinator.com/item?id=48767347) |
| [An American Privacy Emergency](https://scottaaronson.blog/?p=9902) | 138 | [36 comments](https://news.ycombinator.com/item?id=48768992) |
| [crustc: entirety of `rustc`, translated to C](https://github.com/FractalFir/crustc) | 132 | [27 comments](https://news.ycombinator.com/item?id=48768464) |
| [GitHub is proud to announce that you can now obtain your public repo on CD-ROM](https://forms.cloud.microsoft/pages/responsepage.aspx?id=v4j5cvGGr0GRqy180BHbR6G-c11n8yFDlQmk4B-QjDxUQkdTTjZLU0EyTFFRV1E3NVRTVTRTWjRHMy4u&route=shorturl) | 59 | [41 comments](https://news.ycombinator.com/item?id=48768997) |
| [Reality has a surprising amount of detail (2017)](https://johnsalvatier.org/blog/2017/reality-has-a-surprising-amount-of-detail) | 141 | [48 comments](https://news.ycombinator.com/item?id=48702874) |
| [Exapunks (2018)](https://www.zachtronics.com/exapunks/) | 219 | [80 comments](https://news.ycombinator.com/item?id=48765663) |
| [Since Linux 6.9, LUKS suspend stopped wiping disk-encryption keys from memory](https://mathstodon.xyz/@iblech/116769502749142438) | 404 | [190 comments](https://news.ycombinator.com/item?id=48763035) |
| [Right to Local Intelligence](https://righttointelligence.org/) | 29 | [11 comments](https://news.ycombinator.com/item?id=48768951) |
| [Mystery identity of 'Green Boots' climber is finally solved after DNA test](https://www.dailymail.com/news/article-15943905/Mystery-identity-Green-Boots-climber-macabre-landmark-frozen-ice-dying-Everest-finally-solved-DNA-test.html) | 52 | [22 comments](https://news.ycombinator.com/item?id=48768336) |
| [Podman v6.0.0](https://blog.podman.io/2026/07/introducing-podman-v6-0-0/) | 396 | [156 comments](https://news.ycombinator.com/item?id=48762098) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 14.0°C (58.0°F) |
| Average Humidity | 100% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-03 02:06:11 UTC*
