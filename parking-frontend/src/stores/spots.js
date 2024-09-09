import { defineStore } from 'pinia'

export const useSpotStore = defineStore('spots', {
  state: () => {
    return { spots: [] }
  },

  actions: {
    initialization(spots) {     
      this.spots = spots;
    },

    getSpotAvailable() {
      const availableSpot = this.spots.find((spot) => !spot.is_occupied);
      availableSpot.is_occupied = true;
      return availableSpot;
    },

    releaseSpot(spotToRealase) {
      const realeasedSpot = this.spots.find((spot) => spot.spot_number == spotToRealase);
      realeasedSpot.is_occupied = false;
    }
  },
})