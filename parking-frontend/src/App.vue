<template>
  <ParkingSpots />
  <TicketManager />
</template>

<script>
import ParkingSpots from './components/ParkingSpots.vue';
import TicketManager from './components/TicketManager.vue';

export default {
  name: 'App',
  components: {
    ParkingSpots,
    TicketManager,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
