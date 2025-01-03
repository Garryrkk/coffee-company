import axios from "axios";

const API = axios.create({
  baseURL: "https://your-backend-api.com/api",
});

// Add a request interceptor for authorization
API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const loginUser = (credentials) => API.post("/login", credentials);
export const signupUser = (userData) => API.post("/signup", userData);
export const getProfile = () => API.get("/profile");
