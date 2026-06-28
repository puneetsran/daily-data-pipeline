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

### GitHub Trending Repositories (Last Updated: 2026-06-28 02:40:27 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | 2,216 | HTML | Codex 橙皮书：从安装到实战案例的全链路 Codex 使用指南（非官方开源，含可下载 PDF） |
| [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | 1,380 | Python | DeepSpec: a full-stack codebase for training and evaluating speculative decoding... |
| [bikini/exploitarium](https://github.com/bikini/exploitarium) | 1,252 | Python | A single archive of public exploit PoCs and vulnerability research writeups. At ... |
| [BohemiaInteractive/CWR](https://github.com/BohemiaInteractive/CWR) | 663 | C++ | Arma: Cold War Assault Remastered Source Code Repository. |
| [Yu9191/wloc](https://github.com/Yu9191/wloc) | 654 | JavaScript | 修改 Apple 网络定位（gs-loc）返回坐标 · 支持 Surge / Quantumult X / Loon / Stash · 快捷指令一键设置/恢复... |

### Hacker News Top Stories (Last Updated: 2026-06-28 02:40:27 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [AMD Strix Halo RDMA Cluster Setup Guide](https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes/blob/main/rdma_cluster/setup_guide.md) | 41 | [2 comments](https://news.ycombinator.com/item?id=48703258) |
| [Show HN: Decomp Academy – Learn to decompile GameCube games into matching C](https://decomp-academy.dev) | 25 | [9 comments](https://news.ycombinator.com/item?id=48703412) |
| [Choosing a Public DNS Resolver](https://evilbit.de/dns-resolver-guide.html) | 66 | [22 comments](https://news.ycombinator.com/item?id=48702273) |
| [Anonymous GitHub account mass-dropping undisclosed 0-days](https://github.com/bikini/exploitarium) | 685 | [269 comments](https://news.ycombinator.com/item?id=48698617) |
| [OpenRA](https://www.openra.net/) | 594 | [117 comments](https://news.ycombinator.com/item?id=48697560) |
| [Response to AI slop is from Robin Williams](https://jayacunzo.com/blog/your-move-chief) | 32 | [5 comments](https://news.ycombinator.com/item?id=48703452) |
| [AI learns the “dark art” of RFIC design](https://spectrum.ieee.org/ai-radio-chip-design) | 194 | [129 comments](https://news.ycombinator.com/item?id=48660021) |
| [Enhancing X11 Application Security with LXC](https://dobrowolski.dev/article/enhancing-x11-application-security-with-lxc/) | 36 | [10 comments](https://news.ycombinator.com/item?id=48701936) |
| [Fintech Engineering Handbook](https://w.pitula.me/fintech-engineering-handbook/) | 486 | [163 comments](https://news.ycombinator.com/item?id=48696982) |
| [Space Shuttle Endeavour's 20-story vertical display](https://californiasciencecenter.org/about-us/samuel-oschin-air-and-space-center/go-for-stack) | 16 | [1 comments](https://news.ycombinator.com/item?id=48686032) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 22.0°C (71.0°F) |
| Average Humidity | 49% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-06-28 02:40:27 UTC*
