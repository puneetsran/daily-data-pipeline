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

### GitHub Trending Repositories (Last Updated: 2026-08-06 01:47:38 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [trycompai/crm](https://github.com/trycompai/crm) | 6,308 | TypeScript | An open-source, agentic-first CRM. |
| [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | 5,174 | Rust | Convert Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, and PDF to clean ... |
| [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) | 2,583 | C | A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB o... |
| [imsai-sh/zhuzhiliao](https://github.com/imsai-sh/zhuzhiliao) | 2,043 | HTML | 竹知了 —— 一转就哇哇叫的传统玩具，Web 模拟版。零依赖单文件，真实录音采样，移动端优先。 |
| [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) | 1,786 | TypeScript | An AI-native office suite for macOS and Windows: word processor, spreadsheet, pr... |

### Hacker News Top Stories (Last Updated: 2026-08-06 01:47:38 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Discovery Loop](https://www.discoveryloop.com/) | 591 | [380 comments](https://news.ycombinator.com/item?id=49184960) |
| [Zed DeltaDB](https://zed.dev/deltadb) | 300 | [151 comments](https://news.ycombinator.com/item?id=49187256) |
| [The title cards in Blade Runner are amazing](https://randsinrepose.com/archives/blade-runner-title-cards/) | 142 | [59 comments](https://news.ycombinator.com/item?id=49189287) |
| [Changes at Google DeepMind: Demis Hassabis from CEO to Chair, Jeff Dean departs](https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/) | 473 | [589 comments](https://news.ycombinator.com/item?id=49184755) |
| [Beating GPT-5.6 Sol on retrieval with 100x cheaper open models](https://neon.com/blog/how-castform-neon-beats-frontier-models-on-price-and-efficiency) | 223 | [41 comments](https://news.ycombinator.com/item?id=49186762) |
| [Muse Code and Muse Spark 1.2](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) | 172 | [104 comments](https://news.ycombinator.com/item?id=49187575) |
| [Prime Agent: A self-improving RLM agent](https://www.primeintellect.ai/blog/prime-agent) | 103 | [19 comments](https://news.ycombinator.com/item?id=49189075) |
| [Atlassian Rovo Exfiltrates Data, Bypassing Controls](https://www.promptarmor.com/resources/atlassian-rovo-exfiltrates-data) | 169 | [67 comments](https://news.ycombinator.com/item?id=49185983) |
| [NVIDIA’s Vera Whitepaper Has a Thread Loose](https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread) | 83 | [12 comments](https://news.ycombinator.com/item?id=49189234) |
| [Born Against, or why hobby programming communities are against LLM usage](https://blog.fogus.me/llm/born-against.html) | 131 | [140 comments](https://news.ycombinator.com/item?id=49187061) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 27.0°C (81.0°F) |
| Average Humidity | 45% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-06 01:47:38 UTC*
