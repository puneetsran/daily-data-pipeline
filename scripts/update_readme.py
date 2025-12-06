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
        language = row['language'] if pd.notna(row['language']) else 'N/A'
        description = row['description'][:80] + "..." if len(row['description']) > 80 else row['description']
        
        table_rows.append(f"| [{name}]({row['url']}) | {stars} | {language} | {description} |")
    
    return "\n".join(table_rows)


def format_weather_table(df):
    """Format weather data as a markdown table."""
    if df is None or len(df) == 0:
        return "| *Data will be populated by automated pipeline* | - |"
    
    # Calculate summary statistics for Vancouver
    avg_temp_c = df['temperature_c'].mean()
    avg_temp_f = df['temperature_f'].mean()
    avg_humidity = df['humidity'].mean()
    
    city_name = df['city'].iloc[0] if len(df) > 0 else "Vancouver"
    
    table_rows = [
        f"| City Tracked | {city_name} |",
        f"| Average Temperature | {avg_temp_c:.1f}°C ({avg_temp_f:.1f}°F) |",
        f"| Average Humidity | {avg_humidity:.0f}% |",
        f"| Data Points | {len(df)} |"
    ]
    
    return "\n".join(table_rows)


def update_readme():
    """Update the README.md file with latest data."""
    logger.info("Updating README.md...")
    
    try:
        # Read current README
        with open('README.md', 'r') as f:
            lines = f.readlines()
        
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
        
        # Process line by line
        new_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Update GitHub section
            if line.startswith('### GitHub Trending Repositories'):
                new_lines.append(f'### GitHub Trending Repositories (Last Updated: {current_time})\n')
                i += 1
                # Skip until we find the table header
                while i < len(lines) and not lines[i].startswith('| Repository'):
                    i += 1
                if i < len(lines):
                    new_lines.append(lines[i])  # Add header
                    i += 1
                    if i < len(lines) and lines[i].startswith('|---'):
                        new_lines.append(lines[i])  # Add separator
                        i += 1
                    # Skip old data rows until next section
                    while i < len(lines) and not lines[i].startswith('###') and not lines[i].startswith('##'):
                        if lines[i].strip() and not lines[i].startswith('|'):
                            break
                        i += 1
                    # Add new data
                    new_lines.append(github_table + '\n')
                    new_lines.append('\n')  # Add blank line after table
                continue
            
            # Update Weather section
            elif line.startswith('### Weather Data Summary'):
                new_lines.append(line)
                i += 1
                # Skip until we find the table header
                while i < len(lines) and not lines[i].startswith('| Metric'):
                    new_lines.append(lines[i])
                    i += 1
                if i < len(lines):
                    new_lines.append(lines[i])  # Add header
                    i += 1
                    if i < len(lines) and lines[i].startswith('|---'):
                        new_lines.append(lines[i])  # Add separator
                        i += 1
                    # Skip old data rows until next section
                    while i < len(lines) and not lines[i].startswith('##'):
                        if lines[i].strip() and not lines[i].startswith('|'):
                            break
                        i += 1
                    # Add new data
                    new_lines.append(weather_table + '\n')
                    new_lines.append('\n')  # Add blank line after table
                continue
            
            # Update timestamp at bottom
            elif '*This README is automatically updated' in line:
                new_lines.append(f'*This README is automatically updated by the data pipeline. Last update: {current_time}*\n')
                i += 1
                continue
            
            new_lines.append(line)
            i += 1
        
        # Write updated README
        with open('README.md', 'w') as f:
            f.writelines(new_lines)
        
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
