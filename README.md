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

### GitHub Trending Repositories (Last Updated: 2026-10-17 02:17:50 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [jhaizhou-ops/d2r-mobile](https://github.com/jhaizhou-ops/d2r-mobile) | 3,544 | C | Open-source iOS / macOS compatibility layer for Diablo II: Resurrected with the ... |
| [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) | 2,868 | C | Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, ... |
| [Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill) | 2,530 | Python | Qwen-Image 2.1 NSFW/姿势出图 skill：作者级提示词配方 + NSFW LoRA + 136 姿势 VNCCS 人偶控制；适用 Claud... |
| [liseami/CCBaga](https://github.com/liseami/CCBaga) | 2,404 | Rust | No description |
| [HeyPuter/everything](https://github.com/HeyPuter/everything) | 1,754 | JavaScript | We're rebuilding and open-sourcing the world’s software from scratch. |

### Hacker News Top Stories (Last Updated: 2026-10-17 02:17:50 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Tesla Roadster](https://www.tesla.com/roadster) | 1212 | [2187 comments](https://news.ycombinator.com/item?id=50112657) |
| [Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console](https://github.com/cobanov/PS5LM) | 207 | [54 comments](https://news.ycombinator.com/item?id=50122431) |
| [Claude reveals ECDSA curve origins](https://www.anthropic.com/research/ecdsa-curve-origins) | 696 | [274 comments](https://news.ycombinator.com/item?id=50122800) |
| [FLUX 3 Image Klein](https://bfl.ai/blog/flux-3-image-klein) | 117 | [29 comments](https://news.ycombinator.com/item?id=50123580) |
| [You could have invented transformers from memory](https://alexwang.ai/posts/associative-memory/) | 157 | [42 comments](https://news.ycombinator.com/item?id=50122878) |
| [Waymo in Toronto](https://waymo.com/blog/2026/10/waymo-in-toronto/) | 276 | [390 comments](https://news.ycombinator.com/item?id=50118981) |
| [eBay Restricts Listings of Radio Equipment, but Exempts Ham-Band-Only Gear](https://www.arrl.org/arrlletterissue?issue=2026-10-15#eBay-Restricts-Listings-of-Radio-Equipment_-But-Exempts-Ham-Band-Only-Gear) | 177 | [142 comments](https://news.ycombinator.com/item?id=50122034) |
| [Wireless magnetic millirobots that deliver medicine inside the beating heart](https://hub.jhu.edu/2026/10/12/magnetic-millirobots-cardiac-treatment/) | 71 | [8 comments](https://news.ycombinator.com/item?id=50083673) |
| [Designing more efficient quantum circuits with Claude](https://www.anthropic.com/research/designing-efficient-quantum-circuits) | 105 | [20 comments](https://news.ycombinator.com/item?id=50121939) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 15.0°C (59.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-17 02:17:50 UTC*
