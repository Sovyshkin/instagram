<script>
import axios from "axios";
import RightLogin from "./RightLogin.vue";

export default {
  name: "RightScreen",
  components: { RightLogin },
  data() {
    return {
      login: "",
      password: "",
      message: "",
      account1: true,
      active: 1,
      followings: [
        {
          id: 1,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 2,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 3,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 4,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 5,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 6,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 7,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 8,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 9,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 10,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 11,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 12,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 13,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 14,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 15,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 16,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 17,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 18,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 19,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 20,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 21,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 22,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 23,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 24,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 25,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 826,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 27,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 28,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 29,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 30,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 31,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 32,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 33,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 34,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 35,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 36,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 37,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 38,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 39,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 40,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 41,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 42,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 43,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 44,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 45,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 46,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 47,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 48,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 49,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 50,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 51,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 52,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 53,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 54,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 6,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 7,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 8,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 9,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 10,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 11,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 12,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 13,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 14,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 15,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 16,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 17,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 18,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 19,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 20,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 21,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 22,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 23,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 24,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 25,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 826,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 27,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 28,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 29,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 30,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 31,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 32,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 33,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 34,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 35,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 36,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 37,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 38,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 39,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 40,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 41,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 42,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 43,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 44,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 45,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 46,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 47,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 48,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 49,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 50,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 51,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 52,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 53,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 54,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 6,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 7,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 8,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 9,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 10,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 11,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 12,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 13,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 14,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 15,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 16,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 17,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 18,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 19,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 20,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 21,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 22,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 23,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 24,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 25,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 826,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 27,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 28,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 29,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 30,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 31,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 32,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 33,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 34,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 35,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 36,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 37,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 38,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 39,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 40,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 41,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 42,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 43,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 44,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 45,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 46,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 47,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 48,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 49,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 50,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 51,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 52,
          name: "CodeRed",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 53,
          name: "LabelCom",
          img: "avatar.jpeg",
          active: false,
        },
        {
          id: 54,
          name: "Дубровский",
          img: "avatar.jpeg",
          active: false,
        },
      ],
      bookmarks: [
        {
          id: 1,
          name: "Папка_1",
          open: false,
          active: false,
          posts: [
            {
              name: "Пост_1",
              active: false,
            },
            {
              name: "Пост_2",
              active: false,
            },
          ],
        },
        {
          id: 2,
          name: "Папка_2",
          open: false,
          active: false,
          posts: [
            {
              name: "Пост_1",
              active: false,
            },
            {
              name: "Пост_2",
              active: false,
            },
          ],
        },
        {
          id: 3,
          name: "Папка_3",
          open: false,
          active: false,
          posts: [
            {
              name: "Пост_1",
              active: false,
            },
            {
              name: "Пост_2",
              active: false,
            },
          ],
        },
      ],
      following: false,
      countFollowing: 0,
      followingBetweenStart: 0,
      followingBetweenEnd: 50,
      followersBetweenStart: 0,
      followersBetweenEnd: 50,
      followers: [],
      countFollowers: 0,
      countBookmarks: 0,
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
            localStorage.setItem("account1", true);
          }
          setTimeout(() => {
            this.message = "";
          }, 2500);
        }
      } catch (err) {
        console.log(err);
      }
    },

    select_all(s, type) {
      if (s == "following") {
        this.following = !this.following;
        if (type) {
          this.countFollowing = this.followings.length;
        } else {
          this.countFollowing = 0;
        }
        for (let i = 0; i < this.followings.length; i++) {
          this.followings[i].active = type;
        }
      }
      // if (this.subscriptions) {
      //   this.subscriptions.forEach((item) => (item.active = !item.active));
      // }
    },

    countSelect(type, id) {
      if (type == "following") {
        for (let i = 0; i < this.followings.length; i++) {
          if (this.followings[i].id == id) {
            if (this.followings[i].active) {
              this.countFollowing -= 1;
            } else {
              this.countFollowing++;
            }
            this.followings[i].active = !this.followings[i].active;
          }
        }
      }
    },
    async load_info() {
      try {
        this.account1 = localStorage.getItem("account1");
      } catch (err) {
        console.log(err);
      }
    },

    selectBookmark(id) {
      for (let i = 0; i < this.bookmarks.length; i++) {
        let item = this.bookmarks[i];
        if (item.id == id) {
          if (item.posts) {
            if (item.active) {
              item.posts.forEach((post) => (post.active = false));
              item.active = false;
            } else {
              item.posts.forEach((post) => (post.active = true));
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
          let active = bookmark.posts.find((post) => post.active);
          if (active) {
            bookmark.active = true;
          } else {
            bookmark.active = false;
          }
        }
        this.bookmarks[i] = bookmark;
      }
    },

    postActive(id, name) {
      for (let i = 0; i < this.bookmarks.length; i++) {
        let item = this.bookmarks[i];
        if (item.id == id) {
          if (item.posts) {
            for (let j = 0; j < item.posts.length; j++) {
              let post = item.posts[j];
              if (post.name == name) {
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
  },
  mounted() {
    // this.load_info();
  },
};
</script>
<template>
  <div class="wrapper">
    <RightLogin />
    <div class="info" v-if="account1">
      <div class="wrap_btns">
        <button
          class="btn"
          :class="{ active: active == 1 }"
          @click="this.active = 1"
        >
          <span>Following</span>
          <span>({{ countFollowing }} of {{ this.followings.length }})</span>
        </button>
        <button
          class="btn"
          :class="{ active: active == 2 }"
          @click="this.active = 2"
        >
          <span>Followers</span>
          <span>({{ countFollowers }} of {{ this.followers.length }})</span>
        </button>
        <button
          class="btn"
          :class="{ active: active == 3 }"
          @click="this.active = 3"
        >
          <span>Bookmarks</span>
          <span>({{ countBookmarks }} of {{ bookmarks.length }})</span>
        </button>
        <button class="btn delete">Delete Selected</button>
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
            @click="countSelect('following', item.id)"
            v-for="item in followings.slice(
              followingBetweenStart,
              followingBetweenEnd + 1
            )"
            :key="item.id"
            :class="{ item_active: item.active }"
          >
            <div class="item_group">
              <img
                class="checkbox"
                @click="select_all('following')"
                src="../assets/select.png"
                alt=""
                v-if="item.active"
              />
              <img
                class="checkbox"
                @click="select_all('following')"
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
              v-for="post in item.posts"
              :key="post.name"
              @click="postActive(item.id, post.name)"
            >
              <span class="name">{{ post.name }}</span>
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

.item_avatar {
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
</style>
