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

### GitHub Trending Repositories (Last Updated: 2026-08-10 01:04:32 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | 2,096 | Python | 让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。 |
| [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | 1,956 | N/A | No description |
| [Binaryify/open-kimi-ppt-skill](https://github.com/Binaryify/open-kimi-ppt-skill) | 1,607 | N/A | 非官方 Kimi Slides Skill：让 AI Agent 生成可编辑 PPTD + PPTX，并附带本地浏览器编辑器 Unofficial Kimi S... |
| [ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness) | 859 | Python | let your agent control your phone |
| [mikiarlo3/awesome-growth-hacking-skills](https://github.com/mikiarlo3/awesome-growth-hacking-skills) | 795 | Shell | Find agentic growth hacking skills for Claude, ChatGPT, Manus | by enso.bot |

### Hacker News Top Stories (Last Updated: 2026-08-10 01:04:32 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [How I use LLMs to learn complex topics](https://laurentiugabriel.github.io/blog/articles/how-i-use-llms-to-learn/) | 384 | [211 comments](https://news.ycombinator.com/item?id=49234675) |
| [New Zealand lost its music media, and what we're building to replace it](https://propelmusic.co.nz/articles/the-sound-went-quiet-nz-music-media) | 68 | [32 comments](https://news.ycombinator.com/item?id=49235641) |
| ["The Persian MâR-Nâmeh Or, the Book for Taking Omens from Snakes" (1892)](https://publicdomainreview.org/collection/marnameh/) | 21 | [1 comments](https://news.ycombinator.com/item?id=49205793) |
| [Mea Culpa – Dark Hours](https://blog.terrygodier.com/2026/08/09/mea-culpa-dark-hours.html) | 550 | [249 comments](https://news.ycombinator.com/item?id=49231154) |
| [Ask HN: What are you working on? (August 2026)](https://news.ycombinator.com/item?id=49233423) | 161 | [613 comments](https://news.ycombinator.com/item?id=49233423) |
| [Taxi drivers rarely die of Alzheimer's](https://theconversation.com/taxi-drivers-rarely-die-of-alzheimers-how-complex-mental-maps-and-spatial-reasoning-protect-your-brain-286650) | 172 | [126 comments](https://news.ycombinator.com/item?id=49232253) |
| [Cool URIs Don't Change (1998)](https://www.w3.org/Provider/Style/URI) | 179 | [38 comments](https://news.ycombinator.com/item?id=49231809) |
| [Tuxedo No. 2 – Cocktail recipes](https://tuxedono2.com) | 40 | [9 comments](https://news.ycombinator.com/item?id=49235697) |
| [The tragedy of the commons, AI edition](https://www.economist.com/britain/2026/08/06/the-tragedy-of-the-commons-ai-edition) | 70 | [36 comments](https://news.ycombinator.com/item?id=49235011) |
| [Andrew Wiles on proving Fermat’s Last Theorem (1995) [video]](https://www.youtube.com/watch?v=GS7CxAtV5Ks) | 30 | [18 comments](https://news.ycombinator.com/item?id=49203626) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 24.0°C (76.0°F) |
| Average Humidity | 58% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-10 01:04:32 UTC*
