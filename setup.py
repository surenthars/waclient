from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="waclient",
    version="0.1.0",
    author="Surenthar",
    author_email="surentharsenthilkumar2003@gmail.com",
    description="Simplified Python SDK for WhatsApp Business Cloud API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Start-up-Kraft/waclient",
    packages=find_packages(where="waclient"),
    package_dir={"": "waclient"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Chat",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",

    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.9",
        ],
    },
    keywords="whatsapp business api cloud meta facebook messaging",
    project_urls={
        "Bug Reports": "https://github.com/Start-up-Kraft/waclient/issues",
        "Source": "https://github.com/Start-up-Kraft/waclient",
        "Documentation": "https://github.com/Start-up-Kraft/waclient#readme",
    },
)
