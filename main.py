from Text_Summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

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
