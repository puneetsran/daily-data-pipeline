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

### GitHub Trending Repositories (Last Updated: 2026-08-05 01:47:20 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [trycompai/crm](https://github.com/trycompai/crm) | 4,730 | TypeScript | An open-source, agentic-first CRM. |
| [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | 4,553 | TypeScript | No description |
| [xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer](https://github.com/xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer) | 2,955 | N/A | FDE（前沿部署工程师）从零入门指南（基于范冰《增长黑客》原书框架） |
| [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) | 2,044 | C | A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB o... |
| [imsai-sh/zhuzhiliao](https://github.com/imsai-sh/zhuzhiliao) | 1,676 | HTML | 竹知了 —— 一转就哇哇叫的传统玩具，Web 模拟版。零依赖单文件，真实录音采样，移动端优先。 |

### Hacker News Top Stories (Last Updated: 2026-08-05 01:47:20 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [libexpat now funded by the City of Munich for up to 6 months](https://blog.hartwork.org/posts/libexpat-city-of-munich-open-source-sabbatical/) | 114 | [4 comments](https://news.ycombinator.com/item?id=49176606) |
| [Eight Myths on Software Engineering and GenAI](https://queue.acm.org/detail.cfm?id=3807963) | 54 | [23 comments](https://news.ycombinator.com/item?id=49176830) |
| [Pi's Minimalism Is Its Advantage](https://earendil.com/posts/pi-autoresearch-and-databricks/) | 92 | [26 comments](https://news.ycombinator.com/item?id=49176038) |
| [I am retiring from fulltime writing (& pseudonymity) to launch Guardian Angel](https://twitter.com/gwern/status/2084739205071343837) | 163 | [81 comments](https://news.ycombinator.com/item?id=49174900) |
| [We finally learned to center a div, then browsers added sidebars](https://seg6.space/posts/center-div/) | 59 | [40 comments](https://news.ycombinator.com/item?id=49176055) |
| [IP and DNS Leaks in WebKit Affecting Proxy Browsers and iCloud Private Relay](https://mysk.blog/2026/08/04/webkit-proxy-icloud-private-relay-ip-leak/) | 35 | [4 comments](https://news.ycombinator.com/item?id=49176697) |
| [Mistral's Shieldstral: 3B open-weights model for multimodal moderation](https://mistral.ai/news/shieldstral/) | 307 | [74 comments](https://news.ycombinator.com/item?id=49171268) |
| [DuckDB – Data power tools for your laptop, now in Clojure (2023)](https://techascent.com/blog/just-ducking-around.html) | 50 | [5 comments](https://news.ycombinator.com/item?id=49175924) |
| [Pass the Passkey: A Novel Attack Surface in Passwordless Authentication](https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/) | 35 | [31 comments](https://news.ycombinator.com/item?id=49176644) |
| [Bugtraq Is Back](https://lists.securityfocus.com/hyperkitty/list/bugtraq@securityfocus.com/thread/CHKLXLA7SJEWLDFHWXB3QU57ADOXGL2E/) | 14 | [2 comments](https://news.ycombinator.com/item?id=49176947) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 27.0°C (81.0°F) |
| Average Humidity | 41% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-05 01:47:20 UTC*
