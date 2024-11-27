import subprocess
import os
import platform

class PeliasWrapper:
    def __init__(self):
        # Path to cli.js (ensure correct path to cli.js)
        self.cli_path = os.path.join(os.path.dirname(__file__), 'bin', 'cli.js')

        # Check if cli.js exists
        if not os.path.exists(self.cli_path):
            raise FileNotFoundError(f"{self.cli_path} not found. Ensure cli.js is included in the package.")

        # Check if Node.js is installed
        if not self._is_node_installed():
            self._install_node()

    def _is_node_installed(self):
        """Check if Node.js is installed."""
        try:
            subprocess.run(['node', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def _install_node(self):
        """Guide the user to install Node.js."""
        system = platform.system()
        if system == 'Linux':
            print("Node.js is not installed. Please install it using your package manager (e.g., `sudo apt install nodejs`).")
        elif system == 'Darwin':
            print("Node.js is not installed. You can install it using Homebrew: `brew install node`.") 
        elif system == 'Windows':
            print("Node.js is not installed. Download the installer from https://nodejs.org and follow the instructions.")
        else:
            raise EnvironmentError("Unsupported OS. Please install Node.js manually.")
        raise RuntimeError("Node.js is required to use this wrapper.")

    def run_command(self, command):
        """Run a command using the Pelias CLI, capture the output, and print it."""
        full_command = ['node', self.cli_path, command]
        try:
            # Run the Pelias CLI command and capture the output
            result = subprocess.run(
                full_command,
                check=True,
                text=True,
                capture_output=True
            )

            # Print the full output for debugging
            print("Full CLI Output:")
            print(result.stdout)

            # Optionally, write the full output to a text file for inspection
            with open('pelias_output.txt', 'w') as output_file:
                output_file.write(result.stdout)

            return result.stdout  # Return the output for further processing if needed

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Pelias CLI error: {e.stderr}") from e

