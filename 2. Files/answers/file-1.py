# solution for Exercise 1: Filter and Combine Log Files

from pathlib import Path
import pandas as pd

# Get all log files
log_folder = Path('data/logs')
log_files = list(log_folder.glob('*.log'))

print(f"Found {len(log_files)} log files")

# Read and filter logs
all_logs = []

for log_file in log_files:
    with open(log_file, 'r') as f:
        for line in f:
            line = line.strip()
            if 'ERROR' in line or 'WARNING' in line:
                # Parse the line
                parts = line.split(maxsplit=3)  # Split into 4 parts max
                if len(parts) >= 4:
                    timestamp = f"{parts[0]} {parts[1]}"
                    level = parts[2]
                    message = parts[3]
                    server = log_file.stem  # Get filename without extension
                    
                    all_logs.append({
                        'timestamp': timestamp,
                        'level': level,
                        'message': message,
                        'server': server
                    })

# Create DataFrame
df_logs = pd.DataFrame(all_logs)

# Sort by timestamp
df_logs['timestamp'] = pd.to_datetime(df_logs['timestamp'])
df_logs = df_logs.sort_values('timestamp').reset_index(drop=True)

print("\nFiltered and combined logs:")
print(df_logs)

print(f"\nTotal ERROR/WARNING entries: {len(df_logs)}")
print(f"Errors: {len(df_logs[df_logs['level'] == 'ERROR'])}")
print(f"Warnings: {len(df_logs[df_logs['level'] == 'WARNING'])}")

# Group by server
print("\nIssues by server:")
print(df_logs.groupby('server')['level'].value_counts())