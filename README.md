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

### GitHub Trending Repositories (Last Updated: 2026-07-28 01:47:06 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc) | 1,766 | TypeScript | TypeScript-to-Native Compiler |
| [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | 1,751 | Python | No description |
| [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | 1,432 | N/A | Open Frontier Intelligence |
| [mshumer/Claude-of-Duty](https://github.com/mshumer/Claude-of-Duty) | 1,030 | JavaScript | A Call of Duty-quality FPS in Three.js, built from a single prompt. |
| [mikiarlo3/ai-copywriter](https://github.com/mikiarlo3/ai-copywriter) | 939 | Python | An AI copywriter that uses real copywriting skills + real marketing knowledge wi... |

### Hacker News Top Stories (Last Updated: 2026-07-28 01:47:06 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Our position on open-weights models](https://www.anthropic.com/news/position-open-weights-models) | 447 | [612 comments](https://news.ycombinator.com/item?id=49076057) |
| [Benchmarking Opus 5 on SlopCodeBench](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-opus-5-on-slop-code-bench.md) | 113 | [28 comments](https://news.ycombinator.com/item?id=49076391) |
| [DConf 2026 in London](https://dconf.org/2026/index.html) | 44 | [15 comments](https://news.ycombinator.com/item?id=49076840) |
| [Astronauts describe persistent 'observer' sensation after 6 month missions](https://spacedaily.com/sd-v-astronauts-returning-from-six-month-missions-describe-a-persistent-observer-sensation-the-feeling-of-watching-their-own-lives-from-a-half-step-outside-the-frame-weeks-after-theyr/) | 40 | [17 comments](https://news.ycombinator.com/item?id=49076900) |
| [Watching Go's new garbage collector move through the heap](https://theconsensus.dev/p/2026/07/19/observing-gos-garbage-collector-old-and-new.html) | 171 | [17 comments](https://news.ycombinator.com/item?id=49045474) |
| [C/C++ projects packaged for Zig](https://github.com/allyourcodebase) | 25 | [17 comments](https://news.ycombinator.com/item?id=49076791) |
| [Launch HN: Rise Reforming (YC S26) – Turning Waste Gases into Valuable Chemicals](https://www.rise-reforming.com) | 60 | [22 comments](https://news.ycombinator.com/item?id=49074817) |
| [The Burau representation of the braid group is faithful for n = 4](https://arxiv.org/abs/2607.05283) | 13 | [5 comments](https://news.ycombinator.com/item?id=49077209) |
| [Three Theses on the Literacy Crisis](https://trevoraleo.substack.com/p/three-theses-on-the-literacy-crisis) | 12 | [6 comments](https://news.ycombinator.com/item?id=49050021) |
| [Self-contained highly-portable Python distributions](https://gregoryszorc.com/docs/python-build-standalone/main/) | 112 | [22 comments](https://news.ycombinator.com/item?id=49073942) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 24.0°C (75.0°F) |
| Average Humidity | 71% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-28 01:47:06 UTC*
