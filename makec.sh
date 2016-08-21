cd ./app/chatprocess
rm __init__.py
rm __init__.pyc
python setup.py build_ext --inplace
touch __init__.py
echo "from Engine import *" > __init__.py

