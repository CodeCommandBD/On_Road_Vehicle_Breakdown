<template>
  <div class="top-gara">
    <div class="top-gara-head">
      <div class="subscription d-flex align-items-center">
        <svg class="setting-icon" xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none">
          <path
            d="M0 9.11058C0.119355 9.72495 0.198523 10.0225 0.769556 10.7789C1.22733 11.224 2.10196 11.9136 2.86037 11.9651C2.29231 12.2918 0.220829 10.2473 0 9.11058Z"
            fill="#FF6644" />
          <path
            d="M6.95329 7.88544C8.29113 8.2351 9.77255 7.89161 10.821 6.846C12.0012 5.67073 12.2951 3.94825 11.7039 2.49909L9.72188 4.47471L7.97807 4.01223L7.51016 2.27123L9.49271 0.295053C8.03944 -0.294262 6.3114 -0.0007267 5.13177 1.1751C4.08335 2.22071 3.73875 3.69681 4.09067 5.03315L0 9.11058C0.119355 9.72495 0.198523 10.0225 0.769556 10.7789C1.22733 11.224 2.10196 11.9136 2.86037 11.9651L6.95329 7.88544Z"
            fill="#FF6644" />
        </svg>
        <div class="test-head-text">
          <h5>TOP MECHANIC</h5>
        </div>
      </div>
      <h1 class="top_garage">Meet Our Top Garage</h1>
    </div>

    <div class="top-gara-card-area">
      <div class="top-gara-two-div" v-for="(item, index) in garageItems" :key="index">
        <div class="top-gara-line">
          <h4 class="progress-item">{{ (index + 1).toString().padStart(2, '0') }}</h4>
          <div class="progress-item-line"></div>
        </div>
        <div class="top-gara-card">
          <div class="top-gara-card-img">
            <img :src="item.img" alt="" class="top-gara-img" />
          </div>
          <div class="top-gara-card-body">
            <div class="mb-3">
              <svg xmlns="http://www.w3.org/2000/svg" width="31" height="30" viewBox="0 0 31 30" fill="none">
                <path
                  d="M14.5019 2.5549C14.7632 1.75073 15.9009 1.75072 16.1622 2.5549L18.5038 9.76161C18.6206 10.1213 18.9558 10.3647 19.3339 10.3647H26.9115C27.7571 10.3647 28.1086 11.4468 27.4246 11.9438L21.2942 16.3978C20.9882 16.62 20.8602 17.014 20.9771 17.3736L23.3187 24.5804C23.58 25.3845 22.6596 26.0532 21.9755 25.5562L15.8451 21.1022C15.5392 20.88 15.1249 20.88 14.819 21.1022L8.68858 25.5562C8.00451 26.0532 7.0841 25.3845 7.34539 24.5804L9.68699 17.3736C9.80385 17.014 9.67583 16.62 9.36991 16.3978L3.23951 11.9438C2.55544 11.4468 2.907 10.3647 3.75256 10.3647H11.3302C11.7083 10.3647 12.0434 10.1213 12.1603 9.76161L14.5019 2.5549Z"
                  fill="#F23C13" />
              </svg>
              <svg xmlns="http://www.w3.org/2000/svg" width="31" height="30" viewBox="0 0 31 30" fill="none">
                <path
                  d="M14.5019 2.5549C14.7632 1.75073 15.9009 1.75072 16.1622 2.5549L18.5038 9.76161C18.6206 10.1213 18.9558 10.3647 19.3339 10.3647H26.9115C27.7571 10.3647 28.1086 11.4468 27.4246 11.9438L21.2942 16.3978C20.9882 16.62 20.8602 17.014 20.9771 17.3736L23.3187 24.5804C23.58 25.3845 22.6596 26.0532 21.9755 25.5562L15.8451 21.1022C15.5392 20.88 15.1249 20.88 14.819 21.1022L8.68858 25.5562C8.00451 26.0532 7.0841 25.3845 7.34539 24.5804L9.68699 17.3736C9.80385 17.014 9.67583 16.62 9.36991 16.3978L3.23951 11.9438C2.55544 11.4468 2.907 10.3647 3.75256 10.3647H11.3302C11.7083 10.3647 12.0434 10.1213 12.1603 9.76161L14.5019 2.5549Z"
                  fill="#F23C13" />
              </svg>
              <svg xmlns="http://www.w3.org/2000/svg" width="31" height="30" viewBox="0 0 31 30" fill="none">
                <path
                  d="M14.5019 2.5549C14.7632 1.75073 15.9009 1.75072 16.1622 2.5549L18.5038 9.76161C18.6206 10.1213 18.9558 10.3647 19.3339 10.3647H26.9115C27.7571 10.3647 28.1086 11.4468 27.4246 11.9438L21.2942 16.3978C20.9882 16.62 20.8602 17.014 20.9771 17.3736L23.3187 24.5804C23.58 25.3845 22.6596 26.0532 21.9755 25.5562L15.8451 21.1022C15.5392 20.88 15.1249 20.88 14.819 21.1022L8.68858 25.5562C8.00451 26.0532 7.0841 25.3845 7.34539 24.5804L9.68699 17.3736C9.80385 17.014 9.67583 16.62 9.36991 16.3978L3.23951 11.9438C2.55544 11.4468 2.907 10.3647 3.75256 10.3647H11.3302C11.7083 10.3647 12.0434 10.1213 12.1603 9.76161L14.5019 2.5549Z"
                  fill="#F23C13" />
              </svg>
              <svg xmlns="http://www.w3.org/2000/svg" width="31" height="30" viewBox="0 0 31 30" fill="none">
                <path
                  d="M14.5019 2.5549C14.7632 1.75073 15.9009 1.75072 16.1622 2.5549L18.5038 9.76161C18.6206 10.1213 18.9558 10.3647 19.3339 10.3647H26.9115C27.7571 10.3647 28.1086 11.4468 27.4246 11.9438L21.2942 16.3978C20.9882 16.62 20.8602 17.014 20.9771 17.3736L23.3187 24.5804C23.58 25.3845 22.6596 26.0532 21.9755 25.5562L15.8451 21.1022C15.5392 20.88 15.1249 20.88 14.819 21.1022L8.68858 25.5562C8.00451 26.0532 7.0841 25.3845 7.34539 24.5804L9.68699 17.3736C9.80385 17.014 9.67583 16.62 9.36991 16.3978L3.23951 11.9438C2.55544 11.4468 2.907 10.3647 3.75256 10.3647H11.3302C11.7083 10.3647 12.0434 10.1213 12.1603 9.76161L14.5019 2.5549Z"
                  fill="#F23C13" />
              </svg>
              <svg xmlns="http://www.w3.org/2000/svg" width="31" height="30" viewBox="0 0 31 30" fill="none">
                <path
                  d="M14.5019 2.5549C14.7632 1.75073 15.9009 1.75072 16.1622 2.5549L18.5038 9.76161C18.6206 10.1213 18.9558 10.3647 19.3339 10.3647H26.9115C27.7571 10.3647 28.1086 11.4468 27.4246 11.9438L21.2942 16.3978C20.9882 16.62 20.8602 17.014 20.9771 17.3736L23.3187 24.5804C23.58 25.3845 22.6596 26.0532 21.9755 25.5562L15.8451 21.1022C15.5392 20.88 15.1249 20.88 14.819 21.1022L8.68858 25.5562C8.00451 26.0532 7.0841 25.3845 7.34539 24.5804L9.68699 17.3736C9.80385 17.014 9.67583 16.62 9.36991 16.3978L3.23951 11.9438C2.55544 11.4468 2.907 10.3647 3.75256 10.3647H11.3302C11.7083 10.3647 12.0434 10.1213 12.1603 9.76161L14.5019 2.5549Z"
                  fill="#F23C13" />
              </svg>
            </div>
            <h2>{{ item.name }}</h2>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ScrollMagic from "scrollmagic";

