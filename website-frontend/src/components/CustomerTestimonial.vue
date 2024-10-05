<template>
  <div class="testimonial">
    <div class="test-head">
      <div class="subscription d-flex align-items-center justify-content-center gap-2">
        <svg class="setting-icon" xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12"
             fill="none">
          <!-- SVG paths here -->
        </svg>
        <div class="test-head-text">
          <h5>TESTIMONIAL</h5>
        </div>
      </div>
    </div>
    <div class="testi">
      <h1 class="testi-title" :class="{ visible: isTitleVisible }">See Why our Customers <br> Love us</h1>
    </div>
    <div class="test-body swiper">
      <ul class="swiper-wrapper">
        <li class="d-flex justify-content-center swiper-slide" v-for="(testimonial, index) in testimonials"
            :key="index">
          <div class="wrapper">
            <div class="thumbnail">
              <img :src="testimonial.image" alt="">
            </div>
            <div class="aside">
              <p>{{ testimonial.text }}</p>
              <div class="name">
                <h4 class="mb-3">{{ testimonial.name }}</h4>
                <p class="mb-0">{{ testimonial.position }}</p>
              </div>
            </div>
          </div>
        </li>
      </ul>

      <div class="swiper-pagination"></div>
      <div class="swiper-button-prev"></div>
      <div class="swiper-button-next"></div>
    </div>
  </div>
</template>


<script>
import Swiper from 'swiper';
import ScrollMagic from 'scrollmagic';

export default {
  data() {
    return {
      isTitleVisible: false,
      testimonials: [
        {
          image: './Testimonial-img/testi-profile.png',
          text: 'Lorem ipsum dolor sit, amet consectetur adipisicing elit...',
          name: 'Mr. Tony Rutherford',
          position: 'Product Quality Engineer',
        },
        {
          image: './Testimonial-img/testi-profile.png',
          text: 'Lorem ipsum dolor sit, amet consectetur adipisicing elit...',
          name: 'Mr. Tony Rutherford',
          position: 'Product Quality Engineer',
        },
        // Add more testimonials as needed
      ],
    };
  },
  mounted() {
    // Initialize Swiper
    new Swiper('.swiper', {
      autoHeight: true,
      loop: true,
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    });

    // ScrollMagic for triggering animations
    const controller = new ScrollMagic.Controller();
    new ScrollMagic.Scene({
      triggerElement: '.testi-title',
      triggerHook: 0.9,
    })
        .setClassToggle('.testi-title', 'visible')
        .addTo(controller);
  }
};
</script>


<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

a {
  text-decoration: none;
  color: inherit;
}

ul {
  list-style: none;
}

.testimonial {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  padding: 80px 20px;
  text-align: center;
}

.test-body {
  width: 100%;
}

.wrapper {
  max-width: 1200px;
  margin: 0 auto;
}

.thumbnail {
  width: 150px;
  height: 150px;
  position: relative;
  flex-shrink: 0;
}

.thumbnail::before {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: calc(100% + 30px);
  height: calc(100% + 20px);
  background: linear-gradient(140deg, #FF532D 0%, #E02900 100%);
  border-radius: 50%;
  z-index: -1;
  box-shadow: 0px 0px 25px #df836ef5;
  transition: border-radius .5s .3s;
}

.swiper-slide-active .thumbnail::before {
  border-radius: 33% 67% 50% 50% / 50% 14% 86% 50%;
}

.thumbnail img {
  object-fit: cover;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  transform: scale(2);
  transition: transform .5s;
}

.test-body .swiper-slide-active .thumbnail img {
  transform: scale(1);
}

.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 60px;
  padding: 30px 0;
}

.aside {
  position: relative;
  padding-top: 15px;
  display: flex;
  flex-direction: column;
  align-self: flex-end;
}

.aside p {
  position: relative;
  color: #1E1E1E;
  font-size: 17px;
  font-style: normal;
  font-weight: 500;
  line-height: 30px;
  margin-bottom: 40px;
}

.aside p::before,
.aside p::after {
  font-size: 80px;
  font-weight: 800px;
  line-height: 1;
  position: absolute;
  color: rgb(167, 165, 165);
  height: 40px;
  z-index: -1;
  font-family: serif;
}

.aside > p::before {
  content: open-quote;
  top: -60px;
  left: 10px;
}

.aside > p::after {
  content: close-quote;
  bottom: -40px;
  right: 10px;
}

.aside .name {
  position: relative;
  width: fit-content;
  line-height: 1;
  opacity: 0;
  transform: translateX(30px);
  transition: transform 1s .2s, opacity 1s .3s;
  text-align: end;
}

.swiper-slide-active .name {
  transform: translateX(0);
  opacity: 1;
}

.name h4 {
  color: #FF532D;
  font-size: 18px;
  font-style: normal;
  font-weight: 800;
  line-height: 18px;
  opacity: .8;
}

.name p {
  color: #0505059c;
  font-size: 12px;
  font-style: normal;
  font-weight: 400;
  line-height: 12px;
}

.test-body :is(.swiper-button-next, .swiper-button-prev) {
  right: 220px;
  background: rgb(136, 136, 146);
  height: 38px;
  width: 38px;
  border-radius: 50%;
  transition: background-color .3s;
  box-shadow: 0px 0px 15px rgb(168, 158, 158);
}

.test-body :is(.swiper-button-next, .swiper-button-prev):hover {
  background: linear-gradient(140deg, #FF532D 0%, #E02900 100%);
}

.test-body :is(.swiper-button-next, .swiper-button-prev)::after {
  font-size: 18px;
  font-weight: 800;
  color: rgb(255, 255, 255);
}

.swiper-button-prev,
.swiper-rtl .swiper-button-next {
  left: 250px;
}

.test-body .swiper-pagination {
  position: relative;
}

.test-body .swiper-pagination span {
  background: gray;
  transition: width .3s;
  opacity: 1;
}

.test-body .swiper-pagination-bullet-active {
  width: 25px;
  border-radius: 4px;
  background: linear-gradient(140deg, #FF532D 0%, #E02900 100%) !important;
}

.setteing-icon {
  animation: set 3s ease-in-out infinite;
}

.testi-title {
  opacity: 0;
  transform: translateY(50px);
  transition: all 1s ease-out;
}

.testi-title.visible {
  opacity: 1;
  transform: none;
}

@keyframes set {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1.2);
    transition: 2s;
  }

  100% {
    transform: scale(1);
  }
}

.test-head-text h5 {
  color: #F23C13;
  font-size: 12px;
  font-style: normal;
  font-weight: 400;
  line-height: 14px;
  letter-spacing: 0.7px;
  text-transform: uppercase;
  margin-bottom: 0;
}

.subcription {
  margin-bottom: 20px;
}

.testi {
  margin-bottom: 65px;
}

.testi h1 {
  color: #1E1E1E;
  font-size: 36px;
  font-style: normal;
  font-weight: 700;
  line-height: 160%;
  letter-spacing: 0.5px;
  text-transform: capitalize;
  margin-bottom: 0;
}

.test-rate {
  display: flex;
  margin-bottom: 20px;
  gap: 15px;
}

@media screen and (min-width: 768px) {
  .wrapper {
    flex-direction: row;
    padding: 30px 100px;
    gap: 100px;
  }

  .thumbnail {
    width: 200px;
    height: 200px;
  }

  .testi h1 {
    font-size: 48px;
  }

  .test-body :is(.swiper-button-next, .swiper-button-prev) {
    right: 50px;
  }

  .swiper-button-prev,
  .swiper-rtl .swiper-button-next {
    left: 50px;
  }
}
</style>