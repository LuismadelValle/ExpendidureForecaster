<template>
  <div class="auth-button-container">
    <button @click="toggleAuth">
      <i :class="'pi ' + currentIcon"></i>
      {{ buttonText }}
    </button>
  </div>
</template>

<script>
export default {
  name: 'AuthButton',
  data() {
    return {
      isLoggedIn: false, // Tracks login state
      icons: {
        login: 'pi-sign-in',
        logout: 'pi-sign-out'
      },
      username: 'User'
    };
  },
  computed: {
    currentIcon() {
      return this.isLoggedIn ? this.icons.logout : this.icons.login;
    },
    buttonText() {
      return this.isLoggedIn ? 'Log out' : 'Log in';
    }
  },
  methods: {
    toggleAuth() {
      this.isLoggedIn = !this.isLoggedIn;
      if (this.isLoggedIn) {
        console.log('User logged in');
        this.$emit('update-username', 'User Logged');
      } else {
        console.log('User logged out');
        this.$emit('update-username', 'User');
      }
    }
  }
};
</script>

<style scoped>
.auth-button-container {
  position: fixed;
  top: 5px;
  right: 5px;
  z-index: 1000;
}

button {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  font-size: 14px;
  cursor: pointer;
  border: none;
  border-radius: 5px;
  background-color: #2a2a2e;
  color: white;
}

button:hover {
  background-color: #4285f4;
}
</style>