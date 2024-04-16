from Text_Summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from Text_Summarizer.pipeline.stasge_03_data_transformation import DataTransformationPipeline
from Text_Summarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from Text_Summarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from Text_Summarizer.logging import logger



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    dataingestion=DataIngestionTrainingPipeline()
    dataingestion.main()
    logger.info(f">>>>>>>stage {STAGE_NAME} completed <><<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    datavalidation=DataValidationPipeline()
    datavalidation.main()
    logger.info(f">>>>>>>stage {STAGE_NAME} completed <><<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    datavalidation=DataTransformationPipeline()
    datavalidation.main()
    logger.info(f">>>>>>>stage {STAGE_NAME} completed <><<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    modeltrainer=ModelTrainerPipeline()
    modeltrainer.main()
    logger.info(f">>>>>>>stage {STAGE_NAME} completed <><<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e