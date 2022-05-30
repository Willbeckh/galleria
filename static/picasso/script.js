const urlBtns = [...document.getElementsByClassName("link-btn")];

urlBtns.forEach((btn) =>
  // adds click listener to all btns and copies link
  btn.addEventListener("click", () => {
    let img_url = btn.getAttribute("data-url");
    navigator.clipboard.writeText(img_url);
    btn.textContent = "copied";
  })
);
