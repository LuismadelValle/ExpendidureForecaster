<template>
    <div>
        <label for="currentMonthInput">Current month income:</label>
        <input type="number" id="currentMonthIncome">
        <input type="button" value="Submit" onclick="alert('Hello')">
    </div>
</template>

<script>
export default {
    name: 'PersonalBudget',
    // methods: {
    //     msg() {
    //         alert(this.currentMonthIncome)
    //     }
    // }
}
</script>

<style lang="css">
#currentMonthIncome {
    color:black;
    border-radius: 5px;
    margin-right: 10px;
    margin-left: 10px;
}
</style>