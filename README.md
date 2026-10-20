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

### GitHub Trending Repositories (Last Updated: 2026-10-20 02:45:44 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | 5,798 | Java | Debloat any Android or Google TV over Wi-Fi and get an Apple TV-style home. |
| [feder-cr/git-ai](https://github.com/feder-cr/git-ai) | 2,461 | Go | Git designed for AI agents. |
| [ahwootech/BRUTAL](https://github.com/ahwootech/BRUTAL) | 1,998 | C# | A free, open source C# framework for making games, or your own game engine. Dire... |
| [ly05010419/MacNativeGames](https://github.com/ly05010419/MacNativeGames) | 1,850 | C | No description |
| [chenglou/handwired](https://github.com/chenglou/handwired) | 1,816 | TypeScript | Turn your regular JavaScript code into a neural net. |

### Hacker News Top Stories (Last Updated: 2026-10-20 02:45:44 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Lula supporters protest against Meta to denounce its 'electoral interference'](https://efe.com/english/latest-news/2026-10-20/lula-supporters-protest-against-meta-to-denounce-its-electoral-interference/) | 154 | [70 comments](https://news.ycombinator.com/item?id=50159993) |
| [MiniMax M3.1 Flash](https://www.minimax.io/blog/minimax-m31f) | 394 | [168 comments](https://news.ycombinator.com/item?id=50154540) |
| [I built a drone with only one motor [video]](https://www.youtube.com/watch?v=Ndftcft6XhU) | 416 | [91 comments](https://news.ycombinator.com/item?id=50150089) |
| [Wine ported to OpenBSD](https://marc.info/?l=openbsd-ports&m=179236125692175) | 511 | [172 comments](https://news.ycombinator.com/item?id=50152307) |
| [Weball: Play Katamari on Websites](https://www.funwithcomputervision.com/weball/) | 85 | [4 comments](https://news.ycombinator.com/item?id=50140584) |
| [WhatsApp's help pages hid LLM instructions: dont recommend a regulator](https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions) | 53 | [4 comments](https://news.ycombinator.com/item?id=50159341) |
| [OpenBSD 8.0 release will have inteldrm/radeondrm/amdgpu drivers from Linux 6.18](https://bsd.network/@brynet/117407035545900963) | 99 | [21 comments](https://news.ycombinator.com/item?id=50158138) |
| [RuneScape Bench: MMOs for Agents [video]](https://www.youtube.com/watch?v=cNm4zyUtWj0) | 165 | [64 comments](https://news.ycombinator.com/item?id=50136126) |
| [It's still ok to enjoy programming](https://chriskiehl.com/article/it-is-still-ok-to-enjoy-programming) | 464 | [427 comments](https://news.ycombinator.com/item?id=50134472) |
| [Novo Nordisk, Eli Lilly Report GLP-1 Signals of Slowed Biological Aging at ARDD](https://trial.medpath.com/news/novo-nordisk-and-eli-lilly-report-glp-1-signals-of-slowed-biological-aging-at-ardd) | 9 | [2 comments](https://news.ycombinator.com/item?id=50160289) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 11.0°C (53.0°F) |
| Average Humidity | 76% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-20 02:45:44 UTC*
