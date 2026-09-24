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

### GitHub Trending Repositories (Last Updated: 2026-09-24 02:24:01 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 20,684 | Python | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no deci... |
| [zai-org/ZCode](https://github.com/zai-org/ZCode) | 6,551 | TypeScript | Z.ai's coding agent harness. Powerful, intelligent, extensible. |
| [mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx) | 5,982 | Python | Native MLX runtime for Laya typed decision models — 7–14 ms short decisions on M... |
| [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | 5,308 | Kotlin | 装在手机上的对话副驾：在微信 / QQ / X / 飞书里读懂对方、给出候选回复、一键填入输入框，发不发由你。非侵入，只读屏幕，不 hook 不改包。 |
| [unreallabsai/unreal-agent](https://github.com/unreallabsai/unreal-agent) | 1,742 | Go | Async-first agent harness |

### Hacker News Top Stories (Last Updated: 2026-09-24 02:24:01 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Linux support is coming to Snapdragon X2 Series](https://www.qualcomm.com/news/onq/2026/09/snapdragon-summit-agentic-ai-pcs-linux) | 167 | [71 comments](https://news.ycombinator.com/item?id=49823582) |
| [Claude discovers a novel enzyme system with CRISPR-like repeats](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) | 515 | [538 comments](https://news.ycombinator.com/item?id=49820134) |
| [Meta VR Glasses](https://www.meta.com/vr-glasses/) | 239 | [196 comments](https://news.ycombinator.com/item?id=49824268) |
| [VSCode's SSH Agent Is Bananas (2025)](https://fly.io/blog/vscode-ssh-wtf/) | 135 | [87 comments](https://news.ycombinator.com/item?id=49822555) |
| [ArXiv receives multiyear commitments to support it as an independent nonprofit](https://blog.arxiv.org/2026/09/23/arxiv-receives-multiyear-investment/) | 61 | [10 comments](https://news.ycombinator.com/item?id=49823664) |
| [Virtio-nvgpu: Near-native Nvidia GPU access inside a KVM guest](https://github.com/nestrilabs/virtio-nvgpu) | 10 | [3 comments](https://news.ycombinator.com/item?id=49824864) |
| [The "Windows XP Box" (2003)](https://www.mini-itx.com/projects/windowsxpbox/) | 59 | [9 comments](https://news.ycombinator.com/item?id=49796372) |
| [Mercury 2.5 LLM hits 770 tokens per second](https://artificialanalysis.ai/models/mercury-2-5) | 55 | [26 comments](https://news.ycombinator.com/item?id=49823348) |
| [Feds Target AI Critics as "Foreign Agents"](https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign) | 17 | [4 comments](https://news.ycombinator.com/item?id=49824686) |
| [Fixing the Portobello Police Station Clock](https://pointinthecloud.com/2026-04-11-211700.html) | 382 | [89 comments](https://news.ycombinator.com/item?id=49817469) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 15.0°C (59.0°F) |
| Average Humidity | 74% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-24 02:24:01 UTC*
