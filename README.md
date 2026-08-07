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

### GitHub Trending Repositories (Last Updated: 2026-08-07 02:11:09 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | 8,601 | Rust | Convert Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, and PDF to clean ... |
| [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) | 2,840 | C | A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB o... |
| [imsai-sh/zhuzhiliao](https://github.com/imsai-sh/zhuzhiliao) | 2,302 | HTML | 竹知了 —— 一转就哇哇叫的传统玩具，Web 模拟版。零依赖单文件，真实录音采样，移动端优先。 |
| [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | 1,870 | TypeScript | An interactive 3D human anatomy explorer built using threejs with GPT 5.6 Sol |
| [DannyMac180/sol-advisor](https://github.com/DannyMac180/sol-advisor) | 1,708 | Shell | Codex-native architect orchestration with Luna and Terra implementation lanes an... |

### Hacker News Top Stories (Last Updated: 2026-08-07 02:11:09 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [AMD acquires Taalas to boost inference performance by etching models in silicon](https://www.theregister.com/systems/2026/08/06/amd-acquires-ai-chip-startup-taalas-to-boost-inference-performance-by-etching-models-into-silicon/5284344) | 384 | [299 comments](https://news.ycombinator.com/item?id=49201970) |
| [Scientists discover Kelvin-Helmholtz Instability on the surface of the Sun](https://nso.edu/press-release/nsf-inouye-solar-telescope-enables-major-discovery-of-a-hidden-solar-process/) | 146 | [27 comments](https://news.ycombinator.com/item?id=49184355) |
| [Mario Meets Pareto](https://www.mayerowitz.io/blog/mario-meets-pareto) | 883 | [150 comments](https://news.ycombinator.com/item?id=49195231) |
| [Welcoming the Nepalese Government to Have I Been Pwned](https://www.troyhunt.com/welcoming-the-nepalese-government-to-have-i-been-pwned/) | 88 | [15 comments](https://news.ycombinator.com/item?id=49203105) |
| [I stopped trusting USB-C cable labels and started testing them](https://www.makeuseof.com/i-stopped-trusting-usb-c-cable-labels-started-testing-with-meter-instead/) | 79 | [47 comments](https://news.ycombinator.com/item?id=49152255) |
| [Bioengineered chewing gum may offer a way to fight HPV and other microbes](https://www.sciencedaily.com/releases/2026/08/260803080917.htm) | 56 | [8 comments](https://news.ycombinator.com/item?id=49202716) |
| [Taste Is All That's Left](https://notashelf.dev/posts/taste-is-all-thats-left) | 216 | [173 comments](https://news.ycombinator.com/item?id=49199346) |
| [Inside vLLM: Anatomy of a High-Throughput LLM Inference System (2025)](https://www.aleksagordic.com/blog/vllm) | 65 | [2 comments](https://news.ycombinator.com/item?id=49202852) |
| [Herdr is joining Y Combinator. The runtime stays open](https://herdr.dev/blog/herdr-is-joining-y-combinator/) | 147 | [101 comments](https://news.ycombinator.com/item?id=49201003) |
| [Almost no skill required to cook a steak](https://blog.sydorets.com/en/posts/almost-no-skill-required-to-cook-a-steak/) | 279 | [324 comments](https://news.ycombinator.com/item?id=49198069) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 27.0°C (81.0°F) |
| Average Humidity | 54% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-07 02:11:09 UTC*
