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

### GitHub Trending Repositories (Last Updated: 2026-08-16 00:46:16 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 115,398 | TypeScript | DeepSeek Harness: Everything is a Plugin. |
| [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | 9,745 | Python | Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrit... |
| [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | 5,893 | TypeScript | 为 DeepSeek Harness (DSH) 生态打造的现代化桌面端体验 |
| [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | 3,004 | Python | A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表 |
| [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | 2,713 | TypeScript | Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git g... |

### Hacker News Top Stories (Last Updated: 2026-08-16 00:46:16 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Semaglutide linked to lower predicted dementia risk](https://alz-journals.onlinelibrary.wiley.com/doi/10.1002/dad2.70432) | 336 | [234 comments](https://news.ycombinator.com/item?id=49311651) |
| [Cultivating a state of mind where new ideas are born (2023)](https://www.henrikkarlsson.xyz/p/good-ideas) | 68 | [17 comments](https://news.ycombinator.com/item?id=49314235) |
| [Abdominal fat predicts heart disease risk better than BMI](https://www.acc.org/about-acc/press-releases/2026/08/11/14/59/abdominal-fat-predicts-heart-disease-risk-better-than-bmi) | 129 | [91 comments](https://news.ycombinator.com/item?id=49314403) |
| [AI in drug discovery – what it is, where we stand and the path forward](https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really) | 79 | [41 comments](https://news.ycombinator.com/item?id=49313367) |
| [At-home test for infected ticks could improve Lyme Disease diagnosis](https://www.smithsonianmag.com/innovation/the-first-at-home-test-for-infected-ticks-could-improve-lyme-disease-diagnosis-180989235/) | 207 | [71 comments](https://news.ycombinator.com/item?id=49310682) |
| [SugarTrack – an offline Android logbook for blood sugar (no account, no cloud)](https://sugartrack-beta.vercel.app/) | 14 | [3 comments](https://news.ycombinator.com/item?id=49314884) |
| [AI has access to a vastly larger working memory than the human brain](https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians) | 395 | [349 comments](https://news.ycombinator.com/item?id=49312845) |
| [RISC-V: They Should Have Known Better](https://dmitry.gr/?r=06.%20Thoughts&proj=12.%20RV) | 219 | [288 comments](https://news.ycombinator.com/item?id=49298035) |
| [Auto-research with codex: How I achieved a 232x Faster Kernel](https://sankalp.bearblog.dev/autoresearch/) | 388 | [86 comments](https://news.ycombinator.com/item?id=49309549) |
| [Tracking down a Zsh history data loss bug](https://michael.stapelberg.ch/posts/2026-08-09-zsh-history-truncation-bug/) | 25 | [3 comments](https://news.ycombinator.com/item?id=49314579) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 21.0°C (69.0°F) |
| Average Humidity | 67% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-16 00:46:16 UTC*
