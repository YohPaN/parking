<template>
    <div>
      <h1>Parking Spots</h1>
      <div class="parking">
        <span v-for="spot in spots" :key="spot.spot_number">
            <div v-if="spot.is_occupied" class="occupied slot">{{ spot.spot_number }}</div>
            <div v-else class="free slot">{{ spot.spot_number }}</div>
        </span>
      </div>
    </div>
  </template>
  
  <script>
  import { getParkingSpots } from '../api';


  export default {
    data() {
        return {
            spots: [],
        }
    },

    async created() {
        this.spots = await getParkingSpots();
        this.spots.sort((a, b) => {
            return a.spot_number > b.spot_number
        })
    },
  };
  </script>

<style>
.parking {
    display: flex;
    flex-direction: row;
    justify-content: center;
    max-width: 100%;
    flex-wrap: wrap;
}

.slot {
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 5px;
    margin: 5px;
    width: 100px;
    height: 100px;
}

.free {
    background-color: green;
}

.occupied {
    background-color: red;
}
</style>
  