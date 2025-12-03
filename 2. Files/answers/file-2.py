# Model solution for Exercise 2: Configuration Merger

from pathlib import Path
import pandas as pd
import json

# Read all config files
config_folder = Path('data/configs')
config_files = list(config_folder.glob('*.json'))

print(f"Found {len(config_files)} config files")

# Store configs by environment
configs = {}

for config_file in config_files:
    env_name = config_file.stem  # dev, staging, prod
    with open(config_file, 'r') as f:
        configs[env_name] = json.load(f)

print(f"Environments: {list(configs.keys())}")

# Flatten nested configs
def flatten_dict(d, parent_key='', sep='_'):
    """Flatten a nested dictionary"""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# Flatten all configs
flattened_configs = {}
for env, config in configs.items():
    flattened_configs[env] = flatten_dict(config)

# Create DataFrame
df_configs = pd.DataFrame(flattened_configs)

print("\nConfiguration comparison across environments:")
print(df_configs)

print("\n" + "="*60)

# Identify settings that differ
print("\nSettings that differ across environments:")
for setting in df_configs.index:
    values = df_configs.loc[setting]
    if values.nunique() > 1:  # More than one unique value
        print(f"\n{setting}:")
        for env, value in values.items():
            print(f"  {env}: {value}")