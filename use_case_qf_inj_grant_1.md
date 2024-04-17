# DI-QRNG Use Cases

## Injective Grant DAO round-1 voter Ninja NFT airdrop

The Injective Grant DAO's first voting round airdrops one Ninja NFT to one voter address among the list of all post-sybil address list. The address was selected via the DI-QRNG random number generator ran on IonQ cloud QC.

To perform the DI-QRNG, four circuits are used:

Circuit 1 diagram:

![image](https://github.com/dorahacksglobal/quantum-randomness-generator/assets/2503532/76b01616-45f9-49ee-bed7-72fe6eea5c72)

IonQ-Aria1 execution record:

![image](https://github.com/dorahacksglobal/quantum-randomness-generator/assets/2503532/bb1c01ca-272f-4408-866c-5ec12b469ff0)

Circuit 2 diagram:

![image](https://github.com/dorahacksglobal/quantum-randomness-generator/assets/2503532/e70d66dd-3753-4236-8c72-72c0a20ec665)

IonQ-Aria1 execution record:

![image](https://github.com/dorahacksglobal/quantum-randomness-generator/assets/2503532/49d735fd-4f2e-4ef5-b183-aa2c91614bb1)

Circuit 3 diagram:

![image](https://github.com/dorahacksglobal/quantum-randomness-generator/assets/2503532/ea5cda6e-e6ae-44cc-820b-895258701209)

IonQ-Aria1 execution record:

![image](https://github.com/dorahacksglobal/quantum-randomness-generator/assets/2503532/f64cc70d-1e55-4f84-b090-6ba977b1c269)

Circuit 4 diagram:

![image](https://github.com/dorahacksglobal/quantum-randomness-generator/assets/2503532/3ca6d382-d496-4d90-9328-55a77bb218c8)

IonQ-Aria1 execution record:

![image](https://github.com/dorahacksglobal/quantum-randomness-generator/assets/2503532/a6e156f9-d19d-4e8d-8dc8-7653d223b177)

After completing all execution, we calculated the CHSH score = 0.83125. The corresponding min-entropy is 0.17239. As a result, we obtain 690 random numbers (or bits) in total after randomness extraction.

The post-sybil address list can be found [here](https://github.com/dorahacksglobal/quadratic-grant-injective/blob/main/round-1-post-sybil-address-list-duplication-removed).
