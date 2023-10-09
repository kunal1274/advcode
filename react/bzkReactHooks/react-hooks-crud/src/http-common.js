import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:8000/myapp/api",
  headers: {
    "Content-type": "application/json"
  }
});