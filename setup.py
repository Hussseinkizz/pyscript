from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyscript-tools",
    version="0.0.1",
    author="Hussein Kizz",
    author_email="hssnkizz@gmail.com",
    description="A comprehensive toolkit for PyScript development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hussseinkizz/pyscript-tools",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click>=8.0.0", "rich>=10.0.0"],
    entry_points={
        "console_scripts": [
            "pyscript=pyscript.cli:cli",
        ],
    },
    package_data={
        "pyscript": ["templates/*"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Pyscript :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
