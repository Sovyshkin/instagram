<script>
import axios from "axios";
import LoaderSpinner from "./LoaderSpinner.vue";
export default {
  name: "AppLogin",
  components: { LoaderSpinner },
  data() {
    return {
      login: "",
      password: "",
      message: "",
      id: "",
      status: "",
      img: "",
      username: "",
      isLoading: false,
    };
  },
  methods: {
    async log() {
      try {
        if (this.login && this.password) {
          this.isLoading = true;
          let response = await axios.post(`/login`, {
            login: this.login,
            password: this.password,
          });
          console.log(response);
          this.id = response.data.id;
          this.status = response.status;
          if (this.id && this.status == 200) {
            this.message = "Успешно";
            localStorage.setItem("login1", this.id);
            this.load_info();
            this.$emit("updateInfo");
          } else {
            this.message = "Неправильно введен логин или пароль";
          }
          setTimeout(() => {
            this.message = "";
          }, 2500);
        }
      } catch (err) {
        console.log(err);
      } finally {
        this.isLoading = false;
      }
    },

    async load_info() {
      try {
        this.id = localStorage.getItem("login1");
        if (this.id) {
          let response = await axios.get(`/account_info?login=${this.id}`);
          console.log(response);
          this.username = response.data.username;
          this.img = response.data.profile_pic_url;
          if (this.img) {
            let imgRef = document.querySelector(".avatar-img");
            imgRef.src = `http://37.1.208.253:3000${this.img}`;
          }
        }
      } catch (err) {
        console.log(err);
      }
    },
  },
  mounted() {
    this.load_info();
  },
};
</script>
<template>
  <div class="wrap-login">
    <h2>1. Log in to your existing and new Instagram account:</h2>
    <span
      >We strongly advise to use temporary passwords and change them immediately
      after the transfer</span
    >
    <LoaderSpinner v-if="isLoading" />
    <div class="form" v-else>
      <div class="avatar" v-if="id">
        <img class="avatar-img" alt="" />
        <span>{{ username }}</span>
      </div>
      <div class="infoLogin">
        <h2>Old Account</h2>
        <div class="list-group">
          <div class="group">
            <label for="login">Login</label>
            <input
              v-model="login"
              id="login"
              type="text"
              placeholder="Enter the user name"
            />
          </div>
          <div class="group">
            <label for="password">Password</label>
            <input
              v-model="password"
              id="password"
              type="password"
              placeholder="Enter the password"
            />
          </div>
        </div>
      </div>
      <button @click="log" class="btn">Sign in</button>
    </div>
    <h2>2. Select what you want to export to your new account:</h2>
    <span
      >Browse through all subscriptions, subscribers, and bookmarks, select
      whatever you want to transfer, and click "TRANSFER" above</span
    >
  </div>
</template>
<style scoped>
.wrap-login {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: start;
}

.form {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.list-group {
  width: 100%;
  display: flex;
  gap: 10px;
}

.group {
  width: 50%;
  display: flex;
  flex-direction: column;
  gap: 12px;
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
  gap: 20px;
  padding: 20px 0;
}

.infoLogin span {
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;
}

label {
  font-weight: 600;
  opacity: 40%;
  font-size: 14px;
  line-height: 16px;
}

.infoLogin input {
  padding: 12px 16px;
  background-color: rgba(255, 255, 255, 0.1) !important;
  border-radius: 8px;
}

input::placeholder {
  font-weight: 400;
  font-size: 14px;
  line-height: 22px;
}

.btn {
  width: 100%;
  text-align: center;
  border-radius: 8px;
  padding: 16px 24px;
  background-color: #1960e1;
  margin-bottom: 20px;
}

h2 {
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
}
span {
  font-weight: 400;
  font-size: 14px;
  line-height: 19px;
  opacity: 80%;
}

.avatar-img {
  width: 48px;
  height: 48px;
  object-fit: cover;
  border-radius: 100%;
}
</style>
