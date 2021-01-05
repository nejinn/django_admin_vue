<template>
  <div class="login-page" style="min-height: 512.391px;">
    <div class="login-box">
      <div class="login-logo">
        <nly-link to="/" v-if="siteHeader">
          <span
            class="login-log-text"
            v-for="(item, index) in siteHeader"
            :key="index"
            ><b>{{ item }}</b></span
          >
          <!-- <span class="login-log-text"><b>l</b></span>
          <span class="login-log-text"><b>y</b></span>
          <span class="login-log-text">A</span>
          <span class="login-log-text">d</span>
          <span class="login-log-text">m</span>
          <span class="login-log-text">i</span>
          <span class="login-log-text">n</span>
          <span class="login-log-text">l</span>
          <span class="login-log-text">t</span>
          <span class="login-log-text">e</span>
          <span class="login-log-text"><b>V</b></span>
          <span class="login-log-text"><b>u</b></span>
          <span class="login-log-text"><b>e</b></span> -->
        </nly-link>
      </div>

      <nly-card>
        <nly-card-body class="login-card-body">
          <p class="login-box-msg">输入账号密码登录</p>
          <nly-form>
            <nly-input-group
              size="sm"
              :invalid-feedback="usernameInvalid"
              :valid="usernameValid"
            >
              <nly-input
                type="email"
                placeholder="Username"
                v-model="userInfo.username"
              />
              <nly-input-group-append is-text>
                <nly-icon icon="fas fa-envelope" />
              </nly-input-group-append>
            </nly-input-group>

            <nly-input-group
              size="sm"
              :invalid-feedback="passwordInvalid"
              :valid="passwordValid"
              class="mt-3"
            >
              <nly-input
                :type="showPassword === false ? 'password' : 'text'"
                placeholder="Password"
                v-model="userInfo.password"
              />
              <nly-input-group-append is-text>
                <nly-icon icon="fas fa-lock" />
              </nly-input-group-append>
            </nly-input-group>
            <nly-row class="mt-2">
              <nly-col xs="12" sm="8">
                <nly-form-checkbox class="text-sm"
                  >记住账号密码</nly-form-checkbox
                >
              </nly-col>

              <nly-col xs="12" sm="4">
                <nly-switch
                  class="text-sm"
                  on-variant="danger"
                  v-model="showPassword"
                >
                  显示密码
                </nly-switch>
              </nly-col>
            </nly-row>
            <nly-row class="mt-2">
              <nly-col class="text-right">
                <nly-button
                  size="xs"
                  class="mr-2"
                  variant="outlineDanger"
                  v-nly-popover.hover.top="'重置表单'"
                  @click="resetUserInfo"
                >
                  <nly-icon icon="oi oi-loop-square mr-1 ml-1" />
                </nly-button>
                <nly-button
                  size="xs"
                  variant="outlineInfo"
                  v-nly-popover.hover.top="'登录'"
                  @click="login"
                >
                  <nly-icon icon="oi oi-account-login mr-1 ml-1" />
                </nly-button>
              </nly-col>
            </nly-row>
          </nly-form>
        </nly-card-body>
      </nly-card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showPassword: false,
      userInfo: {
        username: undefined,
        password: undefined
      },
      usernameInvalid: undefined,
      passwordInvalid: undefined,
      usernameValid: "novalid",
      passwordValid: "novalid",
      title: undefined,
      siteTitle: undefined,
      siteHeader: undefined
    };
  },
  methods: {
    resetUserInfo() {
      this.userInfo = {
        username: undefined,
        password: undefined
      };
      this.usernameInvalid = undefined;
      this.usernameValid = "novalid";
      this.passwordInvalid = undefined;
      this.passwordValid = "novalid";
    },
    login() {
      const data = this.userInfo;
      const { username, password } = data;
      if (!username) {
        this.usernameInvalid = "用户名不能为空";
        this.usernameValid = "invalid";
      }

      if (!password) {
        this.passwordInvalid = "密码不能为空";
        this.passwordValid = "invalid";
      }
      const that = this;
      this.$api.HttpsLogin.loginPost(that, data);
    }
  },
  mounted() {
    const obj = this;
    this.$api.HttpsLogin.loginGet(obj);
    // document.title = this.title + "|" + this.siteTitle;
  }
};
</script>

<style scoped>
.login-box {
  margin-bottom: 0;
  transition: 0.3s ease-out;
}
.login-box:hover {
  margin-bottom: 2rem;
  transition: 0.3s ease-out;
}

.login-log-text {
  animation: bounce 0.75s cubic-bezier(0.05, 0, 0.2, 1) infinite alternate;
  display: inline-block;
  transform: translate3d(0, 0, 0);
  margin-top: 0.5em;
  text-shadow: rgba(255, 255, 255, 0.4) 0 0 0.05em;
  font: normal 500 "Varela Round", sans-serif;
  font-size: inherit;
}
.login-log-text:nth-child(1) {
  animation-delay: 0s;
  color: #bf360c;
}
.login-log-text:nth-child(2) {
  animation-delay: 0.05s;
  color: #d84315;
}
.login-log-text:nth-child(3) {
  animation-delay: 0.1s;
  color: #e64a19;
}
.login-log-text:nth-child(4) {
  animation-delay: 0.15s;
  color: #f4511e;
}
.login-log-text:nth-child(5) {
  animation-delay: 0.2s;
  color: #ff5722;
}
.login-log-text:nth-child(6) {
  animation-delay: 0.25s;
  color: #ff7043;
}
.login-log-text:nth-child(7) {
  animation-delay: 0.35s;
  color: #ff8a65;
}
.login-log-text:nth-child(8) {
  animation-delay: 0.4s;
  color: #4db6ac;
}
.login-log-text:nth-child(9) {
  animation-delay: 0.45s;
  color: #26a69a;
}
.login-log-text:nth-child(10) {
  animation-delay: 0.5s;
  color: #009688;
}
.login-log-text:nth-child(11) {
  animation-delay: 0.55s;
  color: #00897b;
}
.login-log-text:nth-child(12) {
  animation-delay: 0.6s;
  color: #00796b;
}
.login-log-text:nth-child(13) {
  animation-delay: 0.65s;
  color: #00695c;
}
.login-log-text:nth-child(14) {
  animation-delay: 0.7s;
  color: #004d40;
}
@keyframes bounce {
  0% {
    transform: translate3d(0, 0, 0);
    text-shadow: rgba(255, 255, 255, 0.4) 0 0 0.05em;
  }
  100% {
    transform: translate3d(0, -0.5em, 0);
    text-shadow: rgba(255, 255, 255, 0.4) 0 1em 0.35em;
  }
}
</style>
