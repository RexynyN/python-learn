setTimeout(async () => {
    let imgs = []
    let numberPages = Number(document.getElementsByClassName("num-pages")[0].textContent); 

    for (var i = 0; i < numberPages; i++) {
        var img = document.getElementsByTagName("img")[1];
        imgs.push(img.src);
        document.getElementsByClassName("next")[0].click();
    }
    await window.navigator.clipboard.writeText(imgs)
}, 2000);