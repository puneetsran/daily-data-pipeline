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

### GitHub Trending Repositories (Last Updated: 2026-08-09 01:02:43 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | 12,128 | Rust | Convert Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, and PDF to clean ... |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | 1,989 | Python | 让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。 |
| [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | 1,725 | N/A | No description |
| [Binaryify/open-kimi-ppt-skill](https://github.com/Binaryify/open-kimi-ppt-skill) | 1,588 | N/A | 非官方 Kimi Slides Skill：让 AI Agent 生成可编辑 PPTD + PPTX，并附带本地浏览器编辑器 Unofficial Kimi S... |
| [mikiarlo3/awesome-growth-hacking-skills](https://github.com/mikiarlo3/awesome-growth-hacking-skills) | 764 | Shell | Find agentic growth hacking skills for Claude, ChatGPT, Manus | by enso.bot |

### Hacker News Top Stories (Last Updated: 2026-08-09 01:02:43 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [My server is a phone now](https://seg6.space/posts/phone-server/) | 66 | [25 comments](https://news.ycombinator.com/item?id=49226636) |
| [Fastmail offers EU data region](https://www.fastmail.com/blog/fastmail-offers-eu-data-region/) | 314 | [140 comments](https://news.ycombinator.com/item?id=49223082) |
| [Improving Heuristics for A* Pathfinding](https://www.redblobgames.com/pathfinding/heuristics/differential.html) | 29 | [6 comments](https://news.ycombinator.com/item?id=49079995) |
| [_for-sale DNS records](https://specification.website/spec/foundations/for-sale-dns/) | 341 | [131 comments](https://news.ycombinator.com/item?id=49221668) |
| [Open-source interactive map for the Aug 12 total solar eclipse](https://eclipsefan.org/?v=2&t=max&layers=eclipse%2Cbesselian%2Cumbra-live%2Cshadow-3d%2Ccloud-projection%2Cosm&lat=43.4623&lon=-3.8099&opacity=besselian%3A0.2%2Cumbra-live%3A0.2&zoom=6&palier=minute) | 83 | [18 comments](https://news.ycombinator.com/item?id=49225139) |
| [Making difficulty curves in games](http://www.davetech.co.uk/difficultycurves) | 49 | [13 comments](https://news.ycombinator.com/item?id=49180649) |
| [Can Intel finally beat ARM on performance per Watt?](https://hackaday.com/2026/08/08/want-energy-efficiency-dude-youre-getting-a-dell/) | 154 | [86 comments](https://news.ycombinator.com/item?id=49223079) |
| [Title 7 Disparate Impact Liability Makes Almost Everything Presumptively Illegal](https://www.nyujll.com/volume-14/title-vii-disparate-impact-liability-makes-almost-everything-presumptively-illegal) | 7 | [0 comments](https://news.ycombinator.com/item?id=49226827) |
| [DeepMind's WeatherNext model achieves breakthrough forecasting cyclones](https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/) | 377 | [115 comments](https://news.ycombinator.com/item?id=49220126) |
| [Timeline of the OpenAI accidental attack against Hugging Face](https://simonwillison.net/2026/Aug/7/openai-timeline/) | 328 | [335 comments](https://news.ycombinator.com/item?id=49220609) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 27.0°C (80.0°F) |
| Average Humidity | 52% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-09 01:02:43 UTC*
