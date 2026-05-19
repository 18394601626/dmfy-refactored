from typer import Typer, Option
from ....core.config.settings import HereticSettings
optimize_app = Typer(help="定向消融参数优化")
@optimize_app.callback()
def main(config: str = Option("config.default.toml", "--config", "-c")):
    from .handler import run_optimization
    run_optimization(config)