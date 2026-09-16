import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 15000,
});

export async function getLocations() {
  const response = await api.get("/locations");
  return response.data.locations;
}

export async function getHealth() {
  const response = await api.get("/health");
  return response.data;
}

export async function predictPrice(payload) {
  const response = await api.post("/predict", payload);
  return response.data;
}
