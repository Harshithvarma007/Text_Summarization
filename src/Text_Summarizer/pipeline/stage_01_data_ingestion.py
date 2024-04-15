from Text_Summarizer.config.configuration import ConfigurationManager  

from Text_Summarizer.components.data_ingestion import DataIngestion
from Text_Summarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        
        pass
    def main(self):
        config=ConfigurationManager()
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()        
