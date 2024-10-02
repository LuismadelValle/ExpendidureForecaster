import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import SideMenu from './components/SideMenu.vue'
import { createMemoryHistory, createRouter } from 'vue-router'

const routes = [
  {
    path: '/', component: SideMenu,
    path2: '/budget/personalFinances', component2: SideMenu,
    path3: '/budget/familyFinances', component3: SideMenu,
    path4: '/forecaster/user', component4: SideMenu,
    path5: '/forecaster/family', component5: SideMenu,
    path6: '/settings', component6: SideMenu,
  },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

createApp(App).use(router).mount('#app')
