import argparse
import subprocess

def pip_download(
    package=None,
    python_version="3.8.9",
    dest="./downloaded"
):
    # List of platform tags
    platform_tags = [
        "win32",
        "win_amd64",
        "manylinux1_x86_64",
        "manylinux2010_x86_64",
        "manylinux2014_x86_64",
        "manylinux_2_17_x86_64",
        "manylinux_2_5_i686",
        "manylinux_2_12_i686",
        # "macosx_10_6_intel",
        # "macosx_10_9_x86_64",
        "any"
    ]

    # Common options for pip download command
    common_options = [
        "pip", "download",
        "--python-version", python_version,
        "--only-binary=:all:",
        "--dest", dest
    ]

    for platform in platform_tags:
        # Construct the pip download command
        command = common_options + ["--platform", platform]

        # Add the package or -r requirements.txt option
        if package is None:
            command += ["-r", "requirements.txt"]
        else:
            command.append(package)

        # Run the command using subprocess and capture output
        try:
            result = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                check=True
            )
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error downloading packages for platform {platform}: {e}")
            print(e.stderr)

# Commented out the argument parser lines at the end
# import argparse
# parser = argparse.ArgumentParser(description="Download package for specific platform and Python version")
# parser.add_argument("--package", help="Package name and version")
# parser.add_argument("--python-version", default="3.8.9", help="Python version (default: 3.8.9)")
# parser.add_argument("--dest", default="./downloaded", help="Destination directory (default: ./downloaded)")
# args = parser.parse_args()



if __name__ == "__main__":
    # Commented out the execution of the function
    pip_download(args.package, args.python_version, args.dest)
