const hre = require("hardhat");
const { MerkleTree } = require("merkletreejs");
const keccak256 = require("keccak256");

async function main() {
    // We first create two fake users
    // One that is in the whitelist (vip) and one that is not (notVip)
    const [vip, notVip] = await hre.ethers.getSigners();
    const whitelist = [vip.address];

    // We generate the Merkle Tree and get the root
    // for later use in the contract
    const leaves = whitelist.map(addr => keccak256(addr));
    const tree = new MerkleTree(leaves, keccak256, { sortPairs: true });
    const root = tree.getHexRoot();

    console.log("-------------------------------------------");
    console.log("🔐 Generating merkle tree security...");
    console.log("📜 Whitelist:", whitelist);
    console.log("🌳 Root:", root);

    // Then we deploy the contract
    const Bank = await hre.ethers.getContractFactory("Bank");
    const bank = await Bank.deploy(root);
    await bank.waitForDeployment();
    console.log("🏦 Bank deployed at:", await bank.getAddress());
    console.log("-------------------------------------------");

    // Finally we test the success scenario
    console.log("✅ SUCCESS: VIP deposits 1 ETH.");
    const vipProof = tree.getHexProof(keccak256(vip.address));

    await bank.connect(vip).deposit(vipProof, { value: hre.ethers.parseEther("1") });
    console.log("   Resultado: ÉXITO. Saldo guardado.");

    // And the failure scenario
    console.log("\n⛔ FAILURE: Not VIP tries to deposit...");
    const notVipProof = tree.getHexProof(keccak256(notVip.address));

    try {
        await bank.connect(notVip).deposit(notVipProof, { value: hre.ethers.parseEther("1") });
    } catch (error) {
        console.log("   RESULT: ", error.message);
    }
    console.log("-------------------------------------------");
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});