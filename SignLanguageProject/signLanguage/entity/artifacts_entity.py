from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_path: str
    data_zip_file_path: str