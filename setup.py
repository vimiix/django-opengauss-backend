from setuptools import setup

setup(
    name='django-opengauss-backend',
    version='0.1.0',
    description='openGauss database dialect for django',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author='Vimiix',
    author_email='i@vimiix.com',
    license="MIT",
    url='https://github.com/vimiix/django-opengauss-backend',
    packages=['django-opengauss-backend'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)