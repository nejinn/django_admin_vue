<template>
  <nly-navbar variant="white" header border size="sm" :dark="false">
    <nly-navbar-nav>
      <nly-nav-item v-nly-sidebar-collapse.sidebar-collapse>
        <nly-icon icon="nlyfont nly-icon-logo-windows" />
      </nly-nav-item>
      <nly-row align-v="center">
        <nly-col class="d-none d-md-block">
          <nly-breadcrumb
            :item="breadcrumbArray.breadcrumbItems"
            breadcrumb-class="align-items-center p-0 ml-2 mr-0 mt-0 mb-0 bg-transparent"
          />
        </nly-col>
      </nly-row>
    </nly-navbar-nav>
    <nly-navbar-nav class="ml-auto">
      <nly-nav-item>
        {{ userInfo }}
      </nly-nav-item>

      <nly-nav-item>
        <nly-icon icon="nlyfont nly-icon-setting-fill" />
      </nly-nav-item>
    </nly-navbar-nav>
  </nly-navbar>
</template>

<script>
export default {
  name: "TheHeader",
  props: {
    userInfo: {
      type: [String, Object],
      default: null
    }
  },
  methods: {
    logout() {
      this.$router.push({
        name: "Login"
      });
      this.$store.commit("clearLoginUserInfo");
    }
  },
  computed: {
    breadcrumbArray() {
      const routerArray = [];
      this.$route.matched.forEach(item => {
        if (item.name == this.$route.name) {
          routerArray.push({
            text: item.meta.title,
            active: true,
            to: item.path,
            linkClass: "text-orange"
          });
        } else {
          if (item.path == "") {
            if (this.$route.name !== "Home") {
              routerArray.push({
                text: item.meta.title,
                to: "/",
                linkClass: "text-info"
              });
            }
          } else {
            routerArray.push({
              text: item.meta.title,
              to: item.path,
              linkClass: "text-info"
            });
          }
        }
      });

      return {
        breadcrumbItems: routerArray,
        currentName: this.$route.matched.slice(-1)[0].meta.title
      };
    }
  }
};
</script>
