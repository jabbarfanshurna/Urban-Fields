import axios from "axios";

export const getUsers = () => {
    return axios.get("http://localhost:5000/users")
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            return [];
        });
};