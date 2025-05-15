import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import './input.css'
import { createWebHistory, createRouter } from 'vue-router'
import Dashboard from './components/Dashboard.vue'
import PersonalBudget from './components/personalBudget.vue'
import FamilyBudget from './components/familyBudget.vue'
import PersonalForecaster from './components/personalForecaster.vue'
import ForecasterFamily from './components/forecasterFamily.vue'
import Settings from './components/settings.vue'


const routes = [
  {path: '/', component: App},
  {path: '/dashboard', component: Dashboard},
  {path: '/budget/personal', component: PersonalBudget},
  {path: '/budget/familyFinances', component: FamilyBudget},
  {path: '/forecaster/user', component: PersonalForecaster},
  {path: '/forecaster/family', component: ForecasterFamily},
  {path: '/settings', component: Settings},
]

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
})

createApp(App).use(router).mount('#app')
