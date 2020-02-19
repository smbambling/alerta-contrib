
from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name="alerta-federation",
    version=version,
    description='Alerta plugin for federation',
    url='https://github.com/alerta/alerta-contrib',
    license='MIT',
    author='Steven Bambling',
    author_email='smbambling@gmail.com',
    packages=find_packages(),
    py_modules=['alerta_federation'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'alerta'
    ],
    entry_points={
        'alerta.plugins': [
            'federation = alerta_federation:FederateAlert'
        ]
    }
)
