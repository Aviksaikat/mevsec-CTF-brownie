#!/usr/bin/python3
import json
import subprocess
from re import findall


def get_values():
    # Run the curl command and capture the output
    output = subprocess.check_output(
        ["curl", "-s", "http://5.196.27.132:8080/create_challenge?challenge_number=0"]
    )

    # Parse the output as JSON and save it to a variable
    result = json.loads(output)

    # result = json.loads(
    #     """
    # {"message":"New instance of mevsec_ctf0 created. The RPC url to connect to this private blockchain is  http://ctf.mevsec.com:50417. The Setup contract has been deployed at the following address: 0x876807312079af775c49c916856A2D65f904e612. If you need to deploy a contract or send a tx you can use the account 0x133756e1688E475c401d1569565e8E16E65B1337 with the private key 0xedbc6d1a8360d0c02d4063cdd0a23b55c469c90d3cfbc2c88a015f9dd92d22b3. Please don't forget you will need the following ID to flag => 8d8b7e39950c32a949dab2667993dfb9e98de62437eb7e2fc1ebcfdb64251ec1. Be careful the instance will stop automatically after 20 minutes..","status":"success"}"""
    # )

    # print(result)

    # Extract the required values
    RPC_URL = findall(r"(http:\/\/\S+)", result["message"])[0][:-1]
    setup = result["message"].split(": ")[-1].split(".")[0]
    PRIVATE_KEY = result["message"].split("private key ")[-1].split(".")[0]
    FLAG_ID = result["message"].split("=> ")[-1].split(".")[0]

    # Print the extracted values
    print("RPC_URL:", RPC_URL)
    print("setup:", setup)
    print("PRIVATE_KEY:", PRIVATE_KEY)
    print("FLAG_ID:", FLAG_ID)

    return RPC_URL, setup, PRIVATE_KEY, FLAG_ID
