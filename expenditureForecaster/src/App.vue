<template>
  <v-app class="d-flex flex-column fill-height">
    <v-main>
      <MainComponent />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import 'primeicons/primeicons.css';
import MainComponent from './components/mainComponent.vue';
</script>

<style scoped>
html, body, #app {
  height: 100%;
  margin: 0;
}

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
