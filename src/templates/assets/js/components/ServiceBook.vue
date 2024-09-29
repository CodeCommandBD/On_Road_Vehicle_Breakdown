<template>
  <div class="service-book d-flex gap-5 justify-content-center">
    <div class="service-book-left">
      <div class="row m-0 position-relative dot">
        <div class="col-5">
          <div class="d-flex flex-column gap-4">
            <img class="service-img-one" src="./service-book-img/service-book-img-one.png" alt="" />
            <img class="service-img-two" src="./service-book-img/service-book-img-two.png" alt="" />
          </div>
        </div>
        <div class="col-5">
          <div class="d-flex flex-column gap-4">
            <img class="service-img-three" src="./service-book-img/service-book-img-three.png" alt="" />
            <img class="service-img-four" src="./service-book-img/service-book-img-four.png" alt="" />
          </div>
        </div>
      </div>
    </div>
    <div class="service-book-right d-flex flex-column align-items-end justify-content-center">
      <div class="subcription d-flex align-items-center">
        <svg class="setteing-icon" xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none">
          <path
            d="M0 9.11058C0.119355 9.72495 0.198523 10.0225 0.769556 10.7789C1.22733 11.224 2.10196 11.9136 2.86037 11.9651C2.29231 12.2918 0.220829 10.2473 0 9.11058Z"
            fill="#FF6644" />
          <path
            d="M6.95329 7.88544C8.29113 8.2351 9.77255 7.89161 10.821 6.846C12.0012 5.67073 12.2951 3.94825 11.7039 2.49909L9.72188 4.47471L7.97807 4.01223L7.51016 2.27123L9.49271 0.295053C8.03944 -0.294262 6.3114 -0.0007267 5.13177 1.1751C4.08335 2.22071 3.73875 3.69681 4.09067 5.03315L0 9.11058C0.119355 9.72495 0.198523 10.0225 0.769556 10.7789C1.22733 11.224 2.10196 11.9136 2.86037 11.9651L6.95329 7.88544Z"
            fill="#FF6644" />
        </svg>
        <div class="test-head-text">
          <h5>SPECIAL OFFER</h5>
        </div>
      </div>
      <div class="service-title">
        <h1>
          Get Your <span>Car/Bike</span><br />
          Serviced Today
        </h1>
      </div>
      <a class="book-link" href="">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        Book Service
      </a>
    </div>
  </div>
</template>

<script>
import ScrollMagic from 'scrollmagic';

export default {
  mounted() {
    const controller = new ScrollMagic.Controller();

    new ScrollMagic.Scene({
      triggerElement: '.service-img-one',
      triggerHook: 0.9,
    })
      .on('enter', () => {
        setTimeout(() => {
          document.querySelector('.service-img-one').classList.add('visible');
        }, 1000);
      })
      .addTo(controller);

    new ScrollMagic.Scene({
      triggerElement: '.service-img-two',
      triggerHook: 0.9,
    })
      .on('enter', () => {
        setTimeout(() => {
          document.querySelector('.service-img-two').classList.add('visible');
        }, 1000);
      })
      .addTo(controller);

    new ScrollMagic.Scene({
      triggerElement: '.service-img-three',
      triggerHook: 0.9,
    })
      .on('enter', () => {
        setTimeout(() => {
          document.querySelector('.service-img-three').classList.add('visible');
        }, 1000);
      })
      .addTo(controller);

    new ScrollMagic.Scene({
      triggerElement: '.service-img-four',
      triggerHook: 0.9,
    })
      .on('enter', () => {
        setTimeout(() => {
          document.querySelector('.service-img-four').classList.add('visible');
        }, 1000);
      })
      .addTo(controller);
  },
};
</script>

<style scoped>
.service-book {
  padding: 100px;
}

.subcription {
  gap: 10px;
  margin-bottom: 20px;
}

.test-head-text h5 {
  color: #F23C13;
  font-size: 12px;
  font-style: normal;
  font-weight: 400;
  line-height: 14px;
  /* 100% */
  letter-spacing: 0.7px;
  text-transform: uppercase;
  margin-bottom: 0;
}

