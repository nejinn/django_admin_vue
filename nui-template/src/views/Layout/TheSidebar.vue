<template>
  <nly-sidebar-menu v-bind="sidebarList" />
</template>

<script>
export default {
  name: "TheSidebar",
  props: {
    sidebar: {
      type: [Array, Object],
      default: null
    }
  },
  data() {
    return {
      logo: undefined
    };
  },
  created() {
    this.logo = require("../../assets/static/img/NLYLOGO.png");
  },
  computed: {
    sidebarList() {
      const sidebarVnode = [
        {
          _type: "nly-sidebar-nav",
          _key: 0,
          // flat: true,
          dataGroup: "one",
          compact: true,
          size: "sm",
          exact: true,
          _children: this.sidebar["sidebar-list"],
          sidebarNavClass: "mt-2"
        }
      ];
      const all_props = this.sidebar;
      all_props["sidebar-list"] = sidebarVnode;
      return all_props;
    }
  }
};
</script>
