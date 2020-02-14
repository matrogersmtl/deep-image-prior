from setuptools import setup, find_packages

setup(
    name="deep-image-prior",
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Framework :: Jupyter",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.6",
)
