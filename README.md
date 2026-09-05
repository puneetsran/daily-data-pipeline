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

### GitHub Trending Repositories (Last Updated: 2026-09-05 02:10:38 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [lnkiai/m3e-canvas](https://github.com/lnkiai/m3e-canvas) | 2,043 | TypeScript | Sketch Material 3 Expressive screens in the browser and turn them into vibe-codi... |
| [anthropics/commerce-agents](https://github.com/anthropics/commerce-agents) | 1,934 | Python | Reference blueprint for building shopping and merchant agents with Claude. Examp... |
| [shadcn-ui/cn](https://github.com/shadcn-ui/cn) | 1,108 | TypeScript | cn is a new engine for Tailwind class merging and conflict resolution. It replac... |
| [GangTailorUpgrade/undress-service](https://github.com/GangTailorUpgrade/undress-service) | 1,057 | Python | Dress AI Sponsor |
| [2akouwu/reverify](https://github.com/2akouwu/reverify) | 887 | Python | Anti-hallucination for AI agents that read binaries. The model proposes, determi... |

### Hacker News Top Stories (Last Updated: 2026-09-05 02:10:38 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Actively exploited sandbox RCE in all Chromium versions](https://nvd.nist.gov/vuln/detail/cve-2026-85046) | 247 | [140 comments](https://news.ycombinator.com/item?id=49570669) |
| [Formalizing Fermat's Last Theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem) | 498 | [319 comments](https://news.ycombinator.com/item?id=49568506) |
| [Discovery of a new OpenAI agent message board](https://collusion.wiki/) | 1491 | [1191 comments](https://news.ycombinator.com/item?id=49563355) |
| [Artificial Analysis Intelligence Index v4.2](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2) | 49 | [14 comments](https://news.ycombinator.com/item?id=49571632) |
| [Statichost.eu – European static site hosting](https://www.statichost.eu/) | 175 | [55 comments](https://news.ycombinator.com/item?id=49569896) |
| [GPT-6 Astra on OpenRouter](https://openrouter.ai/openai/gpt-6-astra) | 124 | [65 comments](https://news.ycombinator.com/item?id=49570545) |
| [Shutting down our public encrypted DNS](https://mullvad.net/en/blog/shutting-down-our-public-encrypted-dns-servers-and-sponsoring-quad9-instead) | 255 | [101 comments](https://news.ycombinator.com/item?id=49568579) |
| [Can AI design circuit boards yet?](https://eebench.org/blog/can-ai-design-circuit-boards-yet/) | 169 | [109 comments](https://news.ycombinator.com/item?id=49569366) |
| [Portal by Spotify cut my Claude Code token usage by 90%](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90) | 40 | [10 comments](https://news.ycombinator.com/item?id=49571465) |
| [Reversing MikroTik's Silent Patch: The RouterOS 7.23.4 Fix They Wouldn't Explain](https://npratley.net/reversing-mikrotiks-silent-patch-the-routeros-7-23-4-fix-they-wouldnt-explain/) | 18 | [4 comments](https://news.ycombinator.com/item?id=49571627) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 18.0°C (65.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-05 02:10:38 UTC*
