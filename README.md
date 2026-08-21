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

### GitHub Trending Repositories (Last Updated: 2026-08-21 00:47:33 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 160,428 | TypeScript | DeepSeek Harness: Everything is a Plugin. |
| [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | 13,593 | TypeScript | 为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。 |
| [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | 8,897 | Python | A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表 |
| [yjh051108/dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) | 6,037 | PowerShell | dsh-routing-suite — injector + router-standard kit: install the runtime injector... |
| [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | 3,559 | JavaScript | Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard... |

### Hacker News Top Stories (Last Updated: 2026-08-21 00:47:33 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [The August 17 outage, and the work ahead](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/) | 291 | [335 comments](https://news.ycombinator.com/item?id=49378957) |
| [Copyright does not protect AI-generated content in EU](https://mathstodon.xyz/@maxpool/117128107757895678) | 20 | [10 comments](https://news.ycombinator.com/item?id=49382041) |
| [Consumer Rights Wiki](https://consumerrights.wiki/w/Main_Page) | 205 | [22 comments](https://news.ycombinator.com/item?id=49378243) |
| [I like 'em thick: an apology to my English teachers](https://www.experimental-history.com/p/i-like-em-thick) | 545 | [252 comments](https://news.ycombinator.com/item?id=49347543) |
| [Aaron Swartz was prosecuted for scraping, while Meta does it without consequence](https://blog.curiousquail.com/im-upset-again-about-a-co-creator-of-rss-being-prosecuted-for-something-meta-is-doing-with-little-consequence/) | 852 | [197 comments](https://news.ycombinator.com/item?id=49379550) |
| [AliExpress runs silent WebAudio fingerprinting that breaks Bluetooth multipoint](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html) | 864 | [281 comments](https://news.ycombinator.com/item?id=49372583) |
| [I should have loved biology (2020)](https://jsomers.net/i-should-have-loved-biology/) | 188 | [71 comments](https://news.ycombinator.com/item?id=49377853) |
| [HTML Can Do That](https://chrisburnell.com/html-can-do-that/) | 552 | [155 comments](https://news.ycombinator.com/item?id=49362689) |
| [Malicious Rust crate Arrayref runs a build-time payload](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) | 383 | [357 comments](https://news.ycombinator.com/item?id=49374269) |
| [CIA funding helped keep NeXT afloat in the 80s](https://www.wsj.com/tech/steve-jobs-apple-next-cia-161b65f9?st=NWWds1&reflink=desktopwebshare_permalink) | 321 | [206 comments](https://news.ycombinator.com/item?id=49368886) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 28.0°C (82.0°F) |
| Average Humidity | 53% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-08-21 00:47:33 UTC*
