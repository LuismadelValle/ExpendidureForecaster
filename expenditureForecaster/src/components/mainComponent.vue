<template>
    <div class="flex h-screen">
        <!-- Sidebar -->
        <div 
            :class="{
                'w-64': !isCollapsed,
                'w-16': isCollapsed
            }" 
            class="transition-all duration-300 text-white"
        >
            <sidebar-menu 
                :menu="menu" 
                :collapsed="isCollapsed"  
                @update:collapsed="onToggleCollapse" 
                @item-click="onItemClick"
            />
        </div>

        <!-- Main Content -->
        <div class="flex-1 flex flex-col">
            <!-- Top Navigation -->
            <div class="shadow">
                <TopNav 
                    @update-username="updateUsername" 
                    @dashboard-Visible-After-Login="displayDashboardAfterLogin" 
                    @hide-Welcome-Message="hideAfterWait" 
                />
            </div>

            <!-- Main Content Area -->
            <div class="flex-1 flex flex-col">
                <!-- Welcome Message -->
                <div v-if="hideAfterAwait" class="text-center mt-4">
                    <h3 class="text-xl font-bold">Welcome {{ username }}</h3>
                </div>

                <!-- Dashboard -->
                <div class="flex-1 mt-20">
                    <router-view></router-view>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { defineAsyncComponent } from 'vue';
import { SidebarMenu } from 'vue-sidebar-menu';
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css';
import TopNav from './TopNav.vue'; 

const Dashboard = defineAsyncComponent(() => 
	import('./Dashboard.vue')
);

const PersonalBudget = defineAsyncComponent(() => 
	import('./personalBudget.vue')
);
  
  export default {
	components: {
	  SidebarMenu,
	  TopNav,
	  Dashboard,
	  PersonalBudget
	},
	data() {
	  return {
		isCollapsed: true,
		username: 'User',
		hideAfterAwait: false,
		displayDashboard: false,
		menu: [
		  {
			header: 'User Menu',
			hiddenOnCollapse: true
		  },
		  {
			title: 'User', 
			icon: 'pi pi-user',
			disabled: true
		  },
		  {
			href: '/dashboard',
			title: 'Dashboard',
			icon: 'pi pi-objects-column',
            exact: true
		  },
		  {
			title: 'Budget',
			icon: 'pi pi-wallet',
			href: "#",
			child: [
			  {
				href: '/budget/personal',
				title: 'Personal Budget',
			  }, 
			  {
				href: '/budget/familyFinances',
				title: 'Family Budget'
			  }
			]
		  },
		  {
			title: 'Forecaster',
			icon: 'pi pi-chart-scatter',
			href: "#",
			child: [
			  {
				href: '/forecaster/user',
				title: 'Personal Budget Forecast'
			  },
			  {
				href: '/forecaster/family',
				title: 'Family Budget Forecast'
			  }
			]
		  },
		  {
			href: '/settings',
			title: 'User Settings',
			icon: 'pi pi-cog'
		  }
		]
	  };
	},
	methods: {
	  onToggleCollapse(collapsed) {
		this.isCollapsed = collapsed;
	  },
	  onItemClick(event, item) {
		if (item.child && !this.isCollapsed) {
            item._showChild = !item._showChild;
        }

		if (item.href && item.href !== "#") {
            // Check if Vue Router exists and if route is different
            if (this.$router && this.$route.path !== item.href) {
                this.$router.push(item.href).catch(err => {
                    if (err.name !== "NavigationDuplicated") {
                        console.error(err);
                    }
                });
            }
        }
	  },
	  updateUsername(newUsername) {
		console.log(this.username, newUsername)
		this.username = newUsername;
		this.menu[1].title = newUsername;
	  },
      hideAfterWait(hide){
		this.hideAfterAwait = hide;

		setTimeout(() => {
			this.hideAfterAwait = false;
		}, 2000);
	  },
	  displayDashboardAfterLogin(){
		this.$router.push('/dashboard');
	  }
	},

  };
</script>
  
<style>
  .v-sidebar-menu {
	--vsm-primary-color: #4285f4;
	--vsm-base-bg: #2a2a2e;
	--vsm-item-color: #fff;
	--vsm-item-active-color:#FFFFFF;
	--vsm-item-active-bg:#2a2a2e;
	--vsm-item-active-line-color: var(--vsm-primary-color);
	--vsm-item-open-color: #fff;
	--vsm-item-hover-color:#fff;
	--vsm-item-open-bg: var(--vsm-primary-color);
	--vsm-item-hover-bg: rgba(30, 30, 33, 0.5);
	--vsm-icon-color: var(--vsm-item-color);
	--vsm-icon-bg: #1e1e21;
	--vsm-icon-active-color: #fff;
	--vsm-icon-active-bg:transparent;
	--vsm-icon-open-color: #fff;
	--vsm-icon-open-bg:transparent;
	--vsm-mobile-item-color: #fff;
	--vsm-mobile-item-bg: var(--vsm-primary-color);
	--vsm-mobile-icon-color: var(--vsm-mobile-item-color);
	--vsm-mobile-icon-bg: transparent;
	--vsm-dropdown-bg: #36363b;
	--vsm-header-item-color: rgba(255, 255, 255, 0.7);
	--vsm-toggle-btn-color: #fff;
	--vsm-toggle-btn-bg: #1e1e21;
	--vsm-item-font-size: 16px;
	--vsm-item-line-height: 35px;
	--vsm-item-padding: 10px 15px;
	--vsm-icon-height: 35px;
	--vsm-icon-width: 35px;
 	}
	.sidebar.v-sidebar-menu .vsm--mobile-item {
		z-index: 0 !important;
	}
</style>