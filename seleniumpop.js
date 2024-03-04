// // Remove all the occurences of a CSS class
// for (var j = 0; j < 10; j++) {
//     html = document.getElementsByClassName(" ")
//     for (var i = 0; i < html.length; i++)
//         html[i].classList.remove(" ");
// }

// // Get the Parent Node of a element
// document.getElementById("myLI").parentElement;

// // Get the list of tags inside an element
// var imgContainerItems = document.getElementById("test").getElementsByTagName("img");

// // Get the parent div element by searching text
// // TODO: Make sure that the parent element is either a div, main, article, or a correlated container (exclude spans or other p tags)
// const matches = [];
// for (const p of document.querySelectorAll('p')) {
//   if (p.textContent.includes("<TEXT>")) {
//     matches.push(p);
//   }
// }
// matches[0].parentElement


const myTimeout = setTimeout(scrapImage, 5000);

// Get the dataUrl of a image
function getImgDataUrl(img) {
  var c = document.createElement('canvas');
  // var img = document.getElementsByClassName('rg_i Q4LuWd')[0];
  c.height = img.naturalHeight;
  c.width = img.naturalWidth;
  var ctx = c.getContext('2d');

  ctx.drawImage(img, 0, 0, c.width, c.height);
  return c.toDataURL();
}

// Return all the DataUrls of a MangaDex manga chapter images
function scrapImage() {
  var images = [];
  for (let img of document.getElementsByClassName("img limit-width")) {
    let imgObj = {
      "data": getImgDataUrl(img)
    }

    images.push(imgObj);
  }
console.log(images);

}
return myTimeout;


// // Return the URLs of a youtube playlist
// let soign = document.getElementsByClassName("yt-simple-endpoint style-scope ytd-playlist-video-renderer");
// let stringLinks = [];
// for(var i = 0; i < soign.length ; i++){
//     stringLinks.push(soign[i].href);
// }

// return stringLinks