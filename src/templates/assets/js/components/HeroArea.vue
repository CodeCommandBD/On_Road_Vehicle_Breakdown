<template>
  <div class="swiper">
    <!-- Follow Us Section -->
    <div class="main-content">
      <div class="content d-flex align-items-center">
        <h1 class="mb-0">FOLLOW US</h1>
        <div class="content-item d-flex gap-3">
          <a href="#">
            <svg xmlns="http://www.w3.org/2000/svg" width="21" height="20" viewBox="0 0 21 20" fill="none">
              <path
                  d="M8.10717 20V10.8771H5.03711V7.32167H8.10717V4.69968C8.10717 1.65687 9.96561 0 12.68 0C13.9802 0 15.0977 0.0968046 15.4234 0.140073V3.31999L13.5408 3.32084C12.0646 3.32084 11.7787 4.02233 11.7787 5.05171V7.32167H15.2994L14.841 10.8771H11.7787V20H8.10717Z"
                  fill="#e9e6e6"/>
            </svg>
          </a>
          <a href="#">
            <svg xmlns="http://www.w3.org/2000/svg" width="21" height="20" viewBox="0 0 21 20" fill="none">
              <path
                  d="M20.4188 20L20.4238 19.9992V12.6642C20.4238 9.07583 19.6513 6.31167 15.4563 6.31167C13.4397 6.31167 12.0863 7.41833 11.5338 8.4675H11.4755V6.64667H7.49799V19.9992H11.6397V13.3875C11.6397 11.6467 11.9697 9.96333 14.1255 9.96333C16.2497 9.96333 16.2813 11.95 16.2813 13.4992V20H20.4188ZM0.753828 6.6475H4.9005V20H0.753828V6.6475ZM2.82549 0C1.49966 0 0.423828 1.07583 0.423828 2.40167C0.423828 3.7275 1.49966 4.82583 2.82549 4.82583C4.15133 4.82583 5.22716 3.7275 5.22716 2.40167C5.22672 1.76484 4.97355 1.15422 4.52324 0.703919C4.07294 0.253615 3.46232 0.000441474 2.82549 0Z"
                  fill="#e9e6e6"/>
            </svg>
          </a>
          <a href="#">
            <svg xmlns="http://www.w3.org/2000/svg" width="21" height="21" viewBox="0 0 21 21" fill="none">
              <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M6.30254 2H0L7.47254 11.8703L0.478034 20.1503H3.70971L8.99994 13.8879L13.6975 20.0927H20L12.3103 9.93549L12.3239 9.95301L18.9449 2.11526H15.7132L10.7963 7.93572L6.30254 2Z"
                    fill="#e9e6e6"/>
            </svg>
          </a>
        </div>
      </div>
    </div>

    <!-- Email and Phone -->
    <a href="#" class="position-absolute email d-flex align-items-center gap-4">
      <div class="pulse">
        <div class="pulse_img">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="14" viewBox="0 0 16 14" fill="none">
            <path d="..." fill="#FFF"/>
          </svg>
        </div>
      </div>
      <div class="email">
        <h1>abc@gmail.com</h1>
      </div>
    </a>

    <a href="#" class="position-absolute phone d-flex align-items-center gap-4">
      <div class="pulse">
        <div class="pulse_img">
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" fill="none">
            <path d="..." stroke="#FFF" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
      </div>
      <div class="email">
        <h1>+4252055568575</h1>
      </div>
    </a>

    <!-- Slides -->
    <div class="swiper-wrapper">
      <div class="swiper-slide">
        <img src="./Hero-img/hero-slide-one.png" alt=""/>
        <div class="hero-content">
          <h1>CAR REPAIR & AUTO <br/>SERVICE</h1>
          <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptas, ex? Illo voluptatem praesentium
            molestias corporis?</p>
          <a href="#">APPLY</a>
        </div>
      </div>

      <div class="swiper-slide">
        <img class="bg_black" src="./Hero-img/hero-slide-two.png" alt=""/>
        <div class="hero-content">
          <h1>CAR REPAIR & AUTO <br/>SERVICE</h1>
          <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptas, ex? Illo voluptatem praesentium
            molestias corporis?</p>
          <a href="#">APPLY</a>
        </div>
      </div>

      <div class="swiper-slide">
        <img src="./Hero-img/hero-slide-one.png" alt=""/>
        <div class="hero-content">
          <h1>CAR REPAIR & AUTO <br/>SERVICE</h1>
          <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptas, ex? Illo voluptatem praesentium
            molestias corporis?</p>
          <a href="#">APPLY</a>
        </div>
      </div>
    </div>

    <!-- Pagination and Navigation -->
    <div class="swiper-pagination"></div>
    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>
  </div>
</template>

<script>
import Swiper from 'swiper/bundle';


export default {
  name: "HeroArea",
  mounted() {
    new Swiper('.swiper', {
      direction: 'horizontal',
      loop: true,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
    });
  },
}
</script>

