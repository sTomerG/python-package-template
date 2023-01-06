# type: ignore[attr-defined]
import typer
from rich.console import Console

from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} import version
from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}.logger import logger


app = typer.Typer(
    name="{{ cookiecutter.project_name }}",
    help="{{ cookiecutter.project_description }}",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]{{ cookiecutter.project_name }}[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command()
def main(
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the {{ cookiecutter.project_name }} package.",
    ),
) -> None:
 
    ...
    
    # last line
    logger.info("Executed program without unexpected exception!")


if __name__ == "__main__":
    try:
        app()
    except BaseException
        logger.error("Error happened!", exc_info=True)
