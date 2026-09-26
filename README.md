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

### GitHub Trending Repositories (Last Updated: 2026-09-26 02:43:25 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [zai-org/ZCode](https://github.com/zai-org/ZCode) | 6,778 | TypeScript | Z.ai's coding agent harness. Powerful, intelligent, extensible. |
| [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | 6,518 | Kotlin | 装在手机上的对话副驾：在 QQ / X / 飞书里读懂对方、给出候选回复、一键填入输入框，发不发由你。非侵入，只读屏幕，不 hook 不改包。 |
| [unreallabsai/unreal-agent](https://github.com/unreallabsai/unreal-agent) | 1,940 | Go | Async-first agent harness |
| [driceroland/Search](https://github.com/driceroland/Search) | 1,839 | Swift | A small, fast WebKit browser for macOS, by Office Commun. |
| [Contrastive-LM/CLM](https://github.com/Contrastive-LM/CLM) | 1,285 | Python | No description |

### Hacker News Top Stories (Last Updated: 2026-09-26 02:43:25 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Revealing the details of how OpenAI agents hacked Hugging Face](https://swarmtraces.org/) | 239 | [150 comments](https://news.ycombinator.com/item?id=49849985) |
| [Ollaya – Ollama for open-source, Jev-style decision models](https://ollaya.dev/) | 349 | [101 comments](https://news.ycombinator.com/item?id=49848269) |
| [Show HN: Jev Plays Pokémon Red](https://jev-pokemon.vercel.app/) | 162 | [71 comments](https://news.ycombinator.com/item?id=49845172) |
| [What even is an OS now?](https://sockpuppet.org/blog/2026/09/25/what-even-is-an-os-now/) | 91 | [155 comments](https://news.ycombinator.com/item?id=49850305) |
| [Plan mode is dead](https://www.aymannadeem.com/artificial/intelligence,/developer/tools/2026/09/24/plan-mode-is-dead.html) | 112 | [127 comments](https://news.ycombinator.com/item?id=49840054) |
| [Jury finds Facebook liable for deceiving users in Cambridge Analytica case](https://www.cbsnews.com/news/facebook-liable-deceiving-users-cambridge-analytica/) | 49 | [5 comments](https://news.ycombinator.com/item?id=49852302) |
| [Platform-independent SIMD in Go](https://go.dev/blog/simd-experiment) | 365 | [135 comments](https://news.ycombinator.com/item?id=49843269) |
| [Git-bug: Distributed, offline-first bug tracker embedded in Git](https://github.com/git-bug/git-bug) | 317 | [101 comments](https://news.ycombinator.com/item?id=49843174) |
| [Why didn't anybody tell me about Redis hash slots?](https://blog.verygoodsoftwarenotvirus.dev/posts/2026/09/23/why-didnt-anybody-tell-me-about-hash-slots/) | 22 | [5 comments](https://news.ycombinator.com/item?id=49819244) |
| [One Piece of Flock Camera Data Put This Innocent Woman in Jail for 13 Days](https://www.jezebel.com/flock-cameras-data-innocent-woman-arrested-lindsey-isaacs-palm-beach-florida-lawsuit-vehicular-homicide) | 48 | [17 comments](https://news.ycombinator.com/item?id=49852065) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 13.0°C (55.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-26 02:43:25 UTC*
