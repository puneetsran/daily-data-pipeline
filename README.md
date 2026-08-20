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

### GitHub Trending Repositories (Last Updated: 2026-08-20 00:43:01 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | 7,542 | N/A | Open Frontier Intelligence |
| [mshumer/Claude-of-Duty](https://github.com/mshumer/Claude-of-Duty) | 2,406 | JavaScript | A Call of Duty-quality FPS in Three.js, built from a single prompt. |
| [VictorTaelin/OptMem](https://github.com/VictorTaelin/OptMem) | 934 | Python | Permanent memory for AI agents. A 426-token prompt, a script, plug and play. |
| [xikhar/persona](https://github.com/xikhar/persona) | 676 | JavaScript | Bringing real-time voice to life. |
| [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | 564 | JavaScript | Makes your AI agent think like the laziest senior dev in the room. The best code... |

### Hacker News Top Stories (Last Updated: 2026-08-20 00:43:01 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [OpenRouter is joining Stripe](https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/) | 597 | [317 comments](https://news.ycombinator.com/item?id=49364559) |
| [Gardner police discontinue Flock cameras as license plate readers face scrutiny](https://www.kmbc.com/article/gardner-kansas-flock-cameras-license-plate-readers-privacy/73468724) | 49 | [11 comments](https://news.ycombinator.com/item?id=49368625) |
| [Go 1.27](https://go.dev/blog/go1.27) | 420 | [102 comments](https://news.ycombinator.com/item?id=49365405) |
| [Google replaced Git tags for certain source code with obtaining via Google Drive](https://grapheneos.social/@GrapheneOS/117057099753905023) | 271 | [107 comments](https://news.ycombinator.com/item?id=49364745) |
| [Unlocking a locked/deactivated e-waste Cricut Maker](https://sprocketfox.io/xssfox/2026/07/01/cricut-unlock/) | 122 | [33 comments](https://news.ycombinator.com/item?id=49365841) |
| [Unsloth Dynamic 3.0 GGUFs](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs) | 173 | [64 comments](https://news.ycombinator.com/item?id=49365443) |
| [Os8088.com: IBM XT OS now has a Browser, CP/M 2.2 with Z80 core and MS Word 1.1a](https://os8088.com/spotlight/) | 37 | [22 comments](https://news.ycombinator.com/item?id=49367256) |
| [Sol Loves to Cheat](https://jumploops.com/blog/sol-loves-to-cheat/) | 65 | [35 comments](https://news.ycombinator.com/item?id=49348189) |
| [A joke domain purchase turned in geopolitical warfare](https://sprocketfox.io/xssfox/2026/08/19/sondehub-and-war/) | 732 | [112 comments](https://news.ycombinator.com/item?id=49360015) |
| [Casio F-B100W-1A](https://www.casio.com/uk/watches/casio/product.F-B100W-1A/) | 264 | [212 comments](https://news.ycombinator.com/item?id=49362887) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 23.0°C (74.0°F) |
| Average Humidity | 60% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-20 00:43:01 UTC*
