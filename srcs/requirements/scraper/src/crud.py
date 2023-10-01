from sqlalchemy.orm import Session

import models
from Logger import logger

def add_category(db: Session, category: models.Category):
    logger.logger.info(f"New category addded to database: {category.category}")
    db.add(category)
    db.commit()