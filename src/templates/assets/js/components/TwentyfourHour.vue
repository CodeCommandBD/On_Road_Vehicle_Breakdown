<template>
  <div class="hour">
    <!-- Header Section -->
    <div class="hour-header">
      <div class="subcription d-flex align-items-center">
        <svg class="setteing-icon" xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12"
             fill="none">
          <path
              d="M0 9.11058C0.119355 9.72495 0.198523 10.0225 0.769556 10.7789C1.22733 11.224 2.10196 11.9136 2.86037 11.9651C2.29231 12.2918 0.220829 10.2473 0 9.11058Z"
              fill="#FF6644"/>
          <path
              d="M6.95329 7.88544C8.29113 8.2351 9.77255 7.89161 10.821 6.846C12.0012 5.67073 12.2951 3.94825 11.7039 2.49909L9.72188 4.47471L7.97807 4.01223L7.51016 2.27123L9.49271 0.295053C8.03944 -0.294262 6.3114 -0.0007267 5.13177 1.1751C4.08335 2.22071 3.73875 3.69681 4.09067 5.03315L0 9.11058C0.119355 9.72495 0.198523 10.0225 0.769556 10.7789C1.22733 11.224 2.10196 11.9136 2.86037 11.9651L6.95329 7.88544Z"
              fill="#FF6644"/>
        </svg>
        <div class="test-head-text">
          <h5>WHY CHOOSE US</h5>
        </div>
      </div>
      <h1 class="anytime">24/7 Availability: Repair <br> Serviced Anytime</h1>
    </div>

    <!-- Body Section -->
    <div class="hour-body overflow-hidden d-flex align-items-center justify-content-between">
      <!-- Cards -->
      <div class="card bg-transparent" v-for="(card, index) in cards" :key="index">
        <div class="hour-card-area">
          <div class="hour-card">
            <img  :src="card.image" alt="Card Image">

            <div class="hour-card-body">
              <h2>{{ card.title }}</h2>
              <p>{{ card.description }}</p>
            </div>

            <div class="learn">
              <a class="learn-more" href="">{{ card.linkText }}</a>
              <img :src="card.linkIcon" alt="Link Icon">
            </div>
          </div>
        </div>
      </div>

      <!-- Line Separators -->
      <div class="line line-one"></div>
      <div class="line line-two"></div>
    </div>
  </div>
</template>

<script>
import ScrollMagic from 'scrollmagic';

export default {
  data() {
    return {
      cards: [
        {
          image: require('@assets/js/components/Twentyfour-hour-img/Vector (12).png'),
          title: 'Easy Booking',
          description: 'Our user-friendly platform makes it easy to book car or bike maintenance and repairs quickly and conveniently.',
          linkText: 'Learn More',
          linkIcon: require('@assets/js/components/Twentyfour-hour-img/Icon.png'),
        },
        {
          image: require('@assets/js/components/Twentyfour-hour-img/Vector (13).png'),
          title: 'Expert Mechanics',
          description: 'Our skilled technicians will keep your car running smoothly and safely, handling everything from check-ups to repairs.',
          linkText: 'Learn More',
          linkIcon: require('@assets/js/components/Twentyfour-hour-img/Icon.png')
        },
        {
          image: require('@assets/js/components/Twentyfour-hour-img/Vector (14).png'),
          title: 'Genuine parts',
          description: 'We use only original, high-quality parts for repairs, ensuring your car runs smoothly, lasts longer, and stays safe.',
          linkText: 'Learn More',
          linkIcon: require('@assets/js/components/Twentyfour-hour-img/Icon.png')
        }
      ]
    };
  },
  mounted() {
    const controller = new ScrollMagic.Controller();

    new ScrollMagic.Scene({
      triggerElement: ".anytime",
      triggerHook: 0.9,
    })
        .setClassToggle(".anytime", "visible")
        .addTo(controller);

    new ScrollMagic.Scene({
      triggerElement: ".line-one",
      triggerHook: 0.9,
    })
        .setClassToggle(".line-one", "visible")
        .addTo(controller);

    new ScrollMagic.Scene({
      triggerElement: ".line-two",
      triggerHook: 0.9,
    })
        .setClassToggle(".line-two", "visible")
        .addTo(controller);
  }
};
</script>

<style scoped>
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

.hour-header h1 {
  color: #1E1E1E;
  font-size: 48px;
  font-style: normal;
  font-weight: 700;
  line-height: 160%;
  /* 76.8px */
  letter-spacing: 0.5px;
  text-transform: capitalize;
}

.hour-header {
  padding: 80px 80px 0;
  margin-bottom: 60px;
}

.hour-body {
  width: 100%;
  height: 400px;
  padding: 0 80px;
  background: url(./Twentyfour-hour-img/24hour-bg.png);
  background-repeat: no-repeat;
  background-position: right;
  background-attachment: fixed;
  background-size: cover;
}

.hour-card-body {
  margin: 25px 0;
  width: fit-content;
}

.hour-card-body h2 {
  color: #F23C13;
  font-size: 30px;
  font-style: normal;
  font-weight: 700;
  line-height: 140%;
  /* 42px */
  margin-bottom: 12px;
}

.hour-card-body p {
  color: #ffffff;
  text-align: justify;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 180%;
  /* 25.2px */
  margin-bottom: 0;
}

.learn-more {
  position: relative;
  text-decoration: none;
  color: white;
  font-size: 16px;
  font-style: normal;
  font-weight: 700;
  line-height: 172%;
  /* 27.52px */
  display: inline-block;
  /* z-index: 1; */
}

.learn {
  width: fit-content;
}

.learn > img {
  opacity: 0;
  transition: 0.5s;
}

.learn:hover img {
  opacity: 1;
  transform: translateX(5px);

}

.learn-more::after {
  content: '';
  bottom: -5px;
  opacity: 0;
  left: 0;
  height: 1.5px;
  width: 0%;
  background: #ff2f00;
  position: absolute;
  transition: 0.5s;
}

.learn:hover .learn-more::after {
  opacity: 1;
  width: 135%;
}

.hour-card-area {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.line {
  width: 2px;
  height: 300px;
  background: #ff2f00;
}

.hour-card > img {
  transition: 1s;
}

.hour-card-area:hover .hour-card > img {
  transform: rotateY(360deg);
}


.anytime {
  opacity: 0;
  transform: translateY(50px);
  transition: all 1s ease-out;
}

.anytime.visible {
  opacity: 1;
  transform: none;
}

.line-one {
  margin: 0 40px;
  opacity: 0;
  transform: translateY(150px);
  transition: all 1s ease-out;
}

.line-one.visible {
  opacity: 1;
  transform: none;
}

.line-two {
  margin: 0 40px;
  opacity: 0;
  transform: translateY(-150px);
  transition: all 1s ease-out;
}

.line-two.visible {
  opacity: 1;
  transform: none;
}

@media only screen and (max-width: 991px) {
}
</style>