from src.utils import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj= DataIngestionTrainPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=========")
except Exception as e:
    logger.exception(e)
    raise e

















# from src.utils import logger
# # from src import logger

# logger.info("This is a test for custom logs")






# # create ml functions