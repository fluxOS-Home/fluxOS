import os
import subprocess
import json
import argparse
import platform

print("FluxOS Control  Utility")
print("FluxOS is running")
print("========================")
print(f"Running as: {os.getlogin()}")
print(f"Home Directory:{os.path.expanduser('~')}")
print("\nSystem information:")
subprocess.run(["uname","-a"])

with open("config/fluxos.json", "r") as file:
	config = json.load(file)

print(f"FluxOS version: {config['version']}")
print(f"Security enabled: {config['security']['enabled']}")

def system_info():
	print("\nSystem Information")
	print("======================")

	print(f"User: {os.getlogin()}")
	print(f"Home: {os.path.expanduser('~')}")

	print("\nKernel")
	subprocess.run(["uname","-r"])

	print("\nArchitecture")
	subprocess.run(["uname","-m"])

      
	print("\nCPU")

	with open("/proc/cpuinfo", "r") as file:
		cpuinfo = file.read()

	model="unknown"
	for line in cpuinfo.splitlines():
		if line.startswith("model name"):
			print(f"Model:{line.split(':',1)[1].strip()}")
			break

	cores = cpuinfo.count("processor\t:")
	print(f"Model: {model}")
       	print f"Cores: {cores}")
	
	print("\nHostname")
	subprocess.run(["hostname"])

	print("\nUptime")
	subprocess.run(["uptime","-p"])

	print(f"\nFluxOS Version: {config['version']}")
	print(f"security Enabled: {config['security']['enabled']}")

def main():
	parser = argparse.ArgumentParser(
	prog="fluxctl",
	description="FluxOS Control Utility"
)
	subparsers  = parser.add_subparsers(dest="command")

	system_parser= subparsers.add_parser("system")
	system_subparser=system_parser.add_subparsers(dest="system_command")

	system_subparser.add_parser("info")
	
	args = parser.parse_args()

	if args.command =="system":
		if args.system_command=="info":
			system_info()
		else:
			system_parser.print_help()
	else:
		parser.print_help()

if __name__ == "__main__":
	main()
