<template>
  <div class="nav w-100 ">
    <nav class="navbar navbar-expand-lg d-flex justify-content-between bg-black">
      <a class="navbar-brand" href="#">
        <img src="./Nav-img/main-logo.svg" alt=""/>
      </a>
      <div class="container-fluid">
        <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link wave-text" href="#">
                <span style="--i: 1">H</span>
                <span style="--i: 2">O</span>
                <span style="--i: 3">M</span>
                <span style="--i: 4">E</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link wave-text" href="#">
                <span style="--i: 1">A</span>
                <span style="--i: 2">B</span>
                <span style="--i: 3">O</span>
                <span style="--i: 4">U</span>
                <span style="--i: 5">T</span>
              </a>
            </li>
            <li class="nav-item uniq-item">
              <div class="position-relative">
                <a class="nav-link wave-text show-item" href="#">
                  <span style="--i: 1">S</span>
                  <span style="--i: 2">E</span>
                  <span style="--i: 3">R</span>
                  <span style="--i: 4">V</span>
                  <span style="--i: 5">I</span>
                  <span style="--i: 6">C</span>
                  <span style="--i: 7">E</span>
                  <span style="--i: 8">S</span>
                </a>
                <a class="icon text-decoration-none" @click="toggleContent">{{ icon }}</a>
              </div>
            </li>
          </ul>

          <div class="nav_content position-absolute d-flex" :class="{ show: isContentVisible }"
               @mouseleave="hideContent">
            <div class="car-bike">
              <ul class="d-flex flex-column align-items-start m-0 nav nav-fill nav-justified nav-tabspb-3 mt-4"
                  id="myTab" role="tablist">
                <li class="nav-item" role="presentation">
                  <button
                      class="nav-link nav-one date-btn previous-date-border p-2"
                      id="home-tab"
                      data-bs-toggle="tab"
                      data-bs-target="#home"
                      type="button"
                      role="tab"
                      aria-controls="home"
                      aria-selected="true"
                      @click="activateTab('#home')"
                  >
                    <a class="for_nav_content" href="#">
                      <span style="--i: 1">C</span>
                      <span style="--i: 2">A</span>
                      <span style="--i: 3">R</span>
                      <span style="--i: 4">S</span>
                    </a>
                  </button>
                </li>

                <li class="nav-item" role="presentation">
                  <button
                      class="nav-link nav-two date-btn p-2"
                      id="profile-tab"
                      data-bs-toggle="tab"
                      data-bs-target="#profile"
                      type="button"
                      role="tab"
                      aria-controls="profile"
                      aria-selected="false"
                      @click="activateTab('#profile')"
                  >
                    <a class="for_nav_content" href="#">
                      <span style="--i: 1">B</span>
                      <span style="--i: 2">I</span>
                      <span style="--i: 3">K</span>
                      <span style="--i: 4">E</span>
                      <span style="--i: 5">S</span>
                    </a>
                  </button>
                </li>
              </ul>
            </div>
            <div class="mid_line"></div>
            <div class="tab-content">
              <div v-for="(pane, index) in panes" :key="index" :id="pane.id" class="tab-pane"
                   :class="{ active: activeTab === pane.id }">
                <div class="service_items">
                  <div class="service_item_box m-0 gap-4">
                    <div v-for="(service, index) in pane.services" :key="index"
                         class="service__item d-flex align-items-center gap-3 service_item">
                      <img :src="service.imgSrc" :alt="service.altText"/>
                      <div class="item_name">
                        <h4>{{ service.title }}</h4>
                        <p>{{ service.description }}</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="profile">
        <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36" fill="none">
          <circle cx="18" cy="18" r="17.5" stroke="#fff"/>
          <path
              d="M21.2744 18.6384C22.1562 17.9446 22.7999 16.9932 23.1158 15.9165C23.4317 14.8398 23.4043 13.6915 23.0371 12.6312C22.67 11.5709 21.9816 10.6513 21.0675 10.0005C20.1535 9.34973 19.0593 9 17.9373 9C16.8152 9 15.7211 9.34973 14.807 10.0005C13.893 10.6513 13.2045 11.5709 12.8374 12.6312C12.4703 13.6915 12.4428 14.8398 12.7587 15.9165C13.0747 16.9932 13.7184 17.9446 14.6002 18.6384C13.0891 19.2438 11.7707 20.2479 10.7854 21.5436C9.80012 22.8394 9.18493 24.3783 9.00543 25.9961C8.99243 26.1143 9.00283 26.2338 9.03603 26.3479C9.06923 26.462 9.12458 26.5684 9.19891 26.6612C9.34904 26.8484 9.56741 26.9683 9.80596 26.9946C10.0445 27.0208 10.2837 26.9512 10.471 26.8011C10.6582 26.651 10.7781 26.4326 10.8044 26.194C11.0019 24.4357 11.8403 22.8118 13.1594 21.6326C14.4785 20.4533 16.1859 19.8014 17.9553 19.8014C19.7246 19.8014 21.432 20.4533 22.7511 21.6326C24.0702 22.8118 24.9086 24.4357 25.1061 26.194C25.1306 26.4151 25.2361 26.6192 25.4022 26.767C25.5683 26.9149 25.7833 26.9959 26.0056 26.9946H26.1046C26.3404 26.9674 26.5559 26.8482 26.7041 26.6629C26.8524 26.4776 26.9214 26.2411 26.8961 26.0051C26.7158 24.3827 26.0973 22.8399 25.1069 21.5421C24.1166 20.2443 22.7917 19.2406 21.2744 18.6384ZM17.9373 17.9998C16.8734 17.9998 15.8535 17.5893 15.0984 16.8574C14.3434 16.1256 13.9073 15.1307 13.9073 14.0966C13.9073 13.0626 14.3434 12.0677 15.0984 11.3358C15.8535 10.604 16.8734 10.1935 17.9373 10.1935C19.0012 10.1935 20.0211 10.604 20.7761 11.3358C21.5312 12.0677 21.9673 13.0626 21.9673 14.0966C21.9673 15.1307 21.5312 16.1256 20.7761 16.8574C20.0211 17.5893 19.0012 17.9998 17.9373 17.9998Z"
              fill="#fff"
          />
        </svg>
         <a href="">Book Service</a>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isContentVisible: false,
      icon: '+',
      activeTab: '#home',
      panes: [
        {
          id: 'home',
          services: [
            {
              imgSrc: './Nav-img/nav-one.png',
              altText: 'Service 1',
              title: 'Service 1',
              description: 'Service 1 description',
            },
            {
              imgSrc: './Nav-img/service2.svg',
              altText: 'Service 2',
              title: 'Service 2',
              description: 'Service 2 description',
            },
            // Add more services as needed
          ],
        },
        {
          id: 'profile',
          services: [
            {
              imgSrc: './Nav-img/service3.svg',
              altText: 'Service 3',
              title: 'Service 3',
              description: 'Service 3 description',
            },
            {
              imgSrc: './Nav-img/service4.svg',
              altText: 'Service 4',
              title: 'Service 4',
              description: 'Service 4 description',
            },
            // Add more services as needed
          ],
        },
      ],
    };
  },
  methods: {
    toggleContent() {
      this.isContentVisible = !this.isContentVisible;
      this.icon = this.isContentVisible ? '-' : '+';
    },
    hideContent() {
      this.isContentVisible = false;
      this.icon = '+';
    },
    activateTab(tabId) {
      this.activeTab = tabId;
    },
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
}


