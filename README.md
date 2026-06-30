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

### GitHub Trending Repositories (Last Updated: 2026-06-30 02:35:12 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | 3,945 | Python | DeepSpec: a full-stack codebase for training and evaluating speculative decoding... |
| [Yu9191/wloc](https://github.com/Yu9191/wloc) | 1,527 | JavaScript | 修改 Apple 网络定位（gs-loc）返回坐标 · 支持 Surge / Quantumult X / Loon / Stash · 快捷指令一键设置/恢复... |
| [Krishnagangwal/CS-Fundamentals](https://github.com/Krishnagangwal/CS-Fundamentals) | 965 | N/A | Curated CS fundamentals for placement prep: DSA,Computer Networks, DBMS & SQL, O... |
| [winsznx/theeleven](https://github.com/winsznx/theeleven) | 715 | TypeScript | Eleven autonomous AI agents open live football prop markets on X Layer — custom ... |
| [baairon/torlink](https://github.com/baairon/torlink) | 698 | TypeScript | A sleek, zero-setup torrent finder and downloader that lives right in your termi... |

### Hacker News Top Stories (Last Updated: 2026-06-30 02:35:12 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [.self: A new top-level domain designed to support self-hosting](https://hccf.onmy.cloud/2026/06/21/reclaiming-our-digital-selves-hccfs-vision-for-a-human-centered-top-level-domain/) | 353 | [199 comments](https://news.ycombinator.com/item?id=48724230) |
| [Qwen 3.6 27B is the sweet spot for local development](https://quesma.com/blog/qwen-36-is-awesome/) | 630 | [522 comments](https://news.ycombinator.com/item?id=48721903) |
| [Free the Icons](https://weblog.rogueamoeba.com/2026/06/26/free-the-icons/) | 236 | [63 comments](https://news.ycombinator.com/item?id=48698908) |
| [Memory Safe Context Switching (longjmp, setjmp) in Fil-C](https://fil-c.org/context_switches) | 35 | [14 comments](https://news.ycombinator.com/item?id=48727177) |
| [Exploring PDP-1 Lisp (1960)](https://obsolescence.dev/pdp1-lisp-introduction.html) | 17 | [12 comments](https://news.ycombinator.com/item?id=48727323) |
| [LongCat-2.0, a large-scale MoE model with 1.6T total and 48B Active](https://longcat.chat/blog/longcat-2.0/) | 29 | [6 comments](https://news.ycombinator.com/item?id=48727116) |
| [Why Won't Europe Build AI Data Centers in Iceland?](https://mrkt30.com/why-wont-europe-build-ai-data-centers-in-iceland/) | 12 | [6 comments](https://news.ycombinator.com/item?id=48727538) |
| [Rocketlab acquires Iridium](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) | 374 | [231 comments](https://news.ycombinator.com/item?id=48719485) |
| [Scientists find molecular-level evidence for two structures in liquid water](https://phys.org/news/2026-06-scientists-molecular-evidence-liquid.html) | 67 | [22 comments](https://news.ycombinator.com/item?id=48726073) |
| [Ornith-1.0: self-improving open-source models for agentic coding](https://github.com/deepreinforce-ai/Ornith-1) | 161 | [32 comments](https://news.ycombinator.com/item?id=48722052) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 19.0°C (67.0°F) |
| Average Humidity | 68% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-06-30 02:35:12 UTC*
