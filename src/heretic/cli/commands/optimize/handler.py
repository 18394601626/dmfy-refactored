from ....core.config.settings import HereticSettings
from ....core.optimization.runner import OptimizationRunner
def run_optimization(config_path: str):
    settings = HereticSettings()
    runner = OptimizationRunner(settings)
    runner.run()