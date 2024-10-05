<template>
  <div class="main-faq">
    <div class="faq-container">
    <div class="faq-header">
      <h1 class="faq-title" :class="{ visible: isTitleVisible }">Frequently Asked Questions Online <br> Repair Service</h1>
    </div>

    <div
      v-for="(faq, index) in faqs"
      :key="index"
      :class="['tab', index % 2 === 0 ? 'left' : 'right']"
    >
      <input
        type="radio"
        :id="'acc' + index"
        name="acc"
        v-model="activeIndex"
        :value="index"
      >
      <label :for="'acc' + index">
        <h1>{{ index + 1 }}</h1>
        <h4>{{ faq.question }}</h4>
      </label>
      <div class="content" v-if="activeIndex === index">
        <p>{{ faq.answer }}</p>
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
      activeIndex: null,
      isTitleVisible: false,
      faqs: [
        {
          question: "What is Webflow and why is it the best website builder?",
          answer:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        },
        {
          question: "What is your favorite template from BRIX Templates?",
          answer:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        },
        {
          question: "What is your favorite template from BRIX Templates?",
          answer:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        },
        {
          question: "What is your favorite template from BRIX Templates?",
          answer:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        },
      ],
    };
  },
  mounted() {
    // ScrollMagic for triggering animations
    const controller = new ScrollMagic.Controller();

    // Title animation
    new ScrollMagic.Scene({
      triggerElement: ".faq-title",
      triggerHook: 0.9,
    })
      .setClassToggle(".faq-title", "visible")
      .addTo(controller);

    // Left tab animation
    new ScrollMagic.Scene({
      triggerElement: ".left",
      triggerHook: 0.9,
    })
      .setClassToggle(".left", "visible")
      .addTo(controller);

    // Right tab animation
    new ScrollMagic.Scene({
      triggerElement: ".right",
      triggerHook: 0.9,
    })
      .setClassToggle(".right", "visible")
      .addTo(controller);
  },
};
</script>

<style scoped>

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

.main-faq {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #f5f8ff;
}

.faq-container {
  width: 70%;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.faq-header h1 {
  color: #1E1E1E;
  font-size: 48px;
  font-style: normal;
  font-weight: 700;
  line-height: 160%;
  /* 76.8px */
  letter-spacing: 0.5px;
  text-transform: capitalize;
}

.tab {
  position: relative;
  background: #FFF;
  padding: 0 20px 20px;
  border-radius: 18px;
  box-shadow: 0px 5px 16px 0px rgba(8, 15, 52, 0.06);
  overflow: hidden;
}

.tab input {
  appearance: none;
}

.tab label {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.tab label::after {
  content: '+';
  position: absolute;
  right: 50px;
  font-size: 40px;
  font-weight: 600;
  color: rgba(0, 0, 0, 0.1);
  transition: transform 1s;
}

.tab:hover label::after {
  color: #333;
}

.tab input:checked ~ label::after {
  transform: rotate(135deg);
  color: white;
}

.tab label h1 {
  width: 40px;
  height: 40px;
  background: #333;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
  font-size: 1.25em;
  border-radius: 5px;
  margin-right: 10px;
}

.tab label h4 {
  position: relative;
  color: #1E1E1E;
  font-size: 20px;
  font-style: normal;
  font-weight: 500;
  line-height: 28px;
  /* 127.273% */
  z-index: 10;
}

.tab .content {
  max-height: 0;
  transition: max-height 0.6s ease-out, padding 0.6s ease-out;
  overflow: hidden;
  padding: 0 20px;
}

.tab input:checked ~ .content {
  max-height: 100vh;
  padding: 10px;

}

.tab .content p {
  position: relative;
  padding: 10px 0;
  color: #333;
  z-index: 10;
  font-size: 20px;
}

.tab:nth-child(2) label h1 {
  background: linear-gradient(135deg, #3bbb3b, #49c628);
}

.tab:nth-child(3) label h1 {
  background: linear-gradient(135deg, #3c8ce7, #01c1d3);
}

.tab:nth-child(4) label h1 {
  background: linear-gradient(135deg, #ec55e5, #c32bac);
}

.tab:nth-child(5) label h1 {
  background: linear-gradient(135deg, #fd6e6a, #d8aa03);
}

.tab input:checked ~ label h1 {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  color: rgba(255, 255, 255, 0.2);
  font-size: 8em;
  justify-content: flex-end;
  padding: 20px;

}

.tab input:checked ~ .content p {
  color: white;
}

.tab input:checked ~ label h4 {
  background: #FFF;
  padding: 2px 10px;
  color: #333;
  border-radius: 3px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
}

.faq-title {
  opacity: 0;
  transform: translateY(50px);
  transition: all 1s ease-out;
}

.faq-title.visible {
  opacity: 1;
  transform: none;
}

.left {
  opacity: 0;
  transform: translateX(-80px);
  transition: all 1s ease-out;
}

.left.visible {
  opacity: 1;
  transform: none;
}

.right {
  opacity: 0;
  transform: translateX(80px);
  transition: all 1s ease-out;
}

.right.visible {
  opacity: 1;
  transform: none;
}
</style>