# Pixi Installation & Usage Guide

### Install Pixi

To get started with Pixi, simply run:
```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

This command will download and run the Pixi installation script, setting up Pixi on your system. Make sure you have `curl` installed before running this command.

### Install All Packages in `pyproject.toml`

After installation, use Pixi to install all required packages listed in your `pyproject.toml` file:
```bash
pixi install
```

This command reads the `pyproject.toml` file and installs all the dependencies specified there, ensuring your environment is properly set up.

### Running with CUDA or CPU Support

To run your project with CUDA support for GPU acceleration:
```bash
pixi run -e cuda python your_script.py
```

This command runs the specified Python script with CUDA support enabled, which is ideal for machine learning or other GPU-intensive tasks.

Or, if you prefer to run with CPU support:
```bash
python your_script.py
```

Replace `your_script.py` with the name of the script you want to run. This command will use the default Python environment without GPU acceleration.

### Installing a New Package

1. **Search on [prefex.dev](https://prefex.dev)**:
   - If the package is available, install it using:
     ```bash
     pixi add {package_name}
     ```

   Pixi will add the package to your project and update the `pyproject.toml` file accordingly.

2. **Search on [PyPI](https://pypi.org)**:
   - If not available on prefex.dev, search on PyPI and run:
     ```bash
     pixi add {package_name} --pypi
     ```

   This command will install the package from PyPI and add it to your `pyproject.toml` file, ensuring compatibility with your project.

### Updating Packages

To update all installed packages to their latest versions, run:
```bash
pixi update
```

This command will check for newer versions of all installed packages and update them.

To update a specific package, use:
```bash
pixi update {package_name}
```

Replace `{package_name}` with the name of the package you want to update. This is useful if you only want to update one package without affecting others.

### Removing a Package

If you need to remove a package, run the following command:
```bash
pixi remove {package_name}
```

This command will uninstall the specified package and remove it from the `pyproject.toml` file, keeping your project dependencies clean.

### Listing Installed Packages

To see a list of all currently installed packages, use:
```bash
pixi list
```

This command provides a summary of all the packages currently installed in your environment, along with their versions.

### Clean Up Cache

To clean up unnecessary cache files and free up space, run:
```bash
pixi clean
```

This command will remove old package caches and temporary files, helping to keep your environment tidy and free up disk space.

### Running the TTS Server

To run the TTS (Text-To-Speech) server, use the following command:
```bash
python tts_server/server.py --debug --host 127.0.0.1 --port 5050
```

This command will start the TTS server in debug mode, running on `localhost` (127.0.0.1) and port `5050`.

### Testing the TTS Server

To test the TTS server, you can use the following `curl` command to send a POST request:
```bash
curl -X POST -H "Content-Type: application/json" -H "Accept: audio/wav" \
     -d '{"sessionId": 1234, "voice": "en-f-1", "text": "Jack Server Not Running: The error indicates that the Jack server is not running or cannot be started. Jack is often used for professional audio applications. If you\'re not using Jack, you can ignore these errors, or you could install and start Jack with:", "seed": 5678}' \
     http://127.0.0.1:5050/tts --output - | aplay -B 1000
```

This command sends a request to the TTS server, generating audio from the given text. The resulting audio is then played using `aplay`.

Happy coding with Sunsilkk! 🚀
# TTS-Server
