<template>
    <div>
    <h2>Manage Parking Ticket</h2>
    <form @submit.prevent="createTicket">
        <button id="enter-button" type="submit">Get Ticket</button>
    </form>
    <input v-model="spotNumber" type="number" placeholder="Enter spot number" required min="0" />
    <button id="release-button" @click="releaseTicket">Release Ticket</button>
    <p v-if="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  import api from '../api';
  import { useSpotStore } from '@/stores/spots';
  
  export default {
    data() {
      return {
        spotNumber: '',
        message: '',
      };
    },
    methods: {
        async createTicket() {
            let spotAvailable = null;
            try {
                const spotStore = useSpotStore();
                spotAvailable = spotStore.getSpotAvailable();
                
                const response = await api.post(`ticket/create/${spotAvailable.spot_number}/`);
                
                this.message = `Ticket created for spot ${spotAvailable.spot_number}. Your ticket number is the ${response.data.id}`;
            } catch (error) {
                if(spotAvailable == undefined) {
                    this.message = "No more place, please come later";
                } else {
                    this.message = 'Error creating ticket.';
                }
            }
        },
        async releaseTicket() {
            try {
                const spotStore = useSpotStore();
                spotStore.releaseSpot(this.spotNumber);

                await api.post(`ticket/release/${this.spotNumber}/`);

                this.message = `Spot ${this.spotNumber} released.`;
            } catch (error) {
                this.message = 'Error releasing ticket';
            }
        },
    },
  };
  </script>
  
  <style>
    button {
        border-radius: 5px;
        border: 0;
        padding: 10px 15px 10px 15px;
        margin: 1em;
    }

    #release-button {
        background-color: rgb(0, 89, 255);
    }

    #enter-button {
        background-color: green;
    }

</style>