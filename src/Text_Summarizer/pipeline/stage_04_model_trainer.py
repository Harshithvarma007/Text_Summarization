from Text_Summarizer.config.configuration import ConfigurationManager
from Text_Summarizer.components.model_trainer import ModelTrainer

class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()     