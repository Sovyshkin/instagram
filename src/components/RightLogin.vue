<script>
import axios from "axios";
export default {
  name: "RightLogin",
  data() {
    return {
      login: "",
      password: "",
      message: "",
    };
  },
  methods: {
    async log() {
      try {
        if (this.login && this.password) {
          let response = await axios.post(`/login`, {
            params: {
              login: this.login,
              password: this.password,
            },
          });
          this.message = response.data.message;
          if (this.message == "Успешно") {
            localStorage.setItem("login", true);
            this.$emit("updateLogin", false);
          }
          setTimeout(() => {
            this.message = "";
          }, 2500);
        }
      } catch (err) {
        console.log(err);
      }
    },
  },
  mounted() {},
};
</script>
<template>
  <div class="wrap">
    <h2>4. Log in to the receiving Instagram account:</h2>
    <i
      >We strongly advise to use temporary passwords and change them immediately
      after the transfer
    </i>
    <div class="form">
      <div class="avatar">
        <img src="" alt="" />
        <span>Sarah Eastern</span>
      </div>
      <div class="infoLogin">
        <span>New Account</span>
        <input v-model="login" type="text" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
      </div>
      <button class="btn">Log in</button>
    </div>
    <h2>5. Browse through the copied accounts and bookmarks:</h2>
    <i
      >You can select and delete those copied in error. You can redo the export,
      the duplicates will be omitted
    </i>
  </div>
</template>
<style scoped>
.wrap {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: start;
}

.form {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 15px;
}

.avatar {
  display: flex;
  flex-direction: column;
  gap: 6px;
  justify-content: center;
  align-items: center;
}

.infoLogin {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.infoLogin span {
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;
}

.infoLogin input {
  background-color: #fbfbfb;
  padding: 20px 5px 5px;
  min-width: 142px;
  min-height: 40px;
  font-weight: 600;
  font-size: 14px;
  line-height: 20px;
  color: #a7a5a5;
}

.btn {
  width: 95px;
  height: 73px;
  border-radius: 10px;
  background-color: #cbdeff;
}

h2 {
  font-weight: 700;
  font-size: 14px;
  line-height: 12px;
}
i {
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
}
</style>
