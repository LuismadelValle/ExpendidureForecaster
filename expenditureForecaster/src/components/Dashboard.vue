<template>
    <v-container id="dashbboardContainer">
        <v-row>
            <v-col cols="6">
                <div>
                    <yearIncome />
                </div>
            </v-col>
            <v-col cols="6">
                <div>
                    <lastYearIncome />
                </div>
            </v-col>
        </v-row>
    </v-container>
    
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

<style scoped>
#dashbboardContainer {
    background-color: white;
}
</style>