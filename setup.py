from setuptools import find_packages
from setuptools import setup


def get_version():
    with open('version') as version_file:
        return version_file.read()


def get_requirements():
    with open('requirements.txt') as requirements_file:
        return [dependency.strip() for dependency in requirements_file if dependency.strip()]


def get_test_requirements():
    with open('tests/requirements.txt') as requirements_file:
        return [dependency.strip() for dependency in requirements_file if dependency.strip()]


setup_requires = [
    'pytest-runner',
    'flake8',
]

setup(name='appointment_service',
      version=get_version(),
      packages=find_packages(),
      include_package_data=True,
      install_requires=get_requirements(),
      tests_require=get_test_requirements(),
      setup_requires=setup_requires,
      entry_points="""\
      [paste.app_factory]
      main = appointment_service.server:serve
      """,
      )
