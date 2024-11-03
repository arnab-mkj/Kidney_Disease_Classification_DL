from dataclasses import dataclass
from pathlib import Path

#dataclass to assign above any python class to consider it as an entity. It will not like be typical py class but like variables that can be acceses from other files

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path