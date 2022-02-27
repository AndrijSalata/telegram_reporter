from setuptools import setup

setup(
    name='telegramm_report_bot_ua',
    version='1.1',
    install_requires=[
        'questionary~=1.10.0',
        'Telethon~=1.24.0',
    ],
    entry_points={
        'console_scripts': [
            'telegram_reporter=telegram_reporter.main:main',
        ],
    }
)