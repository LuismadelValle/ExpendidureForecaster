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

import { createVuetify } from 'vuetify'
import 'vuetify/styles'
import '@mdi/font/css/materialdesignicons.css'

import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import EmptyView from './components/emptyView.vue'



const routes = [
  {path: '/', component: EmptyView},
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

const vuetifyInstance = createVuetify({
  components,
  directives,
})

createApp(App).use(router).use(vuetifyInstance).mount('#app')




