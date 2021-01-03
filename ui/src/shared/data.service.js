import * as axios from 'axios';
import { API } from './config';

const getTopics = async () => {
    try {
        const response = await axios.get(`${API}/topics`);
        return response.data;
    } catch (error) {
        throw new Error(error);
    }
};

const getStarter = async (topic) => {
    try {
        const response = await axios.get(`${API}/questions/${topic}?roulette=true`);
        return response.data;
    } catch (error) {
        throw new Error(error);
    }
};

const getRandom = async () => {
    try {
        const response = await axios.get(`${API}/questions/roulette`);
        return response.data;
    } catch (error) {
        throw new Error(error);
    }
};

export const dataService = {
    getTopics,
    getStarter,
    getRandom,
};