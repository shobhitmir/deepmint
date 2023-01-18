var web3;
var metamaskInstalled = true;

const metamaskEnabled = new Promise((resolve, reject) =>
{
  if (window.ethereum) 
  {
    web3 = new Web3(window.ethereum);
    window.ethereum.enable()
    .then(resolve())
    .catch(reject())
  }
  else
  {
    reject();
  }
});

const getPublicKey = function()
{
  metamaskEnabled.then(
  () =>  
    {
      getMetamaskAccounts();
    }
  )
  .catch(
  () =>
    {
        metamaskInstalled = false
    }
  )
}

const generateNonce = function() 
{
  var text = "";
  var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  for(var i = 0; i < 100; i++) 
  {
      text += possible.charAt(Math.floor(Math.random() * possible.length));
  }
  return web3.utils.sha3(text);
}

function getMetamaskAccounts()
{
    web3.eth.getAccounts(
    (err, res) =>
    {
        if (err)
        {
            window.alert('Could not retrieve Metamask Account !!')
        }
        else
        {
            if (res.length > 0 )
            {
                const public_address=res[0]
                console.log(public_address)
                $("#public_key").val(public_address)
            }
            else
            {
                metamaskInstalled = false
            }
        }
    })
}

const reverify = (e) =>
{
    document.getElementById('verified_icon')
    .src="/static/images/unverified_icon.png";
    $("#verified").val("false")
}

const verify_account = (e) =>
{
    try
    {
        const nonce = generateNonce()
        console.log('Nonce : ',nonce)
        const public_address= document.getElementById('public_key').value
        sign_message(nonce,public_address)
    }
    catch
    {
        metamaskInstalled = false
    }
}

function validate_user(public_address, validation_address)
{
    console.log('valid')
    if (public_address.toLowerCase()===validation_address)
    {
        document.getElementById('verified_icon')
        .src="/static/images/verified_icon.png";
        $("#verified").val("true")
    }
    else
    {
        window.alert("Authentication Failed !!")
    }
}

function recover_address(nonce, signature, public_address)
{
    web3.eth.personal.ecRecover(nonce, signature,
    (err,result) =>
    {
        if (err)
        {
            window.alert('Failed to verify.. try again later..')
        }
        else
        {
            const validation_address=result
            console.log('Recovered Address : ',validation_address)
            validate_user(public_address, validation_address);
        }
    })
}

function sign_message(nonce,public_address)
{
    web3.eth.personal.sign(nonce,public_address,
    (err,result) =>
    {
        if (err)
        {
            window.alert('Failed to sign message!!')
        }
        else
        {
            const signature=result
            console.log('Signature : ',signature)
            recover_address(nonce,signature,public_address);
        }
    })
}

window.onload= getPublicKey()