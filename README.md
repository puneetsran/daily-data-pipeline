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

### GitHub Trending Repositories (Last Updated: 2026-10-27 03:02:36 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [JustAResearcher/gpu-unlock-ada](https://github.com/JustAResearcher/gpu-unlock-ada) | 3,895 | C | GPU tensor unlock source for RTX 4090 and experimental RTX 4070 Ti SUPER; firmwa... |
| [wesbos/3d-model-anything](https://github.com/wesbos/3d-model-anything) | 2,087 | Swift | Capture iPhone LiDAR and photos, reconstruct editable Three.js rooms, and explor... |
| [rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner) | 2,075 | Python | 关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。 |
| [xevrion/hatchzip](https://github.com/xevrion/hatchzip) | 2,063 | Rust | HatchZip is a free, open-source archive extractor for Windows, macOS and Linux t... |
| [ikow/php2shell-poc](https://github.com/ikow/php2shell-poc) | 1,838 | Python | CVE-2026-109618/109619 — 5 RCE chains + detection rules (Suricata, Sigma, ModSec... |

### Hacker News Top Stories (Last Updated: 2026-10-27 03:02:36 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Three new discoveries in mathematics, computer science, and physics](https://openai.com/index/building-scientific-understanding-with-academic-communities/) | 563 | [235 comments](https://news.ycombinator.com/item?id=50251344) |
| [The Exponential Time Hypothesis Is False [pdf]](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf) | 363 | [139 comments](https://news.ycombinator.com/item?id=50251661) |
| [Sebastian Raschka's from-scratch video course on building reasoning models](https://magazine.sebastianraschka.com/p/building-reasoning-models) | 588 | [85 comments](https://news.ycombinator.com/item?id=50245138) |
| [16-bit Windows (Windows 1.x, 2.x, 3.0, 3.1, etc.) on 64-bit Windows](https://github.com/otya128/winevdm) | 29 | [2 comments](https://news.ycombinator.com/item?id=50253529) |
| [Oldest GUI application that still runs on Windows 11](https://blog.enlyth.com/posts/oldest-windows-gui-app-win-11/) | 324 | [197 comments](https://news.ycombinator.com/item?id=50248055) |
| [Type Server Protocol](https://github.com/microsoft/pylance-release/blob/main/docs/tsp/type-server-protocol.md) | 204 | [142 comments](https://news.ycombinator.com/item?id=50248371) |
| [Cross-request KV cache exposure in the GLM-5.3 Workers AI model (155 responses)](https://blog.cloudflare.com/kv-cache-exposure-remediation/) | 89 | [25 comments](https://news.ycombinator.com/item?id=50252159) |
| [A Printer Printing onto Paper](https://twitter.com/macrofying/status/2112904628509528219) | 72 | [20 comments](https://news.ycombinator.com/item?id=50204697) |
| [CSS-Tricks has a new owner](https://css-tricks.com/css-tricks-has-a-new-owner/) | 398 | [91 comments](https://news.ycombinator.com/item?id=50245831) |
| [LISPy things you can do in 64K bytes of core (2019)](https://t3x.org/lisp64k/index.html) | 35 | [6 comments](https://news.ycombinator.com/item?id=50231041) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 10.0°C (50.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-27 03:02:36 UTC*
