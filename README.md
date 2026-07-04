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

### GitHub Trending Repositories (Last Updated: 2026-07-04 02:04:19 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [Krishnagangwal/CS-Fundamentals](https://github.com/Krishnagangwal/CS-Fundamentals) | 1,510 | N/A | Curated CS fundamentals for placement prep: DSA,Computer Networks, DBMS & SQL, O... |
| [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | 1,296 | Python | No description |
| [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | 1,251 | JavaScript | Standalone iOS app to spoof GPS location without jailbreak. Includes Shadowrocke... |
| [Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills) | 801 | N/A | A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): re... |
| [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | 523 | Python | Let Claude (or any LLM) actually watch a video — scene-aware, deduplicated frame... |

### Hacker News Top Stories (Last Updated: 2026-07-04 02:04:19 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Giant trees have no trouble pumping water to top branches](https://news.exeter.ac.uk/faculty-of-environment-science-and-economy/giant-trees-have-no-trouble-pumping-water-to-top-branches/) | 85 | [39 comments](https://news.ycombinator.com/item?id=48780870) |
| [Leanstral 1.5: Proof Abundance for All](https://mistral.ai/news/leanstral-1-5/) | 85 | [22 comments](https://news.ycombinator.com/item?id=48780801) |
| [MSI Center – How to gain SYSTEM privileges in seconds](https://mrbruh.com/msicenter/) | 22 | [6 comments](https://news.ycombinator.com/item?id=48781688) |
| [GLM5.2 on AMD MI355X at 2626 tok/s/node at over 2x lower cost than Blackwell](https://www.wafer.ai/blog/glm52-amd) | 92 | [25 comments](https://news.ycombinator.com/item?id=48780417) |
| [Steam Controller Auto-Charge – pilot to magnetic charging puck using CV](https://github.com/FossPrime/Steam-Controller-Auto-Charge) | 68 | [11 comments](https://news.ycombinator.com/item?id=48780865) |
| [SearXNG: A free internet metasearch engine](https://github.com/searxng/searxng) | 133 | [41 comments](https://news.ycombinator.com/item?id=48779454) |
| [The circuit that lets your brain think and see](https://www.engineering.columbia.edu/about/news/circuit-lets-your-brain-think-and-see) | 38 | [4 comments](https://news.ycombinator.com/item?id=48780996) |
| [Amsterdam invented the fire department](https://worksinprogress.co/issue/how-amsterdam-invented-the-fire-department/) | 38 | [9 comments](https://news.ycombinator.com/item?id=48780913) |
| [Jamesob's guide to running SOTA LLMs locally](https://github.com/jamesob/local-llm) | 277 | [125 comments](https://news.ycombinator.com/item?id=48775921) |
| [Applied Category Theory Course (2018)](https://math.ucr.edu/home/baez/act_course/index.html) | 54 | [7 comments](https://news.ycombinator.com/item?id=48779723) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 20.0°C (68.0°F) |
| Average Humidity | 68% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-04 02:04:19 UTC*
