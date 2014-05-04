from setuptools import setup, find_packages

setup(
    name='wonder_tool',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts':
            'wonder = wonder_tool.main:wonder_main'
    },
    zip_safe=False,
    classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
    ],
)
