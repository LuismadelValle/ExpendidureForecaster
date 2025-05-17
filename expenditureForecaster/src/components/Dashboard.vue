<template>
  <v-container fluid class="fill-height fill-width pa-4">
    <v-row class="fill-width" no-gutters>
      <v-col cols="12" md="6">
        <Pie :data="data" :options="options" />
      </v-col>
      <v-col cols="12" md="6">
        <Line :data="data2" :options="options2" />
      </v-col>
    </v-row>

    <v-row class="fill-width">
      <v-col cols="12">
        <h4 class="mb-5 mt-10">Your last {{ totalData }} expenses</h4>
        <v-data-table :items="items" hide-default-footer></v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, ref, reactive, onMounted } from 'vue'
import { VDataTable } from 'vuetify/components/VDataTable'
import { Chart as ChartJS, ArcElement, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement, Title } from 'chart.js'
import { Pie, Line } from 'vue-chartjs'
import * as chartConfig from './chartConfig'
import axios from 'axios';

ChartJS.register(ArcElement, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement, Title)

export default defineComponent({
  name: 'LineChart',
  components: { Pie, Line, VDataTable },
  data() {
    return chartConfig
  },
  setup() {
    let items = ref([])

    const fetchPersonalList = async() => {
      try {
        const listResponse = await axios.get('http://localhost:8000/dashboard_last_personal_list')

        items.value = listResponse.data.slice(0, 12)
      } catch (error) {
        throw new Error('There was an error')
      }
    }

    onMounted(() => {
      fetchPersonalList()
    })

    return {
      items
    }
  }, 
  computed: {
    totalData() {
        return this.items.length;
    }
  }
})
</script>
