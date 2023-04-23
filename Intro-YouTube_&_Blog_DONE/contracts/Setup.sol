// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.0;
import "./VideoChalllengeIntro.sol";

contract Setup {
	VideoChallengeIntro public vci;

	constructor() payable {
		require(msg.value >= 100, "Not enough ETH to create the challenge..");
		vci = (new VideoChallengeIntro){ value: 100 ether }();
	}

	function isSolved() public view returns (bool) {
		return address(vci).balance == 0;
	}
}
