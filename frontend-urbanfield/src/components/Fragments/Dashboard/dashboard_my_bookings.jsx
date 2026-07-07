import { useState, useEffect } from 'react';
import { jwtDecode } from 'jwt-decode';
import { getMyBookings, deleteBooking } from '../../../services/db/booking.service';
import { useModal } from '../../../context/ModalContext';


const DashboardMyBookings = () => {
    const [bookings, setBookings] = useState([]);
    const [userId, setUserId] = useState(null);
    const { showAlert, showConfirm } = useModal();

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
            window.location.href = '/login';
            return;
        }

        try {
            const decodedToken = jwtDecode(token);
            const extractedUserId = decodedToken.sub && typeof decodedToken.sub === 'object' ? decodedToken.sub.id : decodedToken.sub;
            setUserId(extractedUserId);
            loadBookings(extractedUserId);
        } catch (error) {
            console.error('Error decoding token:', error);
            window.location.href = '/login';
        }
    }, []);

    const loadBookings = (uid) => {
        getMyBookings(uid).then((data) => {
            setBookings(data);
        });
    };

    const handleCancel = async (bookingId) => {
        const confirmed = await showConfirm('Apakah Anda yakin ingin membatalkan reservasi ini?', 'Batalkan Reservasi');
        if (!confirmed) return;

        try {
            await deleteBooking(bookingId);
            loadBookings(userId);
        } catch (error) {
            const message = error.response?.data?.error || 'Gagal membatalkan reservasi. Silakan coba lagi.';
            await showAlert(message, 'Gagal');
        }
    };

    function formatDate(dateString) {
        const date = new Date(dateString);
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');

        return `${year}-${month}-${day}`;
    }

    function isPastBooking(dateString) {
        const bookingDate = new Date(dateString);
        bookingDate.setHours(0, 0, 0, 0);

        const today = new Date();
        today.setHours(0, 0, 0, 0);

        return bookingDate < today;
    }

    return (
        <div className="mt-5 mx-10 font-Inter font-medium">
            <div className="ml-4">
                <h1 className="text-2xl font-bold">RESERVASI SAYA</h1>
            </div>
            <div className="mt-8 mx-12">
                {bookings.length === 0 ? (
                    <p className="text-gray-500">Belum ada reservasi.</p>
                ) : (
                    <table className="w-full">
                        <thead className="border-b-[1px] border-gray-800">
                            <tr>
                                <th className="text-left font-medium py-4">ORDER ID</th>
                                <th className="text-left font-medium py-4">FIELD</th>
                                <th className="text-left font-medium py-4">DATE</th>
                                <th className="text-left font-medium py-4">TIME</th>
                                <th className="text-left font-medium py-4">PAYMENT</th>
                                <th className="text-left font-medium py-4">ACTION</th>
                            </tr>
                        </thead>
                        <tbody className="mt-4">
                            {bookings.map((booking) => (
                                <tr key={booking.id}>
                                    <td className="py-4">{booking.id}</td>
                                    <td className="py-4">{booking.field_name}</td>
                                    <td className="py-4">{formatDate(booking.date)}</td>
                                    <td className="py-4">{booking.time}</td>
                                    <td className="py-4">{booking.payment_method_name}</td>
                                    <td className="py-4">
                                        {isPastBooking(booking.date) ? (
                                            <span className="text-gray-400">Selesai</span>
                                        ) : (
                                            <button
                                                onClick={() => handleCancel(booking.id)}
                                                className="text-red-600 hover:underline"
                                            >
                                                Cancel
                                            </button>
                                        )}
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
            </div>
        </div>
    );
};

export default DashboardMyBookings;
