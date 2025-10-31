#!/usr/bin/env python3
"""
Data Collection Script
Collects data from various public APIs and saves to raw data directory.
"""

import requests
import json
import csv
from datetime import datetime
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def ensure_directories():
    """Ensure required directories exist."""
    directories = ['data/raw', 'data/processed', 'data/archive']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    logger.info("Directories verified/created")


def collect_github_trending():
    """Collect trending repositories from GitHub."""
    logger.info("Collecting GitHub trending data...")
    
    try:
        # Using GitHub's public API (no auth required for basic data)
        url = "https://api.github.com/search/repositories"
        params = {
            'q': 'stars:>1000',
            'sort': 'stars',
            'order': 'desc',
            'per_page': 10
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract relevant information
        trending_repos = []
        for repo in data.get('items', [])[:10]:
            trending_repos.append({
                'name': repo['full_name'],
                'stars': repo['stargazers_count'],
                'language': repo['language'] or 'N/A',
                'description': (repo['description'] or 'No description')[:100],
                'url': repo['html_url'],
                'updated_at': repo['updated_at']
            })
        
        # Save to file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'data/raw/github_trending_{timestamp}.json'
        
        with open(filename, 'w') as f:
            json.dump({
                'collected_at': datetime.now().isoformat(),
                'source': 'GitHub API',
                'data': trending_repos
            }, f, indent=2)
        
        logger.info(f"GitHub trending data saved to {filename}")
        return trending_repos
        
    except Exception as e:
        logger.error(f"Error collecting GitHub data: {e}")
        return []


def collect_weather_data():
    """Collect weather data for major tech cities."""
    logger.info("Collecting weather data...")
    
    try:
        # Using wttr.in - a free weather API that doesn't require API key
        cities = ['Vancouver', 'Toronto', 'Seattle', 'San Francisco', 'New York']
        weather_data = []
        
        for city in cities:
            try:
                url = f"https://wttr.in/{city}?format=j1"
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                
                data = response.json()
                current = data['current_condition'][0]
                
                weather_data.append({
                    'city': city,
                    'temperature_c': current['temp_C'],
                    'temperature_f': current['temp_F'],
                    'condition': current['weatherDesc'][0]['value'],
                    'humidity': current['humidity'],
                    'wind_speed_kmph': current['windspeedKmph'],
                    'collected_at': datetime.now().isoformat()
                })
                
            except Exception as e:
                logger.warning(f"Error collecting weather for {city}: {e}")
                continue
        
        # Save to file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'data/raw/weather_{timestamp}.json'
        
        with open(filename, 'w') as f:
            json.dump({
                'collected_at': datetime.now().isoformat(),
                'source': 'wttr.in',
                'data': weather_data
            }, f, indent=2)
        
        logger.info(f"Weather data saved to {filename}")
        return weather_data
        
    except Exception as e:
        logger.error(f"Error collecting weather data: {e}")
        return []


def collect_crypto_prices():
    """Collect cryptocurrency prices."""
    logger.info("Collecting cryptocurrency data...")
    
    try:
        # Using CoinGecko public API (no auth required)
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            'ids': 'bitcoin,ethereum,cardano,solana,polkadot',
            'vs_currencies': 'usd',
            'include_24hr_change': 'true',
            'include_market_cap': 'true'
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        crypto_data = []
        for coin, info in data.items():
            crypto_data.append({
                'coin': coin,
                'price_usd': info.get('usd', 0),
                'market_cap': info.get('usd_market_cap', 0),
                'change_24h': info.get('usd_24h_change', 0),
                'collected_at': datetime.now().isoformat()
            })
        
        # Save to file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'data/raw/crypto_{timestamp}.json'
        
        with open(filename, 'w') as f:
            json.dump({
                'collected_at': datetime.now().isoformat(),
                'source': 'CoinGecko API',
                'data': crypto_data
            }, f, indent=2)
        
        logger.info(f"Crypto data saved to {filename}")
        return crypto_data
        
    except Exception as e:
        logger.error(f"Error collecting crypto data: {e}")
        return []


def main():
    """Main execution function."""
    logger.info("=" * 50)
    logger.info("Starting data collection pipeline")
    logger.info("=" * 50)
    
    # Ensure directories exist
    ensure_directories()
    
    # Collect data from various sources
    github_data = collect_github_trending()
    weather_data = collect_weather_data()
    crypto_data = collect_crypto_prices()
    
    # Summary
    logger.info("=" * 50)
    logger.info("Data collection complete!")
    logger.info(f"GitHub repos collected: {len(github_data)}")
    logger.info(f"Weather data points: {len(weather_data)}")
    logger.info(f"Crypto currencies: {len(crypto_data)}")
    logger.info("=" * 50)


if __name__ == "__main__":
    main()
