from abc import ABC, abstractmethod
from ..types import AblationConfig
class BaseModelWrapper(ABC):
    @abstractmethod
    def load(self): pass
    @abstractmethod
    def compute_residuals(self, prompts): pass
    @abstractmethod
    def apply_ablation(self, config): pass