from typer import Typer

app = Typer(name="heretic", help="LLM 定向去审查工具")

if __name__ == "__main__":
    app()