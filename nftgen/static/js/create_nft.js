const pinata_api_key = "22757a7ae1c143ba9b8b"
const pinata_secret_api_key = "e21c5c1c34ba012d31ce2eb7c36aa2e3c80e5e5c11cbb6e8ffa4bdd8f9873037"

const create_nft = async()  => 
{
    const form = document.getElementById('nftgenform');
    const name = document.getElementById('nft_name').value
    const desc = document.getElementById('nft_desc').value
    
    const formData = new FormData(form);
    const file = formData.get('nft_img')
    const imgformData = new FormData()
    imgformData.append("file", file);

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