# DeepMint
DeepMint is a Decentralized Application (DApp) that enables users to mint Non-Fungible Tokens (NFTs) using Deep Learning. Nowadays, many individuals wish to mint NFTs as a source of income. However, this requires the need to have expertise in creating digital art which can then be sold as an NFT to gain income. DeepMint overcomes this hurdle and makes it easy for individuals to mint NFTs. DeepMint uses the Stable Diffusion Deep Learning model to generate digital art which can then be minted as an NFT and can be sold on NFT martketplaces such as OpenSea
<br>
<br>


## Features
1. Generate Digital Art
    * The digital art generator uses the Stable Diffusion API to generate realistic digital art based on user inputs (text prompt, image quality, random seed, initial image) 
    <br>
    
2. Create NFT Collection
    * Users can create a new NFT Collection to group similar NFTs together. This results in deploying an ERC721 smart contract with details (name, symbol) of the NFT Collection  
    <br>
    
3. Mint NFTs
    * Users can specify metadata (name, description, image) of an NFT and also select an NFT Collection in which to include the minted NFT. Then the deployed ERC721 smart contract's method is called to mint the       NFT. This NFT can be viewed on platforms such as OpenSea and can be bought/sold
    <br>
    
4. Secure Authentication
    * Digital Signature Verification is used to authenticate users using their blockchain wallet keys. It provides a secure and convenient way to authenticate users
    <br>

## Tech Stack
1. Front-End 
    * HTML used for structuring the web application
    * CSS used for styling the web application
    * Javascript used for bulding a dynamic web application
    
2. Back-End
    * Python django framework used for developing the web application
    * Solidity used for writing the ERC721 NFT smart contract to create an NFT Collection and mint NFTs
    * Stable Diffusion API used for generating realistic digital art
    * Pinata API used for storing NFT metadata on Interplanetary File System (IPFS)
    * Cloudinary used for serving django media files in production environment
<br>

## Installation
1. Instructions to visit web application
   * Visit link : https://deepmint.up.railway.app/  OR https://deepmint.onrender.com/
   * Connect Metamask wallet with the DApp
   * Switch to Goerli Test Network in Metamask as smart contract has been deployed on Goerli Test Network

2. Instructions to RUN the project locally
   * Download the project folder
   * Install necessary dependencies by typing `pip install -r requirements.txt` in command prompt in the folder containing requirements.txt file
   * In the root directory of project, type `python manage.py runserver` in command prompt
   * Django will serve the web application on localhost and will provide the link in command prompt
   * Visit the link and explore the DApp
   * Connect Metamask wallet with the DApp
   * Switch to Goerli Test Network in Metamask as smart contract has been deployed on Goerli Test Network
<br>

## Screenshots

### Landing Page
![image](https://github.com/shobhitmir/deepmint/assets/73059947/bf89b639-7834-453f-ad5f-86f3872cd671)
<br>
<br>
<br>


### Login Page
![image](https://github.com/shobhitmir/deepmint/assets/73059947/6333fc95-df0f-46fa-a441-4b478e8a62ad)
<br>
<br>
<br>



### Digital Art Generator Page
![image](https://github.com/shobhitmir/deepmint/assets/73059947/bd1ace55-1695-4919-8c62-262c5179c25e)
<br>
<br>
<br>


### Viewing the Generated Art
![image](https://github.com/shobhitmir/deepmint/assets/73059947/52eef455-c11e-47b5-a42d-6f956d851aa6)
<br>
<br>
<br>


### Creating an NFT Collection
![image](https://github.com/shobhitmir/deepmint/assets/73059947/abfd392e-7127-4b93-b447-b9e35af0931b)
<br>
<br>
<br>


### Viewing an NFT Collection on OpenSea
![image](https://github.com/shobhitmir/deepmint/assets/73059947/bdffa1b6-39de-4189-91de-c50d8c329be4)
<br>
<br>
<br>

### Minting an NFT
![image](https://github.com/shobhitmir/deepmint/assets/73059947/9e0c7a92-6c6d-45ee-8771-d48e3035c5df)
<br>
<br>
<br>


### Viewing the NFT on OpenSea
![image](https://github.com/shobhitmir/deepmint/assets/73059947/5032214f-8a6e-430b-9f6a-52f131a67db4)
<br>
<br>
<br>


### User Profile Page
![image](https://github.com/shobhitmir/deepmint/assets/73059947/e17dc050-7987-4847-8dc9-0ddbda61f040)
<br>
<br>
<br>
