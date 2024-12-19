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
    <h2>4. Log in to the receiving Instagram account:</h2>
    <span
      >We strongly recommend using temporary passwords and changing them
      immediately after the transfer
    </span>
    <LoaderSpinner v-if="isLoading" />
    <div class="form" v-else>
      <div class="avatar" v-if="id">
        <img class="avatar-img2" alt="" />
        <span>{{ username }}</span>
      </div>
      <div class="infoLogin">
        <h2>New Account</h2>
        <div class="list-group">
          <div class="group">
            <label for="login2">Username</label>
            <input
              v-model="login"
              type="text"
              id="login2"
              placeholder="Enter the user name"
            />
          </div>
          <div class="group">
            <label for="password2">Password</label>
            <input
              v-model="password"
              id="password2"
              type="password"
              placeholder="Enter the password"
            />
          </div>
        </div>
      </div>
      <button @click="log" class="btn">Sign in</button>
    </div>
    <h2>5. View the copied accounts and bookmarks:</h2>
    <span
      >You can select and delete those that were copied by mistake. You can
      repeat the export, duplicates will be deleted
    </span>
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

.avatar-img2 {
  width: 48px;
  height: 48px;
  object-fit: cover;
  border-radius: 100%;
}
</style>
