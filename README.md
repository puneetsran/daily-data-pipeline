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

### GitHub Trending Repositories (Last Updated: 2026-07-01 02:41:31 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | 5,337 | Python | DeepSpec: a full-stack codebase for training and evaluating speculative decoding... |
| [baairon/torlink](https://github.com/baairon/torlink) | 1,720 | TypeScript | A sleek, zero-setup torrent finder and downloader that lives right in your termi... |
| [Krishnagangwal/CS-Fundamentals](https://github.com/Krishnagangwal/CS-Fundamentals) | 1,225 | N/A | Curated CS fundamentals for placement prep: DSA,Computer Networks, DBMS & SQL, O... |
| [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | 831 | Python | No description |
| [winsznx/theeleven](https://github.com/winsznx/theeleven) | 691 | TypeScript | Eleven autonomous AI agents open live football prop markets on X Layer — custom ... |

### Hacker News Top Stories (Last Updated: 2026-07-01 02:41:31 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [The President Made More Than $1Billon in Crypto Deals](https://www.wsj.com/politics/policy/trump-made-more-than-1-billion-on-crypto-deals-part-of-2025-windfall-ee917d3f) | 66 | [10 comments](https://news.ycombinator.com/item?id=48741012) |
| [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) | 889 | [499 comments](https://news.ycombinator.com/item?id=48736605) |
| [Claude Code is steganographically marking requests](https://thereallo.dev/blog/claude-code-prompt-steganography) | 1429 | [409 comments](https://news.ycombinator.com/item?id=48734373) |
| [Google copybara: moving code between repositories](https://github.com/google/copybara) | 49 | [6 comments](https://news.ycombinator.com/item?id=48740698) |
| [Department of Commerce has lifted export controls on Claude Fable 5 and Mythos 5](https://twitter.com/AnthropicAI/status/2072106151890809341) | 232 | [90 comments](https://news.ycombinator.com/item?id=48740771) |
| [Forestiere Underground Gardens](https://en.wikipedia.org/wiki/Forestiere_Underground_Gardens) | 10 | [1 comments](https://news.ycombinator.com/item?id=48741359) |
| [From brain waves to words: a new path to communication without surgery](https://ai.meta.com/blog/brain2qwerty-brain-ai-human-communication/?_fb_noscript=1) | 109 | [58 comments](https://news.ycombinator.com/item?id=48739466) |
| [Claude Science](https://claude.com/product/claude-science) | 371 | [122 comments](https://news.ycombinator.com/item?id=48735770) |
| [Nano Banana 2 Lite](https://deepmind.google/models/gemini-image/flash-lite/) | 308 | [120 comments](https://news.ycombinator.com/item?id=48735444) |
| [Leanstral 1.5](https://docs.mistral.ai/models/model-cards/leanstral-1-5-26-06) | 102 | [19 comments](https://news.ycombinator.com/item?id=48738938) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 18.0°C (65.0°F) |
| Average Humidity | 64% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-01 02:41:31 UTC*
