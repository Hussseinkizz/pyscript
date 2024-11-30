# Pyscript Tools v0.0.1

A comprehensive toolkit for PyScript development, providing commands for project initialization, development server, production builds, testing, and code analysis.

## Installation

From PyPI (recommended):
```bash
pip install pyscript-tools
```

For development:
```bash
git clone https://github.com/yourusername/pyscript-tools
cd pyscript-tools
pip install -e .
```

## Available Commands

### `pyscript init [PROJECT_NAME]`
Initialize a new PyScript project. This command is fully implemented and:
- Creates a new project directory (or uses current directory with ".")
- Sets up initial project structure
- Copies template files

Example:
```bash
pyscript init my-app     # Create in new directory
pyscript init .          # Initialize in current directory
```

## Planned Features (Work in Progress)

The following commands are currently placeholders and will be implemented in future releases:

### `pyscript serve` (TODO)
Development server with hot reload
```bash
pyscript serve           # Default port 8000
pyscript serve -p 3000   # Custom port
```

### `pyscript build` (TODO)
Production build process
```bash
pyscript build          # Basic build
pyscript build --no-optimize  # Skip optimization
```

### `pyscript test` (TODO)
Test runner with watch mode
```bash
pyscript test           # Run tests once
pyscript test -w        # Watch mode
```

### `pyscript lint` (TODO)
Code analysis and best practices
```bash
pyscript lint          # Check code
pyscript lint --fix    # Auto-fix issues
```

## Contributing

This project is under active development. Feel free to contribute by implementing any of the planned features or suggesting new ones.

## License

[MIT License](LICENSE)
