import * as axios from 'axios';
import { API } from './config';

const getTopics = async () => {
    try {
        const response = await axios.get(`${API}/topics`)
        return response.data;
    } catch (error) {
        throw new Error(error);
    }
};

const getStarter = async (topic) => {
    try {
        const response = await axios.get(`${API}/starters/${topic}`)
        return response.data;
    } catch (error) {
        throw new Error(error);
    }
};

export const dataService = {
    getTopics,
    getStarter,
};