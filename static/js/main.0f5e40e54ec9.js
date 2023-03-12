window.addEventListener("load", ()=>{
    // aos initialisation
AOS.init({
    offset: 70,
    delay: 100,
    duration: 700,
    easing: 'ease',
    once: false,
    mirror: false,
    anchorPlacement: 'top-bottom'
})
// making the nav links stay highlighted when clicked
const navLinks = document.querySelectorAll(".nav-list a")

navLinks.forEach(link =>{
    link.addEventListener("click", activeLink)
})

function activeLink() {
    navLinks.forEach(link => {
        link.classList.remove("active")
        this.classList.add("active")
        link.addEventListener("click", deactivateMobileNav)
    })
}

// the buttons in the navbar
const searchBtn = document.querySelector(".icons-box .search-btn")
const menuBtn = document.querySelector(".icons-box .menu-btn")
const closeNavBtn = document.querySelector(".nav-list .mobile-menu-close-btn")
const mobileNav = document.querySelector("nav .nav-list")
const searchForm = document.querySelector("nav form")

searchBtn.addEventListener("click", activateSearch)
menuBtn.addEventListener("click", activateMobileNav)
closeNavBtn.addEventListener("click", deactivateMobileNav)

function activateSearch() {
    searchForm.classList.toggle("active")
}
function activateMobileNav() {
    mobileNav.classList.add("active")
}
function deactivateMobileNav() {
    mobileNav.classList.remove("active")
}
    // updating the date in the footer every year
    const date = document.getElementById("date")
    date.innerHTML = new Date().getFullYear()


})