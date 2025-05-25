<template>
  <v-container fluid class="pa-4">
    <v-row>
      <v-col md="3">
        <div class="chart-wrapper">
          <Pie :data="distributionData" :options="optionsPie" />
        </div>
      </v-col>
      <v-col md="3">
        <div class="chart-wrapper">
          <Line :data="lineChartData" :options="options" />
        </div>
      </v-col>
    </v-row>
  </v-container>

  <v-container>
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
import axios from 'axios';

ChartJS.register(ArcElement, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement, Title)

export default defineComponent({
  name: 'LineChart',
  components: { Pie, Line, VDataTable },
  data() {
    return
  },
  setup() {
    function generateRandomColors(count: number) {
      const colors = [];
      for (let i = 0; i < count; i++) {
        const color = `hsl(${Math.floor(Math.random() * 360)}, 70%, 60%)`;
        colors.push(color);
      }
      return colors;
    }

    let items = ref([])
    const fieldLabels = [
      'Name', 'Month', 'Income from Work', 'Bills', 'Food', 'Taxes',
      'Transport Expenses', 'Other Expenses', 'Savings'
    ];
    const distributionData = ref<{
      labels: string[],
      datasets: Array<{ backgroundColor: string[], data: any[] }>
    }>({
      labels: [],
      datasets: []
    })
    const lineChartData = ref<{
      labels: string[],
      datasets: Array<{
        label: string,
        data: number[],
        backgroundColor: string,
        borderColor: string,
        fill: boolean,
        tension: number,
        yAxisID: string
      }>
    }>({
      labels: [],
      datasets: []
    });

    const fetchPersonalList = async() => {
      try {
        const listResponse = await axios.get('http://localhost:8000/api/dashboard_last_personal_list')

        items.value = listResponse.data.slice(0, 12)
        const responseData = listResponse.data
        const datasetsMapping: { [key: string]: { label: string, data: any[], backgroundColor: string, borderColor: string, fill: boolean, tension: number, yAxisID: string } } = {}
        const monthLabels = responseData.map((row: any) => row["Month"]);

        for (let col = 2; col < fieldLabels.length; col++) {
          const label = fieldLabels[col];
          const values = responseData.map((row: any) => parseFloat(row[label]) || 0);
          const hue = Math.floor(Math.random() * 360);
          const borderColor = `hsl(${hue}, 70%, 60%)`;
          const backgroundColor = `hsla(${hue}, 70%, 60%, 0.2)`;

          datasetsMapping[label] = {
            label,
            data: values,
            borderColor,
            backgroundColor,
            fill: false,
            tension: 0.3,
            yAxisID: 'y'
          };
        }

        console.log(datasetsMapping, monthLabels)

        lineChartData.value = {
          labels: monthLabels,
          datasets: Object.values(datasetsMapping)
        };
      } catch (error) {
        throw new Error('There was an error')
      }
    }

    const expendituresByCategory = async() => {
      try {
        const distribution = await axios.get('http://localhost:8000/api/expenditures')
        
        const numDataPoints = distribution.data.length
        distributionData.value = {
          labels: ['Bills' ,'Food' ,'Taxes' ,'Transport Expenses' ,'Other Expenses'],
          datasets: [{
            backgroundColor: generateRandomColors(numDataPoints),
            data: [distribution.data[0], distribution.data[1], distribution.data[2], distribution.data[3], distribution.data[4], distribution.data[5]]
          }
            
          ]
        }
      } catch (error) {
        throw new Error('There was an error')
      }
    }

    const optionsPie = {
      responsive: true,
      maintainAspectRatio: false,
    }

    const options = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Amount ($)'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Month'
          }
        }
      }
    }

    onMounted(() => {
      fetchPersonalList()
      expendituresByCategory()
    })

    return {
      items,
      distributionData,
      lineChartData,
      options,
      optionsPie
    }
  }, 
  computed: {
    totalData() {
        return this.items.length;
    }
  }
})
</script>

<style scoped>
.chart-wrapper {
  height: 400px;
  width: 100%;
  padding: 1rem;
}
</style>