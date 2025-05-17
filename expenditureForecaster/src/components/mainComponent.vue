<template>
	<v-app>
		<TopNav 
			@update-username="updateUsername" 
			@dashboard-Visible-After-Login="handleDashboardRedirect"
			@toggle-drawer="toggleCollapse"
		/>
		<v-navigation-drawer :width="drawerWidth" :permanent="true" class="transition-all duration-300" v-model="drawerOpen">
			<v-list>
				<v-list-item link title="Dashboard" prepend-icon="mdi-home-analytics" href="/dashboard"></v-list-item>
					<v-list-group value="Budget">
						<template v-slot:activator="{ props }">
							<v-list-item
								v-bind="props"
								prepend-icon="mdi-wallet-bifold"
								title="Budget"
							></v-list-item>
						</template>
						<v-list-item
							v-for="([title, icon, href], i) in budgets"
							:key="i"
							:prepend-icon="icon"
							:title="title"
							link
							:href="href"
						></v-list-item>
					</v-list-group>
					<v-list-group value="Forecaster">
						<template v-slot:activator="{ props }">
							<v-list-item
								v-bind="props"
								prepend-icon="mdi-wallet-bifold"
								title="Forecaster"
							></v-list-item>
						</template>
						<v-list-item
							v-for="([title, icon, href], i) in forecasters"
							:key="i"
							:prepend-icon="icon"
							:title="title"
							link
							:href="href"
						></v-list-item>
					</v-list-group>
					<v-list-item link title="User Settings" prepend-icon="mdi-cog" href="/settings"></v-list-item>
				</v-list>
			</v-navigation-drawer>
		<v-main>
			<RouterView />
		</v-main>
	</v-app>
</template>

<script>
import TopNav from './TopNav.vue'; 
import Dashboard from './Dashboard.vue'
import PersonalBudget from './personalBudget.vue';
import { RouterView } from 'vue-router';

export default {
	components: {
	  TopNav,
	  Dashboard,
	  PersonalBudget
	},
	data() {
	  return {
		username: 'User',
		shouldDisplayDashboard: false,
		isCollapsed: false,
    drawerWidth: 200,
    minDrawerWidth: 100,
		drawerOpen: true,
		budgets: [
			['Personal Budget', 'mdi-card-account-details', '/budget/personal'],
			['Family Budget', 'mdi-human-male-female-child', '/budget/familyFinances']
		],
		forecasters: [
			['Personal Budget Forecast', 'mdi-chart-timeline-variant-shimmer', '/forecaster/user',],
			['Family Budget', 'mdi-chart-areaspline','/forecaster/family']
		],
	  };
	},
	methods: {
	  updateUsername(newUsername) {
			console.log(this.username, newUsername)
			this.username = newUsername;
	  },
	  handleDashboardRedirect(visible) {
			this.shouldDisplayDashboard = visible;

			if (this.shouldDisplayDashboard) {
			this.$router.push('/dashboard');
			} else {
			this.$router.push('/');
			}
		},
		toggleCollapse() {
			if (!this.drawerOpen) {
				this.drawerOpen = true;
				this.isCollapsed = true;
				this.drawerWidth = 256;
			} else {
				this.isCollapsed = !this.isCollapsed;
				this.drawerWidth = this.isCollapsed ? this.minDrawerWidth : 256;
			}
		},
		handleResize() {
			const width = window.innerWidth;

			if (width <= 600) {
				this.drawerOpen = false;
			} else if (width <= 1024) {
				this.drawerOpen = true;
				this.drawerWidth = this.isCollapsed ? this.minDrawerWidth : 120;
			} else {
				this.drawerOpen = true;
				this.drawerWidth = this.isCollapsed ? this.minDrawerWidth : 256;
			}
		}
	},
	mounted() {
		window.addEventListener('resize', this.handleResize),
  	this.handleResize()
	},
	beforeUnmount() {
		window.removeEventListener('resize', this.handleResize);
	},
};
</script>
  
<style>

</style>