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

### GitHub Trending Repositories (Last Updated: 2026-08-28 08:09:03 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [b-nnett/grok-bot-0.18-reconstructed](https://github.com/b-nnett/grok-bot-0.18-reconstructed) | 3,386 | TypeScript | Unofficial source-oriented reconstruction and extension of Grok Bot 0.18.0 for m... |
| [HEJustinSun/my-girlfriend-jingtian-latex](https://github.com/HEJustinSun/my-girlfriend-jingtian-latex) | 2,895 | TeX | No description |
| [tobi/walgit](https://github.com/tobi/walgit) | 2,271 | Rust | No description |
| [duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server) | 1,595 | Zig | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg tha... |
| [ApodexAI/FrontierAgent](https://github.com/ApodexAI/FrontierAgent) | 1,176 | Python | 🧩 FrontierAgent, our agent framework, open-sourced alongside it — native command... |

### Hacker News Top Stories (Last Updated: 2026-08-28 08:09:03 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Saving 100 terabytes of memory by optimizing 1.1.1.1's DNS cache](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) | 706 | [212 comments](https://news.ycombinator.com/item?id=49468083) |
| [Small Models Have Arrived](https://calv.info/small-models-have-arrived) | 608 | [277 comments](https://news.ycombinator.com/item?id=49466917) |
| [Sovereign Tech Agency invests €500k in Flatpak](https://modal.cx/blog/announcing-flatpak-sta/) | 66 | [28 comments](https://news.ycombinator.com/item?id=49474786) |
| [Show HN: OpenTIE and OpenXWA, Modern Ports of Tie Fighter and X-Wing Alliance](https://github.com/elyosh/OpenTIE/) | 150 | [37 comments](https://news.ycombinator.com/item?id=49471965) |
| [507 Mechanical Movements](https://507movements.com/) | 562 | [72 comments](https://news.ycombinator.com/item?id=49465169) |
| [Gemini-3.5-Transcribe](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) | 257 | [81 comments](https://news.ycombinator.com/item?id=49468818) |
| [Microduck](https://pollen-robotics.com/microduck/) | 629 | [209 comments](https://news.ycombinator.com/item?id=49462763) |
| [We found a division by zero bug in FFmpeg with a vibecoded fuzzer](https://code.ffmpeg.org/FFmpeg/FFmpeg/issues/24290) | 228 | [172 comments](https://news.ycombinator.com/item?id=49468642) |
| [Doctors are finally learning to manage antidepressant withdrawal](https://www.newscientist.com/article/2584861-antidepressant-withdrawal-symptoms-are-prompting-a-radical-rethink-of-how-we-treat-depression/) | 100 | [92 comments](https://news.ycombinator.com/item?id=49472090) |
| [Terminal-Bench-Science: Evaluating AI agents on scientific research workflows](https://www.terminal-bench-science.ai/announcement) | 72 | [23 comments](https://news.ycombinator.com/item?id=49472820) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 14.0°C (57.0°F) |
| Average Humidity | 86% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-28 08:09:03 UTC*
