<template>
  <div class="login-bg">
    <div class="login-bg-img">
      <div class="bg-img bg-img-one active">
        <img src="./login-img/login.png" alt="Login Background"/>
      </div>
      <div class="bg-img bg-img-two">
        <img src="./login-img/user-bg.png" alt="User Background"/>
      </div>

      <div class="login">
        <h1 class="login-title">
          WELCOME TO<br/><span>QUICK</span> SERVICE
        </h1>

        <div class="user_garage d-flex align-items-center">
          <ul class="d-flex gap-5 align-items-start nav nav-fill nav-justified nav-tabspb-3" id="myTab" role="tablist">
            <li class="nav-item" role="presentation">
              <button
                  class="nav-link nav-one btn-one active date-btn previous-date-border p-0"
                  id="home-tab"
                  data-bs-toggle="tab"
                  data-bs-target="#home"
                  type="button"
                  role="tab"
                  aria-controls="home"
                  aria-selected="true"
                  @click="setActiveTab('home')"
              >
                <div class="user" id="user">
                  <svg xmlns="http://www.w3.org/2000/svg" width="31" height="30" viewBox="0 0 31 30" fill="none">
                    <path
                        d="M16.3347 0C14.1926 0 12.1382 0.790311 10.6235 2.19707C9.10877 3.60384 8.25781 5.51181 8.25781 7.50128C8.25781 9.49074 9.10877 11.3987 10.6235 12.8055C12.1382 14.2122 14.1926 15.0026 16.3347 15.0026C18.4769 15.0026 20.5313 14.2122 22.046 12.8055C23.5607 11.3987 24.4117 9.49074 24.4117 7.50128C24.4117 5.51181 23.5607 3.60384 22.046 2.19707C20.5313 0.790311 18.4769 0 16.3347 0Z"
                        fill="#E5EBED"
                    />
                    <path
                        d="M29.3649 20.1612C25.1629 18.0874 20.4772 17.0029 15.7187 17.0029C10.9603 17.0029 6.27458 18.0874 2.0726 20.1612C1.23875 20.5727 0.71875 21.3771 0.71875 22.253V27.4996C0.71875 28.8798 1.9249 30 3.41106 30H28.0264C28.7405 30 29.4253 29.7366 29.9302 29.2677C30.4351 28.7988 30.7187 28.1628 30.7187 27.4996V22.253C30.7187 21.3771 30.1988 20.5727 29.3649 20.1612Z"
                        fill="#F23C13"
                    />
                  </svg>
                  <div class="user_text garage_text">
                    <h2 class="user-color">USER</h2>
                  </div>
                </div>
              </button>
            </li>

            <li class="nav-item" role="presentation">
              <button
                  class="nav-link nav-two btn-two date-btn p-0"
                  id="profile-tab"
                  data-bs-toggle="tab"
                  data-bs-target="#profile"
                  type="button"
                  role="tab"
                  aria-controls="profile"
                  aria-selected="false"
                  @click="setActiveTab('profile')"
              >
                <div class="user active" id="garage">
                  <svg xmlns="http://www.w3.org/2000/svg" width="67" height="30" viewBox="2 24 65 2" fill="none">
                    <path
                        d="M49.5576 37H16.8799C14.9687 37 13.4141 36.0188 13.4141 34.8125V17.3125C13.4141 17.0639 13.5706 16.8254 13.8491 16.6496C14.1277 16.4738 14.5055 16.375 14.8994 16.375H51.5381C51.932 16.375 52.3098 16.4738 52.5884 16.6496C52.8669 16.8254 53.0234 17.0639 53.0234 17.3125V34.8125C53.0234 36.0188 51.4688 37 49.5576 37Z"
                        fill="#E5EBED"
                    />
                    <path
                        d="M44.7715 37H21.666V22C21.666 21.6685 21.8399 21.3505 22.1494 21.1161C22.4589 20.8817 22.8787 20.75 23.3164 20.75H43.1211C43.5588 20.75 43.9786 20.8817 44.2881 21.1161C44.5976 21.3505 44.7715 21.6685 44.7715 22V37Z"
                        fill="#CB2500"
                    />
                  </svg>
                  <div class="user_text">
                    <h2 class="user-color">GARAGE</h2>
                  </div>
                </div>
              </button>
            </li>
          </ul>
        </div>

        <div class="tab-content w-100">
          <div class="tab-pane active" id="home" role="tabpanel" aria-labelledby="home-tab" v-if="activeTab === 'home'">
            <form action="">
              <div class="login-address">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="26" viewBox="0 0 25 26"
                     fill="none">
                  <path
                      d="M12.5007 10.9167C14.8018 10.9167 16.6673 9.0512 16.6673 6.75001C16.6673 4.44882 14.8018 2.58334 12.5007 2.58334C10.1995 2.58334 8.33398 4.44882 8.33398 6.75001C8.33398 9.0512 10.1995 10.9167 12.5007 10.9167Z"
                      fill="#f94f00"/>
                  <path
                      d="M20.8337 18.7292C20.8337 21.3177 20.8337 23.4167 12.5003 23.4167C4.16699 23.4167 4.16699 21.3177 4.16699 18.7292C4.16699 16.1406 7.89824 14.0417 12.5003 14.0417C17.1024 14.0417 20.8337 16.1406 20.8337 18.7292Z"
                      fill="#f94f00"/>
                </svg>
                <input type="text" name="" id="" placeholder="User Email Address">
              </div>
              <div class="login-pass">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="26" viewBox="0 0 25 26"
                     fill="none">
                  <path
                      d="M12.4838 2.58333C15.6804 2.58333 18.2525 5.09873 18.2525 8.20417V9.8014C20.0466 10.3614 21.3538 11.9856 21.3538 13.9254V19.068C21.3538 21.4696 19.3628 23.4167 16.9082 23.4167H8.09217C5.6365 23.4167 3.64551 21.4696 3.64551 19.068V13.9254C3.64551 11.9856 4.95379 10.3614 6.74685 9.8014V8.20417C6.75743 5.09873 9.32953 2.58333 12.4838 2.58333ZM12.4944 14.442C11.9863 14.442 11.5735 14.8457 11.5735 15.3425V17.6406C11.5735 18.1478 11.9863 18.5515 12.4944 18.5515C13.013 18.5515 13.4258 18.1478 13.4258 17.6406V15.3425C13.4258 14.8457 13.013 14.442 12.4944 14.442ZM12.505 4.39483C10.3563 4.39483 8.60977 6.09247 8.59918 8.18346V9.57677H16.4002V8.20417C16.4002 6.10282 14.6537 4.39483 12.505 4.39483Z"
                      fill="#f94f00"/>
                </svg>
                <input type="password" placeholder="Password">
              </div>
              <div class="remember-forget">
                <label class="remember">
                  <input type="checkbox">
                  <span class="checkbox-container"></span>
                  Remember me
                </label>
                <h2>Forget Password?</h2>
              </div>

              <input class="login-btn" type="submit" value="Login">


              <div class="any-account">
                <h1>Don't have an account?<span> Sign up!</span></h1>
              </div>
            </form>
          </div>
          <div class="tab-pane" id="profile" role="tabpanel" aria-labelledby="profile-tab"
               v-if="activeTab === 'profile'">
            <form action="">
              <div class="login-address">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="26" viewBox="0 0 25 26"
                     fill="none">
                  <path
                      d="M12.5007 10.9167C14.8018 10.9167 16.6673 9.0512 16.6673 6.75001C16.6673 4.44882 14.8018 2.58334 12.5007 2.58334C10.1995 2.58334 8.33398 4.44882 8.33398 6.75001C8.33398 9.0512 10.1995 10.9167 12.5007 10.9167Z"
                      fill="#f94f00"/>
                  <path
                      d="M20.8337 18.7292C20.8337 21.3177 20.8337 23.4167 12.5003 23.4167C4.16699 23.4167 4.16699 21.3177 4.16699 18.7292C4.16699 16.1406 7.89824 14.0417 12.5003 14.0417C17.1024 14.0417 20.8337 16.1406 20.8337 18.7292Z"
                      fill="#f94f00"/>
                </svg>
                <input type="text" name="" id="" placeholder="Garage Email Address">
              </div>
              <div class="login-pass">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="26" viewBox="0 0 25 26"
                     fill="none">
                  <path
                      d="M12.4838 2.58333C15.6804 2.58333 18.2525 5.09873 18.2525 8.20417V9.8014C20.0466 10.3614 21.3538 11.9856 21.3538 13.9254V19.068C21.3538 21.4696 19.3628 23.4167 16.9082 23.4167H8.09217C5.6365 23.4167 3.64551 21.4696 3.64551 19.068V13.9254C3.64551 11.9856 4.95379 10.3614 6.74685 9.8014V8.20417C6.75743 5.09873 9.32953 2.58333 12.4838 2.58333ZM12.4944 14.442C11.9863 14.442 11.5735 14.8457 11.5735 15.3425V17.6406C11.5735 18.1478 11.9863 18.5515 12.4944 18.5515C13.013 18.5515 13.4258 18.1478 13.4258 17.6406V15.3425C13.4258 14.8457 13.013 14.442 12.4944 14.442ZM12.505 4.39483C10.3563 4.39483 8.60977 6.09247 8.59918 8.18346V9.57677H16.4002V8.20417C16.4002 6.10282 14.6537 4.39483 12.505 4.39483Z"
                      fill="#f94f00"/>
                </svg>
                <input type="password" placeholder="Password">
              </div>
              <div class="remember-forget">
                <label class="remember">
                  <input type="checkbox">
                  <span class="checkbox-container"></span>
                  Remember me
                </label>

                <h2>Forget Password?</h2>
              </div>

              <input class="login-btn" type="submit" value="Login">


              <div class="any-account">
                <h1>Don't have an account?<span> Sign up!</span></h1>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserLogin',
  data() {
    return {
      activeTab: 'home', // Default active tab
    };
  },
  methods: {
    setActiveTab(tab) {
      this.activeTab = tab;
    },
  },
};
</script>

