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

### GitHub Trending Repositories (Last Updated: 2026-10-11 03:05:20 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [openai/math](https://github.com/openai/math) | 13,714 | Lean | No description |
| [storytold/wordcraft](https://github.com/storytold/wordcraft) | 3,253 | Rust | An open-source, clean-room reimplementation of Microsoft Word in pure Rust |
| [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 3,233 | JavaScript | 艺术动画skill：35种艺术风格、9种解说语法，用代码让画动起来。 |
| [mhtsec/ARTEX](https://github.com/mhtsec/ARTEX) | 2,939 | Go | AI 自主渗透测试系统 | 百度“agent+”攻防挑战赛冠军项目 |
| [zhongerxin/iPhone-use](https://github.com/zhongerxin/iPhone-use) | 2,594 | Python | 让 Codex 通过 USB 操作真实 iPhone：引导安装、App 自动化、实时屏幕与截图回退。 |

### Hacker News Top Stories (Last Updated: 2026-10-11 03:05:20 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [WallHop – 12ft.io is gone, so I built a replacement](https://wallhop.io/) | 130 | [57 comments](https://news.ycombinator.com/item?id=50038634) |
| [Build your own decision model](https://nishtahir.com/build-your-own-decision-model/) | 140 | [30 comments](https://news.ycombinator.com/item?id=50037949) |
| [2D Vehicles](https://patkerr.co.uk/2d-vehicles/) | 375 | [85 comments](https://news.ycombinator.com/item?id=49991852) |
| [A city-building game in which the city would prefer you didn't](https://housing.over.pizza/) | 201 | [77 comments](https://news.ycombinator.com/item?id=50036864) |
| [500B Tokens Later: Letting AI Agents Decompile a First-Person Shooter](https://momo5502.com/posts/2026-10-09-game-decompilation/) | 29 | [18 comments](https://news.ycombinator.com/item?id=50039092) |
| [PSPi 6 – Raspberry Pi in a PSP](https://github.com/othermod/PSPi-Version-6) | 19 | [4 comments](https://news.ycombinator.com/item?id=50038623) |
| [The Lightbulb Computer](https://lightbulbcomputer.com/) | 276 | [45 comments](https://news.ycombinator.com/item?id=50029487) |
| [Nix wrote half of my debugger](https://fzakaria.com/2026/10/07/nix-wrote-half-of-my-debugger) | 147 | [28 comments](https://news.ycombinator.com/item?id=50017247) |
| [Knuth reward check](https://www.thomas-huehn.com/knuth-reward-check/) | 159 | [61 comments](https://news.ycombinator.com/item?id=50034081) |
| [Veda: The First Agentic Hobby Operating System](https://github.com/vahmoh25/Veda) | 23 | [3 comments](https://news.ycombinator.com/item?id=50038473) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 12.0°C (54.0°F) |
| Average Humidity | 69% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-11 03:05:20 UTC*
