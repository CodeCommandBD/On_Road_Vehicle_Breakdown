<template>
  <div class="serviceBook">
    <div class="modal-book">
      <div class="contact-info">
        <h2>Contract Information</h2>
        <div class="d-flex flex-column w-100 gap-4">
          <div class="d-flex w-100 gap-4">
            <div class="w-50">
              <input type="text" placeholder="Full Name">
            </div>
            <div class="w-50">
              <input type="number" placeholder="Phone Number">
            </div>
          </div>
          <div class="d-flex w-100 gap-4">
            <div class="w-50">
              <input type="email" placeholder="Email">
            </div>
            <div class="w-50">
              <input type="text" placeholder="Location">
            </div>
          </div>

        </div>

      </div>
      <div class="Vehicle-info">
        <h2>Vehicle Information</h2>
        <div class="d-flex flex-column gap-4">
          <div class="d-flex gap-4">
            <div class="w-50 car-bike">
              <h3>Vehicle</h3>
              <div class="d-flex gap-4">
                <div class="w-50 car">
                  <div class="form-check form-check-inline d-flex gap-5">
                    <input class="form-check-input" type="radio" name="inlineRadioOptions"
                           id="car1">
                    <label class="form-check-label" for="car1">
                      Car
                    </label>
                  </div>
                </div>
                <div class="w-50 car">
                  <div class="form-check form-check-inline d-flex gap-5">
                    <input class="form-check-input" type="radio" name="inlineRadioOptions"
                           id="Bike2" checked>
                    <label class="form-check-label" for="Bike2">
                      Bike
                    </label>
                  </div>
                </div>
              </div>

            </div>


            <div class="w-50 car-bike">
              <h3>Fuel</h3>
              <div class="d-flex gap-4">
                <div class="w-50 car">
                  <div class="form-check  d-flex gap-5">
                    <input class="form-check-input" type="radio" name="flexRadioDefault"
                           id="car2">
                    <label class="form-check-label" for="car2">
                      Petrol
                    </label>
                  </div>
                </div>
                <div class="w-50 car">
                  <div class="form-check d-flex gap-5">
                    <input class="form-check-input" type="radio" name="flexRadioDefault"
                           id="Bike3" checked>
                    <label class="form-check-label" for="Bike3">
                      Cng
                    </label>
                  </div>
                </div>
              </div>

            </div>
          </div>


          <div class="d-flex gap-4">
            <div class="car-bike brand w-50">
              <h3>Brand</h3>
              <input type="text" placeholder="Honda">
            </div>
            <div class="car-bike brand w-50">
              <h3>Model Number</h3>
              <input type="text" placeholder="KHA-096-63">
            </div>

          </div>
        </div>

      </div>
      <div class="Repair-Information">
        <h2>
          Repair Information
        </h2>
        <textarea class="textarea">Write  Repair Details...

            </textarea>
      </div>
<!--      <ul class="List d-flex flex-wrap gap-2 p-0 ">-->
<!--        <li>oil change</li>-->
<!--        <li>oil change</li>-->
<!--        <li>oil change</li>-->
<!--        <li>oil change</li>-->
<!--        <li>oil change</li>-->
<!--      </ul>-->
      <div class="condition d-flex gap-3">
        <input type="checkbox">
        <h4>You agree to the <span>Terms and Conditions.</span></h4>
      </div>
      <a href="" class="submit">Submit</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "ServiceModel"
}
</script>

<style scoped>
.serviceBook {
  background: linear-gradient(180deg, rgba(242, 60, 19, 0.80) 0%, rgba(242, 60, 19, 0.00) 100%), url('./service-book-modal-img/image 4.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  display: flex;
  justify-content: center;
  padding: 80px;
}

.modal-book {
  border-radius: 16px;
  border: 1px solid #E7EAF3;
  background: #FFF;
  padding: 60px;
  box-shadow: 0px 6px 12px 0px rgba(201, 203, 208, 0.25);
  width: 100%;
  height: fit-content;
}

.contact-info, .Vehicle-info {
  margin-bottom: 60px;
}

.contact-info h2, .Vehicle-info h2, .Repair-Information h2 {
  color: #1E1E1E;
  font-size: 28px;
  font-style: normal;
  font-weight: 500;
  line-height: 28px; /* 100% */
  letter-spacing: 0.84px;
  margin-bottom: 36px;
}

.contact-info input, .brand input {
  border-radius: 4px;
  border: 1px solid rgba(19, 33, 68, 0.10);
  background: #FFF;
  box-shadow: 0px 0px 12px 0px rgba(204, 204, 204, 0.20);
  padding: 14px 36px;
  color: #4A4A4A;
  font-size: 16px;
  font-style: normal;
  font-weight: 400;
  line-height: 16px; /* 100% */
  letter-spacing: 0.48px;
  width: 100%;
}

.car {
  border-radius: 4px;
  border: 1px solid rgba(19, 33, 68, 0.10);
  background: #FFF;
  box-shadow: 0px 0px 12px 0px rgba(204, 204, 204, 0.20);
  padding: 14px 36px;
}

.car-bike h3 {
  color: #1E1E1E;
  font-size: 18px;
  font-style: normal;
  font-weight: 400;
  line-height: 18px; /* 100% */
  letter-spacing: 0.54px;
  margin-bottom: 12px;
}

.textarea {
  width: 100%;
  border-radius: 4px;
  border: 1px solid rgba(19, 33, 68, 0.10);
  background: #FFF;
  height: 200px;
  box-shadow: 0px 0px 12px 0px rgba(204, 204, 204, 0.20);
  resize: none;
  padding: 30px 36px;
  color: #4A4A4A;
  font-size: 16px;
  font-style: normal;
  font-weight: 400;
  line-height: 16px; /* 100% */
  letter-spacing: 0.48px;
  outline: none;

}

.List {
  margin: 40px 0;
}

.List li {
  list-style: none;
  border-radius: 4px;
  background: #FFF4F1;
  padding: 10px;
  color: #F23C13;
  text-align: center;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 14px; /* 100% */
}

.condition {
  margin-bottom: 40px;
}

.condition h4 {
  color: #4A4A4A;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 14px; /* 100% */
  letter-spacing: 0.5px;
  margin-bottom: 0px;
}

.condition span {
  color: #F23C13;
  font-weight: 500;
  letter-spacing: 0.3px;
}

.submit {
  text-decoration: none;
  padding: 18px;
  text-align: center;
  display: block;
  color: #FFF;
  font-size: 18px;
  font-style: normal;
  font-weight: 600;
  line-height: 18px; /* 100% */
  letter-spacing: 0.54px;
  border-radius: 8px;
  border: 1px solid rgba(19, 33, 68, 0.10);
  background: #F23C13;
  box-shadow: 0px 0px 12px 0px rgba(204, 204, 204, 0.20);

}

</style>