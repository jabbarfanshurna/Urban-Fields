import { useState, useEffect } from 'react';
import { jwtDecode } from 'jwt-decode';
import { getMyBookings } from '../../../services/db/booking.service';

const DashboardMyBookings = () => {
    const [bookings, setBookings] = useState([]);

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
            window.location.href = '/login';
            return;
        }

        try {
            const decodedToken = jwtDecode(token);
            const userId = decodedToken.sub;
            getMyBookings(userId).then((data) => {
                setBookings(data);
            });
        } catch (error) {
            console.error('Error decoding token:', error);
            window.location.href = '/login';
        }
    }, []);

    function formatDate(dateString) {
        const date = new Date(dateString);
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');

        return `${year}-${month}-${day}`;
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