<style scoped>
.login-bg {
  height: 100vh;
}

.login-bg-img {
  width: 100%;
  height: 100%;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;

}

.login-bg-img img {
  width: 100%;
  height: 100%;

}

.login {
  width: 500px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  position: absolute;
  transform: translate(0%, 0%);
  background: white;
  border-radius: 10px;
  padding: 40px;
}

form {
  width: 100%;

}

.login-title {
  color: #1E1E1E;
  font-size: 36px;
  font-style: normal;
  font-weight: 700;
  line-height: 48px;
  /* 133.333% */
  letter-spacing: 1.8px;
  text-transform: capitalize;
  margin-bottom: 48px;
}

.login-title span {
  color: #f94f00;
}

.login-address {
  display: flex;
  align-items: center;
  gap: 36px;
  padding: 10px 36px;
  border: 1px solid rgba(19, 33, 68, 0.10);
  background: #FFF;
  box-shadow: 0px 0px 12px 0px rgba(204, 204, 204, 0.20);
  margin-bottom: 36px;
}

.login-pass {
  display: flex;
  align-items: center;
  gap: 36px;
  padding: 10px 36px;
  border: 1px solid rgba(19, 33, 68, 0.10);
  background: #FFF;
  box-shadow: 0px 0px 12px 0px rgba(204, 204, 204, 0.20);
  margin-bottom: 36px;
}

