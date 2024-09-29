<template>
  <div class="repair">
    <div class="repair-header text-center">
      <div class="subcription d-flex align-items-center justify-content-center">
         <svg class="setteing-icon" xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12"
                    fill="none">
                    <path
                        d="M0 9.11058C0.119355 9.72495 0.198523 10.0225 0.769556 10.7789C1.22733 11.224 2.10196 11.9136 2.86037 11.9651C2.29231 12.2918 0.220829 10.2473 0 9.11058Z"
                        fill="#FF6644" />
                    <path
                        d="M6.95329 7.88544C8.29113 8.2351 9.77255 7.89161 10.821 6.846C12.0012 5.67073 12.2951 3.94825 11.7039 2.49909L9.72188 4.47471L7.97807 4.01223L7.51016 2.27123L9.49271 0.295053C8.03944 -0.294262 6.3114 -0.0007267 5.13177 1.1751C4.08335 2.22071 3.73875 3.69681 4.09067 5.03315L0 9.11058C0.119355 9.72495 0.198523 10.0225 0.769556 10.7789C1.22733 11.224 2.10196 11.9136 2.86037 11.9651L6.95329 7.88544Z"
                        fill="#FF6644" />
                </svg>
        <div class="test-head-text">
          <h5>Repair Services</h5>
        </div>
      </div>
      <h1 class="anytime">
        You Get affordable <br/>
        repair services
      </h1>
    </div>

    <!-- Tab Navigation -->
    <ul class="m-0 nav nav-fill nav-justified nav-tabspb-3 mt-4" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button
            class="nav-link nav-one date-btn previous-date-border p-2"
            id="home-tab"
            :class="{ active: activeTab === 'home' }"
            @click="setActiveTab('home')"
            type="button"
            role="tab"
            aria-controls="home"
            aria-selected="activeTab === 'home'"
        >
          Cars
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
            class="nav-link nav-two date-btn p-2"
            id="profile-tab"
            :class="{ active: activeTab === 'profile' }"
            @click="setActiveTab('profile')"
            type="button"
            role="tab"
            aria-controls="profile"
            aria-selected="activeTab === 'profile'"
        >
          Bikes
        </button>
      </li>
    </ul>

    <!-- Tab Content -->
    <div class="tab-content">
      <div v-if="activeTab === 'home'" id="home" class="tab-pane active" role="tabpanel" aria-labelledby="home-tab">
        <div class="row d-flex justify-content-between mb-5">
          <div v-for="service in carServices" :key="service.name" class="col-2 service-item">
            <img :src="service.icon"/>
            <p class="mb-0">{{ service.name }}</p>
          </div>
        </div>
      </div>

      <div v-if="activeTab === 'profile'" id="profile" class="tab-pane active" role="tabpanel"
           aria-labelledby="profile-tab">
        <div class="row d-flex justify-content-between mb-5">
          <div v-for="service in bikeServices" :key="service.name" class="col-2 service-item">
            <img :src="service.icon"/>
            <p class="mb-0">{{ service.name }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ScrollMagic from 'scrollmagic';

export default {
  data() {
    return {
      activeTab: "profile", // Default active tab
      carServices: [
        { name: "Windshields", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
        { name: "Door", icon: require('@assets/js/components/repair-service-img/Vector (2).png') },
        { name: "Air Condition", icon: require('@assets/js/components/repair-service-img/Vector (3).png') },
        { name: "Batteries", icon: require('@assets/js/components/repair-service-img/Vector (4).png') },
        { name: "Brake", icon: require('@assets/js/components/repair-service-img/Vector (5).png') },
        { name: "Car Check", icon: require('@assets/js/components/repair-service-img/Vector (6).png') },
        { name: "Oil Change", icon: require('@assets/js/components/repair-service-img/Vector (7).png') },
        { name: "Suspension", icon: require('@assets/js/components/repair-service-img/Vector (8).png') },
        { name: "Tire", icon: require('@assets/js/components/repair-service-img/Vector (9).png') },
        { name: "Looking Glass", icon: require('@assets/js/components/repair-service-img/Vector (10).png') },
        { name: "Cleaning", icon: require('@assets/js/components/repair-service-img/Vector (11).png') },
        { name: "Painting", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
      ],
      bikeServices: [
        { name: "Windshields", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
        { name: "Door", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
        { name: "Air Condition", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
        { name: "Batteries", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
        { name: "Brake", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
        { name: "Car Check", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
        { name: "Oil Change", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
        { name: "Suspension", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
        { name: "Tire", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
        { name: "Looking Glass", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
        { name: "Cleaning", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
        { name: "Painting", icon: require('@assets/js/components/repair-service-img/Vector (1).png') },
      ],
    };
  },
  mounted() {
    this.initializeScrollMagic();
  },
  methods: {
    setActiveTab(tab) {
      this.activeTab = tab;
    },
    initializeScrollMagic() {
      const controller = new ScrollMagic.Controller();
      new ScrollMagic.Scene({
        triggerElement: ".anytime",
        triggerHook: 0.9,
      })
          .setClassToggle(".anytime", "visible")
          .addTo(controller);
    },
  },
};

</script>



<style scoped>
.repair {
  padding: 60px;
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

.repair-header {
  margin-bottom: 60px;
}

.repair-button-box {
  width: 100%;
  margin: 35px auto;
  position: relative;


}

.toggle-btn {
  border: none;
  background: transparent;
  position: relative;
  cursor: pointer;
  outline: none;

  /* border-bottom: 2px solid #F23C13; */
}

#btn_line {
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(to right, #F23C13, #F23C13);
  transition: 0.5s;

}

.service-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 60px;
  padding: 40px 0px;
  border-radius: 16px;
  border: 1px solid var(--Border, #E7EAF3);
  background: #FFF;
  width: 200px;
  box-shadow: 0 0 20px rgba(228, 222, 222, 0.637);
}


.nav-fill {
  margin-bottom: 40px !important;
}

.nav-link:focus,
.nav-link:hover {
  color: #F23C13 !important;
}

.date-btn {
  color: #F23C13;
  font-size: 28px;
  font-style: normal;
  font-weight: 600;
  line-height: 160%;
  /* 44.8px */
  font-variant: all-small-caps;
  letter-spacing: 0.5px;

}

.nav-one.active,
.nav-two.active {
  border-bottom: 2px solid #F23C13;
}


.anytime {
  opacity: 0;
  transform: translateY(100px);
  transition: all 1s ease-out;
}

.anytime.visible {
  opacity: 1;
  transform: none;
}
</style>