// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.8.0;

contract CentralizedWhitelist {

    address constant public WHITELIST_SIGNER_ADDRESS = 0x4513218Ce2e31004348Fd374856152e1a026283C;

    modifier onlyValidAccess(uint8 _v, bytes32 _r, bytes32 _s) {
        bytes memory packedHash = abi.encodePacked(address(this), msg.sender);
        bytes32 hash = keccak256(packedHash);
        bytes memory packedString = abi.encodePacked("\x19Ethereum Signed Message:\n32", hash);
        require(ecrecover(keccak256(packedString), _v, _r, _s) == WHITELIST_SIGNER_ADDRESS, "Invalid ECDSA signature");
        _;
    }

    constructor () public {
    }

    function formMessage(address userAddress) external view returns (bytes32) {
        return keccak256(abi.encodePacked(address(this), userAddress));
    }

    function coolFeatureForWhitelistedUser(uint8 _v, bytes32 _r, bytes32 _s) external onlyValidAccess(_v,_r,_s) {
        // ...
    }
}
