from setuptools import setup

setup(
    name='package-danyakr',
    version='0.1.0',
    description='Простой API для получения данных о погоде от OpenWeatherMap',
    author='danyakr',
    author_email='thebrrr2505@gmail.com',
    packages=['package-danyakr'],
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

