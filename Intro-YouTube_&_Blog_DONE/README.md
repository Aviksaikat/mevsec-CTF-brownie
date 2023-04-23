# Intro-YouTube & Blog DONE

![](../media/yt_blog.png)

## Challenge

- https://ctf.mevsec.com/challenges#Intro%20-%20YouTube%20&%20Blog-8

This challenge is an introduction and the writeup is available here on youtube => Writeup - MevSecurity This will explain how the MevSec CTF works and introduce the community.

- To start the challenge please use :

  - curl 'http://5.196.27.132:8080/create_challenge?challenge_number=0'

- To check all the available commands use :

  - curl http://5.196.27.132:8080/

  The challenge will be solved when there are no funds left inside the wallet. Hope you will join us!

Good luck with the bearmarket!

Creator: Ethnical#0954

# Solution

- Put the `Setup.sol` & `VideoChalllengeIntro.sol` in the `contracts` folder.

- Follow the steps shown in the [README.md](../README.md) file of the project.

- Now in the project setup you will see these `scripts`

```js
scripts
├── deploy.py
├── get_data.py
├── hack.py
├── helpful_scripts.py
└── submit.py
```

- `deploy.py` will help to deploy the contracts locally for testing.

- You can ignore the `get_data.py` script as I was trying to automate the curl process but don't know why it was not working

- `hack.py` will solve the challenge

- `helpful_scripts.py` contains the helper scripts

- `submit.py` will submit the instance for the challenge

### Solve

- Run locally by running

```js
brownie run scripts/hack.py

Brownie v1.19.3 - Python development framework for Ethereum

IntroYoutubeBlogDoneProject is the active project.

Launching 'ganache-cli --chain.vmErrorsOnRPCResponse true --wallet.totalAccounts 10 --hardfork istanbul --fork.url https://eth-mainnet.alchemyapi.io/v2/<API_KEY> --miner.blockGasLimit 12000000 --wallet.mnemonic brownie --server.port 8545 --chain.chainId 1'...

Running 'scripts/hack.py::main'...
Transaction sent: 0xb5772d6085a22a3276868343b64d84d48247895516aa538a24c1f15b60ab9f97
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 10
  Setup.constructor confirmed   Block: 17112229   Gas used: 256115 (2.13%)
  Setup deployed at: 0xb6286fAFd0451320ad6A8143089b216C2152c025

Is complete: False
Contract balance: 100 ETH
Transaction sent: 0x2874f1e3386af4a59d72fc258fa4c39bb36dd3cfc3831e9386ceebddb030c758
  Gas price: 0.0 gwei   Gas limit: 200000   Nonce: 5
  VideoChallengeIntro.setOwner confirmed   Block: 17112230   Gas used: 27043 (13.52%)

  VideoChallengeIntro.setOwner confirmed   Block: 17112230   Gas used: 27043 (13.52%)

Transaction sent: 0xde664d5411ed9b55d6579ad9bd11b824b84e87ea77fb238978acffb64e4c1e60
  Gas price: 0.0 gwei   Gas limit: 200000   Nonce: 6
  VideoChallengeIntro.withdraw confirmed   Block: 17112231   Gas used: 30347 (15.17%)

  VideoChallengeIntro.withdraw confirmed   Block: 17112231   Gas used: 30347 (15.17%)

Contract balance: 0 ETH
Is complete: True
Terminating local RPC client...
```

- Now sovle the first challenge by running

```py
brownie run scripts/hack.py --netowrk mevsec
```

![](../media/intro-sol.gif)

# Video Solution

**Coming Soon**

[Subscribe & Stay tuned](https://www.youtube.com/channel/UCQaHnWYnAo-e7YA5T3htj2Q)
