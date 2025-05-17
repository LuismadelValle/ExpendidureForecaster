<template>
  <v-app-bar :elevation="2">
    <template v-slot:prepend>
      <v-app-bar-nav-icon @click="$emit('toggle-drawer')"></v-app-bar-nav-icon>
    </template>

    <v-app-bar-title>{{ username }}</v-app-bar-title>

    <template v-slot:append>
      <v-btn icon="mdi-magnify" />

      <v-btn @click="toggleAuth" class="ml-2" variant="tonal" id="LoginButton">
        <v-avatar image="https://randomuser.me/api/portraits/men/85.jpg" size="40" v-if="isLoggedIn"></v-avatar>
        <v-icon start v-if="notLoggedIn">mdi-account</v-icon>
        {{ buttonText }}
      </v-btn>
    </template>
  </v-app-bar>
</template>

<script>
export default {
  name: 'AuthButton',
  data() {
    return {
      isLoggedIn: false,
      notLoggedIn: true,
      username: '',
    };
  },
  computed: {
    buttonText() {
      return this.isLoggedIn ? 'Log out' : 'Log in';
    },
  },
  methods: {
    toggleAuth() {
      this.isLoggedIn = !this.isLoggedIn;
      this.notLoggedIn = !this.notLoggedIn

      if (this.isLoggedIn) {
        this.username = 'User Logged';
        this.$emit('update-username', this.username);
        this.$emit('dashboard-Visible-After-Login', true);
        this.$emit('hide-Welcome-Message', true);
        this.$router.push('/dashboard');
      } else {
        this.username = '';
        this.$emit('update-username', this.username);
        this.$emit('dashboard-Visible-After-Login', false);
        this.$router.push('/')
      }
    }
  },
};
</script>

<style>
.v-app-bar{
  background-color: #000 !important;
}

.v-app-bar-title {
  color: #fff;
}

.v-btn {
  background-color: #000 !important;
  color: #fff !important;
  font-size: 14px;
  text-transform: none;
  justify-content: center;
  align-items: center;
  display: flex;
}

#LoginButton {
  height: 80px !important;
}
</style>