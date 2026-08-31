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

### GitHub Trending Repositories (Last Updated: 2026-08-31 02:33:42 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | 4,531 | Python | Autonomous research system for measurable, computer-executable research. |
| [HEJustinSun/my-girlfriend-jingtian-latex](https://github.com/HEJustinSun/my-girlfriend-jingtian-latex) | 4,148 | TeX | No description |
| [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt) | 1,441 | TypeScript | ChatGPT thinks. Codex works. Use ChatGPT as the planning brain while keeping the... |
| [MetaMask-AI/metamask-desktop](https://github.com/MetaMask-AI/metamask-desktop) | 1,227 | CSS | 🌐 🔌 The MetaMask desktop app enables browsing Ethereum blockchain enabled websit... |
| [wide-trace/open-higgsfield](https://github.com/wide-trace/open-higgsfield) | 1,084 | TypeScript | A studio for image and video generation — one prompt bar, each model’s own setti... |

### Hacker News Top Stories (Last Updated: 2026-08-31 02:33:42 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [“I just chose words carefully”](https://unsung.aresluna.org/i-just-chose-words-carefully/) | 321 | [84 comments](https://news.ycombinator.com/item?id=49503601) |
| [Creepy Crawlies](https://people.kernel.org/monsieuricon/creepy-crawlies) | 944 | [452 comments](https://news.ycombinator.com/item?id=49491791) |
| [Understanding ChatGPT Work](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) | 32 | [8 comments](https://news.ycombinator.com/item?id=49504625) |
| [Matrox: Graphics for Professionals](https://www.abortretry.fail/p/matrox) | 29 | [2 comments](https://news.ycombinator.com/item?id=49503934) |
| [Haiku R1/beta6 has been released](https://www.haiku-os.org/news/2026-08-26_haiku_r1_beta6) | 261 | [77 comments](https://news.ycombinator.com/item?id=49499867) |
| [Cores in space: The core memory module from a 1980 Spacelab computer](https://www.righto.com/2026/08/spacelab-core-memory.html) | 81 | [13 comments](https://news.ycombinator.com/item?id=49502214) |
| [Show HN: NFC Energy-Harvesting PCB Business Card with an MCU](https://wilsonharper.net/projects/businesscard/) | 111 | [12 comments](https://news.ycombinator.com/item?id=49478426) |
| [Sort branches by last commit date](https://ryangreenberg.com/til/git-branches-by-commit-date/) | 90 | [34 comments](https://news.ycombinator.com/item?id=49435285) |
| [Continuous Diffusion Language Models (CDLM's)](https://sander.ai/2026/08/24/continuous-dlms.html) | 60 | [24 comments](https://news.ycombinator.com/item?id=49502611) |
| [Why open source rocks – a new SM750 (Silicon Motion GPU) HDMI Driver](https://github.com/KodeMunkie/sm750hdmifb) | 74 | [34 comments](https://news.ycombinator.com/item?id=49501611) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 17.0°C (63.0°F) |
| Average Humidity | 81% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-31 02:33:42 UTC*
