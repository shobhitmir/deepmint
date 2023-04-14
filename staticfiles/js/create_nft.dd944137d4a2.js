const pinata_api_key = PINATA_API_KEY
const pinata_secret_api_key = PINATA_API_SECRET

const ABI = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "symbol",
				"type": "string"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "approved",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "ApprovalForAll",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "tokenURI",
				"type": "string"
			}
		],
		"name": "mintNFT",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			},
			{
				"internalType": "bytes",
				"name": "data",
				"type": "bytes"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "setApprovalForAll",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "getApproved",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			}
		],
		"name": "isApprovedForAll",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "ownerOf",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes4",
				"name": "interfaceId",
				"type": "bytes4"
			}
		],
		"name": "supportsInterface",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "tokenURI",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

function getCsrfToken() {
  const csrfCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));
  if (!csrfCookie) {
    return null;
  }
  return csrfCookie.split('=')[1];
}

function save_nft(nft_image_url, tx_receipt, tokenid)
{
    var csrftoken = getCsrfToken()
    const form = document.querySelector('#nftgenform');
    const name = document.getElementById('nft_name').value
    const desc = document.getElementById('nft_desc').value
    const contract_address = document.getElementById("collection_selector").value;

    const formData = new FormData();
    formData.append('name', name);
    formData.append('description', desc);
    formData.append('contract_address', contract_address);
    formData.append('image_url', nft_image_url);
    formData.append('tokenid', tokenid);

    $.ajax({
      type: 'POST',
      url: '/nftgen/',
      headers: {'X-CSRFToken': csrftoken},
      data: formData,
      processData: false,
      contentType: false,
      success: function(data) {
        window.alert(`NFT Minted Successfully : ${JSON.stringify(tx_receipt)}`);
        console.log('NFT saved successfully!');
        loader.style.display = 'none';
        window.location.href = window.location.protocol + '//' + window.location.host + '/profile/';
      },
      error: function(xhr, textStatus, errorThrown) {
        window.alert(`Error saving NFT: ${errorThrown}`);
        location.reload()
      }
    });
}

const create_nft = async(metadata_uri, nft_image_url) =>
{
  const web3 = new Web3(window.ethereum);
  const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
  const fromAddress = accounts[0];

  const contractAddress = document.getElementById("collection_selector").value;

  const UserNFTContract = new web3.eth.Contract(ABI, contractAddress);
  UserNFTContract.methods.mintNFT(metadata_uri)
  .send({ from: fromAddress })
  .then(receipt => {
    console.log("Transaction receipt: ", receipt);
    var tokenid = 0;
    if (receipt.events.Transfer)
    {
      tokenid = receipt.events.Transfer.returnValues.tokenId
    }
    console.log(tokenid)
    save_nft(nft_image_url, receipt,tokenid)
  })
  .catch(error => {
    console.error("Error occurred: ", error);
    window.alert(error.message)
    loader.style.display = 'none';
  });
}

const create_metadata = async()  => 
{
    const form = document.getElementById('nftgenform');
    const name = document.getElementById('nft_name').value
    const desc = document.getElementById('nft_desc').value

    if (name === '')
    {
        window.alert('Name is a required field...')
        return
    }
    else if (desc === '')
    {
        window.alert('Description is a required field...')
        return
    }
    
    loader.style.display = 'block';

    const formData = new FormData(form);
    const fileInput = document.getElementById('nft_img');
	
    if (fileInput.files.length > 0) 
    {
        const file = formData.get('nft_img')
        const imgformData = new FormData()
        imgformData.append("file", file)

        const config = {
          method: "POST",
          maxContentLength: Infinity,
          headers: {
            pinata_api_key: pinata_api_key,
            pinata_secret_api_key: pinata_secret_api_key,
          },
          body: imgformData,
        };
      
          try {
          const response = await fetch('https://api.pinata.cloud/pinning/pinFileToIPFS', config);
          const data = await response.json();
              hash = data.IpfsHash
              image_url = "https://ipfs.io/ipfs/" + hash
              const metadata = {
                  name: name,
                  description: desc,
                  image: image_url
              }
              const metadataString = JSON.stringify(metadata)
              const headers = {
                  'Content-Type': 'application/json',
                  'pinata_api_key': pinata_api_key,
                  'pinata_secret_api_key': pinata_secret_api_key
                };
          
                fetch('https://api.pinata.cloud/pinning/pinJSONToIPFS', {
                  method: 'POST',
                  headers: headers,
                  body: metadataString
                })
                .then(response => response.json())
                .then(data => {
                  metadata_hash = data.IpfsHash
                  const metadata_uri = "https://ipfs.io/ipfs/" + metadata_hash
                  create_nft(metadata_uri, image_url)
                })
                .catch(error => {
                  console.error(error);
                });
        } 
          catch (error) 
          {
          console.log(error)
        }
    } 
    else if (nft_image_url === '')
    {
      window.alert('Please upload a file..')
      loader.style.display = 'none';
      return
    }
    else
    {
      fetch(nft_image_url)
        .then(response => response.blob())
        .then(async(blob) => {
          const imageName = nft_image_url.substring(nft_image_url.lastIndexOf('/')+1);
          const file = new File([blob], imageName, { type: "image/png" });
          const imgformData = new FormData()
          imgformData.append("file", file)

          const config = {
            method: "POST",
            maxContentLength: Infinity,
            headers: {
              pinata_api_key: pinata_api_key,
              pinata_secret_api_key: pinata_secret_api_key,
            },
            body: imgformData,
          };
        
            try {
            const response = await fetch('https://api.pinata.cloud/pinning/pinFileToIPFS', config);
            const data = await response.json();
                hash = data.IpfsHash
                image_url = "https://ipfs.io/ipfs/" + hash
                const metadata = {
                    name: name,
                    description: desc,
                    image: image_url
                }
                const metadataString = JSON.stringify(metadata)
                const headers = {
                    'Content-Type': 'application/json',
                    'pinata_api_key': pinata_api_key,
                    'pinata_secret_api_key': pinata_secret_api_key
                  };
            
                  fetch('https://api.pinata.cloud/pinning/pinJSONToIPFS', {
                    method: 'POST',
                    headers: headers,
                    body: metadataString
                  })
                  .then(response => response.json())
                  .then(data => {
                    metadata_hash = data.IpfsHash
                    const metadata_uri = "https://ipfs.io/ipfs/" + metadata_hash
                    create_nft(metadata_uri, image_url)
                  })
                  .catch(error => {
                    console.error(error);
                  });
          } 
            catch (error) 
            {
            console.log(error)
          }
        })
        .catch(error => console.error(error));
    }
}