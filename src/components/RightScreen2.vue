<script>
import RightLogin from "./RightLogin2.vue";
import axios from "axios";
import LoaderSpinner from "./LoaderSpinner.vue";

export default {
  name: "RightScreen",
  components: { RightLogin, LoaderSpinner },
  data() {
    return {
      login: "",
      password: "",
      message: "",
      account1: true,
      active: 3,
      followings: [],
      bookmarks: [],
      bookmark: false,
      following: false,
      countFollowing: 0,
      followingBetweenStart: 0,
      followingBetweenEnd: 50,
      followersBetweenStart: 0,
      followersBetweenEnd: 50,
      bookmarksBetweenStart: 0,
      bookmarksBetweenEnd: 50,
      followers: [],
      countFollowers: 0,
      countBookmarks: 0,
      isLoading: false,
      selectedFollowing: [],
      selectedBookmarks: [],
    };
  },
  methods: {
    select_all(s, type) {
      if (s == "following") {
        this.following = !this.following;
        if (type) {
          this.countFollowing = this.followings.length;
        } else {
          this.countFollowing = 0;
          this.selectedFollowing = [];
        }
        for (let i = 0; i < this.followings.length; i++) {
          this.followings[i].active = type;
          if (type) {
            this.selectedFollowing.push(this.followings[i].pk);
          }
        }
      } else if (s == "bookmarks") {
        this.bookmark = !this.bookmark;
        if (type) {
          this.countBookmarks = this.followings.length;
        } else {
          this.countBookmarks = 0;
          this.selectBookmarks = [];
        }
        for (let i = 0; i < this.bookmarks.length; i++) {
          this.bookmarks[i].active = type;
          if (type) {
            this.selectedBookmarks.push(this.bookmarks[i].pk);
          }
        }
      }
      // if (this.subscriptions) {
      //   this.subscriptions.forEach((item) => (item.active = !item.active));
      // }
    },

    countSelect(type, pk) {
      if (type == "following") {
        for (let i = 0; i < this.followings.length; i++) {
          if (this.followings[i].pk == pk) {
            if (this.followings[i].active) {
              this.countFollowing -= 1;
              let index = this.selectedFollowing.indexOf(this.followings[i].pk);
              if (index !== -1) {
                this.selectedFollowing.splice(index, 1);
              }
            } else {
              this.countFollowing++;
              this.selectedFollowing.push(this.followings[i].pk);
            }
            this.followings[i].active = !this.followings[i].active;
          }
        }
      }
    },
    async load_info() {
      try {
        this.isLoading = true;
        this.id = localStorage.getItem("login2");
        if (this.active == 1 && this.id) {
          let response = await axios.get(`/get_followings?login=${this.id}`);
          console.log(response);
          let data = response.data;
          if (data) {
            this.followings = Object.values(data);
            if (this.followings) {
              for (let i = 0; i < this.followings.length; i++) {
                this.followings[i].active = false;
              }
            }
            setTimeout(() => {
              let images = document.querySelectorAll(`.item_avatar_foll`);
              console.log("images", images);
              for (let i = 0; i < this.followings.length; i++) {
                images[
                  i
                ].src = `http://37.1.208.253:3000${this.followings[i].profile_pic_url}`;
                console.log(images[i]);
              }
            }, 3000);
          }
        } else if (this.active == 3 && this.id) {
          this.countBookmarks = 0;
          let response = await axios.get(`/get_collections?login=${this.id}`);
          console.log(response);
          let data = response.data;
          if (data) {
            this.bookmarks = data;
            if (this.bookmarks) {
              let posts_for_img = [];
              for (let i = 0; i < this.bookmarks.length; i++) {
                this.bookmarks[i].open = false;
                this.bookmarks[i].active = false;
                if (this.bookmarks[i].medias) {
                  for (let j = 0; j < this.bookmarks[i].medias.length; j++) {
                    this.bookmarks[i].medias[j].active = false;
                    this.countBookmarks++;
                    posts_for_img.push(
                      this.bookmarks[i].medias[j].thumbnail_url
                    );
                  }
                }
              }
              setTimeout(() => {
                let images = document.querySelectorAll(`.post-img2`);
                console.log("images", images);
                for (let i = 0; i < posts_for_img.length; i++) {
                  images[i].src = `http://37.1.208.253:3000${posts_for_img[i]}`;
                }
              }, 3000);
            }
          }
        }
      } catch (err) {
        console.log(err);
      } finally {
        this.isLoading = false;
      }
    },

    selectBookmark(id) {
      for (let i = 0; i < this.bookmarks.length; i++) {
        let item = this.bookmarks[i];
        if (item.id == id) {
          if (item.medias) {
            if (item.active) {
              item.medias.forEach((post) => (post.active = false));
              item.active = false;
              this.selectedBookmarks = [];
            } else {
              item.medias.forEach((post) => {
                post.active = true;
                this.selectedBookmarks.push(post.pk);
              });
              item.active = true;
            }
          }
          this.bookmarks[i] = item;
        }
      }
    },

    checkActive(id) {
      for (let i = 0; i < this.bookmarks.length; i++) {
        let bookmark = this.bookmarks[i];
        if (bookmark.id == id) {
          let active = bookmark.medias.find((post) => post.active);
          if (active) {
            bookmark.active = true;
          } else {
            bookmark.active = false;
          }
        }
        this.bookmarks[i] = bookmark;
      }
    },

    postActive(id, pk) {
      for (let i = 0; i < this.bookmarks.length; i++) {
        let item = this.bookmarks[i];
        if (item.id == id) {
          if (item.medias) {
            for (let j = 0; j < item.medias.length; j++) {
              let post = item.medias[j];
              if (post.pk == pk) {
                if (post.active) {
                  let index = this.selectedBookmarks.indexOf(post.id);
                  console.log(index);
                  if (index !== -1) {
                    this.selectedBookmarks.splice(index, 1);
                  }
                } else {
                  this.selectedBookmarks.push(String(post.id));
                }
                post.active = !post.active;
              }
            }
          }
          this.bookmarks[i] = item;
          this.checkActive(id);
        }
      }
    },

    next(type) {
      if (type == "following") {
        this.followingBetweenEnd += 50;
        this.followingBetweenStart += 50;
        if (this.followingBetweenEnd > this.followings.length) {
          this.followingBetweenEnd = this.followings.length;
          this.followingBetweenStart =
            50 * Math.floor(this.followingBetweenEnd / 50);
        }
      } else if (type == "followers") {
        this.followersBetweenEnd += 50;
        this.followersBetweenStart += 50;
        if (this.followersBetweenEnd > this.followers.length) {
          this.followersBetweenEnd = this.followers.length;
          this.followersBetweenStart =
            50 * Math.floor(this.followersBetweenEnd / 50);
        }
      }
    },

    back(type) {
      if (type == "following") {
        this.followingBetweenEnd -= 50;
        this.followingBetweenStart -= 50;
        if (this.followingBetweenStart <= 0) {
          this.followingBetweenStart = 0;
          this.followingBetweenEnd = 50;
        }
      } else if (type == "followers") {
        this.followersBetweenEnd -= 50;
        this.followersBetweenStart -= 50;
        if (this.followersBetweenStart <= 0) {
          this.followersBetweenStart = 0;
          this.followersBetweenEnd = 50;
        }
      }
    },

    truncateText(text) {
      if (text.length > 60) {
        text = text.slice(0, 60);
        text += "...";
      }
      return text;
    },

    loadActive(n) {
      this.active = n;
      this.load_info();
    },

    async transfer() {
      try {
        if (this.active == 1) {
          let lst = this.selectedFollowing;
          let response = await axios.post(
            `/add_followings?login=${localStorage.getItem("login1")}`,
            lst,
            {
              "Content-Type": "application/json",
            }
          );
          console.log(response);
          let status = response.status;
          if (status == 200) {
            this.message = "Success";
            setTimeout(() => {
              this.message = "";
            }, 3000);
          } else {
            this.message = "Error";
          }
        } else if (this.active == 3) {
          let lst = this.selectedBookmarks;
          let response = await axios.post(
            `/add_medias_to_collection?login=${localStorage.getItem("login1")}`,
            lst,
            {
              "Content-Type": "application/json",
            }
          );
          console.log(response);
          let status = response.status;
          if (status == 200) {
            this.message = "Success";
            setTimeout(() => {
              this.message = "";
            }, 3000);
          } else {
            this.message = "Error";
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
  <LoaderSpinner v-if="isLoading" />
  <div class="wrapper" v-else>
    <RightLogin />
    <div class="warn" v-if="active == 3">
      All posts from all collections will be moved to favorites
    </div>
    <div class="info" v-if="account1">
      <div class="wrap_btns">
        <button
          class="btn"
          :class="{ active: active == 1 }"
          @click="loadActive(1)"
        >
          <span>Following</span>
          <span>({{ countFollowing }} of {{ this.followings.length }})</span>
        </button>
        <button
          class="btn"
          :class="{ active: active == 2 }"
          @click="loadActive(2)"
        >
          <span>Followers</span>
          <span>({{ countFollowers }} of {{ this.followers.length }})</span>
        </button>
        <button
          class="btn"
          :class="{ active: active == 3 }"
          @click="loadActive(3)"
        >
          <span>Bookmarks</span>
          <span>({{ selectedBookmarks.length }} of {{ countBookmarks }})</span>
        </button>
        <button v-if="!message" class="btn transfer" @click="transfer">
          3. TRANSFER
        </button>
        <div
          class="msg"
          :class="{
            success: this.message == 'Успешно',
            error: this.message != 'Успешно',
          }"
          v-if="message"
        >
          {{ message }}
        </div>
      </div>
      <div class="following" v-if="active == 1">
        <div class="item_header">
          <div class="item_group">
            <img
              class="checkbox"
              @click="select_all('following', false)"
              src="../assets/select.png"
              alt=""
              v-if="following"
            />
            <img
              class="checkbox"
              @click="select_all('following', true)"
              src="../assets/not_selected.png"
              alt=""
              v-if="!following"
            />
            <span class="title">Following</span>
          </div>
          <span class="title">User</span>
        </div>
        <div class="items">
          <div
            class="item"
            @click="countSelect('following', item.pk)"
            v-for="item in followings.slice(
              followingBetweenStart,
              followingBetweenEnd + 1
            )"
            :key="item.pk"
            :class="{ item_active: item.active }"
          >
            <div class="item_group">
              <img
                class="checkbox"
                src="../assets/select.png"
                alt=""
                v-if="item.active"
              />
              <img
                class="checkbox"
                src="../assets/not_selected.png"
                alt=""
                v-if="!item.active"
              />
              <span class="name">{{ item.full_name }}</span>
            </div>
            <img class="item_avatar_foll" alt="" />
          </div>
        </div>
        <div class="footer">
          <div class="count">{{ countFollowing }} copied</div>
          <div class="countBetween">
            {{ followingBetweenStart }} - {{ followingBetweenEnd }} ({{
              this.followings.length
            }})
          </div>
          <div class="group-img">
            <img
              @click="back()"
              class="next back"
              src="../assets/next.png"
              alt=""
            />
            <img @click="next()" class="next" src="../assets/next.png" alt="" />
          </div>
        </div>
      </div>
      <div class="following" v-if="active == 2">
        <div class="item_header">
          <div class="item_group">
            <img
              class="checkbox"
              @click="select_all('following', false)"
              src="../assets/select.png"
              alt=""
              v-if="following"
            />
            <img
              class="checkbox"
              @click="select_all('following', true)"
              src="../assets/not_selected.png"
              alt=""
              v-if="!following"
            />
            <span class="title">Followers</span>
          </div>
          <span class="title">User</span>
        </div>
        <div class="items">
          <div
            class="item"
            @click="countSelect('following', item.id)"
            v-for="item in followers.slice(
              followersBetweenStart,
              followersBetweenEnd + 1
            )"
            :key="item.id"
            :class="{ item_active: item.active }"
          >
            <div class="item_group">
              <img
                class="checkbox"
                @click="select_all('followers')"
                src="../assets/select.png"
                alt=""
                v-if="item.active"
              />
              <img
                class="checkbox"
                @click="select_all('followers')"
                src="../assets/not_selected.png"
                alt=""
                v-if="!item.active"
              />
              <span class="name">{{ item.name }}</span>
            </div>
            <img class="item_avatar" src="../assets/avatar.jpeg" alt="" />
          </div>
        </div>
        <div class="footer">
          <div class="count">{{ countFollowers }} copied</div>
          <div class="countBetween">
            {{ followersBetweenStart }} - {{ followersBetweenEnd }} ({{
              this.followers.length
            }})
          </div>
          <div class="group-img">
            <img
              @click="back('followers')"
              class="next back"
              src="../assets/next.png"
              alt=""
            />
            <img
              @click="next('followers')"
              class="next"
              src="../assets/next.png"
              alt=""
            />
          </div>
        </div>
      </div>
      <div class="bookmarks" v-if="active == 3">
        <div class="item_header">
          <div class="item_group">
            <img
              class="checkbox"
              @click="select_all('bookmarks', false)"
              src="../assets/select.png"
              alt=""
              v-if="bookmark"
            />
            <img
              class="checkbox"
              @click="select_all('bookmarks', true)"
              src="../assets/not_selected.png"
              alt=""
              v-if="!bookmark"
            />
            <span class="title">Bookmarks</span>
          </div>
        </div>
        <div class="bookmark" v-for="item in bookmarks" :key="item.id">
          <div class="item">
            <span class="name" @click="item.open = !item.open">{{
              item.name
            }}</span>
            <img
              v-if="item.active"
              @click="selectBookmark(item.id)"
              class="selected"
              src="../assets/select.png"
            />
            <img
              v-if="!item.active"
              class="not_selected"
              @click="selectBookmark(item.id)"
              src="../assets/not_selected.png"
            />
          </div>
          <div class="posts" :class="{ open: item.open }">
            <div
              class="post"
              v-for="post in item.medias"
              :key="post.pk"
              @click="postActive(item.id, post.pk)"
            >
              <img class="post-img2" alt="" />
              <span class="name">{{ truncateText(post.caption_text) }}</span>
              <img
                v-if="post.active"
                class="selected"
                src="../assets/select.png"
              />
              <img
                v-if="!post.active"
                class="not_selected"
                src="../assets/not_selected.png"
              />
            </div>
          </div>
        </div>
        <div class="footer">
          <div class="count">{{ selectedBookmarks.length }} copied</div>
          <div class="countBetween">
            {{ bookmarksBetweenStart }} - {{ bookmarksBetweenEnd }} ({{
              this.bookmarks.length
            }})
          </div>
          <div class="group-img">
            <img
              @click="back('bookmarks')"
              class="next back"
              src="../assets/next.png"
              alt=""
            />
            <img
              @click="next('bookmarks')"
              class="next"
              src="../assets/next.png"
              alt=""
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.wrapper {
  width: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: start;
  gap: 20px;
}
.card {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 25px;
  padding: 32px;
  border-radius: 20px;
  background-color: #fff;
  border: 1px solid #fff;
  width: 360px;
}

.title {
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
  color: #000;
}

.info {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.desc {
  opacity: 80%;
  font-weight: 500;
  font-size: 16px;
  line-height: 22.4px;
}

.btn {
  width: 100%;
  background-color: #cf0032;
  border-radius: 10px;
  padding: 17px 24px;
  color: #fff;
  font-weight: 500;
  font-size: 16px;
  line-height: 16px;
}

.log {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
}

.log span,
a {
  font-weight: 500;
  font-size: 14px;
  line-height: 19.6px;
}

a {
  color: #cf0032;
}

.cancel {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.cancel img {
  cursor: pointer;
  height: 24px;
  width: 24px;
}

input {
  width: 100%;
  border: 1px solid #e6e6e6;
  border-radius: 8px;
  padding: 16px;
}

input::placeholder {
  color: #a5a5a5;
  font-weight: 400;
  font-size: 14px;
  line-height: 19.12px;
}

.forget_pass {
  text-align: end;
}

.group {
  position: relative;
}

.group-value {
  position: absolute;
  top: 0;
  transform: translateY(-50%);
  left: 12px;
  background-color: #fff;
  padding: 0 4px;
  color: #a5a5a5;
  font-weight: 500;
  font-size: 10px;
  line-height: 13.66px;
}

.card:hover {
  cursor: auto;
  transform: none;
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

h2 {
  display: flex;
  align-items: center;
  gap: 10px;
}

.wrap_btns {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.wrap_btns button {
  background-color: #ebf2fe;
  padding: 15px;
  color: #000;
  height: 73px;
  border-radius: 10px;
  transition: all 500ms ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
}

.wrap_btns button span {
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
  text-align: center;
}

.transfer {
  font-size: 14px;
  line-height: 20px;
  text-align: center;
  font-weight: 600;
  margin-left: 20px;
  background-color: #9747ff !important;
}

.active {
  background-color: #cbdeff !important;
}

.delete {
  background-color: #cbdeff !important;
  margin-left: 20px;
}

.wrap_btns button:hover {
  background-color: #cbdeff;
}

.following {
  display: flex;
  flex-direction: column;
}

.items {
  display: flex;
  flex-direction: column;
  height: 70vh;
  overflow-x: hidden;
  overflow-y: scroll;
}

.item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 10px;
}

.item_header {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  background-color: #fbfbfb;
  border-bottom: 1px solid #d8cece;
  padding: 10px 5px;
}

.item_group {
  display: flex;
  align-items: center;
  gap: 20px;
}

.item_avatar,
.item_avatar_foll {
  height: 30px;
  width: 30px;
  object-fit: cover;
  border-radius: 100%;

  transition: all 500ms ease;
}

.name {
  color: #2f65dd;
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
}

.item_active {
  background-color: #ebf2fe;
}

.item_active .item_avatar {
  transform: translateX(10px);
  width: 34px;
  height: 34px;
}

.footer {
  padding: 10px 5px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.group-img {
  display: flex;
  gap: 5px;
}

.next {
  width: 15px;
  height: 15px;
  cursor: pointer;
}

.back {
  transform: scaleX(-1);
}

.posts {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.post {
  margin-left: 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 10px;
}

.post-img2 {
  height: 52px;
  width: 52px;
}

.warn {
  width: 100%;
  padding: 20px;
  background-color: #f9dd4d;
  color: #000;
  font-weight: 600;
  font-size: 14px;
  line-height: 14px;
  text-align: center;
  border-radius: 10px;
}
</style>
