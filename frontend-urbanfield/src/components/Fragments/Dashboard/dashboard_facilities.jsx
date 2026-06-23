import { useState, useEffect } from 'react';
import { useOutletContext } from 'react-router-dom';
import { getFacilities, createFacility, updateFacility, deleteFacility } from '../../../services/db/facility.service';

const DashboardFacilities = () => {
    const [facilities, setFacilities] = useState([]);
    const [showForm, setShowForm] = useState(false);
    const [selectedFacility, setSelectedFacility] = useState(null);
    const [name, setName] = useState('');
    const [icon, setIcon] = useState('');
    const { role } = useOutletContext();

    useEffect(() => {
        if (role !== 'admin') {
            window.location.href = '/dashboard';
        }

        loadFacilities();
    }, []);

    const loadFacilities = () => {
        getFacilities().then((data) => {
            setFacilities(data);
        });
    };

    const openAddForm = () => {
        setSelectedFacility(null);
        setName('');
        setIcon('');
        setShowForm(true);
    };

    const openEditForm = (facility) => {
        setSelectedFacility(facility);
        setName(facility.name);
        setIcon(facility.icon);
        setShowForm(true);
    };

    const closeForm = () => {
        setShowForm(false);
        setSelectedFacility(null);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (selectedFacility) {
                await updateFacility({ id: selectedFacility.id, name, icon });
            } else {
                await createFacility({ name, icon });
            }
            closeForm();
            loadFacilities();
        } catch (error) {
            console.error('Error saving facility:', error);
        }
    };

    const handleDelete = async (id) => {
        try {
            await deleteFacility(id);
            loadFacilities();
        } catch (error) {
            console.error('Error deleting facility:', error);
        }
    };

    return (
        <div className="mt-5 mx-10 font-Inter font-medium">
            <div className="mx-4 flex justify-between">
                <h1 className="text-2xl font-medium">Fasilitas Lapangan</h1>
                <button
                    onClick={openAddForm}
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                >
                    Add
                </button>
            </div>

            <div className="mt-8 mx-4">
                <table className="w-full">
                    <thead className="border-b-[1px] border-gray-800">
                        <tr>
                            <th className="text-left font-medium py-4">ID</th>
                            <th className="text-left font-medium py-4">NAME</th>
                            <th className="text-left font-medium py-4">ICON</th>
                            <th className="text-left font-medium py-4">ACTION</th>
                        </tr>
                    </thead>
                    <tbody>
                        {facilities.map((facility) => (
                            <tr key={facility.id}>
                                <td className="py-4">{facility.id}</td>
                                <td className="py-4">{facility.name}</td>
                                <td className="py-4">{facility.icon}</td>
                                <td className="py-4">
                                    <button
                                        onClick={() => openEditForm(facility)}
                                        className="text-blue-600 hover:underline mr-4"
                                    >
                                        Edit
                                    </button>
                                    <button
                                        onClick={() => handleDelete(facility.id)}
                                        className="text-red-600 hover:underline"
                                    >
                                        Delete
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            {showForm && (
                <div className="fixed inset-0 flex justify-end bg-black bg-opacity-50 z-50">
                    <div className="bg-white p-6 rounded-l-lg shadow-lg w-full max-w-sm relative h-full overflow-auto">
                        <span
                            className="cursor-pointer text-xl font-bold absolute top-4 right-4"
                            onClick={closeForm}
                        >
                            &times;
                        </span>
                        <h2 className="text-xl font-semibold mb-4">
                            {selectedFacility ? 'Edit Fasilitas' : 'Tambah Fasilitas'}
                        </h2>
                        <form onSubmit={handleSubmit}>
                            <label htmlFor="name" className="block text-sm font-medium text-gray-700">
                                Nama Fasilitas:
                            </label>
                            <input
                                type="text"
                                id="name"
                                value={name}
                                onChange={(e) => setName(e.target.value)}
                                className="block w-full p-2 border border-gray-300 rounded mt-1 mb-4"
                                required
                            />

                            <label htmlFor="icon" className="block text-sm font-medium text-gray-700">
                                Icon (nama file/class icon):
                            </label>
                            <input
                                type="text"
                                id="icon"
                                value={icon}
                                onChange={(e) => setIcon(e.target.value)}
                                className="block w-full p-2 border border-gray-300 rounded mt-1 mb-4"
                                required
                            />

                            <button
                                type="submit"
                                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                            >
                                Save
                            </button>
                        </form>
                    </div>
                </div>
            )}
        </div>
    );
};

export default DashboardFacilities;
