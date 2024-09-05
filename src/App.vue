<script>
import LeftScreen from "./components/LeftScreen.vue";
import RightScreen from "./components/RightScreen2.vue";
export default {
  name: "App",
  components: {
    LeftScreen,
    RightScreen,
  },
  data() {
    return {
      login: true,
      main: false,
    };
  },
  methods: {},
  mounted() {},
};
</script>
<template>
  <div class="wrap">
    <LeftScreen />
    <img class="transfer-img" src="./assets/transfer.png" alt="" />
    <RightScreen />
  </div>
</template>
<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Manrope:wght@200..800&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap");
#app {
  font-family: "Montserrat", sans-serif;
  width: 100%;
}
* {
  padding: 0px;
  margin: 0px;
  border: none;
  font-weight: 400;
  font-style: normal;
  font-family: "Montserrat", sans-serif;
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

.wrap {
  display: flex;
  justify-content: space-evenly;
  padding: 40px;
  width: 100%;
}

body,
#app {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

/* Links */

a,
a:link,
a:visited {
  text-decoration: none;
}

a:hover {
  text-decoration: none;
}

/* Common */

aside,
nav,
footer,
header,
section,
main {
  display: block;
}

ul,
ul li {
  list-style: none;
}

img {
  vertical-align: top;
}

img,
svg {
  max-width: 100%;
  height: auto;
}

address {
  font-style: normal;
}

/* Form */

input,
textarea,
button,
select {
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  background-color: transparent;
}

input::-ms-clear {
  display: none;
}

button,
input[type="submit"] {
  display: inline-block;
  box-shadow: none;
  background-color: transparent;
  background: none;
  cursor: pointer;
}

input:focus,
input:active,
button:focus,
button:active {
  outline: none;
  box-shadow: none;
}

button::-moz-focus-inner {
  padding: 0;
  border: 0;
}

.card {
  transition: all 500ms ease;
  cursor: pointer;
}

.wrap {
  max-width: 1440px;
  margin: 0 auto;
}

.transfer-img {
  width: 90px;
  height: 60px;
  margin-top: 400px;
}

.msg {
  padding: 10px 13px;
  font-size: 16px;
  line-height: 16px;
  color: #fff;
  border-radius: 15px;
  width: fit-content;
  margin: 0 auto;
}

.success {
  background-color: #45ed0b;
}

.error {
  background-color: #cf0032;
}

@media (max-width: 1050px) {
  .wrap {
    flex-direction: column;
    align-items: center;
    gap: 50px;
  }

  .wrapper {
    width: 100% !important;
  }

  .transfer-img {
    margin-top: 0px;
    transform: rotate(90deg);
  }

  .wrap_btns {
    flex-wrap: wrap;
  }

  .transfer,
  .delete {
    margin-left: 0px !important;
  }
}
</style>
