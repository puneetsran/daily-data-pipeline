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

### GitHub Trending Repositories (Last Updated: 2026-10-22 02:37:28 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | 19,700 | Java | Debloat any Android or Google TV over Wi-Fi and get an Apple TV-style home. |
| [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | 18,170 | Python | DeepInfer: High-performance, large-scale inference framework for DeepSeek models |
| [ly05010419/MacNativeGames](https://github.com/ly05010419/MacNativeGames) | 3,939 | C | No description |
| [simbasjungles/free-my-tv](https://github.com/simbasjungles/free-my-tv) | 2,778 | Java | A fast, ad-free home screen for Google TV. Open source, built with Claude Code. ... |
| [pengchujin/aerial-tv](https://github.com/pengchujin/aerial-tv) | 2,228 | Kotlin | 给国产电视的一块干净桌面：参照 tvOS 设计的开源 Android TV 桌面，没有广告，开机自动接管。A tvOS-style launcher for X... |

### Hacker News Top Stories (Last Updated: 2026-10-22 02:37:28 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [mitmproxy adds --emudhra option](https://github.com/mitmproxy/mitmproxy/commit/169234499088fc2c414644a67efaed3d64ae2e3b) | 236 | [63 comments](https://news.ycombinator.com/item?id=50189232) |
| [There isn't an easy exploit for this PHP vulnerability](https://eliastaylor.com/noexploit/) | 191 | [89 comments](https://news.ycombinator.com/item?id=50188948) |
| [Security Disclosure](https://blog.railway.com/p/security-disclosure-wednesday-october-21st) | 328 | [172 comments](https://news.ycombinator.com/item?id=50188228) |
| [GitLab Critical Patch Release](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/) | 258 | [64 comments](https://news.ycombinator.com/item?id=50185869) |
| [Rust Style Guide](https://google.github.io/styleguide/rustguide.html) | 222 | [121 comments](https://news.ycombinator.com/item?id=50186010) |
| [LLM Agents Play Pokemon Showdown](https://olivergrabner.com/research/pokemon/) | 9 | [1 comments](https://news.ycombinator.com/item?id=50190334) |
| [Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/) | 447 | [150 comments](https://news.ycombinator.com/item?id=50181114) |
| [No more icons in every menu by default](https://blog.jim-nielsen.com/2026/icons-in-every-menu/) | 195 | [133 comments](https://news.ycombinator.com/item?id=50161346) |
| [Chain of Thought for Humans](https://www.boristhebrave.com/2026/10/18/chain-of-thought-for-humans/) | 37 | [13 comments](https://news.ycombinator.com/item?id=50154100) |
| [Epic vs. Apple AU:Court Orders Alt App Stores,Sideloading and 3rd Party Payments](https://www.judgments.fedcourt.gov.au/judgments/Judgments/fca/single/2026/2026fca1552) | 6 | [1 comments](https://news.ycombinator.com/item?id=50190168) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 12.0°C (54.0°F) |
| Average Humidity | 70% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-22 02:37:28 UTC*
