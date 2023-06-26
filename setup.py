import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ffmpeg_streaming",
    version="0.0.1",
    author="Vamsidhar Yeddu",
    author_email="vamsidhar666@gmail.com",
    description="fork of python-ffmpeg-video-streaming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yvd/python-ffmpeg-video-streaming",
    project_urls={
        "Bug Tracker": "https://github.com/yvd/python-ffmpeg-video-streaming/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)