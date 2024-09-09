import axios from 'axios';
import { useSpotStore } from './stores/spots.js';


const api = axios.create({
  baseURL: 'http://localhost:8000/api/', // Django server URL
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;

export const getParkingSpots = async () => {    
    try {
        const spots = useSpotStore();
        const response = await api.get('spots/');
        spots.initialization(response.data);
        return response.data;
    } catch (error) {
      console.error('Error fetching parking spots:', error);
    }
  };