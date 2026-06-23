import axios from "axios";

export const getFields = () => {
    return axios.get("http://localhost:5000/fields")
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            return [];
        });
};

export const getFieldById = (id) => {
    return axios.get(`http://localhost:5000/fields/${id}`)
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            return {};
        });
};

export const getFieldFacilities = (id) => {
    return axios.get(`http://localhost:5000/fields/${id}/facilities`)
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            return [];
        });
}

export const updateFieldFacilities = (id, facilityIds) => {
    return axios.put(`http://localhost:5000/fields/${id}/facilities`, { facility_ids: facilityIds })
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            throw err;
        });
}

export const createField = (formData) => {
    return axios.post("http://localhost:5000/fields", formData)
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            throw err;
        });
}

export const updateField = (id, formData) => {
    return axios.put(`http://localhost:5000/fields/${id}`, formData)
        .then((res) => res.data)
        .catch((err) => {
            console.log(err);
            throw err;
        });
}