<style scoped>
a {
  text-decoration: none;
}

.swiper-pagination {
  margin-top: 5rem;
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.swiper-pagination-bullet-active {
  opacity: 1 !important;
  background: none;
  color: #ffffff !important;
}

.swiper-pagination-bullet {
  width: auto;
  height: auto;
  background: none;
  opacity: 0.3;
  color: white;
}

.swiper-horizontal > .swiper-pagination-bullets,
.swiper-pagination-bullets.swiper-pagination-horizontal,
.swiper-pagination-custom,
.swiper-pagination-fraction {
  top: -40rem;
  left: -2rem;
  width: 100%;
  align-items: end;
}

.swiper-horizontal > .swiper-pagination-bullets .swiper-pagination-bullet,
.swiper-pagination-horizontal.swiper-pagination-bullets .swiper-pagination-bullet {
  font-size: 25px;
  font-weight: 700;
}

.swiper {
  height: 100vh;
  position: relative;
}

.swiper-wrapper {
  height: 100%;
  width: 100%;
  position: relative;

}

.swiper-button-next,
.swiper-rtl .swiper-button-prev {
  right: 50px;
  left: auto;
  top: 90%;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  backdrop-filter: blur(100px);
  -webkit-backdrop-filter: blur(100px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  background-color: rgba(255, 255, 255, 0.25);
  transition: 0.7s;

}

.swiper-button-prev:hover {
  transform: scale(1.1);
}

.swiper-button-next:hover {
  transform: scale(1.1);
}

.swiper-button-prev,
.swiper-rtl .swiper-button-next {
  left: auto;
  right: 125px;
  top: 90%;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  backdrop-filter: blur(100px);
  -webkit-backdrop-filter: blur(100px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  background-color: rgba(255, 255, 255, 0.25);
  transition: 0.6s;
}

.main-content {
  position: absolute;
  z-index: 2;
  display: flex;
  align-items: center;
  gap: 20px;
  flex-direction: column;
  justify-content: center;
  top: 50%;
  left: -130px;
  transform: rotate(-90deg);
}

.content {
  gap: 160px;
}

.content h1 {
  color: #fff;
  font-size: 20px;

}

.content h1::before {
  content: '';
  top: 13px;
  left: 129px;
  width: 125px;
  height: 1px;
  background: white;
  position: absolute;
}

.content-item a {
  text-decoration: none;

}

.content-item path {
  transition: 0.5s;
}

.content-item a:hover path {
  fill: #FF532D !important;
}

.swiper-button-prev::after {
  content: '';
  width: 50px;
  height: 50px;
  position: absolute;
  bottom: -1px;
  right: -9px;
  background: url(./Hero-img/prev-button.png);
  background-repeat: no-repeat;

}

.swiper-button-next::after {
  content: '';
  width: 50px;
  height: 50px;
  position: absolute;
  bottom: -1px;
  right: -9px;
  background: url(./Hero-img/next-button.png);
  background-repeat: no-repeat;
}

.hero-content {
  width: 450px;
  position: absolute;
  top: 350px;
  left: 12%;
  z-index: 2;
}

.hero-content h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: white;
}

.hero-content p {
  color: rgb(229, 226, 226);
  font-size: 18px;
  line-height: 27px;
  margin-bottom: 50px;
}

.hero-content a {
  color: white;
  padding: 15px 80px;
  font-size: 20px;
  background: #FF532D;
}

.email {
  top: 150px;
  left: 30%;
  z-index: 5;
}

.phone {
  top: 150px;
  left: 55%;
  z-index: 5;
}

.pulse_img {
  position: absolute;
  top: 44%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.pulse {
  position: relative;
  width: 30px;
  height: 30px;
  background: #FF532D;
  border-radius: 50%;

}

.pulse::before,
.pulse::after {
  content: '';
  position: absolute;
  height: 100%;
  width: 100%;
  background-color: #ff2f00b9;
  border-radius: 50%;
  z-index: -1;
  opacity: 0.7;
}

.pulse::before {
  animation: pulse 2s ease-out infinite;
}

.pulse::after {
  animation: pulse 2s 1s ease-out infinite;
}

@keyframes pulse {
  100% {
    transform: scale(2.5);
    opacity: 0;
  }
}

.email h1 {
  color: #fff;
  font-size: 20px !important;
  font-style: normal;
  font-weight: 600;
  line-height: 12px;
  letter-spacing: 0.36px;
}

.bg_black::after {
  content: '';
  position: absolute;
  background: black;
  width: 100%;
  height: 100%;
}

.swiper-slide {
  position: relative;
  width: 100%;
  height: 100%;
}

.swiper-slide img {
  width: 100%;
  height: 100vh;
}

.swiper-slide::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.404); /* Adjust the opacity as needed */
  z-index: 1;
}

</style>