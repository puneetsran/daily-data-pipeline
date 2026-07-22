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

### GitHub Trending Repositories (Last Updated: 2026-07-22 01:51:06 UTC)
| Repository | Stars | Language | Description |
|------------|-------|----------|-------------|
| [lopopolo/harness-engineering](https://github.com/lopopolo/harness-engineering) | 1,626 | Python | 🐎 Ryan Lopopolo’s anthology, field guide, and agent context bundle for harness e... |
| [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | 1,285 | JavaScript | Your clothes, extracted and organized with gpt-image. |
| [pablostanley/yoinks](https://github.com/pablostanley/yoinks) | 964 | TypeScript | yoink any video from your terminal. no shady ads. |
| [nethical6/conversation-steganography](https://github.com/nethical6/conversation-steganography) | 911 | Go | Use LLMs to hide messages inside normal looking conversations |
| [v-modal/vmodal_sdk_flutter](https://github.com/v-modal/vmodal_sdk_flutter) | 777 | Dart | V- Modal AI: Search anything anywhere SDK Flutter |

### Hacker News Top Stories (Last Updated: 2026-07-22 01:51:06 UTC)
| Title | Score | Discussion |
|-------|-------|------------|
| [OpenAI and Hugging Face address security incident during model evaluation](https://openai.com/index/hugging-face-model-evaluation-security-incident/) | 720 | [480 comments](https://news.ycombinator.com/item?id=48997548) |
| [Kimi K3 Is Competitive with Fable; Kimi K3 and Fable Is SoTA](https://fireworks.ai/blog/kimik3-fable) | 292 | [155 comments](https://news.ycombinator.com/item?id=48999291) |
| [FreeInk: Open ecosystem for e-readers](https://freeink.org/) | 411 | [102 comments](https://news.ycombinator.com/item?id=48996318) |
| [A digestion of the Jacobian conjecture counterexample](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/) | 168 | [53 comments](https://news.ycombinator.com/item?id=48998362) |
| [Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/) | 618 | [492 comments](https://news.ycombinator.com/item?id=48993414) |
| [Advertise in ChatGPT](https://ads.openai.com/) | 307 | [309 comments](https://news.ycombinator.com/item?id=48996571) |
| ["Drawing" the Mona Lisa with GPT-5.6, Claude, Gemini, and Grok](https://www.tryai.dev/blog/ai-drawing-arena-colored-pencils-claude-gpt-grok) | 111 | [39 comments](https://news.ycombinator.com/item?id=48998404) |
| [Long presumed dead, a thriving coral reef is discovered in West Africa](https://e360.yale.edu/digest/benin-coral-reef) | 304 | [56 comments](https://news.ycombinator.com/item?id=48993816) |
| [Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting](https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git) | 245 | [220 comments](https://news.ycombinator.com/item?id=48995213) |
| [Apple defeats liability for not scanning iCloud for CSAM](https://blog.ericgoldman.org/archives/2026/07/apple-defeats-liability-for-not-scanning-icloud-for-csam-but-the-judge-was-not-pleased-amy-v-apple.htm) | 350 | [329 comments](https://news.ycombinator.com/item?id=48992870) |

### Weather Data Summary

| Metric | Value |
|--------|-------|
| City Tracked | Vancouver |
| Average Temperature | 33.0°C (92.0°F) |
| Average Humidity | 32% |
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

*This README is automatically updated by the data pipeline. Last update: 2026-07-22 01:51:06 UTC*
