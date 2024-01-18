[![Tests](https://github.com/gislab-augsburg/ckanext-glab/workflows/Tests/badge.svg?branch=main)](https://github.com/gislab-augsburg/ckanext-glab/actions)

# ckanext-glab

Ckanext-glab provides functionality to GDPR regulations with its module gdpr:
- API access on user_list und user_show is limited to system and organization admins. 
- GUI access user list, user details and user activity is limited to system and organization admins. 
- API user_show, GUI user details and user activity is still available for a user's own account.
Organinization admins need access for user management of their organizations.

Most of the code is extracted from https://github.com/qld-gov-au/ckanext-qgov.


## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.6 and earlier | not tested    |
| 2.7             | not tested    |
| 2.8             | not tested    |
| 2.9             | yes           |
| 2.10            | not tested    |


## Installation

To install ckanext-glab GDPR functions:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com/gislab-augsburg/ckanext-glab.git
    cd ckanext-glab
    pip install -e .

3. Add `gdpr` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


## Config settings

None at present


## Developer installation

To install ckanext-glab for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/gislab-augsburg/ckanext-glab.git
    cd ckanext-glab
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-glab

If ckanext-glab should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
