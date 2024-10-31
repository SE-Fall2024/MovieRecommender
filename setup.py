import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SaisumanthT",  # Replace with your own username
    version="1.0.0",
    author="Saisumanth,Sathwik,Rajasri",
    author_email="stallap@ncsu.edu",
    description="A recommendation engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SE-Fall2024/MovieRecommender",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
