python -m build --sdist .
python -m build --wheel .

echo ""
echo "Connect to PyPi and upload project:"

python -m twine upload dist/*