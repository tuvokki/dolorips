VER=`pipenv run bump`
pipenv run python setup.py sdist bdist_wheel
pipenv run twine upload --repository-url https://pip.tuvok.nl/ dist/dolorips-$VER*
