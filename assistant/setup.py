from setuptools import setup, find_namespace_packages

setup(name='assistant',
      version='1',
      description='Very useful user helper',
      url='https://github.com/aleksVoit/Python_web/tree/master/modul_2(Poetry%2BDocker)/docker_test',
      author='Flying Circus',
      author_email='aleksandr.voitushenko@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=['prompt_toolkit'],
      entry_points={'console_scripts': [
            'assistant = assistant.__main__:main'
      ]}
      )
