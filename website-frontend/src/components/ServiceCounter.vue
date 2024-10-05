<template>
  <div class="stats-container">
    <div class="stat" v-for="(stat, index) in stats" :key="index">
      <div ref="odometers" :class="[stat.className, 'odometer', 'plus', 'sub']">0</div>
      <div class="type">{{ stat.label }}</div>
    </div>
  </div>
</template>

<script>
import Odometer from "odometer"; // Ensure you import Odometer or include its script in your project

export default {
  data() {
    return {
      stats: [
        {
          className: "subscribers-odometer",
          value: 29800,
          label: "HAPPY CUSTOMERS",
        },
        {
          className: "videos-odometer",
          value: 10,
          label: "Years of Services",
        },
        {
          className: "projects-odometer",
          value: 89,
          label: "service Completed",
        },
      ],
    };
  },
  mounted() {
    this.stats.forEach((stat, index) => {
      const el = this.$refs.odometers[index];

      const odometer = new Odometer({
        el: el,
        value: 0,
      });

      let hasRun = false;

      const options = {
        threshold: [0, 0.9],
      };

      const callback = (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && !hasRun) {
            odometer.update(stat.value);
            hasRun = true;
          }
        });
      };

      const observer = new IntersectionObserver(callback, options);
      observer.observe(el);
    });
  },
};
</script>

<style scoped>
body {
  margin: 0;

}


.stats-container {
  height: 200px;
  display: grid;
  gap: 24px;
  grid-template-columns: 1fr 1fr 1fr;
  padding: 80px 0px;
  max-width: 1000px;
  margin: auto;

}

.stats-container .stat {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 24px;
  text-align: center;
  gap: 15px;
}


.stats-container .stat .odometer {
  font-size: 50px;
  font-weight: bold;
  display: inline-block;
}

.stats-container .stat .type {
  color: #8d8080;
  font-weight: 700;
  line-height: normal;
  font-size: 24px;
  text-transform: uppercase;
}

.odometer.plus {
  position: relative;
}

.odometer.plus::after {
  content: "+";
  position: absolute;
  top: 0;
  right: -37px;
  font-size: 50px;
}

.sub {
  color: transparent;
  font-weight: 700;
  -webkit-text-stroke: 3px orangered;
}

@media (max-width: 700px) {
  .stats-container {
    grid-template-columns: 1fr;
  }
}
</style>