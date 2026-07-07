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

### GitHub Trending Repositories (Last Updated: 2026-07-07 02:12:49 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | 2,680 | TypeScript | autonomous red teaming platform; multi-agent offensive-security meta-harness |
| [ammaarreshi/Generals-Mac-iOS-iPad](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad) | 1,154 | C++ | Command & Conquer Generals: Zero Hour running natively on macOS, iPhone & iPad —... |
| [jamesob/local-llm](https://github.com/jamesob/local-llm) | 1,077 | Shell | Everything I know about running LLMs locally |
| [synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience) | 801 | TypeScript | The open-source AI workbench for scientific research |
| [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | 739 | N/A | 小隐寺投资百科官方公开索引：美股、期权与加密货币知识框架 |

### Hacker News Top Stories (Last Updated: 2026-07-07 02:12:49 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Fable turned reMarkable into Tom Riddle's diary from Harry Potter](https://github.com/MaximeRivest/Riddle) | 156 | [99 comments](https://news.ycombinator.com/item?id=48811591) |
| [How to sequence your own DNA at home](https://bradleywoolf.com/links-1/sequencing-my-own-dna-at-home) | 58 | [15 comments](https://news.ycombinator.com/item?id=48812156) |
| [OpenWrt One – Open Hardware Router](https://openwrt.org/toh/openwrt/one) | 447 | [176 comments](https://news.ycombinator.com/item?id=48808482) |
| [CoMaps – FOSS Offline Maps](https://www.comaps.app/) | 323 | [63 comments](https://news.ycombinator.com/item?id=48808928) |
| [GLM 5.2 and the coming AI margin collapse](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/) | 173 | [109 comments](https://news.ycombinator.com/item?id=48809877) |
| [Ternlight – 7 MB embedding model that runs in browser (WASM)](https://ternlight-demo.vercel.app/) | 72 | [22 comments](https://news.ycombinator.com/item?id=48811644) |
| [NSA and IETF: Fairness](https://blog.cr.yp.to/20260706-fairness.html) | 40 | [15 comments](https://news.ycombinator.com/item?id=48811887) |
| [A global workspace in language models](https://www.anthropic.com/research/global-workspace) | 272 | [98 comments](https://news.ycombinator.com/item?id=48808002) |
| [Pruning RAG context down to what the answer actually needs](https://www.kapa.ai/blog/how-we-prune-rag-context) | 58 | [5 comments](https://news.ycombinator.com/item?id=48809354) |
| [A 2048-spin bulk acoustic wave Ising machine for number partitioning and Sudoku](https://arxiv.org/abs/2607.02112) | 25 | [1 comments](https://news.ycombinator.com/item?id=48782248) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 27.0°C (81.0°F) |
| Average Humidity | 32% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-07 02:12:49 UTC*
