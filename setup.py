from setuptools import setup, find_packages

setup(
    name='correspondence_management',
    version='1.0.0',
    description='Enterprise Correspondence Management System',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'qrcode',
        'python-barcode'
    ]
)
