<template>
  <sidebar-menu :menu="menu" :width="width" @update:collapsed="onToggleCollapse" @item-click="onItemClick" />
</template>

<script>
import { SidebarMenu } from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'

export default {
	components: {
    	SidebarMenu
  	},
    data() {
      return {
        menu: [
          {
            header: 'User Menu',
            hiddenOnCollapse: true
          },
		  {
			href: '/user',
			title: 'Username',
			icon: 'pi pi-user',
		  },
          {
            href: '/',
            title: 'Dashboard',
            icon: 'pi pi-objects-column'
          },
          {
            href: '/budget',
            title: 'Budget',
            icon: 'pi pi-wallet',
            child: [
			{
                href: '/budget/personalFinances',
                title: 'Personal Budget',
              }, {
                href: '/budget/familyFinances',
                title: 'Family Budget'
              }
            ]
          },
		  {
            title: 'Forecaster',
            icon: 'pi pi-chart-scatter',
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
      }
    },
	methods: {
		onToggleCollapse(collapsed) {},
		onItemClick(event, item) {}
	}
  }  
</script>

<style scoped>
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
</style>