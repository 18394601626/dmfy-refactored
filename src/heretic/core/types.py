from pydantic import BaseModel, Field
from typing import Dict
class AblationConfig(BaseModel):
    direction_indices: list[int] = Field(...)
    kernel_weights: Dict[str, float] = Field(default_factory=dict)
class ResidualDirection(BaseModel):
    vector: list[float]
    layer: int
    component: str