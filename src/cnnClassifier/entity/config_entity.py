from dataclasses import dataclass
from pathlib import Path

#dataclass to assign above any python class to consider it as an entity. It will not like be typical py class but like variables that can be acceses from other files

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen=True)  # True means if user is adding anything else here, that will show error. will not show anything else
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int