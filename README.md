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

### GitHub Trending Repositories (Last Updated: 2026-07-21 01:51:50 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | 11,088 | JavaScript | Codex Dream Skin |
| [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | 1,219 | JavaScript | Your clothes, extracted and organized with gpt-image. |
| [hoainho/img2threejs](https://github.com/hoainho/img2threejs) | 1,028 | Python | Rebuild the object in a reference image as a code-only, procedural, quality-gate... |
| [nethical6/conversation-steganography](https://github.com/nethical6/conversation-steganography) | 881 | Go | Use LLMs to hide messages inside normal looking conversations |
| [pablostanley/yoinks](https://github.com/pablostanley/yoinks) | 869 | TypeScript | yoink any video from your terminal. no shady ads. |

### Hacker News Top Stories (Last Updated: 2026-07-21 01:51:50 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Who's afraid of Chinese models?](https://stratechery.com/2026/whos-afraid-of-chinese-models/) | 261 | [171 comments](https://news.ycombinator.com/item?id=48977128) |
| [Kimi Work](https://www.kimi.com/products/kimi-work) | 398 | [185 comments](https://news.ycombinator.com/item?id=48981703) |
| [Human mathematicians are being outcounterexampled](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/) | 209 | [76 comments](https://news.ycombinator.com/item?id=48983382) |
| [Jelly UI: Soft-body physics for native HTML form controls](https://jelly-ui.com/) | 346 | [135 comments](https://news.ycombinator.com/item?id=48981620) |
| [Hacker wipes Romania's land registry database](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/) | 571 | [325 comments](https://news.ycombinator.com/item?id=48978605) |
| [Jellyfin founder Andrew leaves team](https://forum.jellyfin.org/t-project-leadership-changes) | 36 | [9 comments](https://news.ycombinator.com/item?id=48986091) |
| [Nativ: Run frontier open models locally on your Mac](https://blaizzy.github.io/nativ/) | 178 | [71 comments](https://news.ycombinator.com/item?id=48982681) |
| [The Psychology of Software Teams](https://www.routledge.com/The-Psychology-of-Software-Teams/Hicks/p/book/9781032963389) | 25 | [5 comments](https://news.ycombinator.com/item?id=48923130) |
| [Show HN: Immersive Gaussian Splat tour of grace cathedral, San Francisco](https://vincentwoo.com/3d/grace_cathedral/) | 74 | [14 comments](https://news.ycombinator.com/item?id=48984254) |
| [Airport Simulator](https://airport.apunen.com/) | 706 | [142 comments](https://news.ycombinator.com/item?id=48976846) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 28.0°C (83.0°F) |
| Average Humidity | 47% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-21 01:51:50 UTC*
