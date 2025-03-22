import typer  # type: ignore[import]
from rich.console import Console  # type: ignore[import]
from rich.panel import Panel  # type: ignore[import]

from .agents import agents  # type: ignore[import]


app = typer.Typer()

console = Console()


@app.command()
def ask(
    agent_name: str = typer.Argument(
        ..., help=f"The name of the agent to use. Available: {list(agents.keys())}"),

    question: str = typer.Argument(..., help="The question to ask the agent.")
):
    """
    Ask a question to the agent and get a response.
    """
    agent = agents[agent_name]
    response = agent.run_sync(question).data

    title = "🤖 SYSTEM RESPONSE"

    panel = Panel.fit(
        f"[cyan]{response}[cyan]", title=title, border_style="bright_blue")
    console.print(panel)
