// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract MerkleTreeContract {
    // variables
    bytes32[] public merkleRoots;
    event MerkleRootAdded(bytes32 root);

    // funciones
    function addMerkleRoot(bytes32 _root) public {
        merkleRoots.push(_root);
        emit MerkleRootAdded(_root);
    }

    function verifyMerkleProof(
        bytes32 leaf,
        bytes32[] calldata proof,
        uint256 index,     
        bytes32 root                  
    ) public pure returns (bool) {
        bytes32 computedHash = leaf;

        for (uint i = 0; i < proof.length; i++) {
            if (index % 2 == 0) {
                computedHash = keccak256(abi.encodePacked(computedHash, proof[i]));
            } else {
                computedHash = keccak256(abi.encodePacked(proof[i], computedHash));
            }
            index /= 2;
        }

        return computedHash == root;
    }

    function getMerkleRoots() public view returns (bytes32[] memory) {
        return merkleRoots;
    }
}
