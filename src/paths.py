from pathlib import Path
import os

# Use the current working directory as a fallback when __file__ is not defined
PARENT_DIR = Path(os.getcwd()).resolve()
DATA_DIR = PARENT_DIR / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
TRANSFORMED_DATA_DIR = DATA_DIR / 'transformed'
DATA_CACHE_DIR = DATA_DIR / 'cache'

MODELS_DIR = PARENT_DIR / 'models'

# Create directories if they don't exist
for directory in [DATA_DIR, RAW_DATA_DIR, TRANSFORMED_DATA_DIR, DATA_CACHE_DIR, MODELS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
    
