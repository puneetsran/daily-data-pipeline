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

### GitHub Trending Repositories (Last Updated: 2026-10-12 03:28:41 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [openai/math](https://github.com/openai/math) | 14,133 | Lean | No description |
| [storytold/wordcraft](https://github.com/storytold/wordcraft) | 6,308 | Rust | An open-source, clean-room reimplementation of Microsoft Word in pure Rust |
| [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | 3,660 | JavaScript | An agent skill for creating detailed, interactive isometric illustrations of rea... |
| [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 3,415 | JavaScript | 艺术动画skill：35种艺术风格、9种解说语法，用代码让画动起来。 |
| [mhtsec/ARTEX](https://github.com/mhtsec/ARTEX) | 3,255 | Go | AI 自主渗透测试系统 | 百度“agent+”攻防挑战赛冠军项目 |

### Hacker News Top Stories (Last Updated: 2026-10-12 03:28:41 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Whatever became of holography? (2011)](https://www.americanscientist.org/article/whatever-became-of-holography) | 87 | [36 comments](https://news.ycombinator.com/item?id=50049411) |
| [Total Annihilation, rebuilt for modern computers](https://nanolathe.gg) | 399 | [170 comments](https://news.ycombinator.com/item?id=50045984) |
| [Fingerprints are the new cookies](https://royfish.dev/fingerprints-are-the-new-cookies) | 138 | [55 comments](https://news.ycombinator.com/item?id=50048642) |
| [Cartographers of North Korea (2019)](https://cartographers-nk.wonyoung.so/) | 202 | [38 comments](https://news.ycombinator.com/item?id=50047091) |
| [The gap in shared understanding of LLM capability is widening](https://twitter.com/karpathy/status/2109361546505966046) | 286 | [466 comments](https://news.ycombinator.com/item?id=50047422) |
| [Tattoos you can turn on and off](https://www.livescience.com/technology/cool-chemistry-trick-allows-new-tattoos-to-turn-on-and-off) | 18 | [5 comments](https://news.ycombinator.com/item?id=50047802) |
| [Illustration Beyond Proof](https://terrytao.wordpress.com/2026/10/11/illustration-beyond-proof/) | 40 | [0 comments](https://news.ycombinator.com/item?id=50049133) |
| [Google is illegaly cutting forest to build data centers](https://www.theguardian.com/technology/2026/oct/06/google-datacentres-finland-temporary-halt-environmental-impact-assessment) | 211 | [44 comments](https://news.ycombinator.com/item?id=50048638) |
| [Terence Tao: Math 2.0 [pdf]](https://teorth.github.io/tao-web/slides/math-2-0-caltech-2026.pdf) | 336 | [388 comments](https://news.ycombinator.com/item?id=50043026) |
| [Vectorized CLZ and CTZ](https://purplesyringa.moe/blog/vectorized-clz-and-ctz/) | 18 | [2 comments](https://news.ycombinator.com/item?id=50039608) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 12.0°C (54.0°F) |
| Average Humidity | 62% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-12 03:28:41 UTC*
