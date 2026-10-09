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

### GitHub Trending Repositories (Last Updated: 2026-10-09 03:49:14 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [openai/math](https://github.com/openai/math) | 12,287 | Lean | No description |
| [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 2,539 | JavaScript | 艺术动画skill：35种艺术风格、9种解说语法，用代码让画动起来。 |
| [kargulstudio/sales-crm](https://github.com/kargulstudio/sales-crm) | 1,659 | TypeScript | No description |
| [nullmoth/nvidia-macos-driver](https://github.com/nullmoth/nvidia-macos-driver) | 1,236 | Rust | Metal driver for NVIDIA GeForce RTX cards on macOS 15 Sequoia (Intel / OpenCore)... |
| [Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill) | 1,124 | Python | Eleven free Claude skills that clone any app: reverse-engineer it, rebuild it, t... |

### Hacker News Top Stories (Last Updated: 2026-10-09 03:49:14 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Whistle: Speech to Text in 16.9 MB](https://cactuscompute.com/blog/whistle) | 603 | [134 comments](https://news.ycombinator.com/item?id=50008427) |
| [Reducing undefined behavior in the C language](https://lwn.net/Articles/1095811/) | 33 | [11 comments](https://news.ycombinator.com/item?id=50015074) |
| [Theranos.world](https://www.theranos.world/) | 331 | [124 comments](https://news.ycombinator.com/item?id=50009295) |
| [Man discovers his parents' coffee machine used 1TB of data in 10 days](https://www.dexerto.com/entertainment/man-discovers-his-parents-coffee-machine-used-1tb-of-data-in-10-days-3416399/) | 486 | [308 comments](https://news.ycombinator.com/item?id=49995495) |
| [Bevy 0.20](https://bevy.org/news/bevy-0-20/) | 77 | [13 comments](https://news.ycombinator.com/item?id=50013610) |
| [I hired an illustrator to draw my house. Now it's my Home Assistant dashboard](https://antonfrolov.substack.com/p/i-hired-an-illustrator-to-draw-my) | 455 | [78 comments](https://news.ycombinator.com/item?id=49986882) |
| [Why isn't the industry freaking out about DeepSeek 4.1 Flash?](https://www.dgt.is/blog/2026-10-07-deepseek-freek-out/) | 487 | [409 comments](https://news.ycombinator.com/item?id=50000488) |
| [Keyboard differences between Windows and Macs](https://unsung.aresluna.org/deeper-dive-keyboard-differences-between-windows-and-macs/) | 13 | [6 comments](https://news.ycombinator.com/item?id=50015515) |
| [Yes, and](https://htmx.org/essays/yes-and/) | 241 | [79 comments](https://news.ycombinator.com/item?id=50003796) |
| [The value of not getting to the point (2015)](https://ken.arneson.name/2015/11/the-value-of-not-getting-to-the-point/) | 136 | [42 comments](https://news.ycombinator.com/item?id=50010470) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 14.0°C (57.0°F) |
| Average Humidity | 88% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-09 03:49:14 UTC*
