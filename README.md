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

### GitHub Trending Repositories (Last Updated: 2026-07-23 01:58:21 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [lopopolo/harness-engineering](https://github.com/lopopolo/harness-engineering) | 2,194 | Python | 🐎 Ryan Lopopolo’s anthology, field guide, and agent context bundle for harness e... |
| [nethical6/conversation-steganography](https://github.com/nethical6/conversation-steganography) | 986 | Go | Use LLMs to hide messages inside normal looking conversations |
| [MIgHTy-alIeN/MEV-Arbitrage-Bot](https://github.com/MIgHTy-alIeN/MEV-Arbitrage-Bot) | 920 | Solidity | An arbitrage bot is a smart contract connected to an external automation script ... |
| [Blaizzy/nativ](https://github.com/Blaizzy/nativ) | 762 | Swift | Local AI, native to your Mac. Chat, serve, monitor, and connect MLX models from ... |
| [Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs) | 631 | TypeScript | Dotted thought-orb loading indicators for AI & agent UIs — six tuned states, two... |

### Hacker News Top Stories (Last Updated: 2026-07-23 01:58:21 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [Terrence Tao's ChatGPT Conversation about the Jacobian Conjecture Counterexample](https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56) | 615 | [376 comments](https://news.ycombinator.com/item?id=49010345) |
| [Quality non-fiction books are the antithesis of AI slop](https://resobscura.substack.com/p/quality-non-fiction-books-are-the) | 158 | [75 comments](https://news.ycombinator.com/item?id=49007247) |
| [GigaToken: ~1000x faster Language model tokenization](https://github.com/marcelroed/gigatoken/) | 370 | [72 comments](https://news.ycombinator.com/item?id=49010167) |
| [Show HN: Bento - An entire PowerPoint in one HTML file (edit+view+data+collab)](https://bento.page/slides/) | 653 | [150 comments](https://news.ycombinator.com/item?id=49008211) |
| [Medici family mystery may be solved after more than 400 years](https://www.cnn.com/2026/07/15/science/medici-family-mystery-dna-malaria) | 78 | [18 comments](https://news.ycombinator.com/item?id=49014007) |
| [Are AI Labs Pelicanmaxxing?](https://dylancastillo.co/posts/pelicanmaxxing.html) | 398 | [156 comments](https://news.ycombinator.com/item?id=49010129) |
| [Everyone Should Know SIMD](https://mitchellh.com/writing/everyone-should-know-simd) | 257 | [73 comments](https://news.ycombinator.com/item?id=49010648) |
| [Show HN: Cactus Hybrid: We taught Gemma 4 to know when it's wrong](https://github.com/cactus-compute/cactus-hybrid) | 67 | [12 comments](https://news.ycombinator.com/item?id=49010782) |
| [Malleable Computing, Emacs, and You](http://yummymelon.com/devnull/malleable-computing-emacs-and-you.html) | 68 | [16 comments](https://news.ycombinator.com/item?id=49013538) |
| [John C. Dvorak has died](https://twitter.com/na_announce/status/2079952538040672302) | 555 | [176 comments](https://news.ycombinator.com/item?id=49012070) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 31.0°C (87.0°F) |
| Average Humidity | 39% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-23 01:58:21 UTC*
