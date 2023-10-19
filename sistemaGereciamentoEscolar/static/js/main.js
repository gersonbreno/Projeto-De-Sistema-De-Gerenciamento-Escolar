const AllDayEvent = document.querySelector(".AllDayEvent");
const nextButton = document.querySelector(".next-button");

let currentIndex = 0;

function moveCarousel(direction) {
    currentIndex += direction;

    if (currentIndex < 0) {
        currentIndex = 6;
    } else if (currentIndex > 6) {
        currentIndex = 0;
    }

    const offset = currentIndex * 100;
    AllDayEvent.style.transform = `translateX(-${offset}px)`;
}
nextButton.addEventListener("click", () => moveCarousel(1));


