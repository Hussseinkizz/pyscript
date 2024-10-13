import shutil
from pathlib import Path
import typer
from rich.console import Console
from importlib.resources import path as resource_path

console = Console()
cli = typer.Typer()


def copy_app_contents(target_dir: Path):
    """
    Copy the contents of the app/ directory into the target directory.
    """
    # Get the path to the 'app' directory within the package
    with resource_path('pyscript', 'app') as app_dir:
        app_dir = Path(app_dir)

        if not app_dir.exists():
            console.print("[bold red]App directory not found![/bold red]")
            raise typer.Exit(code=1)

        console.print("Creating your project, hold tight...")

        try:
            # Ensure the target directory exists
            target_dir.mkdir(parents=True, exist_ok=True)

            # Copy the contents of the 'app' directory to the target directory
            for item in app_dir.iterdir():
                dest = target_dir / item.name
                if item.is_dir():
                    shutil.copytree(item, dest)
                else:
                    shutil.copy(item, dest)

            console.print(f"\n🔥 Project created at {target_dir}!")
        except Exception as e:
            console.print(f"[bold red]Error: {e}[/bold red]")
            raise typer.Exit(code=1)


@cli.command()
def init(project_name: str):
    """
    Initializes a new project by copying the template files.
    """
    target_dir = Path.cwd() / project_name
    copy_app_contents(target_dir)


if __name__ == "__main__":
    cli()
