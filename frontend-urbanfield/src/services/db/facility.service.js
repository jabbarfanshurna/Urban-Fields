import axios from "axios";

export const getFacilities = () => {
    return axios.get("http://localhost:5000/facilities")
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            return [];
        });
};

export const createFacility = (formData) => {
    return axios.post("http://localhost:5000/facilities", formData)
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            throw err;
        });
};

export const updateFacility = (formData) => {
    return axios.put("http://localhost:5000/facilities", formData)
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            throw err;
        });
};

export const deleteFacility = (id) => {
    return axios.delete("http://localhost:5000/facilities", { data: { id } })
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            throw err;
        });
};
