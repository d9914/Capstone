function toggleLightbox(img) {
  var lightbox = document.getElementById("lightbox");
  var lightboxImg = document.getElementById("lightbox-img");

  if (lightbox.style.display === "flex" && lightboxImg.src === img.src) {
    closeLightbox();
  } else {
    lightboxImg.src = img.src;
    lightbox.style.display = "flex";
  }
}

function closeLightbox() {
  document.getElementById("lightbox").style.display = "none";
}
