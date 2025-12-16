// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract Bank {
    // Variables to store the root of the merkle tree and the balance of each user
    bytes32 public root;
    mapping(address => uint256) public balance;

    // Initialize the contract by storing the root of the merkle tree
    constructor(bytes32 _root) {
        root = _root;
    }

    // Function to deposit ETH only if the user presents a valid proof (is in the whitelist)
    function deposit(bytes32[] calldata proof) external payable {
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(
            MerkleProof.verify(proof, root, leaf),
            "YOU ARE NOT IN THE WHITELIST"
        );
        balance[msg.sender] += msg.value;
    }

    // Function to get the balance of the user who calls the function
    function getBalance() external view returns (uint256) {
        return balance[msg.sender];
    }
}
