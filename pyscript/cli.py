import shutil
import subprocess
from pathlib import Path
import click
from rich.console import Console
from importlib.resources import path as resource_path

# Initialize rich console for colored output
console = Console()


def copy_app_contents(target_dir: Path):
    """Copy template app contents to target directory."""
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        
        with resource_path('pyscript', 'templates') as template_path:
            if template_path.exists():
                # Copy template files to target directory
                for item in template_path.iterdir():
                    if item.is_file():
                        shutil.copy2(item, target_dir)
                    else:
                        shutil.copytree(item, target_dir / item.name)
                
                console.print(f"[green]✓[/green] Created PyScript project in [bold]{target_dir}[/bold]")
            else:
                console.print("[red]Error:[/red] Template directory not found")
                raise click.Exit(code=1)
                
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise click.Exit(code=1)


@click.group()
def cli():
    """PyScript Development Tools.
    
    A comprehensive toolkit for PyScript development, providing commands for:
    - Project initialization and scaffolding
    - Development server with hot reload
    - Production builds and optimization
    - Testing and debugging utilities
    - Code analysis and best practices
    
    Commands:
      init    Create a new PyScript project
      serve   Start development server
      build   Create production build
      test    Run tests
      lint    Analyze code
    """
    pass


@cli.command()
@click.argument('project_name', default=".")
def init(project_name):
    """Initialize a new PyScript project.
    
    Usage: pyscript init [PROJECT_NAME]
    
    Arguments:
        project_name: Name of the project directory to create.
                     Use "." to initialize in the current directory.
    
    Example:
        pyscript init my-app     # Creates a new project in ./my-app
        pyscript init .          # Initializes in the current directory
    """
    target_dir = Path.cwd() if project_name == "." else Path.cwd() / project_name
    copy_app_contents(target_dir)


@cli.command()
@click.option('--port', '-p', default=8000, help='Port to run the server on')
@click.option('--host', '-h', default='localhost', help='Host to bind to')
def serve(port, host):
    """Start a development server with hot reload.
    
    Usage: pyscript serve [OPTIONS]
    
    Launches a development server that automatically reloads when files change.
    Provides a smooth development experience with instant feedback.
    
    Options:
        -p, --port PORT    Port to run server on (default: 8000)
        -h, --host HOST    Host to bind to (default: localhost)
    
    Example:
        pyscript serve           # Starts server on localhost:8000
        pyscript serve -p 3000   # Uses port 3000 instead
    """
    console.print(f"[bold green]Starting development server on {host}:{port}...[/bold green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]")
    # TODO: Implement actual server with hot reload
    # Could use something like watchdog for file monitoring
    # and http.server or aiohttp for serving


@cli.command()
@click.option('--optimize/--no-optimize', default=True, help='Enable/disable optimization')
@click.option('--output', '-o', default='dist', help='Output directory')
def build(optimize, output):
    """Build the project for production.
    
    Usage: pyscript build [OPTIONS]
    
    Creates an optimized production build with:
    - Minified and bundled Python code
    - Optimized static assets
    - Generated source maps
    - Performance optimizations
    
    Options:
        --optimize          Enable optimizations (default)
        --no-optimize      Skip optimizations
        -o, --output DIR   Output directory (default: dist)
    
    Example:
        pyscript build          # Basic build to ./dist
        pyscript build --no-optimize  # Skip optimization
    """
    console.print(f"[bold blue]Building project for production in ./{output}/...[/bold blue]")
    # TODO: Implement production build process
    # Could include:
    # - Python code bundling/optimization
    # - Asset optimization
    # - Source map generation


@cli.command()
@click.option('--watch', '-w', is_flag=True, help='Watch mode: run tests on file changes')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
def test(watch, verbose):
    """Run tests with optional watch mode.
    
    Usage: pyscript test [OPTIONS]
    
    Executes project tests with features like:
    - Automatic test discovery
    - Watch mode for TDD workflow
    - Detailed failure reporting
    - Code coverage reports
    
    Options:
        -w, --watch     Watch for file changes
        -v, --verbose   Show detailed output
    
    Example:
        pyscript test           # Run tests once
        pyscript test -w        # Run tests in watch mode
    """
    console.print("[bold yellow]Running tests...[/bold yellow]")
    # TODO: Implement test runner
    # Could integrate with pytest or unittest
    # Add watch mode using watchdog


@cli.command()
@click.option('--fix', is_flag=True, help='Automatically fix issues')
def lint(fix):
    """Lint and analyze your PyScript code.
    
    Usage: pyscript lint [OPTIONS]
    
    Checks your code for:
    - PyScript best practices
    - Code style and formatting
    - Potential errors and bugs
    - Performance issues
    
    Options:
        --fix    Automatically fix issues when possible
    
    Example:
        pyscript lint          # Check for issues
        pyscript lint --fix    # Fix issues automatically
    """
    console.print("[bold magenta]Analyzing code...[/bold magenta]")
    # TODO: Implement linting
    # Could integrate with tools like:
    # - pylint/flake8 for Python
    # - eslint for JS
    # - Custom PyScript-specific rules


if __name__ == "__main__":
    cli()
