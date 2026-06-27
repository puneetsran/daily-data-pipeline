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

### GitHub Trending Repositories (Last Updated: 2026-06-27 02:28:04 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | 2,147 | HTML | Codex 橙皮书：从安装到实战案例的全链路 Codex 使用指南（非官方开源，含可下载 PDF） |
| [kanavtwtgg/birds.cafe](https://github.com/kanavtwtgg/birds.cafe) | 735 | JavaScript | No description |
| [BohemiaInteractive/CWR](https://github.com/BohemiaInteractive/CWR) | 625 | C++ | Arma: Cold War Assault Remastered Source Code Repository. |
| [QwenLM/Qwen-AgentWorld](https://github.com/QwenLM/Qwen-AgentWorld) | 568 | Python | Qwen-AgentWorld: Language World Models for General Agents |
| [Yu9191/wloc](https://github.com/Yu9191/wloc) | 469 | JavaScript | 修改 Apple 网络定位（gs-loc）返回坐标 · 支持 Surge / Quantumult X / Loon / Stash · 快捷指令一键设置/恢复... |

### Hacker News Top Stories (Last Updated: 2026-06-27 02:28:04 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Previewing GPT‑5.6 Sol: a next-generation model](https://openai.com/index/previewing-gpt-5-6-sol/) | 860 | [514 comments](https://news.ycombinator.com/item?id=48689028) |
| [Why does kinetic energy increase quadratically, not linearly, with speed? (2011)](https://physics.stackexchange.com/questions/535/why-does-kinetic-energy-increase-quadratically-not-linearly-with-speed) | 96 | [42 comments](https://news.ycombinator.com/item?id=48692946) |
| [A C++ implementation of a fast hash map and hash set using hopscotch hashing](https://github.com/Tessil/hopscotch-map) | 67 | [11 comments](https://news.ycombinator.com/item?id=48692090) |
| [MicroVMs: Run isolated sandboxes with full lifecycle control](https://aws.amazon.com/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/) | 269 | [152 comments](https://news.ycombinator.com/item?id=48642510) |
| [U.S. government will decide who gets to use GPT-5.6](https://www.washingtonpost.com/technology/2026/06/26/openai-says-us-government-will-vet-users-its-latest-ai-model/) | 841 | [940 comments](https://news.ycombinator.com/item?id=48690101) |
| [Show HN: Hacker News on a Train Station Style Flip Board](https://popflame.quickish.space/hn-flipboard/) | 9 | [0 comments](https://news.ycombinator.com/item?id=48693912) |
| [AI in mathematics is forcing big questions](https://spectrum.ieee.org/ai-in-mathematics) | 46 | [20 comments](https://news.ycombinator.com/item?id=48692883) |
| [The gap between open weights LLMs and closed source LLMs](https://blog.doubleword.ai/frontier-os-llm) | 126 | [105 comments](https://news.ycombinator.com/item?id=48692058) |
| [We can still stop California's 3D printer surveillance scheme](https://www.eff.org/deeplinks/2026/06/we-can-still-stop-californias-3d-printer-surveillance-scheme) | 240 | [75 comments](https://news.ycombinator.com/item?id=48692051) |
| [A Tiny Compiler for Data-Parallel Kernels](https://healeycodes.com/a-tiny-compiler-for-data-parallel-kernels) | 28 | [3 comments](https://news.ycombinator.com/item?id=48673115) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 16.0°C (62.0°F) |
| Average Humidity | 83% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-06-27 02:28:04 UTC*
