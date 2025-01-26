import './assets/main.css'

import { createApp } from 'vue'
// import VueRouter from 'vue-router'
import App from './App.vue'
import './input.css'
import { createMemoryHistory, createRouter } from 'vue-router'
import Dashboard from './components/Dashboard.vue'

const routes = [
  {path: '/', component: App},
  {path: '/dashboard', component: Dashboard},
    // path3: '/budget/familyFinances', component3: SideMenu,
    // path4: '/forecaster/user', component4: SideMenu,
    // path5: '/forecaster/family', component5: SideMenu,
    // path6: '/settings', component6: SideMenu,
]

const router = createRouter({
  history: createMemoryHistory('configure-admin'),
  routes: routes,
})

createApp(App).use(router).mount('#app')
