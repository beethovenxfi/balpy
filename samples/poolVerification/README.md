# Pool verification on Fantom

## Setup

Create a `.env` file in the root of the repo with the following contents:

    {
    "customRPC": "https://ftm.sakurarpc.io/",
    "etherscanApiKey": "<your_api_key>",
    "privateKey": "<your_private_key"
    }

Then initialize the git module with the following commands:

    git submodule update --init
    git submodule update --remote

And finally re-generate the pool ABIs by running in a terminal from the root of the repo:

    python3 generateMissingPoolArtifacts.py

## Run verification

1.  Go to [ftmscan](https://ftmscan.com) and lookup the address of the pool you just created
2.  Click on the tab **Internal Txns** and click on the transaction (or the one with **Contract Creation** in the **To** column if there are more transactions)
3.  Click on the tab **Logs** and find the log named **PoolRegistered**
4.  Doubleclick the value (which is the pool id) in **Topic 1** and copy it
5.  Open the file `poolVerification.py` in your favorite editor, paste the copied value into the `poolId` variable (don't forget to add `0x` in front of it again and save the file.
6.  Open a terminal and from the root of the repo run:

    `python3 ./samples/poolVerification/poolVerification.py`

7.  If all goes well you will be presented with a `yarn hardhat verify-contract` command string, copy it entirely and run it in a terminal from within the [balancer-deployments](https://github.com/balancer/balancer-deployments) repo