.navbar {
  padding: 0 80px;
  height: 100px;
  position: fixed !important;
  width: 100%;
  z-index: 999;
  background: rgba(255, 255, 255, 0.03);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  left: 0;
  top: 0px;
  transition: all 0.4s ease;
}

.container-fluid {
  width: fit-content;
}

.navbar-expand-lg .navbar-nav {
  gap: 30px;
}

.wave-text {
  display: inline-block;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  word-spacing: -5px;
  position: relative;
  color: white;

}

.wave-text:hover {
  color: rgb(255, 72, 0);
}

.for_nav_content {
  color: white;
  text-decoration: none;
  padding: 10px 0;
  word-spacing: -5px;
}

.for_nav_content:hover {
  color: #ff4800;
}

.for_nav_content span {
  display: inline-block;
  transition: transform 0.3s ease-in-out;

}

.for_nav_content:hover span {
  animation: navContent 0.3s ease-in-out;
  animation-fill-mode: forwards;
  animation-delay: calc(0.1s * var(--i));
}

@keyframes navContent {
  0% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-10px);
  }

  100% {
    transform: translateY(0);
  }
}


.wave-text span {
  display: inline-block;

  transition: transform 0.3s ease-in-out;
}

@keyframes wave {
  0% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-10px);
  }

  100% {
    transform: translateY(0);
  }
}

.nav-item:hover span {
  animation: wave 0.3s ease-in-out;
  animation-fill-mode: forwards;
  animation-delay: calc(0.1s * var(--i));

}

.icon {
  font-size: 23px;
  color: rgb(255, 72, 0);
  font-weight: 700;
  position: absolute;
  right: -7px;
  top: 3px;
  transition: all 0.3s ease-in-out;
}

li {
  cursor: pointer;
}

.nav_content {
  background: rgb(92 91 91 / 78%);
  padding: 20px;
  font-size: 18px;
  font-weight: 600;
  top: 99px;
  left: 30%;
  opacity: 0;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.5s ease, opacity 0.5s ease;
  border-top: 2px solid rgb(255, 81, 0);
}

.nav_content.show {
  opacity: 1;
  border-top: 2px solid rgb(255, 81, 0);

  max-height: 400px;
  /* Adjust this value based on your content's height */
}

.nav_content p {
  color: white;
}

.profile a {
  color: white;
  padding: 12px 50px;
  background: #ff4800;
  border-radius: 7px;
  font-size: 16px;
  font-style: normal;
  font-weight: 500;
  line-height: 160%;
  letter-spacing: 0.5px;
}

.profile {
  display: flex;
  align-items: center;
  gap: 28px;
}

.mid_line {
  width: 2px;
  height: auto;
  background: white;
  margin-right: 30px;
}

.item_name h4 {
  color: #ffffff;
  font-size: 16px;
  font-style: normal;
  font-weight: 600;
  line-height: normal;
  letter-spacing: 0.08px;
  text-transform: capitalize;
  margin-bottom: 6px;
}

.item_name p {
  width: max-content;
  color: #ffffff;

  font-size: 12px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  text-transform: capitalize;
}

.service_item {
  width: fit-content;
}

.car-bike {
  width: 150px;
}

.service_item_box {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
}
</style>