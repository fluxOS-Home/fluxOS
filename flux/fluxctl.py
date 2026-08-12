import os
import subprocess

print("FluxOS Control  Utility")
print("FluxOS is running")
print("========================")
print(f"Running as: {os.getlogin()}")
print(f"Home Directory:{os.path.expanduser('~')}")
print("\nSystem information:")
subprocess.run(["uname","--a"])
