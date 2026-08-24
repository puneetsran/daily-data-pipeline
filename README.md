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

### GitHub Trending Repositories (Last Updated: 2026-08-24 00:45:18 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill) | 3,901 | N/A | A compact Agent Skill for highly simplified, rounded, subtly neo-skeuomorphic IP... |
| [MengTo/threeui](https://github.com/MengTo/threeui) | 2,895 | HTML | Open-source ThreeUI Community catalog with live interactive components and compl... |
| [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | 1,412 | Python | Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent ne... |
| [vvxw/deploy-vercel](https://github.com/vvxw/deploy-vercel) | 1,213 | JavaScript | Install Command：npm install |
| [duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server) | 866 | Zig | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg tha... |

### Hacker News Top Stories (Last Updated: 2026-08-24 00:45:18 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Everything I own, owned](https://schlarp.com/posts/everything-i-own-owned/) | 184 | [52 comments](https://news.ycombinator.com/item?id=49413320) |
| [How I find problems to solve as a staff engineer](https://lalitm.com/post/find-problems-staff-engineer/) | 247 | [94 comments](https://news.ycombinator.com/item?id=49411643) |
| [Anthropic's best AI model struggles to attract users as cheaper tools thrive](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245) | 170 | [138 comments](https://news.ycombinator.com/item?id=49411102) |
| [Google Workspace thinks my domain is an email provider (2025)](https://blog.elis.cc/articles/google-workspace-thinks-my-domain-is-an-email-provider/) | 157 | [35 comments](https://news.ycombinator.com/item?id=49411717) |
| [AI Chip Architectures](https://www.jepeake.com/ai-chip-architectures) | 29 | [1 comments](https://news.ycombinator.com/item?id=49405657) |
| [My agent.md to improve LLM-assisted code quality](https://fabiensanglard.net/agent.md/index.html) | 139 | [71 comments](https://news.ycombinator.com/item?id=49410932) |
| [What Is a Harness?](https://earendil.com/posts/what-is-a-harness/) | 283 | [129 comments](https://news.ycombinator.com/item?id=49409092) |
| [How Complex Systems Fail (1998)](https://how.complexsystems.fail/) | 228 | [61 comments](https://news.ycombinator.com/item?id=49409473) |
| [Implementation of GPT-2 in pure CMake](https://github.com/AlpinDale/gpt2.cmake) | 18 | [7 comments](https://news.ycombinator.com/item?id=49412909) |
| [Malware infects Android-based automotive head unit firmware](https://securelist.com/android-head-unit-malware/121106/) | 206 | [105 comments](https://news.ycombinator.com/item?id=49408550) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 21.0°C (70.0°F) |
| Average Humidity | 84% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-24 00:45:18 UTC*
