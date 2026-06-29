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

### GitHub Trending Repositories (Last Updated: 2026-06-29 02:40:56 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | 2,322 | Python | DeepSpec: a full-stack codebase for training and evaluating speculative decoding... |
| [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | 2,292 | HTML | Codex 橙皮书：从安装到实战案例的全链路 Codex 使用指南（非官方开源，含可下载 PDF） |
| [bikini/exploitarium](https://github.com/bikini/exploitarium) | 2,221 | Python | A single archive of public exploit PoCs and vulnerability research writeups. At ... |
| [Yu9191/wloc](https://github.com/Yu9191/wloc) | 1,117 | JavaScript | 修改 Apple 网络定位（gs-loc）返回坐标 · 支持 Surge / Quantumult X / Loon / Stash · 快捷指令一键设置/恢复... |
| [winsznx/theeleven](https://github.com/winsznx/theeleven) | 698 | TypeScript | Eleven autonomous AI agents open live football prop markets on X Layer — custom ... |

### Hacker News Top Stories (Last Updated: 2026-06-29 02:40:56 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [GLM 5.2 beats Claude in our benchmarks](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/) | 486 | [239 comments](https://news.ycombinator.com/item?id=48709670) |
| [Historical memory prices 1960-2026](https://dam.stanford.edu/memory-prices.html) | 175 | [72 comments](https://news.ycombinator.com/item?id=48710092) |
| [Knowledge Distillation of Black-Box Large Language Models (2024)](https://arxiv.org/abs/2401.07013) | 56 | [12 comments](https://news.ycombinator.com/item?id=48712420) |
| [5k menus from the New York Public Library’s Buttolph Collection (1880-1920)](https://pudding.cool/2026/06/menu-story/) | 331 | [86 comments](https://news.ycombinator.com/item?id=48707763) |
| [I used Claude Code to get a second opinion on my MRI](https://antoine.fi/mri-analysis-using-claude-code-opus) | 359 | [464 comments](https://news.ycombinator.com/item?id=48708941) |
| [Deciphering Basmala](https://blog.plover.com/lang/bismillah.html) | 17 | [4 comments](https://news.ycombinator.com/item?id=48657131) |
| [Better Images of AI](https://betterimagesofai.org/) | 16 | [11 comments](https://news.ycombinator.com/item?id=48713051) |
| [AI boom risks global financial crash, warn central bankers](https://www.telegraph.co.uk/business/2026/06/28/ai-boom-risks-global-financial-crash-central-bankers-warn/) | 31 | [12 comments](https://news.ycombinator.com/item?id=48713697) |
| [TOP500 at ISC’26: We have a New Number 1 Supercomputer](https://chipsandcheese.com/p/top500-at-isc26-we-have-a-new-number) | 77 | [37 comments](https://news.ycombinator.com/item?id=48710775) |
| [The Boeing 747 begins its final descent](https://www.theatlantic.com/magazine/2026/07/boeing-747-retirement/687304/) | 145 | [199 comments](https://news.ycombinator.com/item?id=48675295) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 19.0°C (66.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-06-29 02:40:56 UTC*
