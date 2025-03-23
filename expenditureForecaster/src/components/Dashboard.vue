<template>
    <!-- Flex Container for Charts -->
    <div class="flex flex-wrap lg:flex-nowrap gap-4">
        <!-- Pie Chart -->
        <div class="flex-1 mr-20">
            <h4 class="mb-5">Your expenditure distribution from last year</h4>
            <Responsive class="w-auto">
                <template #main="{ width }">
                    <Chart
                        direction="circular"
                        :size="{ width: 400, height: 400 }"
                        :data="data"
                        :margin="{
                            left: Math.round((width - 360) / 2),
                            top: 20,
                            right: 0,
                            bottom: 20
                        }"
                        :config="{ controlHover: false }"
                    >
                        <template #layers>
                            <Pie
                                :dataKeys="['name', 'pl']"
                                :pie-style="{ innerRadius: 100, padAngle: 0.05 }" />
                        </template>
                        <template #widgets>
                            <Tooltip
                                :config="{
                                    name: { },
                                    avg: { hide: false },
                                    pl: { label: 'value' },
                                    inc: { hide: false }
                                }"
                                hideLine
                            />
                        </template>
                    </Chart>
                </template>
            </Responsive>
        </div>

        <!-- Line Chart -->
        <div class="flex-1 ml-20">
            <h4 class="mb-4">Your total expenses for each of the last 12 months</h4>
            <Chart
                :size="{ width: 400, height: 400 }"
                :data="data"
                :margin="margin"
                :direction="direction"
                :axis="axis"
            >
                <template #layers>
                    <Grid strokeDasharray="2,2" />
                    <Line :dataKeys="['name', 'pl']" />
                    <Line :dataKeys="['name', 'avg']" :lineStyle="{ stroke: 'red' }" type="step" />
                </template>
                <template #widgets>
                    <Tooltip
                        borderColor="#48CAE4"
                        :config="{
                            name: { hide: false },
                            pl: { color: '#0077b6' },
                            avg: { label: 'average', color: 'red' },
                            inc: { hide: false }
                        }"
                    />
                </template>
            </Chart>
        </div>
    </div>

    <!-- Table -->
    <div class="mt-6 w-full mt-10">
        <h4 class="mb-5">Your last {{ totalData }} expenses</h4>
        <table-lite
            :is-loading="table.isLoading"
            :columns="table.columns"
            :rows="table.rows"
            :total="table.totalRecordCount"
            :sortable="table.sortable"
        ></table-lite>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref, reactive } from 'vue'
import { Chart, Responsive, Pie, Tooltip, Grid, Line } from 'vue3-charts'
import TableLite from "vue3-table-lite/ts";
// import axios from 'axios';

const sampleData1 = (offst, limit) => {
    offst = offst + 1;
    let data = [];
    for (let i = offst; i <= limit; i++) {
        data.push({
            id: i,
            name: "TEST" + i,
            email: "test" + i + "@example.com",
        });
    }
    return data;
};

const sampleData2 = (offst, limit) => {
  let data = [];
  for (let i = limit; i > offst; i--) {
    data.push({
      id: i,
      name: "TEST" + i,
      email: "test" + i + "@example.com",
    });
  }
  return data;
};

export default defineComponent({
  name: 'LineChart',
  components: { Chart, Responsive, Pie, Tooltip, Grid, Line, TableLite },
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

    const table = reactive({
      isLoading: true,
      columns: [
        {
          label: "ID",
          field: "id",
          width: "3%",
          sortable: true,
          isKey: true,
        },
        {
          label: "Name",
          field: "name",
          width: "10%",
          sortable: true,
        },
        {
          label: "Email",
          field: "email",
          width: "15%",
          sortable: true,
        },
      ],
      rows: [],
      totalRecordCount: 0,
      sortable: {
        order: "id",
        sort: "asc",
      },
    });

    const doSearch = (offset, limit, order, sort) => {
      table.isLoading = true;
      setTimeout(() => {
        table.isReSearch = offset == undefined ? true : false;
        if (offset >= 10 || limit >= 20) {
          limit = 20;
        }
        if (sort == "asc") {
          table.rows = sampleData1(offset, limit);
        } else {
          table.rows = sampleData2(offset, limit);
        }
        table.totalRecordCount = 20;
        table.sortable.order = order;
        table.sortable.sort = sort;
      }, 600);
    };

    // First get data
    doSearch(0, 10, "id", "asc");

    return { data, direction, axis, margin, table, doSearch }
  }, 
  computed: {
    totalData() {
        return this.table.rows.length;
    }
  }
})
</script>
