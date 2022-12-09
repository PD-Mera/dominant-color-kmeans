import setuptools

setuptools.setup(
    name="DominantColor",
    version="0.0.1",
    author="PD-Mera",
    author_email="phuongdong1772000@gmail.com",
    description="Using K-means to get dominant colors of an image",
    long_description="This project simply using list of RGB pixels to clustering dominant colors using K-means",
    long_description_content_type="text/markdown",
    url="https://github.com/PD-Mera/Dominant-Color-Kmeans",
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt').readlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)