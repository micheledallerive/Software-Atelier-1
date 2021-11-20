// DO NOT EDIT,
// ONLY AFFECTS HOMEPAGE

const controller = new ScrollMagic.Controller();

const tween = new TimelineMax();

// Hero section

tween.to(".ta-title", 1, { xPercent: $('.ta-title').width() * 0.03 });
tween.to(".logo", 1, { xPercent: - $('.logo').width() * 0.45 }, 0);
tween.to(".logo", 1, { opacity: 1 }, "0.25");
tween.to(".t-cta", 1, { opacity: 1 }, "0.25");

const scene = new ScrollMagic.Scene({
    triggerElement: ".hero",
    triggerHook: "onLeave",
    duration: "300%"
}).setPin(".hero")
    .setTween(tween)
    // .addIndicators()
    .addTo(controller);

// Project section

// // counter animation
let counters = document.querySelectorAll('.counter');
let speed = 400;


new ScrollMagic.Scene({
    triggerElement: ".project",
    // triggerHook: "onLeave",
    duration: "100%"
}).on("start", function() {
    counters.forEach(counter => {
        const updateCounter = () => {
            const target = counter.getAttribute('target');
            const count = +counter.innerText;

            if (count < target) {
                counter.innerText =  Math.floor(count + 1);
                setTimeout(updateCounter, 1);
            } else {
                counter.innerText =  target;
            }
        }
        updateCounter();
    })

})
    // .addIndicators()
    .addTo(controller);


new ScrollMagic.Scene({
    triggerElement: ".project",
    triggerHook: "onLeave",
    duration: "50%"
}).setPin(".project")
    // .addIndicators()
    .addTo(controller);


// Dark mode section

new ScrollMagic.Scene({
    triggerElement: ".dark",
    triggerHook: "onLeave",
    duration: "50%"
}).setPin(".dark")
    // .addIndicators()
    .addTo(controller);

function changeToDark() {
    $("#darkModeSectionIcon").attr("src","images/darkmode-o.svg");
    $("#darkModeSectionText").attr("src","images/dark-o.svg");
}

new ScrollMagic.Scene({
    triggerElement: ".dark",
    triggerHook: "onLeave",
    offset: "-200"
}).on("start", function () {
    let duration = 400;
    $("#darkModeSectionIcon").fadeOut(duration, function () {
        changeToDark();
        $("#darkModeSectionIcon").fadeIn(duration);
    });
}).setClassToggle(".dark", "color-d")
    .reverse(false)
    // .addIndicators()
    .addTo(controller);


// Explore section

new ScrollMagic.Scene({
    triggerElement: ".explore",
    triggerHook: "onLeave",
    offset: "-300",
    duration: "40%",
}).setTween(new TimelineMax().to(".explore-text", 1, { opacity: 1 }))
    // .addIndicators()
    .addTo(controller);

// On end of scroll redirect to page x
let redirect = "html/timeline.html"; //<- adjust page path

window.addEventListener("scroll", () => {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const scrolled = window.scrollY;

    if (scrolled === scrollable) {
        setInterval(() => {
            window.location.href = redirect;
        }, 1000);
    }
})