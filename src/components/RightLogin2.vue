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
            localStorage.setItem("login2", this.id);
            this.load_info();
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
        this.id = localStorage.getItem("login2");
        if (this.id) {
          let response = await axios.get(`/account_info?login=${this.id}`);
          console.log(response);
          this.username = response.data.username;
          this.img = response.data.profile_pic_url;
          if (this.img) {
            let imgRef = document.querySelector(".avatar-img2");
            imgRef.src = `http://localhost:3000${this.img}`;
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
  <div class="wrap">
    <h2>1. Log in to the existing and new Instagram account:</h2>
    <i
      >We strongly advise to use temporary passwords and change them immediately
      after the transfer</i
    >
    <LoaderSpinner v-if="isLoading" />
    <div class="form" v-else>
      <div class="avatar">
        <img class="avatar-img2" alt="" />
        <span>{{ username }}</span>
      </div>
      <div class="infoLogin">
        <span>Old Account</span>
        <input v-model="login" type="text" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
      </div>
      <button @click="log" class="btn">Log in</button>
    </div>
    <h2>2. Select what you wish to be exported to the new account:</h2>
    <i
      >Browse through each following, followers and bookmarks, select all you
      wish to be transferred and hit TRANSFER above</i
    >
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

.avatar-img2 {
  width: 48px;
  height: 48px;
  object-fit: cover;
  border-radius: 100%;
}
</style>
