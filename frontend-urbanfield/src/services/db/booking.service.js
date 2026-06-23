import axios from "axios";

export const getMyBookings = (userId) => {
    return axios.get(`http://localhost:5000/bookings?user_id=${userId}`)
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            return [];
        });
};

export const deleteBooking = (id) => {
    return axios.delete("http://localhost:5000/bookings", { data: { id } })
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            throw err;
        });
};

export const getBookedSlots = (fieldId, date) => {
    return axios.get(`http://localhost:5000/fields/${fieldId}/booked_slots?date=${date}`)
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            return [];
        });
};
