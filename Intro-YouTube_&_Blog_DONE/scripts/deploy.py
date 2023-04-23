#!/usr/bin/python3
from brownie import Setup
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    c = Setup.deploy({"from": owner, "value": "100 ether"})
    return c, owner


def main():
    deploy()


if __name__ == "__main__":
    main()
