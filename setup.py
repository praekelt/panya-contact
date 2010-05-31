from setuptools import setup, find_packages

setup(
    name='django-contact',
    version='dev',
    description='Django site contact app.',
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='https://github.com/praekelt/django-contact',
    packages = find_packages(),
    install_requires = [
        'django-honeypot',
    ],
    include_package_data=True,
)
