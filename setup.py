import subprocess

import setuptools

with open("README.md", "r") as readme:
    readme = readme.read()

with open("requirements.txt", "r") as requirements:
    requirements = requirements.read()

setuptools.setup(
    name="udls",  # Replace with your own username
    version=subprocess.check_output([
        "git",
        "describe",
        "--abbrev=0",
    ]).strip().decode(),
    author="Antoine CAILLON",
    author_email="caillon@ircam.fr",
    description="Base class and presets for fast dataset creation inside IRCAM",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts":
        ["resample = udls.resample:main", "duration = udls.duration:main"]
    },
    install_requires=requirements.split("\n"),
    python_requires='>=3.7',
)
