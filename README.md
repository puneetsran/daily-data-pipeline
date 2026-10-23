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

### GitHub Trending Repositories (Last Updated: 2026-10-23 02:41:49 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | 24,457 | Java | Debloat any Android or Google TV over Wi-Fi and get an Apple TV-style home. |
| [ly05010419/MacNativeGames](https://github.com/ly05010419/MacNativeGames) | 4,518 | C | No description |
| [simbasjungles/free-my-tv](https://github.com/simbasjungles/free-my-tv) | 3,484 | Java | A fast, ad-free home screen for Google TV. Open source, built with Claude Code. ... |
| [pengchujin/aerial-tv](https://github.com/pengchujin/aerial-tv) | 3,207 | Kotlin | 给国产电视的一块干净桌面：参照 tvOS 设计的开源 Android TV 桌面，没有广告，开机自动接管。A tvOS-style launcher for X... |
| [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) | 2,220 | Python | 数学（小学到高中）、英语（三年级到高中）、初中物理的知识图谱：1644 个知识点、2403 条先修边、6723 道题，对齐课标，附自适应前置诊断。 |

### Hacker News Top Stories (Last Updated: 2026-10-23 02:41:49 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Docker is weird](https://codeandcake.dev/posts/2026-10-22-docker-is-weird) | 161 | [70 comments](https://news.ycombinator.com/item?id=50202681) |
| [LLMs are making formal software verification feasible at a much larger scale](https://www.anthropic.com/research/formal-verification) | 141 | [70 comments](https://news.ycombinator.com/item?id=50202217) |
| [Quad9 (DNS Resolver) to Exit France](https://quad9.net/news/blog/au-revoir-france/) | 1022 | [369 comments](https://news.ycombinator.com/item?id=50195959) |
| [The foolishness of "natural language programming" (1978)](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html) | 38 | [36 comments](https://news.ycombinator.com/item?id=50203161) |
| [OpenShell – A safe, private runtime for fleets of autonomous AI agents](https://github.com/NVIDIA/OpenShell) | 314 | [162 comments](https://news.ycombinator.com/item?id=50198675) |
| [Woman faces six years in prison over Cash App account she never opened](https://www.techspot.com/news/114296-woman-spends-three-nights-jail-faces-six-years.html) | 532 | [544 comments](https://news.ycombinator.com/item?id=50194833) |
| [Every AI model has the same "controversial" take on humans](https://www.modelcompare.ai/blog/ai-models-controversial-take-on-humans) | 254 | [317 comments](https://news.ycombinator.com/item?id=50197313) |
| [AI compute is the new oil–and needs a new market](https://www.economist.com/finance-and-economics/2026/10/22/ai-compute-is-the-new-oil-and-needs-a-new-market) | 25 | [16 comments](https://news.ycombinator.com/item?id=50202671) |
| [Getting ready to operate GNU Taler in Germany](https://www.taler.net/en/news/2026-13.html) | 231 | [85 comments](https://news.ycombinator.com/item?id=50197404) |
| [Run full iOS 16.5 firmware on Android Devices](https://github.com/oosexgang/hackios-xnu-kernel) | 334 | [129 comments](https://news.ycombinator.com/item?id=50196718) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 12.0°C (53.0°F) |
| Average Humidity | 72% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-23 02:41:49 UTC*
