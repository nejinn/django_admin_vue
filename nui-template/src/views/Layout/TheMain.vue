<template>
  <nly-content-wrapper>
    <!-- <nly-card class="m-3" header-outline header-variant="secondary">
      <nly-content-header>
        <nly-container fluid>
          <nly-row row-class="mb-2" align-v="end">
            <nly-col sm="6">
              <h1 class="m-0 text-dark">{{ breadcrumbArray.currentName }}</h1>
            </nly-col>
            <nly-col sm="6">
              <nly-breadcrumb
                :item="breadcrumbArray.breadcrumbItems"
                breadcrumb-class="float-sm-right"
              />
            </nly-col>
          </nly-row>
        </nly-container>
      </nly-content-header>
    </nly-card> -->
    <nly-content>
      <nly-row class="p-3">
        <nly-col>
          <router-view />
        </nly-col>
      </nly-row>
    </nly-content>
  </nly-content-wrapper>
</template>

<script>
export default {
  name: "TheMain"
  // computed: {
  //   breadcrumbArray() {
  //     const routerArray = [];
  //     this.$route.matched.forEach(item => {
  //       if (item.name == this.$route.name) {
  //         routerArray.push({
  //           text: item.meta.title,
  //           active: true,
  //           to: item.path
  //         });
  //       } else {
  //         if (item.path == "") {
  //           if (this.$route.name !== "Home") {
  //             routerArray.push({
  //               text: item.meta.title,
  //               to: "/"
  //             });
  //           }
  //         } else {
  //           routerArray.push({
  //             text: item.meta.title,
  //             to: item.path
  //           });
  //         }
  //       }
  //     });

  //     return {
  //       breadcrumbItems: routerArray,
  //       currentName: this.$route.matched.slice(-1)[0].meta.title
  //     };
  //   }
  // }
};
</script>
