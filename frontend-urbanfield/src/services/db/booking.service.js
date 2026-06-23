import axios from "axios";

export const getMyBookings = (userId) => {
    return axios.get(`http://localhost:5000/bookings?user_id=${userId}`)
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            return [];
        });
};
