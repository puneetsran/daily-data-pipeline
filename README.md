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

### GitHub Trending Repositories (Last Updated: 2026-10-08 03:43:46 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [openai/math](https://github.com/openai/math) | 10,045 | Lean | No description |
| [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) | 2,120 | JavaScript | Answer me with HTML — an agent skill that answers hard questions with a one-page... |
| [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 1,814 | JavaScript | 艺术动画skill：35种艺术风格、9种解说语法，用代码让画动起来。 |
| [facebookincubator/muse-gadget-sdk](https://github.com/facebookincubator/muse-gadget-sdk) | 1,676 | C | Open source SDK to build Muse gadgets |
| [kargulstudio/sales-crm](https://github.com/kargulstudio/sales-crm) | 1,637 | TypeScript | No description |

### Hacker News Top Stories (Last Updated: 2026-10-08 03:43:46 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5) | 733 | [371 comments](https://news.ycombinator.com/item?id=49996437) |
| [Margaret Hamilton has died](https://news.mit.edu/2026/margaret-hamilton-computing-pioneer-dies-1007) | 951 | [109 comments](https://news.ycombinator.com/item?id=49998895) |
| [Cleo (Mathematician)](https://en.wikipedia.org/wiki/Cleo_(mathematician)) | 66 | [7 comments](https://news.ycombinator.com/item?id=49982445) |
| [How did Rosalind Franklin miss the helix in her iconic DNA image? She didn't](https://www.science.org/content/article/how-did-rosalind-franklin-miss-helix-her-iconic-dna-image-she-didn-t) | 96 | [44 comments](https://news.ycombinator.com/item?id=49969073) |
| [Living off-grid: Hundred Rabbits](https://100r.ca/site/home.html) | 33 | [6 comments](https://news.ycombinator.com/item?id=49970767) |
| ['Jonathan' is the oldest land animal on Earth](https://www.404media.co/oldest-living-land-animal-jonathan-the-tortoise/) | 84 | [33 comments](https://news.ycombinator.com/item?id=49998066) |
| [Show HN: Bigwords.page – Turn any screen into a sign. The URL is the app](https://bigwords.page/) | 401 | [116 comments](https://news.ycombinator.com/item?id=49994443) |
| [GPT‑6 and Intelligent UI for everyone](https://openai.com/index/gpt-6-for-everyone/) | 539 | [280 comments](https://news.ycombinator.com/item?id=49996425) |
| [Shipping JPEG XL in Chrome](https://developer.chrome.com/blog/jpeg-xl-in-chrome) | 507 | [344 comments](https://news.ycombinator.com/item?id=49991227) |
| [Docker Agent](https://github.com/docker/docker-agent) | 196 | [87 comments](https://news.ycombinator.com/item?id=49996259) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 14.0°C (57.0°F) |
| Average Humidity | 81% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-08 03:43:46 UTC*
