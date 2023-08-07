import sys
import os

path = os.getcwd()
sys.path.append(path)

import balpy
import ast

def main():
	network = "fantom"
	customConfigFile = os.path.join('customConfig', 'fantom.json')
	with open(".env", "r") as data:
		manualEnv = ast.literal_eval(data.read())
	poolId = "0x7761DDB82E5B81AD56FFB7B99F6FFF59514EA2C3000200000000000000000776"
	# On Ethereum, Ethereum testnets & Fantom, you can pass creationHash=None
	# On Polygon, you must pass the pool creation hash to generate verification params
	creationHash = None;
	# creationHash = "0x18c7e1c9235c6e93878e55a87ed249f9d0ceb9d12ee584794e92f80f7645686d";
	verbose = False;

	bal = balpy.balpy.balpy(network, customConfigFile=customConfigFile, manualEnv = manualEnv);
	isVerified = bal.isContractVerified(poolId, verbose=verbose);
	if not isVerified:
		command = bal.balGeneratePoolCreationArguments(poolId, verbose=verbose, creationHash=creationHash);
	else:
		print("Pool is already verified")
		quit();
	
	print()
	print(command)
	print()

	print("If you need more complete instructions on what to do with this command, go to:");
	print("\thttps://dev.balancer.fi/resources/pools/verification\n");
	
if __name__ == '__main__':
	main();
