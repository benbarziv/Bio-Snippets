from setuptools import setup, find_packages

setup(
    name="bio_snippets",           
    version="0.1.0",
    author="Your Name",
    description="Reusable Biopython helper functions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/bio_snippets",
    packages=find_packages(),      
    install_requires=[
        "biopython>=1.79",
    ],
    python_requires=">=3.7",
)
