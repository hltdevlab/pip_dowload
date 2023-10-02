# pip_dowload

# example for download whl:
pip download --dest ./downloaded_packages --only-binary=:all: --python-version 3.8.9 --platform win_amd64 [packages]

# example for download tar:
pip download --dest ./downloaded_packages --no-binary=:all: [packages]

# example for prefer binary
pip download --dest ./downloaded_packages --prefer-binary [packages]

# zip download_packages folder
zip -r downloaded_packages__[package].zip ./downloaded_packages

# clear downloaded_packages folder
rm ./downloaded_packages/*.*

# dry run install
pip install --dry-run [package] > [package]_requirements.txt
