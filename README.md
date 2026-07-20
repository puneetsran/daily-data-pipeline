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

### GitHub Trending Repositories (Last Updated: 2026-07-20 02:09:57 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [xai-org/grok-build](https://github.com/xai-org/grok-build) | 20,133 | Rust | SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensib... |
| [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | 10,378 | JavaScript | Codex Dream Skin |
| [CluvexStudio/Aether](https://github.com/CluvexStudio/Aether) | 1,316 | Rust | No description |
| [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | 1,157 | JavaScript | Your clothes, extracted and organized with gpt-image. |
| [nethical6/conversation-steganography](https://github.com/nethical6/conversation-steganography) | 828 | Go | Use LLMs to hide messages inside normal looking conversations |

### Hacker News Top Stories (Last Updated: 2026-07-20 02:09:57 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s](https://news.ycombinator.com/item?id=48968606) | 1559 | [172 comments](https://news.ycombinator.com/item?id=48968606) |
| [The Zen of Parallel Programming](https://smolnero.com/posts/the-zen-of-parallel-programming) | 112 | [11 comments](https://news.ycombinator.com/item?id=48907390) |
| [Biggest Probabilistic Computer Turns Noise into Answers](https://spectrum.ieee.org/biggest-probabilistic-computer) | 37 | [6 comments](https://news.ycombinator.com/item?id=48971938) |
| [A new Intel Itanium (IA-64) emulator that boots Windows](https://raymii.org/s/blog/Intel_Itanium_IA-64-Emulator_that_boots_Windows.html) | 49 | [33 comments](https://news.ycombinator.com/item?id=48971566) |
| [What I learned selling 2,500 MIDI recorders: Hardware is not so hard](https://chipweinberger.com/articles/20260719-hardware-is-not-so-hard) | 405 | [196 comments](https://news.ycombinator.com/item?id=48966713) |
| [Claude Code uses Bun written in Rust now](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/) | 394 | [557 comments](https://news.ycombinator.com/item?id=48966569) |
| [Minecraft: Java Edition now uses SDL3](https://www.minecraft.net/en-us/article/minecraft-26-3-snapshot-4) | 274 | [180 comments](https://news.ycombinator.com/item?id=48967256) |
| [Talk: The Art of Braiding Algorithms](https://pgadey.ca/notes/talk-relatorium-2026/) | 23 | [0 comments](https://news.ycombinator.com/item?id=48920597) |
| [OpenAI reduces Codex Model Context Size from 372k to 272k](https://github.com/openai/codex/pull/33972/files) | 320 | [149 comments](https://news.ycombinator.com/item?id=48965850) |
| [Who Is America's Homer?](https://www.plough.com/articles/who-is-americas-homer) | 37 | [76 comments](https://news.ycombinator.com/item?id=48913656) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 24.0°C (74.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-20 02:09:57 UTC*
