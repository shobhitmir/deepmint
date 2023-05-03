# DeepMint 
The project is named ‘DeepMint’ as it helps mint NFTs using Deep Learning. It has 2 main components : 
i)	The Digital Art Generator : 
The Digital Art Generator uses the Stable Diffusion Deep Learning model to generate digital art images based on user inputs such as a text prompt, the desired quality (low, medium, high) of the generated art, a seed value, an optional initial image and the initial image’s strength. The generated image can then be converted into an NFT.
ii)	The NFT Generator : 
The NFT Generator takes various inputs from the user, such as the name, description, and the image that needs to be converted into an NFT. It also allows users to specify an NFT Collection in which the minted NFT should be included. Then the NFT Generator mints the required NFT by preparing its metadata and executing the appropriate functions defined in the smart contract. 

# Installation
The system has been deployed on render.com (https://deepmint.onrender.com/) and railway.app (https://deepmint.up.railway.app/) hosting platforms and can be accessed from there. Alternatively, the system can also be set up to run locally by performing the following steps :
i)	The source code of the proposed system is available in a repository on the github platform (https://github.com/shobhitmir/deepmint)
ii)	Install git on the local machine and then clone the repository by typing the following command in the terminal : “git clone https://github.com/shobhitmir/deepmint.git”
iii)	The project directory structure will be as follows :
	|_ contracts/            (The smart contract for NFT)
	|_ deepmint/            (Django server setup files)
	|_ nftgen/                 (A Django app)
	|_ staticfiles/            (Client frontend files)
	|_ requirements.txt  (A list of python libraries needed for running the application)

iv)	Django Setup (Client – Server Setup)

1.	Create a virtual environment: “python -m venv venv”
2.	Activate the virtual environment: “source venv/bin/activate”
3.	Install Django and other dependencies: “pip install -r requirements.txt”
4.	Run the Django app: “python manage.py runserver”

v)	Blockchain Setup

1.	Install the MetaMask wallet. There is a browser extension available for google chrome (https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn?hl=en)
2.	Login to the MetaMask wallet (Create a new account or import an existing account)
3.	Enable the ‘Show test networks’ option in MetaMask wallet’s Advanced settings
4.	Switch to Goerli Test Network
5.	Connect the MetaMask wallet with the Decentralized App (DApp) when prompted
6.	Use the MetaMask wallet to sign messages (during login or registration) and to make transactions (to create NFT Collections or to mint NFTs) 