.setteing-icon {
  animation: set 3s ease-in-out infinite;
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

.dot::after {
  content: '';
  width: 224px;
  height: 224px;
  top: -57px;
  right: 57px;
  position: absolute;
  background: url('./service-book-img/service-book-img-five.png');
  background-repeat: no-repeat;
  z-index: -1;
  animation: Top 8s linear infinite;
}

@keyframes Top {
  0% {
    transform: translateY(0px);
  }

  50% {
    transform: translateY(15px);
  }

  100% {
    transform: translateY(0px);
  }
}

.dot::before {
  content: '';
  width: 224px;
  height: 224px;
  bottom: -57px;
  left: -57px;
  position: absolute;
  background: url('./service-book-img/service-book-img-five.png');
  background-repeat: no-repeat;
  z-index: -1;
  animation: bottom 7.5s linear infinite;
}

@keyframes bottom {
  0% {
    transform: translateX(0px);
  }

  50% {
    transform: translateX(15px);
  }

  100% {
    transform: translateX(0px);
  }
}

.service-img-one {
  opacity: 0;
  transform: translateY(-80px);
  transition: all 1.3s ease-out;
}

.service-img-one.visible {
  opacity: 1;
  transform: none;
}

.service-img-two {
  opacity: 0;
  transform: translateX(-80px);
  transition: all 1.3s ease-out;
}

.service-img-two.visible {
  opacity: 1;
  transform: none;
}

.service-img-three {
  opacity: 0;
  transform: translateX(80px);
  transition: all 1.3s ease-out;
}

.service-img-three.visible {
  opacity: 1;
  transform: none;
}

.service-img-four {
  opacity: 0;
  transform: translateY(80px);
  transition: all 1.3s ease-out;
}

.service-img-four.visible {
  opacity: 1;
  transform: none;
}

.service-title h1 {
  color: #1E1E1E;
  text-align: right;
  font-size: 48px;
  font-style: normal;
  font-weight: 700;
  line-height: 160%;
  /* 76.8px */
  letter-spacing: 0.5px;
  text-transform: capitalize;
  margin-bottom: 60px;
}

.service-title h1 span {
  color: #F23C13;
}

.book-link {
  text-decoration: none;
  border-radius: 6px;
  background: linear-gradient(95deg, #F23C13 36.59%, #D22802 97.13%);
  color: #FFF;
  padding: 12px 60px;
  font-size: 18px;
  font-style: normal;
  font-weight: 600;
  line-height: 160%;
  /* 28.8px */
  letter-spacing: 0.5px;
  transition: 0.5s;
  position: relative;
  overflow: hidden;
  z-index: 2;
}


.book-link:hover {

  color: rgb(255, 255, 255);

}

.book-link::before {
  content: "";
  display: block;
  width: 50px;
  height: 50px;
  transform: translate(-50%, -50%);
  position: absolute;
  border-radius: 50%;
  z-index: -1;
  transition: 1s ease;
  top: -2em;
  left: -2em;
  background: rgb(61, 61, 61);
}

.book-link:hover::before {
  height: 410px;
  width: 410px;

}

.book-link:hover::after {
  height: 410px;
  width: 410px;

}

.book-link::after {
  content: "";
  display: block;
  width: 50px;
  height: 50px;
  transform: translate(-50%, -50%);
  position: absolute;
  border-radius: 50%;
  z-index: -1;
  transition: 1s ease;
  left: calc(100% + 2em);
  top: calc(100% + 2em);
  background: rgb(61, 61, 61);
}


.book-link span:nth-child(1) {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(to right, #2a048b00, rgb(81, 255, 0));
  animation: ani1 2s linear infinite;
}

@keyframes ani1 {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(100%);
  }
}

.book-link span:nth-child(2) {
  position: absolute;
  top: 0;
  right: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(to bottom, #2a048b00, rgb(81, 255, 0));
  animation: ani2 2s linear infinite;
}

@keyframes ani2 {
  0% {
    transform: translateY(-100%);
  }
  100% {
    transform: translateY(100%);
  }
}

.book-link span:nth-child(3) {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(to left, #2a048b00, rgb(81, 255, 0));
  animation: ani3 2s linear infinite;
}

@keyframes ani3 {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(-100%);
  }
}

.book-link span:nth-child(4) {
  position: absolute;
  top: 0;
  left: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(to top, #2a048b00, rgb(81, 255, 0));
  animation: ani4 2s linear infinite;
}

@keyframes ani4 {
  0% {
    transform: translateY(100%);
  }
  100% {
    transform: translateY(-100%);
  }
}


</style>