export default {
  data() {
    return {
      garageItems: [
        { name: "Hanrey Watson", img: require("@assets/js/components/Top-garage-img/top-garage-one.png") },
        { name: "Hanrey Watson", img: require("@assets/js/components/Top-garage-img/top-garage-two.png") },
        { name: "Hanrey Watson", img: require("@assets/js/components/Top-garage-img/top-garage-three.png") }
      ]
    };
  },
  mounted() {
    const controller = new ScrollMagic.Controller();

    new ScrollMagic.Scene({
      triggerElement: ".top-gara-img",
      triggerHook: 0.9
    })
      .setClassToggle(".top-gara-img", "visible")
      .addTo(controller);

    new ScrollMagic.Scene({
      triggerElement: ".top_garage",
      triggerHook: 0.9
    })
      .setClassToggle(".top_garage", "visible")
      .addTo(controller);
  }
};
</script>


<style scoped>
.top-gara {
  padding: 80px;

}

.subscription {
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

.top-gara-head {
  margin-bottom: 60px;
}

.top-gara-card-area {

  display: flex;
  justify-content: space-around;
  gap: 50px;
}

.top-gara-card {
  width: fit-content;
  border-radius: 12px;
  border: 2px solid #c9c7c4;
  padding: 60px;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: .6s;
}

.top-gara-card:hover {
  border-color: #F23C13;
}

.top-gara-line {
  padding: 0 10px;
  margin-bottom: 25px;
  display: flex;
  align-items: center;
  gap: 50px;
}

.progress-item {
  line-height: 1.2em;
  font-weight: 700;
  color: transparent;
  -webkit-text-stroke: 1px #F23C13;
  font-size: 28px;
}

.progress-item-line {
  width: 100%;
  height: 2px;
  background: #F23C13;
}

.top-gara-head h1 {
  color: #1E1E1E;
  font-size: 48px;
  font-style: normal;
  font-weight: 700;
  line-height: 160%;
  /* 76.8px */
  letter-spacing: 0.5px;
  text-transform: capitalize;
}

.top-gara-card-body h4 {
  color: #F23C13;
  font-size: 16px;
  font-style: normal;
  font-weight: 500;
  line-height: 16px;
  /* 100% */
  font-variant: all-small-caps;
  text-align: center;
}

.top-gara-card-body h2 {
  color: #1E1E1E;
  font-size: 24px;
  font-style: normal;
  font-weight: 600;
  line-height: 24px;
  /* 100% */
  text-transform: capitalize;
}

.top-gara-img {
  opacity: 0;
  transform: translateY(40px);
  transition: all 1s ease-out;
}

.top-gara-img.visible {
  opacity: 1;
  transform: none;
}

.top_garage {
  opacity: 0;
  transform: translateX(-40px);
  transition: all 1s ease-out;
}

.top_garage.visible {
  opacity: 1;
  transform: none;
}
</style>