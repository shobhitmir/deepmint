const showimg = (e) =>
    {
        document.getElementById('previewimg').hidden = !document.getElementById('previewimg').hidden
    }

    const changeimg = (e) =>
    {
        const img = document.getElementById('initimg').files[0]
        const bgUrl = URL.createObjectURL(img)
        document.getElementById('previewimg').src = bgUrl
    }

    const expand = (e) =>
    {
        const extra = document.getElementById('extra')
        if (extra.style.display === "block")
          extra.style.display = "none"
        else
          extra.style.display = "block"
    }

    window.onload = () =>
    {
        const extra = document.getElementById('extra')
        extra.style.display = "none"
    }