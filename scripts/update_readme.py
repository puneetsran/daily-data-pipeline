#!/usr/bin/env python3
"""
README Update Script
Updates the README.md file with the latest processed data.
"""

import json
import glob
import pandas as pd
from datetime import datetime
import logging
import os
import re

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


def format_github_table(df):
    """Format GitHub data as a markdown table."""
    if df is None or len(df) == 0:
        return "| *Data will be populated by automated pipeline* | - | - | - |"
    
    table_rows = []
    for _, row in df.head(5).iterrows():  # Show top 5
        name = row['name']
        stars = f"{int(row['stars']):,}"
        language = row['language']
        description = row['description'][:80] + "..." if len(row['description']) > 80 else row['description']
        
        table_rows.append(f"| [{name}]({row['url']}) | {stars} | {language} | {description} |")
    
    return "\n".join(table_rows)


def format_weather_table(df):
    """Format weather data as a markdown table."""
    if df is None or len(df) == 0:
        return "| *Data will be populated by automated pipeline* | - |"
    
    # Calculate summary statistics
    avg_temp_c = df['temperature_c'].mean()
    avg_temp_f = df['temperature_f'].mean()
    avg_humidity = df['humidity'].mean()
    
    cities_list = ", ".join(df['city'].tolist())
    
    table_rows = [
        f"| Cities Tracked | {cities_list} |",
        f"| Average Temperature | {avg_temp_c:.1f}°C ({avg_temp_f:.1f}°F) |",
        f"| Average Humidity | {avg_humidity:.0f}% |",
        f"| Data Points | {len(df)} cities |"
    ]
    
    return "\n".join(table_rows)


def update_readme():
    """Update the README.md file with latest data."""
    logger.info("Updating README.md...")
    
    try:
        # Read current README
        with open('README.md', 'r') as f:
            readme_content = f.read()
        
        # Get latest processed data
        github_file = get_latest_file('data/processed/github_processed_*.csv')
        weather_file = get_latest_file('data/processed/weather_processed_*.csv')
        
        github_df = None
        weather_df = None
        
        if github_file:
            github_df = pd.read_csv(github_file)
            logger.info(f"Loaded GitHub data: {len(github_df)} repositories")
        else:
            logger.warning("No GitHub data file found")
        
        if weather_file:
            weather_df = pd.read_csv(weather_file)
            logger.info(f"Loaded weather data: {len(weather_df)} cities")
        else:
            logger.warning("No weather data file found")
        
        # Format tables
        github_table = format_github_table(github_df)
        weather_table = format_weather_table(weather_df)
        
        # Get current timestamp
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        
        # Update GitHub Trending section
        github_pattern = r'(### GitHub Trending Repositories \(Last Updated:)[^)]*(\).*?\| Repository \| Stars \| Language \| Description \|.*?\|[-\s|]+\|)(.*?)(\n\n###|\n\n##)'
        github_replacement = rf'\1 {current_time}\2\n{github_table}\4'
        readme_content = re.sub(github_pattern, github_replacement, readme_content, flags=re.DOTALL)
        
        # Update Weather Data section
        weather_pattern = r'(### Weather Data Summary.*?\| Metric \| Value \|.*?\|[-\s|]+\|)(.*?)(\n\n##)'
        weather_replacement = rf'\1\n{weather_table}\3'
        readme_content = re.sub(weather_pattern, weather_replacement, readme_content, flags=re.DOTALL)
        
        # Update the final timestamp at the bottom
        timestamp_pattern = r'\*This README is automatically updated by the data pipeline\. Last update: .*?\*'
        timestamp_replacement = f'*This README is automatically updated by the data pipeline. Last update: {current_time}*'
        readme_content = re.sub(timestamp_pattern, timestamp_replacement, readme_content)
        
        # Write updated README
        with open('README.md', 'w') as f:
            f.write(readme_content)
        
        logger.info("README.md updated successfully!")
        return True
        
    except Exception as e:
        logger.error(f"Error updating README: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main execution function."""
    logger.info("=" * 50)
    logger.info("Starting README update")
    logger.info("=" * 50)
    
    success = update_readme()
    
    if success:
        logger.info("=" * 50)
        logger.info("README update complete!")
        logger.info("=" * 50)
    else:
        logger.error("README update failed!")
        exit(1)


if __name__ == "__main__":
    main()