.login-address input {
  border: none;
  outline: none;
  color: #4A4A4A;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 14px;
  /* 100% */
  letter-spacing: 0.42px;
  background: transparent;
  padding: 10px 0;
  width: 100%;
}

.login-pass input {
  border: none;
  outline: none;
  color: #4A4A4A;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 14px;
  /* 100% */
  letter-spacing: 0.42px;
  background: transparent;
  padding: 10px 0;
  width: 100%;
}

.remember-forget {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
}


.remember {
  color: #4A4A4A;
  font-size: 14px;
  font-style: normal;
  font-weight: 500;
  line-height: 12px;
  padding-left: 10px;
  letter-spacing: 0.3px;
  margin: 0;
  display: block;
  position: relative;
  cursor: pointer;
}

.remember-forget h2 {
  color: #4A4A4A;
  font-size: 12px;
  font-style: normal;
  font-weight: 500;
  line-height: 12px;
  /* 100% */
  margin: 0;
}

.login-btn {
  width: 100%;
  border: 1px solid rgba(19, 33, 68, 0.10);
  background: #f94f00;
  box-shadow: 0px 0px 12px 0px rgba(204, 204, 204, 0.20);
  padding: 14px;
  margin-bottom: 40px;
  color: #FFF;
  text-decoration: none;
  font-size: 18px;
  font-style: normal;
  font-weight: 700;
  line-height: 18px;
  /* 100% */
  letter-spacing: 0.54px;

}

.any-account {
  margin-bottom: 60px;
}

.any-account h1 {
  color: #494949;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 14px;
  /* 100% */
  margin-bottom: 0;
}

.any-account h1 span {
  color: #FF6B00;
}

body {
  margin: 0 !important;
  box-sizing: border-box;
  padding: 0;
}

.user_garage {
  gap: 48px;
  margin-bottom: 48px;
}

.user {
  width: 186px;
  display: flex;
  justify-content: center;
  gap: 10px;
  align-items: center;
  border-radius: 4px;
  border: 1px solid #E7EAF3;
  padding: 10px 20px;
}

.user_text h2 {
  color: #1E1E1E;
  text-align: center;
  font-size: 20px;
  font-style: normal;
  font-weight: 700;
  line-height: 20px;
  /* 100% */
  font-variant: all-small-caps;
  letter-spacing: 0.1px;
  margin-bottom: 0;
}

.garage_text {
  margin-left: 10px;
  margin-top: 6px;
}

.btn-one.active,
.btn-two.active {
  background: #f94f00;
}

.btn-one.active .user > svg path {
  fill: white;
}

.btn-one.active .user-color,
.btn-two.active .user-color {
  color: white;
}

.login-address:focus-within,
.login-pass:focus-within {
  border-left: 2px solid red;
}

.login-bg {
  height: 100vh;
  position: relative;
}

.bg-img {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.bg-img.active {
  opacity: 1;
}


.remember input[type=checkbox] {
  visibility: hidden;
}

.checkbox-container {
  position: absolute;
  top: 0;
  left: 0;
  height: 15px;
  width: 15px;
  background-color: transparent;
  border: 1px solid #000;
  border-radius: 3px;
}


.remember input:checked ~ .checkbox-container {
  background-color: #f94f00;
}

/* Checkmark */
.checkbox-container::after {
  content: "";
  position: absolute;
  display: none;
  left: 5px;
  top: 0px;
  width: 4px;
  height: 10px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.remember input:checked ~ .checkbox-container::after {
  display: block;
}
</style>