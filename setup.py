from setuptools import setup, find_packages

setup(
    name="pyscript",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer>=0.3.2",
        "rich>=10.0.0"
    ],
    entry_points={
        "console_scripts": [
            "pyscript=pyscript.cli:cli",
        ],
    },
    package_data={
        "pyscript": ["app/*"],
    },
)
