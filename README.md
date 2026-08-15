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

### GitHub Trending Repositories (Last Updated: 2026-08-15 00:44:05 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 95,708 | TypeScript | DeepSeek Harness: Everything is a Plugin. |
| [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | 8,172 | Python | Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrit... |
| [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | 1,946 | TypeScript | Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git g... |
| [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | 1,899 | TypeScript | 为 DeepSeek Harness (DSH) 生态打造的现代化桌面端体验 |
| [antirez/h3.c](https://github.com/antirez/h3.c) | 1,851 | C | MiniMax H3 inference engine for Mac computers |

### Hacker News Top Stories (Last Updated: 2026-08-15 00:44:05 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Qwen 3.8 27B](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) | 867 | [568 comments](https://news.ycombinator.com/item?id=49299605) |
| [Going Dark, and the era of law enforcement hacking](https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/) | 166 | [107 comments](https://news.ycombinator.com/item?id=49304447) |
| [RISC-V: They should have known better](https://dmitry.gr/?r=06.%20Thoughts&proj=12.%20RV) | 95 | [50 comments](https://news.ycombinator.com/item?id=49305492) |
| [The case for overhauling American science](https://www.economist.com/by-invitation/2026/08/13/the-case-for-overhauling-american-science) | 19 | [10 comments](https://news.ycombinator.com/item?id=49305708) |
| [Why does Opus 5 feel worse to work with?](https://mun-logadan.github.io/why-does-opus-5-feel-worse/) | 762 | [696 comments](https://news.ycombinator.com/item?id=49296740) |
| [Google is making private AI practical with homomorphic encryption](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/) | 267 | [162 comments](https://news.ycombinator.com/item?id=49300314) |
| [RustDesk now supports true unattended remote access on Wayland](https://rustdesk.com/blog/unattended-remote-access-wayland/) | 213 | [93 comments](https://news.ycombinator.com/item?id=49300759) |
| [Super Mario Derivations](https://fzakaria.com/2026/08/05/super-mario-derivations) | 42 | [5 comments](https://news.ycombinator.com/item?id=49215682) |
| [Stop sending me huge PRs; a rant](https://getsmall.xyz/post/cmstjfl9l000if70ljmpzr4va) | 30 | [19 comments](https://news.ycombinator.com/item?id=49305558) |
| [Jane Street suffers $15B hit after meltdown at Situational Awareness](https://www.ft.com/content/47dd5308-dd17-404a-a615-61046defd697) | 50 | [10 comments](https://news.ycombinator.com/item?id=49305927) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 27.0°C (81.0°F) |
| Average Humidity | 56% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-15 00:44:05 UTC*
