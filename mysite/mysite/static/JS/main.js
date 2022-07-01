// =====> Change NavBar Style on scroll <===== //

window.addEventListener("scroll", () => {
    document
        .querySelector("nav")
        .classList.toggle("window-scroll", window.scrollY > 100);
});

// Tablet Show/Hide NavBar

const menu = document.querySelector(".nav-menu");
const menuBtn = document.querySelector("#open-menu-btn");
const closeBtn = document.querySelector("#close-menu-btn");

menuBtn.addEventListener("click", () => {
    menu.style.display = "flex";
    closeBtn.style.display = "inline-block";
    menuBtn.style.display = "none";
});

//Close Nav Menu

const closeNav = () => {
    menu.style.display = "none";
    closeBtn.style.display = "none";
    menuBtn.style.display = "inline-block";
};

closeBtn.addEventListener("click", closeNav);

// =====> Show The Answer p <===== //

const question = document.querySelectorAll(".question");

question.forEach((question) => {
    question.addEventListener("click", () => {
        question.classList.toggle("open");

        // change he Icon
        const icon = question.querySelector(".qustion-icon i");
        if (icon.className === "fa-solid fa-plus") {
            icon.className = "fa-solid fa-minus";
        } else {
            icon.className = "fa-solid fa-plus";
        }
    });
});

// Testimonials Slider

var swiper = new Swiper(".mySwiper", {
    centeredSlides: true,
    loop: true,
    spaceBetween: 20,
    autoplay: {
        delay: 2000,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1200: {
            slidesPerView: 3,
        },
    },
});