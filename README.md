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

### GitHub Trending Repositories (Last Updated: 2026-10-18 02:17:42 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [jhaizhou-ops/d2r-mobile](https://github.com/jhaizhou-ops/d2r-mobile) | 3,717 | C | Open-source iOS / macOS compatibility layer for Diablo II: Resurrected with the ... |
| [Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill) | 2,647 | Python | Qwen-Image 2.1 NSFW/姿势出图 skill：作者级提示词配方 + NSFW LoRA + 136 姿势 VNCCS 人偶控制；适用 Claud... |
| [HeyPuter/everything](https://github.com/HeyPuter/everything) | 2,059 | JavaScript | We're rebuilding and open-sourcing the world’s software from scratch. |
| [ahwootech/BRUTAL](https://github.com/ahwootech/BRUTAL) | 1,798 | C# | A free, open source C# framework for making games, or your own game engine. Dire... |
| [deeplethe/solid-glass](https://github.com/deeplethe/solid-glass) | 1,747 | TypeScript | A design system for AI applications. Material, physical, tactile, technical. |

### Hacker News Top Stories (Last Updated: 2026-10-18 02:17:42 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Zuckerberg's Meta Takes Down No Kings Instagram During Protest Day](https://meidasnews.com/news/zuckerbergs-meta-takes-down-no-kings-instagram-during-massive-protest-day) | 189 | [89 comments](https://news.ycombinator.com/item?id=50136881) |
| [Bleached corals thrive within days when touching healthy neighbour](https://www.nature.com/articles/d41586-026-03266-x) | 334 | [72 comments](https://news.ycombinator.com/item?id=50126253) |
| [Dam removals are bringing fish back across the northeastern United States](https://www.smithsonianmag.com/science-nature/dam-removals-are-bringing-fish-back-across-the-northeastern-united-states-striking-down-one-tiny-barrier-at-a-time-180989679/) | 209 | [55 comments](https://news.ycombinator.com/item?id=50126312) |
| [DeepSeek-v4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | 710 | [592 comments](https://news.ycombinator.com/item?id=50129045) |
| [Furifont, a Japanese font that shows furigana](https://furifont.antfu.me/) | 274 | [58 comments](https://news.ycombinator.com/item?id=50100994) |
| [Pele – Mermaid diagrams as themeable SVG](https://pele.run/) | 249 | [26 comments](https://news.ycombinator.com/item?id=50132193) |
| [The Commodore 64 hardware simulator: break chips and pins, see the results](https://github.com/antirez/c64-hw-simulator) | 146 | [24 comments](https://news.ycombinator.com/item?id=50100366) |
| [Making chicken transparent using Dorito dust](https://chillphysicsenjoyer.substack.com/p/making-chicken-transparent-using) | 259 | [67 comments](https://news.ycombinator.com/item?id=50131213) |
| [NY announces game ownership bill requiring ownership rather than licensing](https://www.tomshardware.com/video-games/new-york-rep-announces-game-ownership-bill-that-would-require-consumer-ownership-rather-than-sale-of-licenses-would-also-require-publishers-to-keep-the-game-functional-after-support-ends) | 57 | [13 comments](https://news.ycombinator.com/item?id=50136536) |
| [Gold is now the top U.S. export](https://www.numismaticnews.net/gold-now-top-u-s-export) | 246 | [127 comments](https://news.ycombinator.com/item?id=50132870) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 13.0°C (56.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-18 02:17:42 UTC*
