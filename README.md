# pip_dowload

# example for download whl:
pip download --dest ./downloaded_packages --only-binary=:all: --python-version 3.8.9 --platform win_amd64 <packages>

# example for download tar:
pip download --dest ./downloaded_packages --only-binary=:none: <packages>
