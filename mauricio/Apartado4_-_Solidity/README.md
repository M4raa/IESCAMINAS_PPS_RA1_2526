# Solidity
Aqui se adjunta la captura que demuestra que he realizado el Beginer to intermediate de [CryptoZombies.io](https://cryptozombies.io/en/solidity)

<image src="BeginnerToIntermediate.png">

# MerkleVerifier

Este contrato en Solidity permite agregar y verificar raíces de Merkle en la cadena de bloques.

## Funciones principales

- **Agregar raíz de Merkle**: Permite agregar una raíz de Merkle al contrato.
- **Verificar prueba de Merkle**: Permite verificar si un dato (hoja) está incluido en un árbol de Merkle utilizando una prueba de inclusión.

## Cómo se usa

1. **Agregar una raíz de Merkle**:  
   Utiliza la función `addMerkleRoot` para agregar una nueva raíz de Merkle al contrato.

2. **Verificar una prueba de Merkle**:  
   Utiliza la función `verifyMerkleProof` para verificar si una hoja está incluida en un árbol de Merkle dado, proporcionando la hoja, la prueba, el índice y la raíz.

## Ejemplo

1. **Agregar una raíz de Merkle**:
   ```solidity
   addMerkleRoot(0x1234567890abcdef...);
   ```

2. **Verificar una prueba de Merkle**:
    ```solidity
    verifyMerkleProof(0xabcdef..., [0x123456...], 0, 0x7890abcd...);
    ```

## Tecnologías

- Solidity 0.8.19

- Compatible con Remix, Truffle, Hardhat