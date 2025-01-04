<template>
    <v-col id="columnForYearIncome">
        <yearIncome />
    </v-col>
    <v-col id="columnForLastYearIncome">
        <lastYearIncome />
    </v-col>
  </template>

<script>
import yearIncome from './dashboardComponents/yearIncome.vue';
import lastYearIncome from './dashboardComponents/lastYearIncome.vue';

export default {
    components: {
        yearIncome,
        lastYearIncome
    }
}
</script>

<style>
#columnForYearIncome {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}
#columnForLastYearIncome {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}
</style>