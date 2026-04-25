from setuptools import setup, find_packages

setup(
    name="scene-reaper",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "scene-reaper=scene_reaper.main:main",
        ],
    },
    install_requires=[
        "opencv-python",
        "numpy",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for scene detection and extraction from media files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/Scene-Reaper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
