This is a simple exercise to publish a package onto PyPi. In order to understand what the package is capable of, you need to run the command "from krasnikov import main"

Основной код проекта: 

```
from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='krasnikov',
  version='1.0.0',
  author='thebrrr',
  author_email='thebrrr2505@gmail.com',
  description='This is my first module',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='home_link',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='example python',
  project_urls={
    'Documentation': 'link'
  },
  python_requires='>=3.7'
)
```

В связи с проблемами на стороне testpypi, выгрузить пакет не получилось, но проект лежит в репозитории 
