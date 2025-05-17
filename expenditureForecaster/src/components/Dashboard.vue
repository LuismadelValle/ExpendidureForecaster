<template>
  <v-container>
    <v-row>
      <v-col>
         <Pie :data="data" :options="options" />
      </v-col>
      <v-col></v-col>
    </v-row>
    <v-row>
      <h4 class="mb-5">Your last {{ totalData }} expenses</h4>
      <v-data-table :items="items" hide-default-footer></v-data-table>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, ref, reactive, onMounted } from 'vue'
// import { Chart, Responsive, Pie, Tooltip, Grid, Line } from 'vue3-charts'
import { VDataTable } from 'vuetify/components/VDataTable'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Pie } from 'vue-chartjs'
import * as chartConfig from './chartConfig'
import axios from 'axios';

ChartJS.register(ArcElement, Tooltip, Legend)

export default defineComponent({
  name: 'LineChart',
  components: { Pie, VDataTable },
  data() {
    return chartConfig
  },
  setup() {
    const data = [
      { name: 'Jan', pl: 1000, avg: 500, inc: 300 },
      { name: 'Feb', pl: 2000, avg: 900, inc: 400 },
      { name: 'Apr', pl: 400, avg: 400, inc: 500 },
      { name: 'Mar', pl: 3100, avg: 1300, inc: 700 },
      { name: 'May', pl: 200, avg: 100, inc: 200 },
      { name: 'Jun', pl: 600, avg: 400, inc: 300 },
      { name: 'Jul', pl: 500, avg: 90, inc: 100 }
    ]

    const direction = ref('horizontal')
    const margin = ref({
      left: 0,
      top: 20,
      right: 20,
      bottom: 0
    })

    const axis = ref({
      primary: {
        type: 'band',
        format: (val: string) => {
          if (val === 'Feb') {
            return '😜'
          }
          return val
        }
      },
      secondary: {
        domain: ['dataMin', 'dataMax + 100'],
        type: 'linear',
        ticks: 8
      }
    })

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
