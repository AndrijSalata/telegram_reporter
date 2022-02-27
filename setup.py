from setuptools import setup

setup(
    name='telegram_reporter',
    version='1.1',
    install_requires=[
        'questionary~=1.10.0',
        'Telethon~=1.24.0',
    ],
    scripts=['telegram_reporter/main.py'],
    entry_points={
        'console_scripts': [
            'telegram_reporter=telegram_reporter:run',
        ],
    }
)