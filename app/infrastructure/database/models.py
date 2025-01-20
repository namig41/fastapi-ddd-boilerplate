from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    Table,
)
from sqlalchemy.orm import registry


mapper_registry = registry()
metadata = mapper_registry.metadata