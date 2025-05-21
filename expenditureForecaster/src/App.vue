<template>
  <v-app class="d-flex flex-column fill-height" app>
    <MainComponent />
  </v-app>
</template>

<script setup lang="ts">
import 'primeicons/primeicons.css';
import MainComponent from './components/mainComponent.vue';
</script>

<style scoped>
html, body, #app, .v-application {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
}

.v-main {
  flex: 1;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.v-container {
  max-width: 100% !important;
  padding: 0 !important;
}
</style>