<template>
  <main>
    <v-row>
      <TopNav @update-username="updateUsername" @dashboard-Visible-After-Login="displayDashboardAfterLogin" @hide-Welcome-Message="hideAfter2s"/>
    </v-row>
    <v-row>
      <v-col class="d-flex flex-column justify-center">
        <SideMenu />
      </v-col>
      <v-col class="d-flex flex-column">
        <v-row>
          <h3 v-if="hideAfterAwait">Welcome {{ username }}</h3>
        </v-row>
        <v-row>
          <Dashboard v-if="dashboardVisisbleBeforeLogin"/>
        </v-row>
      </v-col>
    </v-row>
  </main> 
</template>

<script setup lang="ts">
import { ref } from 'vue';
import 'primeicons/primeicons.css'
import TopNav from './components/TopNav.vue';
import SideMenu from './components/SideMenu.vue'
import Dashboard from './components/Dashboard.vue';

var dashboardVisisbleBeforeLogin = ref(false);
var hideAfterAwait = ref(false);
var username = ref('User');

function updateUsername(newUsername:string) {
  username.value = newUsername;
};

function displayDashboardAfterLogin(newValue:boolean) {
  dashboardVisisbleBeforeLogin.value = newValue;
};

function hideAfter2s(newValue:boolean){
  hideAfterAwait.value = newValue;

  setTimeout(() => {
    hideAfterAwait.value = false;
  }, 2000);
};
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
