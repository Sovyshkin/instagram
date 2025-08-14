<script>
import axios from "axios";
import LoaderSpinner from "./LoaderSpinner.vue";
export default {
  name: "RightLogin2",
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
    <LoaderSpinner v-if="isLoading" />
    <div class="form" v-else>
      <div class="avatar" v-if="id">
        <img class="avatar-img2" alt="" />
        <span>{{ username }}</span>
      </div>
      <div class="infoLogin">
        <h2>New Account</h2>
        <div class="list-group">
            <input
              v-model="login"
              type="text"
              id="login2"
              placeholder="Login"
            />
            <input
              v-model="password"
              id="password2"
              type="password"
              placeholder="Password"
            />
        </div>
      </div>
      <button @click="log" class="btn">Sign in</button>
    </div>
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
  align-items: center;
  justify-content: space-between;
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

input {
  width: 100%;
  padding: 12px 24px;
  border: 1px solid #848484;
  border-radius: 100px;
  font-family: "Manrope", sans-serif;
}

input::placeholder {
  color: #848484;
  font-family: "Manrope", sans-serif;
}

.btn {
  width: 100%;
  text-align: center;
  border-radius: 100px;
  padding: 16px 24px;
  background: linear-gradient(90deg, #951AE8 0%, #FD01BC 50%, #FFC000 100%);
  margin-bottom: 20px;
}

h2 {
  font-weight: 700;
  font-size: 24px;
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
@media (max-width: 600px) {
  .list-group {
    flex-direction: column;
  }
  .group {
    width: 100%;
  }
}
</style>
