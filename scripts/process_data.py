#!/usr/bin/env python3
"""
Data Processing Script
Processes raw data and generates insights.
"""

import json
import glob
import pandas as pd
from datetime import datetime
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_latest_file(pattern):
    """Get the most recent file matching the pattern."""
    files = glob.glob(pattern)
    if not files:
        return None
    return max(files, key=os.path.getctime)


def process_github_data():
    """Process GitHub trending data."""
    logger.info("Processing GitHub data...")
    
    try:
        latest_file = get_latest_file('data/raw/github_trending_*.json')
        if not latest_file:
            logger.warning("No GitHub data file found")
            return None
        
        with open(latest_file, 'r') as f:
            data = json.load(f)
        
        # Convert to DataFrame for easier processing
        df = pd.DataFrame(data['data'])
        
        # Save processed data
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f'data/processed/github_processed_{timestamp}.csv'
        df.to_csv(output_file, index=False)
        
        logger.info(f"Processed GitHub data saved to {output_file}")
        return df
        
    except Exception as e:
        logger.error(f"Error processing GitHub data: {e}")
        return None


def process_weather_data():
    """Process weather data for Vancouver."""
    logger.info("Processing weather data...")
    
    try:
        latest_file = get_latest_file('data/raw/weather_*.json')
        if not latest_file:
            logger.warning("No weather data file found")
            return None
        
        with open(latest_file, 'r') as f:
            data = json.load(f)
        
        # Convert to DataFrame
        df = pd.DataFrame(data['data'])
        
        # Add some calculated fields
        df['temperature_c'] = pd.to_numeric(df['temperature_c'])
        df['humidity'] = pd.to_numeric(df['humidity'])
        
        # Calculate average temperature for Vancouver
        avg_temp = df['temperature_c'].mean()
        logger.info(f"Average temperature for Vancouver: {avg_temp:.1f}°C")
        
        # Save processed data
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f'data/processed/weather_processed_{timestamp}.csv'
        df.to_csv(output_file, index=False)
        
        logger.info(f"Processed weather data saved to {output_file}")
        return df
        
    except Exception as e:
        logger.error(f"Error processing weather data: {e}")
        return None


def process_crypto_data():
    """Process cryptocurrency data."""
    logger.info("Processing crypto data...")
    
    try:
        latest_file = get_latest_file('data/raw/crypto_*.json')
        if not latest_file:
            logger.warning("No crypto data file found")
            return None
        
        with open(latest_file, 'r') as f:
            data = json.load(f)
        
        # Convert to DataFrame
        df = pd.DataFrame(data['data'])
        
        # Format numbers
        df['price_usd'] = pd.to_numeric(df['price_usd'])
        df['change_24h'] = pd.to_numeric(df['change_24h'])
        
        # Add trend indicator
        df['trend'] = df['change_24h'].apply(lambda x: '📈' if x > 0 else '📉')
        
        # Save processed data
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f'data/processed/crypto_processed_{timestamp}.csv'
        df.to_csv(output_file, index=False)
        
        logger.info(f"Processed crypto data saved to {output_file}")
        return df
        
    except Exception as e:
        logger.error(f"Error processing crypto data: {e}")
        return None


def generate_summary():
    """Generate summary statistics."""
    logger.info("Generating summary statistics...")
    
    summary = {
        'generated_at': datetime.now().isoformat(),
        'github_repos_analyzed': 0,
        'weather_cities_tracked': 0,
        'crypto_currencies_tracked': 0
    }
    
    try:
        # Count processed files
        github_files = glob.glob('data/processed/github_processed_*.csv')
        weather_files = glob.glob('data/processed/weather_processed_*.csv')
        crypto_files = glob.glob('data/processed/crypto_processed_*.csv')
        
        if github_files:
            df = pd.read_csv(github_files[-1])
            summary['github_repos_analyzed'] = len(df)
        
        if weather_files:
            df = pd.read_csv(weather_files[-1])
            summary['weather_cities_tracked'] = len(df)
        
        if crypto_files:
            df = pd.read_csv(crypto_files[-1])
            summary['crypto_currencies_tracked'] = len(df)
        
        # Save summary
        with open('data/processed/summary.json', 'w') as f:
            json.dump(summary, f, indent=2)
        
        logger.info("Summary generated successfully")
        return summary
        
    except Exception as e:
        logger.error(f"Error generating summary: {e}")
        return summary


def main():
    """Main execution function."""
    logger.info("=" * 50)
    logger.info("Starting data processing pipeline")
    logger.info("=" * 50)
    
    # Process all data sources
    github_df = process_github_data()
    weather_df = process_weather_data()
    crypto_df = process_crypto_data()
    
    # Generate summary
    summary = generate_summary()
    
    # Log results
    logger.info("=" * 50)
    logger.info("Data processing complete!")
    logger.info(f"GitHub repos: {summary['github_repos_analyzed']}")
    logger.info(f"Weather cities: {summary['weather_cities_tracked']}")
    logger.info(f"Crypto currencies: {summary['crypto_currencies_tracked']}")
    logger.info("=" * 50)


if __name__ == "__main__":
    main()
