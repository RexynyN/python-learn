window.getNumberPages = () => {
    return document.getElementsByClassName("md--progress-page").length;
}

window.getChapterImgs = () => {
    let doc = document.getElementsByClassName("mx-auto md--page flex ");       

    let imgs = []
    for (i of doc[0].childNodes)
    {
        imgs.push(i.src);
    }

    return imgs;
}


window.getImgDataUrl = function (img) {
    var c = document.createElement('canvas');
    // var img = document.getElementsByClassName('rg_i Q4LuWd')[0];
    c.height = img.naturalHeight;
    c.width = img.naturalWidth;
    var ctx = c.getContext('2d');
  
    ctx.drawImage(img, 0, 0, c.width, c.height);
    return c.toDataURL();
}
  

window.scrapImage = () => {
    var img = document.getElementsByTagName("img")[0];
    return window.scrapImage(img);
}

let doc = document.getElementsByClassName("mx-auto md--page flex ");       

let imgs = []
for (i of doc[0].childNodes)
{
    imgs.push(i.src);
}

return imgs;