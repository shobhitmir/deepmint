// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract UserNFT is ERC721URIStorage {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;
    uint256 MAX_SUPPLY = 1000000;

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        mintNFT(
            "https://ipfs.io/ipfs/QmXNnAHjc7z5gbpdUkJX5Mu2iQz5GrGLjfr8HkFinZLjqS"
        );
    }

    function mintNFT(string memory tokenURI) public {
        require(
            _tokenIdCounter.current() <= MAX_SUPPLY,
            "Max NFT minting limit reached !!"
        );
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
    }
}
