from Text_Summarizer.constants import *
from Text_Summarizer.utils.common import read_yaml, create_directories
from Text_Summarizer.entity import DataIngestionConfiguration

class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH):    
        self.config= read_yaml(config_filepath)
        self.params =read_yaml(params_filepath)
        create_directories([self.config.artifacts])

    def get_data_ingestion_config(self)-> DataIngestionConfiguration:
        config=self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config= DataIngestionConfiguration(
            root_dir=config.root_dir,
            source_url =config.source_url,
            local_data_file =config.local_data_file,
            unzip_dir =config.unzip_dir
        )
        return data_ingestion_config