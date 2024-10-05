<template>
  <div class="login-bg">
    <div class="login-bg-img">
      <img src="./sign-up-img/image.png" alt="" />
      <div class="login">
        <h1 class="login-title">SIGN UP</h1>
        <form @submit.prevent="submitForm">
          <div class="login-address">
            <input type="text" v-model="form.name" placeholder="Name" />
          </div>
          <div class="login-address">
            <input type="text" v-model="form.address" placeholder="Address" />
          </div>
          <div class="login-address">
            <input type="text" v-model="form.email" placeholder="Email" />
          </div>
          <div class="login-address">
            <input type="text" v-model="form.phone" placeholder="Phone" />
          </div>
          <div class="row gap-3 mx-auto">
            <div class="col-5 login-address">
              <label class="container d-flex gap-2 p-0">
                <input
                  class="w-25"
                  type="radio"
                  v-model="form.radio"
                  value="cars"
                />
                <span class="checkmark"></span>
                CARS
              </label>
            </div>
            <div class="col-5 login-address">
              <label class="container d-flex gap-2 p-0">
                <input
                  class="w-25"
                  type="radio"
                  v-model="form.radio"
                  value="bikes"
                />
                <span class="checkmark"></span>
                BIKES
              </label>
            </div>
            <div class="col-5 login-address px-4">
              <input
                type="text"
                v-model="form.carsModel"
                placeholder="Cars Model Number"
                :disabled="form.radio !== 'cars'"
                class="model-input"
              />
            </div>
            <div class="col-5 login-address px-4">
              <input
                type="text"
                v-model="form.bikesModel"
                placeholder="Bikes Model Number"
                :disabled="form.radio !== 'bikes'"
                class="model-input"
              />
            </div>
          </div>
          <div class="login-pass">
            <input
              type="password"
              v-model="form.password"
              placeholder="Password"
            />
          </div>
          <div class="remember-forget">
            <label class="remember">
              <input type="checkbox" v-model="form.agreed" />
              <span class="checkbox-container"></span>
              By SignUp you agree to the <span>Terms and Conditions.</span>
            </label>
          </div>
          <button class="login-btn" type="submit">Sign UP</button>
          <div class="any-account">
            <h1>
              Already have an account?
              <a href="/login">Log In!</a>
            </h1>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUp',
  data() {
    return {
      form: {
        name: '',
        address: '',
        email: '',
        phone: '',
        radio: 'cars',
        carsModel: '',
        bikesModel: '',
        password: '',
        agreed: false,
      },
    };
  },
  methods: {
    submitForm() {
      if (!this.form.agreed) {
        alert("You must agree to the terms and conditions.");
        return;
      }
      console.log(this.form);
      // Add your form submission logic here
    },
    goToLogin() {
      // Logic for navigation to login page
      alert("Navigating to Login page...");
    },
  },
};
</script>

<style scoped>
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

.login-address input,
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

.col-5 {
  flex: 0 0 auto;
  width: 48%;
}
</style>