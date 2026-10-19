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

### GitHub Trending Repositories (Last Updated: 2026-10-19 02:33:07 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill) | 2,920 | Python | Qwen-Image 2.1 NSFW/姿势出图 skill：作者级提示词配方 + NSFW LoRA + 136 姿势 VNCCS 人偶控制；适用 Claud... |
| [feder-cr/git-ai](https://github.com/feder-cr/git-ai) | 2,305 | Go | Git designed for AI agents. |
| [HeyPuter/everything](https://github.com/HeyPuter/everything) | 2,225 | JavaScript | We're rebuilding and open-sourcing the world’s software from scratch. |
| [Gathin23/tv-vibehack](https://github.com/Gathin23/tv-vibehack) | 2,159 | Java | Your TV, minus the ads. Debloat any Android TV over ADB and give it a clean, tvO... |
| [ahwootech/BRUTAL](https://github.com/ahwootech/BRUTAL) | 1,906 | C# | A free, open source C# framework for making games, or your own game engine. Dire... |

### Hacker News Top Stories (Last Updated: 2026-10-19 02:33:07 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Hybrid Reasoning Agents: LLM agents that think in latent space, act through text](https://arxiv.org/abs/2610.18861) | 229 | [139 comments](https://news.ycombinator.com/item?id=50145337) |
| [William Gibson and the trademarking of cyberspace](https://colo.to/cyberspace.html) | 76 | [5 comments](https://news.ycombinator.com/item?id=50146625) |
| [There's never been a better time to go into math (by: 3blue1brown) [video]](https://www.youtube.com/watch?v=LKrwhjOI8Nc) | 185 | [177 comments](https://news.ycombinator.com/item?id=50136150) |
| [If you don't run your own LLM proxy, how do you know whats going on?](https://jrdsgl.com/if-you-dont-run-your-own-llm-proxy-how-the-fuck-do-you-even-know-whats-going-on/) | 43 | [31 comments](https://news.ycombinator.com/item?id=50145507) |
| [Someone behind the software](https://karrisaarinen.com/posts/someone-behind-the-software/) | 324 | [137 comments](https://news.ycombinator.com/item?id=50142573) |
| [Laptop Based on 6502 CPU](https://www.maddox.pro/?p=448) | 39 | [15 comments](https://news.ycombinator.com/item?id=50111537) |
| [Free Pascal compiler now supports dynamic packages](https://www.getlazarus.org/dynamic/) | 116 | [23 comments](https://news.ycombinator.com/item?id=50144066) |
| [RepRapMicron](https://github.com/VikOlliver/RepRapMicron/wiki) | 335 | [55 comments](https://news.ycombinator.com/item?id=50141076) |
| [Show HN: WhatsApp MCP running free on Cloudflare](https://github.com/finereli/whatsapp-mcp) | 48 | [34 comments](https://news.ycombinator.com/item?id=50145715) |
| [Dogs seem to agree with humans that 'bouba' is round and 'kiki' is spiky](https://www.sciencealert.com/dogs-seem-to-agree-with-humans-that-bouba-is-round-and-kiki-is-spiky) | 137 | [83 comments](https://news.ycombinator.com/item?id=50136979) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 11.0°C (52.0°F) |
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

*This README is automatically updated by the data pipeline. Last update: 2026-10-19 02:33:07 UTC*
