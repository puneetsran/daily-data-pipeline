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

### GitHub Trending Repositories (Last Updated: 2026-10-21 02:39:42 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | 13,456 | Python | DeepInfer: High-performance, large-scale inference framework for DeepSeek models |
| [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | 12,459 | Java | Debloat any Android or Google TV over Wi-Fi and get an Apple TV-style home. |
| [ly05010419/MacNativeGames](https://github.com/ly05010419/MacNativeGames) | 2,912 | C | No description |
| [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) | 1,965 | Python | Ears for coding agents: let AI hear, review and make sound. CPU-only, open sourc... |
| [simbasjungles/free-my-tv](https://github.com/simbasjungles/free-my-tv) | 1,879 | Java | A fast, ad-free home screen for Google TV. Open source, built with Claude Code. ... |

### Hacker News Top Stories (Last Updated: 2026-10-21 02:39:42 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Show HN: SimCity, but with Permits](https://permit.petercai.com/) | 595 | [304 comments](https://news.ycombinator.com/item?id=50170593) |
| [Learning to live with Waymos](https://www.newyorker.com/magazine/2026/10/19/were-learning-to-live-with-waymos-its-going-weird) | 18 | [13 comments](https://news.ycombinator.com/item?id=50175057) |
| [Feds suspect ransom negotiator ran ShinyHunters extortion site](https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/) | 113 | [40 comments](https://news.ycombinator.com/item?id=50173487) |
| [Good type against all odds](https://unsung.aresluna.org/good-type-against-all-odds/) | 20 | [4 comments](https://news.ycombinator.com/item?id=50175059) |
| [Voxtral 3](https://mistral.ai/news/voxtral-3/) | 540 | [143 comments](https://news.ycombinator.com/item?id=50168396) |
| [The Other Epidemic: Trying to get off benzodiazepines](https://www.thebeliever.net/the-other-epidemic/) | 79 | [52 comments](https://news.ycombinator.com/item?id=50173891) |
| [Google open-sources TorchTPU, a native PyTorch back end for TPUs](https://github.com/google-pytorch/torch_tpu) | 273 | [64 comments](https://news.ycombinator.com/item?id=50169053) |
| [What shall I teach my son?](https://stevekrouse.com/ends) | 283 | [348 comments](https://news.ycombinator.com/item?id=50169707) |
| [Academics have a duty to defend open knowledge systems like Wikipedia](https://blogs.lse.ac.uk/impactofsocialsciences/2026/10/19/academics-have-a-duty-to-defend-open-knowledge-systems-like-wikipedia/) | 148 | [82 comments](https://news.ycombinator.com/item?id=50170917) |
| [SlopCodeBench 10/2026 – Opus 5.5, Astra wins overall, xhigh considered harmful](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md) | 183 | [81 comments](https://news.ycombinator.com/item?id=50108717) |

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

*This README is automatically updated by the data pipeline. Last update: 2026-10-21 02:39:42 UTC*
