from typer import Typer
from .commands.optimize.command import optimize_app
from .commands.chat.command import chat_app
from .commands.evaluate.command import evaluate_app
from .commands.analyze.command import analyze_app
from .commands.visualize.command import visualize_app

app = Typer(name="heretic", help="LLM 定向去审查工具 - 极细粒度重构版", no_args_is_help=True)
app.add_typer(optimize_app, name="optimize")
app.add_typer(chat_app, name="chat")
app.add_typer(evaluate_app, name="evaluate")
app.add_typer(analyze_app, name="analyze")
app.add_typer(visualize_app, name="visualize")

if __name__ == "__main__":
    app()