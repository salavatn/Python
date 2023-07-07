# Run tests and generate coverage report
echo '\n\n\n'
coverage run -m pytest #-v
echo '\n\n\n'

echo 'COVERAGE REPORT:'
coverage report
echo '\n\n\n'

echo 'COVERAGE HTML:'
coverage html > /dev/null
echo 'file:///Users/salavat/GitHub/Python/PetProject/FileInfo/htmlcov/index.html'
echo '\n\n\n'

# Clear cache
sh clear_cache.sh
