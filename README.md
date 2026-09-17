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

### GitHub Trending Repositories (Last Updated: 2026-09-17 02:36:59 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [ai-sucks-butt/ai-sucks-butt](https://github.com/ai-sucks-butt/ai-sucks-butt) | 1,882 | Python | If you think AI sucks, star the repo. |
| [Chuloo/mural](https://github.com/Chuloo/mural) | 1,261 | Kotlin | The language app you eventually delete. A native iPhone companion for learning t... |
| [yifanzhang-pro/recurrent-looped-tranformer](https://github.com/yifanzhang-pro/recurrent-looped-tranformer) | 861 | HTML | Official Project Page for Recurrent Looped Transformer (RLT) |
| [kruzovic7/ai-data-extractor](https://github.com/kruzovic7/ai-data-extractor) | 827 | Python | Free open-source extractor for AI coding assistant chat histories. Supports Clau... |
| [zjwzcx/Awesome-Astra-Embodied-AI](https://github.com/zjwzcx/Awesome-Astra-Embodied-AI) | 773 | N/A | GPT-6 Astra for embodied AI and robotics. |

### Hacker News Top Stories (Last Updated: 2026-09-17 02:36:59 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Nvidia announces native GPU programming in Rust](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/) | 329 | [131 comments](https://news.ycombinator.com/item?id=49724881) |
| [Training a 4B model to produce 81% faster query plans than Postgres](https://rohanbansal.com/qorl) | 417 | [85 comments](https://news.ycombinator.com/item?id=49731285) |
| [Xiaomi Mimo 2.6 live post-training dashboard](https://mimo.xiaomi.com/rl/) | 279 | [69 comments](https://news.ycombinator.com/item?id=49732270) |
| [Breaking the 1.58-bit Barrier for Ternary LLMs](https://arxiv.org/abs/2609.16338) | 148 | [20 comments](https://news.ycombinator.com/item?id=49732931) |
| [Backups Aren't Simple](https://filipovski.net/2026/09/16/backups-arent-simple.html) | 101 | [45 comments](https://news.ycombinator.com/item?id=49732513) |
| [Small programming tricks](https://will-keleher.com/posts/small-programming-tricks-matter/) | 412 | [186 comments](https://news.ycombinator.com/item?id=49729000) |
| [The engineering behind the US Strategic Petroleum Reserve](https://johnjwang.com/post/2026/09/15/engineering-behind-us-strategic-petroleum-reserve) | 118 | [43 comments](https://news.ycombinator.com/item?id=49719596) |
| [Developing provably correct Rust code with Verus](https://www.amazon.science/blog/developing-provably-correct-rust-code-with-verus) | 29 | [2 comments](https://news.ycombinator.com/item?id=49700153) |
| [OpenSpec – A lightweight and configurable AI spec framework](https://openspec.dev/) | 77 | [29 comments](https://news.ycombinator.com/item?id=49734264) |
| [The Return of Sail Power: Cargo Ships Are Turning Back to the Wind](https://gcaptain.com/the-return-of-sail-power-cargo-ships-are-turning-back-to-the-wind/) | 23 | [4 comments](https://news.ycombinator.com/item?id=49734929) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 17.0°C (63.0°F) |
| Average Humidity | 72% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-09-17 02:36:59 UTC*
